# Generated by Django 2.2.2 on 2021-04-04 13:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('admission', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='dob',
        ),
    ]