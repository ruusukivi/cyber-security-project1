# Generated by Django 3.2.6 on 2021-12-27 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0005_auto_20211227_1158'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='feedback_text',
            field=models.CharField(default='feedback', max_length=400),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='nickname',
            field=models.CharField(default='nickname', max_length=200),
        ),
    ]