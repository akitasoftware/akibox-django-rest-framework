# Generated by Django 3.1.6 on 2021-02-03 01:47

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.CharField(default=uuid.UUID('d632f5a6-65c1-11eb-81f4-3e22fb0d93ba'), max_length=128, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('contents', models.TextField()),
            ],
            options={
                'ordering': ['created_at'],
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.CharField(default=uuid.UUID('d632e1e2-65c1-11eb-81f4-3e22fb0d93ba'), max_length=128, primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=128)),
                ('last_name', models.CharField(max_length=128)),
                ('email', models.CharField(max_length=256)),
                ('phone', models.CharField(max_length=128)),
            ],
            options={
                'ordering': ['last_name'],
            },
        ),
    ]