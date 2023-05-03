# Generated by Django 3.1.2 on 2022-11-04 05:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ecommerce', '0002_bankaccount'),
    ]

    operations = [
        migrations.CreateModel(
            name='VendorPayments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('request_amount', models.FloatField(blank=True, default=0.0, null=True)),
                ('fee', models.FloatField(blank=True, default=0.0, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('status', models.CharField(choices=[('Paid', 'Paid'), ('Pending', 'Pending'), ('Progressing', 'Progressing'), ('Refunded', 'Refunded')], default='Pending', max_length=13)),
                ('method', models.CharField(choices=[('Bank', 'Bank'), ('Paypal', 'Paypal')], default='Bank', max_length=15)),
                ('comment', models.TextField(blank=True, null=True)),
                ('date', models.DateTimeField(auto_now_add=True, null=True)),
                ('date_update', models.DateTimeField(auto_now=True, null=True)),
                ('vendor_profile', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-id',),
            },
        ),
    ]
