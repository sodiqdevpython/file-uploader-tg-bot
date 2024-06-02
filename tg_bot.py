import os
import tempfile
import requests
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ConversationHandler, ContextTypes

API_URL = "https://fileuploadertgbot.pythonanywhere.com/"

FIO, PROJECT_NAME, TEL_NUMBER = range(3)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    tg_id = update.message.from_user.id
    response = requests.get(API_URL, params={'tg_id': tg_id})
    
    if response.status_code == 200 and len(response.json()) > 0:
        keyboard = [
            ["Taqdimot fayli"],
            ["BMI hisoboti"],
            ["Raxbar mulohazasi"],
            ["Taqriz"],
            ["Loyiha"],
            ["Anotatsiya"],
            ["Hammasini o'chirish"]
        ]
    else:
        keyboard = [
            ["Ishlarni yuklash"]
        ]
    
    reply_markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard=True)
    await update.message.reply_text(
        "Ma'lumotlaringizni yuklashingiz mumkin !",
        reply_markup=reply_markup
    )

async def add_data(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    tg_id = update.message.from_user.id
    response = requests.get(API_URL, params={'tg_id': tg_id})
    if response.status_code == 200 and len(response.json()) >= 1:
        await update.message.reply_text("Faqat 1 marta ma'lumot yuklay olasiz")
        return ConversationHandler.END
    else:
        await update.message.reply_text("To'liq ism, familiya, otangizning ismi (FIO):")
        return FIO

async def fio(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    context.user_data['fio'] = update.message.text
    await update.message.reply_text("Mavzuingiz nomi:")
    return PROJECT_NAME

async def project_name(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    context.user_data['project_name'] = update.message.text
    await update.message.reply_text("Telefon raqamingiz:")
    return TEL_NUMBER

async def tel_number(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    context.user_data['tel_number'] = update.message.text
    tg_id = update.message.from_user.id
    data = {
        'tg_id': tg_id,
        'fio': context.user_data['fio'],
        'project_name': context.user_data['project_name'],
        'tel_number': context.user_data['tel_number'],
    }
    response = requests.post(API_URL, data=data)
    if response.status_code == 201:
        await update.message.reply_text("Ma'lumotlaringiz saqlandi, endi fayl yuklay olasiz")
        await start(update, context)
    else:
        await update.message.reply_text("Nimadir xato ketdi")
    
    return ConversationHandler.END

async def prompt_document_upload(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    document_field_mapping = {
        "Taqdimot fayli": "document",
        "BMI hisoboti": "document2",
        "Raxbar mulohazasi": "document3",
        "Taqriz": "document4",
        "Loyiha": "document5",
        "Anotatsiya": "document6",
    }
    document_field = document_field_mapping.get(update.message.text)
    context.user_data['document_field'] = document_field
    await update.message.reply_text(f"Fayl yuklang {update.message.text}.")

async def document_upload(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    document_field = context.user_data.get('document_field')
    if document_field and update.message.document:
        tg_id = update.message.from_user.id
        file_id = update.message.document.file_id
        file = await context.bot.get_file(file_id)
        
        with tempfile.TemporaryDirectory() as tmpdirname:
            file_path = os.path.join(tmpdirname, update.message.document.file_name)
            await file.download_to_drive(file_path)

            with open(file_path, 'rb') as f:
                files = {document_field: f}
                data = {'tg_id': tg_id}
                response = requests.post(f"{API_URL}upload-{document_field}/", data=data, files=files)
            
            if response.status_code == 201:
                await update.message.reply_text(f"{update.message.text} muvaffaqiyatli saqlandi.")
            elif response.status_code == 200:
                await update.message.reply_text(f"{update.message.text} muvaffaqiyatli saqlandi.")
            else:
                await update.message.reply_text(f"Nimadir xato ketdi: {response.content.decode()}")
    else:
        await update.message.reply_text("To'g'ri formatdagi fayl yuklang")

    await start(update, context)

async def delete_data(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    tg_id = update.message.from_user.id
    response = requests.delete(f"{API_URL}delete/", params={'tg_id': tg_id})
    if response.status_code == 204:
        await update.message.reply_text("Ma'lumotlaringiz o'chirildi")
    else:
        await update.message.reply_text("Nimadir xato ketdi qaytadan urinib ko'ring")
    await start(update, context)

async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Bekor qilindi.")
    return ConversationHandler.END

def main() -> None:
    application = Application.builder().token("7317498633:AAFcH_ozodKB8vtEQwLzCpbSBmCZrfixzTE").build()

    conv_handler = ConversationHandler(
        entry_points=[MessageHandler(filters.Regex("(?i)Ishlarni yuklash"), add_data)],
        states={
            FIO: [MessageHandler(filters.TEXT & ~filters.COMMAND, fio)],
            PROJECT_NAME: [MessageHandler(filters.TEXT & ~filters.COMMAND, project_name)],
            TEL_NUMBER: [MessageHandler(filters.TEXT & ~filters.COMMAND, tel_number)]
        },
        fallbacks=[CommandHandler('cancel', cancel)],
    )

    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.Regex("(?i)Taqdimot fayli$"), prompt_document_upload))
    application.add_handler(MessageHandler(filters.Regex("(?i)BMI hisoboti$"), prompt_document_upload))
    application.add_handler(MessageHandler(filters.Regex("(?i)Raxbar mulohazasi$"), prompt_document_upload))
    application.add_handler(MessageHandler(filters.Regex("(?i)Taqriz$"), prompt_document_upload))
    application.add_handler(MessageHandler(filters.Regex("(?i)Loyiha$"), prompt_document_upload))
    application.add_handler(MessageHandler(filters.Regex("(?i)Anotatsiya$"), prompt_document_upload))
    application.add_handler(MessageHandler(filters.Document.ALL, document_upload))
    application.add_handler(MessageHandler(filters.Regex("(?i)Hammasini o'chirish"), delete_data))
    application.add_handler(conv_handler)

    application.run_polling()

if __name__ == '__main__':
    main()
