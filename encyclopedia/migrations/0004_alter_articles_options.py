# Generated by Django 4.0 on 2021-12-14 01:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('encyclopedia', '0003_rename_created_at_articles_created_on_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='articles',
            options={'ordering': ['-created_on'], 'verbose_name_plural': 'Articles'},
        ),
    ]
