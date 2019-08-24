# Generated by Django 2.2.4 on 2019-08-23 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_auto_20190823_1947'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='url',
            new_name='view_url',
        ),
        migrations.AddField(
            model_name='project',
            name='code_url',
            field=models.CharField(default='', max_length=20),
        ),
    ]