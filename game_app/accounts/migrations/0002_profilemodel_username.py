# Generated by Django 4.1.3 on 2023-06-19 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profilemodel',
            name='username',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
