# Generated by Django 2.0.2 on 2018-04-01 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0004_auto_20180401_1537'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='subject',
            field=models.CharField(default='', max_length=200),
        ),
    ]