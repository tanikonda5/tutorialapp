# Generated by Django 2.0.5 on 2018-07-03 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutorial', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='lesson',
            name='length',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]
