# Generated by Django 4.2.5 on 2023-10-25 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0002_registerdb1_delete_registerdb'),
    ]

    operations = [
        migrations.CreateModel(
            name='cartdb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Username', models.CharField(blank=True, max_length=20, null=True)),
                ('Productname', models.CharField(blank=True, max_length=20, null=True)),
                ('Description', models.CharField(blank=True, max_length=20, null=True)),
                ('Quantity', models.IntegerField(blank=True, null=True)),
                ('Totalprize', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]