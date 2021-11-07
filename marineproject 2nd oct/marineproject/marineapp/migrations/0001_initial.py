# Generated by Django 3.2.8 on 2021-11-07 08:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Hangman',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.CharField(max_length=250)),
                ('word_hint', models.TextField(blank=True, max_length=100)),
            ],
            options={
                'ordering': ['word'],
            },
        ),
        migrations.CreateModel(
            name='Module1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=2000)),
                ('right_option', models.CharField(max_length=1000)),
                ('first_wrong_option', models.CharField(max_length=1000)),
                ('second_wrong_option', models.CharField(max_length=1000)),
                ('third_wrong_option', models.CharField(max_length=1000)),
                ('explanation', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Module2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=2000)),
                ('right_option', models.CharField(max_length=1000)),
                ('first_wrong_option', models.CharField(max_length=1000)),
                ('second_wrong_option', models.CharField(max_length=1000)),
                ('third_wrong_option', models.CharField(max_length=1000)),
                ('explanation', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Module3',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word1', models.CharField(max_length=250)),
                ('word2', models.CharField(max_length=250)),
                ('question', models.CharField(max_length=2000)),
                ('right_option', models.CharField(max_length=1000)),
                ('first_wrong_option', models.CharField(max_length=1000)),
                ('second_wrong_option', models.CharField(max_length=1000)),
                ('third_wrong_option', models.CharField(max_length=1000)),
                ('explanation', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Module4',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hangman_word', models.CharField(max_length=250)),
                ('question', models.CharField(max_length=2000)),
                ('right_option', models.CharField(max_length=1000)),
                ('first_wrong_option', models.CharField(max_length=1000)),
                ('second_wrong_option', models.CharField(max_length=1000)),
                ('third_wrong_option', models.CharField(max_length=1000)),
                ('explanation', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Module5',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hangman_word', models.CharField(max_length=250)),
                ('question', models.CharField(max_length=2000)),
                ('right_option', models.CharField(max_length=1000)),
                ('first_wrong_option', models.CharField(max_length=1000)),
                ('second_wrong_option', models.CharField(max_length=1000)),
                ('third_wrong_option', models.CharField(max_length=1000)),
                ('explanation', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=250, verbose_name='Full Name')),
                ('email', models.EmailField(max_length=254)),
                ('hr', models.BooleanField(default=False, verbose_name='HR')),
                ('trainer', models.BooleanField(default=False, verbose_name='Trainer')),
                ('trainee', models.BooleanField(default=False, verbose_name='Trainee')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.CharField(max_length=100, unique=True)),
                ('question_relation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='marineapp.hangman')),
            ],
        ),
    ]
