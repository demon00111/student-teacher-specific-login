# Generated by Django 3.2.7 on 2022-04-08 06:01

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('account', '0004_auto_20220408_0601'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='user',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]