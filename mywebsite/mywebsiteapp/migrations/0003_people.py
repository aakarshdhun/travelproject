# Generated by Django 4.1.1 on 2022-09-23 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mywebsiteapp', '0002_alter_place_desc'),
    ]

    operations = [
        migrations.CreateModel(
            name='people',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('image', models.ImageField(upload_to='picture')),
                ('about', models.TextField()),
            ],
        ),
    ]