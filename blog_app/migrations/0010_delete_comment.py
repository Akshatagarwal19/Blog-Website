# Generated by Django 4.2.1 on 2023-08-16 10:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0009_rename_messsage_comment_message_comment_blog'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Comment',
        ),
    ]
