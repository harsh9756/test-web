# Generated by Django 4.2.4 on 2023-09-17 07:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=25, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='ContactUS',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('email', models.EmailField(max_length=60)),
                ('subject', models.TextField()),
                ('message', models.TextField()),
                ('active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='mainCategory',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=25, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('maincat', models.CharField(max_length=50)),
                ('brand', models.CharField(max_length=50)),
                ('props', models.TextField()),
                ('banPic', models.ImageField(upload_to='productimg/')),
                ('baseprice', models.IntegerField(default=0)),
                ('discount', models.IntegerField(default=0)),
                ('finalPrice', models.IntegerField(default=0)),
                ('color', models.CharField(max_length=20)),
                ('size', models.CharField(max_length=10)),
                ('desc', models.TextField()),
                ('stock', models.BooleanField(default=True)),
                ('time', models.DateField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=70)),
                ('username', models.CharField(max_length=50, unique=True)),
                ('phone', models.IntegerField()),
                ('actype', models.CharField(max_length=50)),
                ('pin', models.IntegerField(blank=True, null=True)),
                ('city', models.CharField(blank=True, default='', max_length=50, null=True)),
                ('state', models.CharField(blank=True, default='', max_length=50, null=True)),
                ('otp', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Subscribers',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Wishlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('q', models.IntegerField(default=1)),
                ('prodId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainApp.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Pics',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='productimg/')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainApp.product')),
            ],
        ),
        migrations.CreateModel(
            name='Checkout',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('products', models.TextField()),
                ('total', models.IntegerField()),
                ('shipping', models.IntegerField()),
                ('finalAmt', models.IntegerField()),
                ('time', models.DateField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
                ('mode', models.IntegerField(choices=[(1, 'COD'), (2, 'Credit Card'), (3, 'Net Banking')], default=1)),
                ('orderStatus', models.IntegerField(choices=[(1, 'Not Packed'), (2, 'Ready for Shipment'), (3, 'Shipped'), (4, 'Delivered')], default=1)),
                ('paymentStatus', models.IntegerField(choices=[(1, 'Pending'), (2, 'Success')], default=1)),
                ('orderid', models.CharField(blank=True, max_length=500, null=True)),
                ('razor_payment_id', models.CharField(blank=True, max_length=500, null=True)),
                ('razor_sign', models.CharField(blank=True, max_length=500, null=True)),
                ('buyer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainApp.profile')),
            ],
        ),
    ]