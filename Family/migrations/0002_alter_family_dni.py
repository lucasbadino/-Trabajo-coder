# Generated by Django 4.0.6 on 2022-07-24 21:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Family', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='family',
            name='Dni',
            field=models.IntegerField(),
        ),
    ]
