# Generated by Django 4.1.4 on 2023-05-17 18:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_order_productsday_orderslist'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductKey',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(max_length=255)),
                ('products', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='p_key', to='shop.product')),
            ],
        ),
    ]
