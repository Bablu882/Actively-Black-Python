# Generated by Django 4.0.6 on 2022-08-09 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0003_delete_user_manage'),
    ]

    operations = [
        migrations.CreateModel(
            name='forget_password',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=50)),
            ],
        ),
    ]
