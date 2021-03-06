# Generated by Django 3.2.9 on 2022-02-14 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0014_post_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='postimage',
            name='post',
        ),
        migrations.RemoveField(
            model_name='post',
            name='short_description',
        ),
        migrations.RemoveField(
            model_name='post',
            name='thumbnail',
        ),
        migrations.RemoveField(
            model_name='post',
            name='user',
        ),
        migrations.AddField(
            model_name='post',
            name='post_image',
            field=models.ImageField(null=True, upload_to='post/post-image/'),
        ),
        migrations.DeleteModel(
            name='ImportantPoint',
        ),
        migrations.DeleteModel(
            name='PostImage',
        ),
    ]
