from django.contrib import admin
from django.utils.html import format_html
from .models import mainData, DocsData, DocsData2, DocsData3, DocsData4, DocsData5, DocsData6

class DocsInline(admin.TabularInline):
    model = DocsData
    extra = 0
    fields = ['document']

class Docs2Inline(admin.TabularInline):
    model = DocsData2
    extra = 0
    fields = ['document2']

class Docs3Inline(admin.TabularInline):
    model = DocsData3
    extra = 0
    fields = ['document3']

class Docs4Inline(admin.TabularInline):
    model = DocsData4
    extra = 0
    fields = ['document4']

class Docs5Inline(admin.TabularInline):
    model = DocsData5
    extra = 0
    fields = ['document5']

class Docs6Inline(admin.TabularInline):
    model = DocsData6
    extra = 0
    fields = ['document6']

@admin.register(mainData)
class AdminViewMainData(admin.ModelAdmin):
    list_display = ['fio', 'tel_number', 'get_docs', 'get_docs2', 'get_docs3', 'get_docs4', 'get_docs5', 'get_docs6', 'created_at']
    search_fields = ['fio', 'tel_number']
    inlines = [DocsInline, Docs2Inline, Docs3Inline, Docs4Inline, Docs5Inline, Docs6Inline]

    def get_docs(self, obj):
        docs = DocsData.objects.filter(user=obj)
        return format_html(", ".join([f'<a href="{doc.document.url}" target="_blank">{doc.document.name}</a>' for doc in docs]))
    get_docs.short_description = 'Taqdimot fayli'

    def get_docs2(self, obj):
        docs = DocsData2.objects.filter(user=obj)
        return format_html(", ".join([f'<a href="{doc.document2.url}" target="_blank">{doc.document2.name}</a>' for doc in docs]))
    get_docs2.short_description = 'BMI hisoboti'

    def get_docs3(self, obj):
        docs = DocsData3.objects.filter(user=obj)
        return format_html(", ".join([f'<a href="{doc.document3.url}" target="_blank">{doc.document3.name}</a>' for doc in docs]))
    get_docs3.short_description = 'Raxbar mulohazasi'

    def get_docs4(self, obj):
        docs = DocsData4.objects.filter(user=obj)
        return format_html(", ".join([f'<a href="{doc.document4.url}" target="_blank">{doc.document4.name}</a>' for doc in docs]))
    get_docs4.short_description = 'Taqriz'

    def get_docs5(self, obj):
        docs = DocsData5.objects.filter(user=obj)
        return format_html(", ".join([f'<a href="{doc.document5.url}" target="_blank">{doc.document5.name}</a>' for doc in docs]))
    get_docs5.short_description = 'Loyiha'

    def get_docs6(self, obj):
        docs = DocsData6.objects.filter(user=obj)
        return format_html(", ".join([f'<a href="{doc.document6.url}" target="_blank">{doc.document6.name}</a>' for doc in docs]))
    get_docs6.short_description = 'Anotatsiya'

@admin.register(DocsData)
class AdminViewDocsData(admin.ModelAdmin):
    list_display = ['user', 'document']
    search_fields = ['user__fio', 'user__tel_number']

@admin.register(DocsData2)
class AdminViewDocsData2(admin.ModelAdmin):
    list_display = ['user', 'document2']
    search_fields = ['user__fio', 'user__tel_number']

@admin.register(DocsData3)
class AdminViewDocsData3(admin.ModelAdmin):
    list_display = ['user', 'document3']
    search_fields = ['user__fio', 'user__tel_number']

@admin.register(DocsData4)
class AdminViewDocsData4(admin.ModelAdmin):
    list_display = ['user', 'document4']
    search_fields = ['user__fio', 'user__tel_number']

@admin.register(DocsData5)
class AdminViewDocsData5(admin.ModelAdmin):
    list_display = ['user', 'document5']
    search_fields = ['user__fio', 'user__tel_number']

@admin.register(DocsData6)
class AdminViewDocsData6(admin.ModelAdmin):
    list_display = ['user', 'document6']
    search_fields = ['user__fio', 'user__tel_number']
