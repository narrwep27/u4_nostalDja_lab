# Generated by Django 4.0.2 on 2022-02-02 00:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nostaldja_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fad',
            name='description',
            field=models.CharField(max_length=500),
        ),
    ]
