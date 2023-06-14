# Generated by Django 4.1.4 on 2023-05-23 19:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0018_shopuser_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='productkey',
            name='order',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='shop.order'),
            preserve_default=False,
        ),
    ]