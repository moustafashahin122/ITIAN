# Generated by Django 4.2.1 on 2023-06-02 03:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myaccount', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='password',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='username',
            field=models.CharField(max_length=40),
        ),
    ]
