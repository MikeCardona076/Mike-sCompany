# Generated by Django 2.2.7 on 2019-11-06 02:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('curso', '0005_auto_20191106_0244'),
    ]

    operations = [
        migrations.AlterField(
            model_name='curso',
            name='tipo_curso',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='curso',
            name='titulo_curso',
            field=models.CharField(max_length=30),
        ),
    ]