# Generated by Django 5.1.6 on 2025-02-19 14:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('customer', '0001_initial'),
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customer.customer')),
            ],
        ),
        migrations.CreateModel(
            name='CartBook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.book')),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cart.cart')),
            ],
        ),
        migrations.AddField(
            model_name='cart',
            name='books',
            field=models.ManyToManyField(blank=True, through='cart.CartBook', to='product.book'),
        ),
        migrations.CreateModel(
            name='CartClothes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cart.cart')),
                ('clothes', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.clothes')),
            ],
        ),
        migrations.AddField(
            model_name='cart',
            name='clothes',
            field=models.ManyToManyField(blank=True, through='cart.CartClothes', to='product.clothes'),
        ),
    ]
