# Generated by Django 2.0.7 on 2019-12-24 14:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('club', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='user',
            field=models.OneToOneField(db_constraint=False, on_delete=django.db.models.deletion.DO_NOTHING, related_name='order', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='club',
            name='creat_user',
            field=models.OneToOneField(db_constraint=False, default=1, on_delete=django.db.models.deletion.DO_NOTHING, related_name='club_user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='club',
            name='detail',
            field=models.OneToOneField(db_constraint=False, default=1, on_delete=django.db.models.deletion.CASCADE, to='club.Detail'),
        ),
        migrations.AddField(
            model_name='club',
            name='image',
            field=models.OneToOneField(db_constraint=False, on_delete=django.db.models.deletion.CASCADE, to='club.Images'),
        ),
    ]