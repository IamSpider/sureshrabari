# Generated by Django 3.1.7 on 2021-04-07 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logic', '0002_eventsandtours_district'),
    ]

    operations = [
        migrations.CreateModel(
            name='contactUs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=50)),
                ('contact', models.TextField(max_length=100)),
                ('message', models.TextField(max_length=200)),
            ],
        ),
    ]
