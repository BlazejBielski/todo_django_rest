# Generated by Django 4.1.3 on 2022-11-27 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TodoList',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=150)),
                ('done', models.BooleanField()),
                ('author_ip', models.CharField(max_length=15)),
                ('create_date', models.DateTimeField()),
                ('done_date', models.DateTimeField()),
            ],
        ),
    ]
