# Generated by Django 4.2.1 on 2023-05-16 02:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lynk_up_server', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='friend',
            name='friend_id',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]