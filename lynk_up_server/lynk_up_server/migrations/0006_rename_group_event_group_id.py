# Generated by Django 4.2.1 on 2023-05-23 20:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lynk_up_server', '0005_remove_friend_friend_id_friend_friend'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='group',
            new_name='group_id',
        ),
    ]
