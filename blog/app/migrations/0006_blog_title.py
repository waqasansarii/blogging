# Generated by Django 5.1.2 on 2024-10-31 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_alter_category_name_blog'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='title',
            field=models.CharField(default='', max_length=30),
            preserve_default=False,
        ),
    ]
