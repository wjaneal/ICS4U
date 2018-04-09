# Generated by Django 2.0.2 on 2018-04-01 20:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0006_remove_post_subject'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='subject',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='catagory', to='post.ProgrammingCategory'),
        ),
    ]
