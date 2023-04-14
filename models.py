from django.db import models


class announcement(models.Model):
    title = models.CharField('Название', max_length=50)
    task = models.TextField('Описание')
    photo = models.ImageField(upload_to = 'photos', blank=False,null=True)
    time_create = models.DateTimeField(auto_now=True,null=True,blank=True)
    time_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'