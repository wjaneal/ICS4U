# Generated by Django 2.0.2 on 2018-04-02 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0008_auto_20180401_1639'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='subject',
        ),
        migrations.AddField(
            model_name='post',
            name='Catagory',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.DeleteModel(
            name='ProgrammingCategory',
        ),
    ]
