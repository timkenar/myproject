# Generated by Django 5.0.6 on 2024-06-06 07:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_rename_user_visitor_names'),
    ]

    operations = [
        migrations.RenameField(
            model_name='visitor',
            old_name='names',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='host',
            name='user',
        ),
    ]
