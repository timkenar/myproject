# Generated by Django 5.0.6 on 2024-06-06 07:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_host_email_visitor_email'),
    ]

    operations = [
        migrations.RenameField(
            model_name='visitor',
            old_name='user',
            new_name='names',
        ),
    ]
