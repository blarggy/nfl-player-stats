# Generated by Django 2.0 on 2017-12-17 15:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nfl_data', '0003_game'),
    ]

    operations = [
        migrations.RenameField(
            model_name='game',
            old_name='kick_return_tocuhdowns',
            new_name='kick_return_touchdowns',
        ),
    ]