# Generated by Django 3.2.6 on 2021-12-27 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_rename_author_feedback_author_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='feedback',
            name='author_id',
        ),
        migrations.AddField(
            model_name='feedback',
            name='nickname',
            field=models.CharField(default=None, max_length=200),
        ),
    ]
