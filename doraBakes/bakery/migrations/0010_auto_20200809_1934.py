# Generated by Django 3.0.7 on 2020-08-09 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bakery', '0009_auto_20200809_1728'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='image',
            field=models.URLField(null=True),
        ),
    ]