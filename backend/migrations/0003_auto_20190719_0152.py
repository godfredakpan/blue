# Generated by Django 2.2.2 on 2019-07-19 00:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('backend', '0002_auto_20190717_2342'),
    ]

    operations = [
        migrations.CreateModel(
            name='personalinformation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('MiddleName', models.CharField(max_length=32)),
                ('MobileNumber2', models.IntegerField(null=True)),
                ('DateOfBirth', models.DateField(null=True)),
                ('MaritalStatus', models.CharField(max_length=50)),
                ('PlaceOfBirth', models.CharField(max_length=100)),
                ('NumberOfDependent', models.IntegerField(null=True)),
                ('DateAtAddress', models.DateField(null=True)),
                ('HomeAddress', models.TextField(null=True)),
                ('email', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='user',
        ),
    ]