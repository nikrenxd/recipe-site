# Generated by Django 4.2.6 on 2023-11-06 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meals', '0003_meal_slug_alter_meal_meal_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meal',
            name='slug',
            field=models.SlugField(unique=True),
        ),
    ]
