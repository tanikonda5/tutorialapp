# Generated by Django 2.0.5 on 2018-06-29 01:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('description', models.TextField(blank=True, null=True)),
                ('slug', models.SlugField(max_length=250, unique=True)),
                ('active', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('video', models.TextField(blank=True, null=True)),
                ('content', models.TextField(blank=True, null=True)),
                ('slug', models.SlugField(max_length=250, unique=True)),
                ('free_preview', models.BooleanField(default=False)),
                ('active', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='StudentExperience',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('experience_level', models.CharField(choices=[('Beginner', 'Beginner'), ('Intermediate', 'Intermediate'), ('Advanced', 'Advanced')], default='Beginner', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='TutorialSeries',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('description', models.TextField(blank=True, null=True)),
                ('archived', models.BooleanField(default=False)),
                ('slug', models.SlugField(max_length=250, unique=True)),
                ('language', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tutorial.Language')),
                ('studentExperience', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tutorial.StudentExperience')),
            ],
        ),
        migrations.AddField(
            model_name='lesson',
            name='tutorial_series',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tutorial.TutorialSeries'),
        ),
    ]
