# Generated by Django 4.1.4 on 2023-05-21 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0011_rename_user_shopuser'),
    ]

    operations = [
        migrations.AddField(
            model_name='catalogproduct',
            name='slug',
            field=models.SlugField(default=''),
        ),
    ]