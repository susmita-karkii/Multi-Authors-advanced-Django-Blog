# Generated by Django 3.1.5 on 2021-04-24 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='auth_status',
            field=models.CharField(max_length=100, null=True),
        ),
    ]