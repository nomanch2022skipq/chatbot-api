# Generated by Django 5.2 on 2025-04-29 11:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bots', '0002_delete_botchannels_alter_botsagent_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='botsagent',
            name='channels',
        ),
    ]
