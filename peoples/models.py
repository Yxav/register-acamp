from django.db import models

class Register(models.Model):
    first_name = models.CharField(max_length=100, verbose_name='First name')
    last_name = models.CharField(max_length=100, verbose_name='Last name')
    phone = models.CharField(max_length=16, default='', blank=True, verbose_name='Phone number')
    age =  models.CharField(max_length=2, default='', blank=True, verbose_name='Age')
    city = models.CharField(max_length=100, verbose_name='City')
    email = models.EmailField()
    obs = models.CharField(max_length=500, verbose_name='Obs')
    file = models.FileField(upload_to="media", default='', blank = 'true', verbose_name = 'Authorization')
    food = models.CharField(max_length=100,default='', blank=True, verbose_name='Food restrition')
    sleep = models.CharField(max_length=100, verbose_name='Type alocation')

    def __str__ (self):
        return (self.first_name)