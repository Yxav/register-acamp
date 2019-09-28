from django.db import models
from django import forms




class Register(models.Model):
    first_name = models.CharField(max_length=100, verbose_name='primeiro nome')
    last_name = models.CharField(max_length=100, verbose_name='ultimo nome')
    phone = models.CharField(max_length=15, default='', blank=True, verbose_name='telefone')
    age =  models.CharField(max_length=2, default='', blank=True, verbose_name='idade')
    church = models.CharField(max_length=100, verbose_name='igreja')
    city = models.CharField(max_length=100, verbose_name='cidade')
    email = models.EmailField()
    obs = models.CharField(max_length=500, verbose_name='observação')
    file = models.FileField(upload_to="media", default='', blank = 'true', verbose_name = 'Autorização dos resṕnsáveis')
    food = models.CharField(max_length=100,default='', blank=True, verbose_name='Restrição Alimentar')
    sleep = models.CharField(max_length=100, verbose_name='Alocação')

    def __str__ (self):
        return (self.first_name)
