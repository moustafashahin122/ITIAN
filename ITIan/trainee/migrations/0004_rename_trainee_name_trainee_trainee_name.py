# Generated by Django 4.2.1 on 2023-06-02 06:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trainee', '0003_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='trainee',
            old_name='Trainee_name',
            new_name='trainee_name',
        ),
    ]