# Generated by Django 4.2.5 on 2023-09-28 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='shopdb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CName', models.CharField(blank=True, max_length=100, null=True)),
                ('CDes', models.CharField(blank=True, max_length=100, null=True)),
                ('Cimage', models.ImageField(blank=True, null=True, upload_to='profile')),
            ],
        ),
    ]
