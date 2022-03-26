# Generated by Django 4.0.3 on 2022-03-26 15:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('habitapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tracker',
            name='habit',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='trackers', to=settings.AUTH_USER_MODEL),
        ),
    ]
