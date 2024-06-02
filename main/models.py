from django.db import models

class mainData(models.Model):
    tg_id = models.CharField(max_length=100)
    fio = models.CharField(max_length=30, help_text="Familiya, Ism, Otasining ismi", verbose_name='Ism, familiya')
    project_name = models.CharField(max_length=250, verbose_name='Project Name', help_text='Name of the project')
    tel_number = models.CharField(max_length=20, verbose_name='Telefon raqam', help_text='Contact telephone number')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Yaratildi")

    def __str__(self):
        return self.fio

    class Meta:
        verbose_name = "Foydalanuvchi"
        verbose_name_plural = "Foydalanuvchilar"

class DocsData(models.Model):
    user = models.ForeignKey(mainData, on_delete=models.CASCADE)
    document = models.FileField(upload_to='document/', verbose_name="Taqdimot fayli", null=True, blank=True)

    def __str__(self):
        return str(self.user)
    
    class Meta:
        verbose_name = "Taqdimot fayli"
        verbose_name_plural = "Taqdimot fayllari"

class DocsData2(models.Model):
    user = models.ForeignKey(mainData, on_delete=models.CASCADE)
    document2 = models.FileField(upload_to='document/', verbose_name="BMI hisoboti", null=True, blank=True)

    def __str__(self):
        return str(self.user)
    
    class Meta:
        verbose_name = "BMI hisoboti"
        verbose_name_plural = "BMI hisobotlari"

class DocsData3(models.Model):
    user = models.ForeignKey(mainData, on_delete=models.CASCADE)
    document3 = models.FileField(upload_to='document/', verbose_name="Raxbar mulohazasi", null=True, blank=True)

    def __str__(self):
        return str(self.user)
    
    class Meta:
        verbose_name = "Raxbar mulohazasi"
        verbose_name_plural = "Raxbar mulohazalari"

class DocsData4(models.Model):
    user = models.ForeignKey(mainData, on_delete=models.CASCADE)
    document4 = models.FileField(upload_to='document/', verbose_name="Taqriz", null=True, blank=True)

    def __str__(self):
        return str(self.user)
    
    class Meta:
        verbose_name = "Taqriz"
        verbose_name_plural = "Taqrizlar"

class DocsData5(models.Model):
    user = models.ForeignKey(mainData, on_delete=models.CASCADE)
    document5 = models.FileField(upload_to='document/', verbose_name="Loyiha", null=True, blank=True)

    def __str__(self):
        return str(self.user)
    
    class Meta:
        verbose_name = "Loyiha"
        verbose_name_plural = "Loyihalar"

class DocsData6(models.Model):
    user = models.ForeignKey(mainData, on_delete=models.CASCADE)
    document6 = models.FileField(upload_to='document/', verbose_name="Anotatsiya", null=True, blank=True)

    def __str__(self):
        return str(self.user)
    
    class Meta:
        verbose_name = "Anotatsiya"
        verbose_name_plural = "Anotatsiyalar"
