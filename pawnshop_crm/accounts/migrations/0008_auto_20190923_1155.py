# Generated by Django 2.1.5 on 2019-09-23 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_auto_20190923_1154'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='middle_name',
            field=models.CharField(blank=True, default=None, max_length=30, null=True, verbose_name='Отчество'),
        ),
    ]
