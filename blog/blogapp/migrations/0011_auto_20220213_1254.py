# Generated by Django 3.2.9 on 2022-02-13 07:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0010_importantpoints'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='post_image',
        ),
        migrations.AddField(
            model_name='post',
            name='thumbnail',
            field=models.ImageField(null=True, upload_to='post/post-thumbnail/'),
        ),
        migrations.CreateModel(
            name='PostImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.ImageField(null=True, upload_to='post/post-images')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blogapp.post')),
            ],
        ),
    ]