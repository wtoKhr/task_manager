# Generated by Django 3.2.3 on 2023-07-17 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0005_task_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='task_status',
            field=models.CharField(choices=[('New', 'Создана'), ('In_Progress', 'В работе'), ('Completed', 'Ответ')], default=('New', 'Создана'), max_length=12),
        ),
    ]