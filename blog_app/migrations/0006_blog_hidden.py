# Generated by Django 4.1.5 on 2023-08-14 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0005_author_user_alter_author_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='hidden',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
