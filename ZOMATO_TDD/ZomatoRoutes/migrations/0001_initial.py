# Generated by Django 4.2.4 on 2023-08-17 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dishname', models.CharField()),
                ('price', models.PositiveIntegerField()),
                ('available', models.CharField()),
            ],
        ),
    ]
