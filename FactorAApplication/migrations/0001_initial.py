# Generated by Django 3.2.7 on 2021-10-15 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('auto_increment_id', models.AutoField(primary_key=True, serialize=False)),
                ('score', models.FloatField(default=None)),
                ('title', models.TextField(default=None)),
            ],
        ),
    ]
