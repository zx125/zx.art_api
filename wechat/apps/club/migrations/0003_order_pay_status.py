# Generated by Django 2.0.7 on 2019-12-24 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('club', '0002_auto_20191224_1454'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='pay_status',
            field=models.SmallIntegerField(choices=[(0, '未付款'), (1, '已付款')], default=0),
        ),
    ]
