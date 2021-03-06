# Generated by Django 3.1.7 on 2021-03-24 20:56

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('roza', '0007_home'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contacts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('email', models.TextField()),
                ('subject', models.CharField(max_length=255)),
                ('phone_nr', models.CharField(max_length=255)),
                ('message', models.TextField(blank=True)),
                ('contact_date', models.DateTimeField(blank=True, default=django.utils.timezone.now)),
            ],
        ),
    ]
