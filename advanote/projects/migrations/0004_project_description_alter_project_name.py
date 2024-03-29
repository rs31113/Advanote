# Generated by Django 4.2 on 2023-12-20 15:18

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        (
            "projects",
            "0003_remove_project_members_remove_project_note_and_more",
        ),
    ]

    operations = [
        migrations.AddField(
            model_name="project",
            name="description",
            field=models.TextField(
                blank=True,
                help_text="Введите описание проекта",
                null=True,
                verbose_name="описание",
            ),
        ),
        migrations.AlterField(
            model_name="project",
            name="name",
            field=models.CharField(
                help_text="Максимально 150 символов",
                max_length=150,
                verbose_name="название",
            ),
        ),
    ]


__all__ = ()
