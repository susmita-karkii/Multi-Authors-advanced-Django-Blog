# Generated by Django 3.1.5 on 2021-05-11 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_auto_20210511_1947'),
    ]

    operations = [
        migrations.AddField(
            model_name='catagory',
            name='description',
            field=models.CharField(max_length=500, null=True, verbose_name='Description'),
        ),
        migrations.AddField(
            model_name='catagory',
            name='image',
            field=models.CharField(max_length=300, null=True),
        ),
    ]