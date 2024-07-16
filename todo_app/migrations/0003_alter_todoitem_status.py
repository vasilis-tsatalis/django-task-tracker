# Generated by Django 5.0.7 on 2024-07-16 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_app', '0002_todoitem_notes_todoitem_status_todolist_created_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todoitem',
            name='status',
            field=models.CharField(choices=[('OPEN', 'OPEN'), ('IN PROGRESS', 'IN PROGRESS'), ('PENDING', 'PENDING'), ('CLOSED', 'CLOSED')], default='OPEN', max_length=20),
        ),
    ]
