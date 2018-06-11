# Generated by Django 2.0.4 on 2018-06-10 22:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Encuesta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=140)),
                ('incremento', models.DecimalField(decimal_places=2, max_digits=4)),
                ('numIteraciones', models.IntegerField()),
                ('categoria', models.TextField()),
                ('date', models.DateTimeField()),
            ],
        ),
    ]