# Generated by Django 3.2.3 on 2023-07-18 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0008_auto_20230717_1717'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='update_date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='task_status',
            field=models.CharField(choices=[('New', 'Создана'), ('In_Progress', 'В работе'), ('Completed', 'Ответ')], default='New', max_length=12),
        ),
    ]