# Generated by Django 3.2.3 on 2023-07-17 17:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0015_alter_task_update_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='update_date',
        ),
    ]