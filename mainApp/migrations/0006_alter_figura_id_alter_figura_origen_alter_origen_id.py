# Generated by Django 4.2.2 on 2023-07-05 03:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0005_alter_figura_id_alter_origen_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='figura',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False, verbose_name='Id'),
        ),
        migrations.AlterField(
            model_name='figura',
            name='origen',
            field=models.CharField(max_length=50, verbose_name='Origen'),
        ),
        migrations.AlterField(
            model_name='origen',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False, verbose_name='Id'),
        ),
    ]
