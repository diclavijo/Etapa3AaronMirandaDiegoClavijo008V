# Generated by Django 3.1.2 on 2020-12-10 21:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0011_auto_20201210_1643'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alimento',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='media/'),
        ),
    ]
