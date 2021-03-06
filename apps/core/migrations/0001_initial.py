# Generated by Django 3.2 on 2021-04-15 23:34

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_on', models.DateTimeField(auto_now_add=True, verbose_name='Created on')),
                ('updated_on', models.DateTimeField(auto_now=True, verbose_name='Updated_on')),
                ('active', models.BooleanField(default=True, verbose_name='active')),
                ('filename', models.CharField(blank=True, max_length=128, verbose_name='filename')),
                ('function_name', models.CharField(blank=True, max_length=128, verbose_name='function name')),
                ('level_name', models.CharField(blank=True, max_length=32, verbose_name='level name')),
                ('level_number', models.PositiveSmallIntegerField(default=0, verbose_name='level number')),
                ('line_number', models.PositiveSmallIntegerField(default=0, verbose_name='line number')),
                ('message', models.TextField(blank=True, null=True, verbose_name='message')),
                ('module', models.CharField(blank=True, max_length=128, null=True, verbose_name='module')),
                ('path', models.CharField(blank=True, max_length=255, verbose_name='path')),
                ('stack_info', models.TextField(blank=True, null=True, verbose_name='stack')),
                ('args', models.TextField(blank=True, verbose_name='args')),
            ],
            options={
                'ordering': ('-created_on',),
            },
        ),
    ]
