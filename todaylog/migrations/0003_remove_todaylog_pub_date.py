# Generated by Django 3.2.7 on 2021-09-25 07:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todaylog', '0002_alter_todaylog_rating'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todaylog',
            name='pub_date',
        ),
    ]