# Generated by Django 4.0 on 2021-12-13 21:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('encyclopedia', '0002_rename_body_articles_textarea'),
    ]

    operations = [
        migrations.RenameField(
            model_name='articles',
            old_name='created_at',
            new_name='created_on',
        ),
        migrations.RenameField(
            model_name='articles',
            old_name='updated_at',
            new_name='updated_on',
        ),
    ]
