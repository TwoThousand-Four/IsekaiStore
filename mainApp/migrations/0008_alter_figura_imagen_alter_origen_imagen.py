# Generated by Django 4.2.2 on 2023-07-05 04:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0007_alter_figura_id_alter_figura_origen_alter_origen_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='figura',
            name='imagen',
            field=models.ImageField(null=True, upload_to='imagenes/figuras', verbose_name='Imagen'),
        ),
        migrations.AlterField(
            model_name='origen',
            name='imagen',
            field=models.ImageField(null=True, upload_to='imagenes/origen', verbose_name='Imagen'),
        ),
    ]