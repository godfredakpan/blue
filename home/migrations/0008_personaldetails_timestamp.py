# Generated by Django 2.2.2 on 2019-07-13 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_contact'),
    ]

    operations = [
        migrations.AddField(
            model_name='personaldetails',
            name='timestamp',
            field=models.DateTimeField(auto_now=True),
        ),
    ]