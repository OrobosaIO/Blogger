# Generated by Django 4.0.1 on 2022-03-03 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_post_title_tag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='title_tag',
            field=models.CharField(max_length=255),
        ),
    ]