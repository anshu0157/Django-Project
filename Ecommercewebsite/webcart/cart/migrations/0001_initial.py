# Generated by Django 3.1.6 on 2021-02-11 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=150)),
                ('product_descrip', models.CharField(max_length=300)),
                ('product_date', models.DateField(auto_now=True)),
            ],
        ),
    ]
