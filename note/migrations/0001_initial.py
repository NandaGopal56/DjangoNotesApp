# Generated by Django 4.0.4 on 2022-05-30 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField(blank=True, null=True)),
                ('updatedTime', models.DateTimeField(auto_now=True)),
                ('createdTime', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]