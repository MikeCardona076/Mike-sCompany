# Generated by Django 2.2.7 on 2019-11-06 02:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('curso', '0004_auto_20191106_0233'),
    ]

    operations = [
        migrations.AlterField(
            model_name='curso',
            name='fecha_fin',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='curso',
            name='fecha_inicio',
            field=models.DateField(),
        ),
    ]
