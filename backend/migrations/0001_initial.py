# Generated by Django 2.2.2 on 2019-07-08 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FirstName', models.CharField(max_length=38, null=True)),
                ('Surname', models.CharField(max_length=38, null=True)),
                ('Role', models.CharField(max_length=38, null=True)),
                ('EmailAddress', models.EmailField(max_length=254, null=True)),
                ('MobileNumber', models.DecimalField(decimal_places=0, max_digits=11, null=True)),
                ('Password', models.CharField(max_length=38, null=True)),
                ('ConfirmPassword', models.CharField(max_length=38, null=True)),
            ],
        ),
    ]
