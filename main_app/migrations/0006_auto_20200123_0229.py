# Generated by Django 2.2.9 on 2020-01-23 02:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_ingredient_details'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredient',
            name='details',
            field=models.TextField(default='No description', max_length=500),
        ),
    ]