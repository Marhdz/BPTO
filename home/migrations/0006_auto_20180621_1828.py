# Generated by Django 2.0.6 on 2018-06-22 00:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_auto_20180618_1411'),
    ]

    operations = [
        migrations.AddField(
            model_name='marca',
            name='precioE',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=4),
        ),
        migrations.AlterField(
            model_name='encuesta',
            name='numIteraciones',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='opciones',
            name='nIteracion',
            field=models.PositiveIntegerField(),
        ),
    ]