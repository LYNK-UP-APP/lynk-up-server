# Generated by Django 4.2.1 on 2023-05-16 16:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lynk_up_server', '0002_friend_friend_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='lynk_up_server.user'),
            preserve_default=False,
        ),
    ]