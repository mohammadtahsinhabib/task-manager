# Generated by Django 5.0.1 on 2025-07-12 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("tasks", "0008_task_assigned_to_alter_task_status"),
    ]

    operations = [
        migrations.AlterField(
            model_name="task",
            name="status",
            field=models.CharField(
                choices=[
                    ("Pending", "PENDING"),
                    ("IN_PROGRESS", "In Progress"),
                    ("Completed", "COMPLETED"),
                ],
                default="PENDING",
                max_length=15,
            ),
        ),
    ]
