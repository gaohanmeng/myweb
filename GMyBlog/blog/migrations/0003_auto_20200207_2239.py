# Generated by Django 2.2 on 2020-02-07 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20200207_2013'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=50, verbose_name='标题'),
        ),
    ]
