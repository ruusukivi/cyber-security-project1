# Generated by Django 3.2.6 on 2021-12-27 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feedback_text', models.CharField(max_length=400)),
                ('pub_date', models.DateTimeField(verbose_name='date')),
            ],
        ),
    ]
