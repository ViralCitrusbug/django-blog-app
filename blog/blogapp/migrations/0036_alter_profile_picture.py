# Generated by Django 3.2.5 on 2022-02-24 05:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0035_rename_topic_1_post_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='picture',
            field=models.ImageField(default='default-profile/default-profile.png', upload_to='user/profile/profile-pic'),
        ),
    ]
