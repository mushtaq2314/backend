# Generated by Django 4.2 on 2023-07-11 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='customizations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=255)),
                ('occasion', models.CharField(max_length=255)),
                ('pricerange', models.CharField(max_length=255)),
                ('skintone', models.CharField(max_length=255)),
                ('upper', models.CharField(max_length=1000)),
                ('lower', models.CharField(max_length=1000)),
                ('firstname', models.CharField(max_length=255)),
                ('lastname', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('country', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=255)),
                ('state', models.CharField(max_length=255)),
                ('pincode', models.CharField(max_length=255)),
                ('method', models.CharField(max_length=255)),
            ],
        ),
    ]