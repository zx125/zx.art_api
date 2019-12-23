# Generated by Django 2.0.7 on 2019-12-23 21:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0002_auto_20191223_1502'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='user',
            field=models.ForeignKey(db_constraint=False, default=1, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
