# Generated by Django 2.2 on 2019-09-25 13:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pawnshop', '0012_loan'),
    ]

    operations = [
        migrations.AddField(
            model_name='pledgeitem',
            name='category',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='pledge_items', to='pawnshop.Category', verbose_name='Относится к категории'),
        ),
        migrations.AlterField(
            model_name='loan',
            name='client',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='loans', to='pawnshop.Client', verbose_name='Клиент'),
        ),
    ]
