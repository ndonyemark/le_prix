# Generated by Django 3.0.7 on 2020-06-06 21:09

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('awardsapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='project_pub_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
