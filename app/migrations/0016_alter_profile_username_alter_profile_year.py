# Generated by Django 4.2.3 on 2023-08-18 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0015_profile_college_profile_year'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='username',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='profile',
            name='year',
            field=models.CharField(max_length=20, null=True),
        ),
    ]