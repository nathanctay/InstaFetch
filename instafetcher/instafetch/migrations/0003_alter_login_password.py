# Generated by Django 4.1.6 on 2023-03-25 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instafetch', '0002_login'),
    ]

    operations = [
        migrations.AlterField(
            model_name='login',
            name='password',
            field=models.CharField(max_length=50),
        ),
    ]
