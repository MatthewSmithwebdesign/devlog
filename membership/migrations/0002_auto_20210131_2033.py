# Generated by Django 3.1.4 on 2021-01-31 20:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('membership', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='membership',
            name='membership_type',
            field=models.CharField(choices=[('pre', 'Premium'), ('free', 'Free')], default='Free', max_length=7),
        ),
        migrations.AlterField(
            model_name='usermembership',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='users_user', to=settings.AUTH_USER_MODEL),
        ),
    ]
