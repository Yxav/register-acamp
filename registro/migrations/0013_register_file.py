# Generated by Django 2.2.5 on 2019-09-05 02:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registro', '0012_remove_register_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='register',
            name='file',
            field=models.FileField(blank='true', default='', upload_to='media', verbose_name='Autorização dos resṕnsáveis'),
        ),
    ]
