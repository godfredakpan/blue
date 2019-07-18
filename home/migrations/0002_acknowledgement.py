# Generated by Django 2.2.2 on 2019-07-17 23:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Acknowledgement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('terms_and_conditions', models.CharField(blank=True, max_length=255)),
                ('how_you_heard_about_us', models.CharField(blank=True, max_length=255)),
                ('signature', models.ImageField(upload_to='signatures/')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
                ('user_id', models.ForeignKey(default='1', on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]