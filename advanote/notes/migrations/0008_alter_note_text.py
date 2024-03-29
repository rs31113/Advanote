# Generated by Django 4.2 on 2023-12-22 22:10

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("notes", "0007_alter_note_tags"),
    ]

    operations = [
        migrations.AlterField(
            model_name="note",
            name="text",
            field=models.TextField(
                blank=True,
                help_text="Запишите сюда текст заметки",
                null=True,
                verbose_name="текст заметки",
            ),
        ),
    ]


__all__ = ()
