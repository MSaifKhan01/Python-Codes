# Generated by Django 5.0.6 on 2024-05-12 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CrudApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='address',
            field=models.CharField(max_length=265),
        ),
    ]