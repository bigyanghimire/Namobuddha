# Generated by Django 2.0.6 on 2018-06-29 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('domsapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='document',
            field=models.FileField(blank=True, upload_to='', verbose_name='/nagar/doms/domsapp/static/'),
        ),
    ]
