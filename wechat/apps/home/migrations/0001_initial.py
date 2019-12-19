# Generated by Django 2.0.7 on 2019-12-19 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_delete', models.BooleanField(default=False, verbose_name='是否删除')),
                ('is_show', models.BooleanField(default=True, verbose_name='是否上线')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('updated_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('title', models.CharField(max_length=16, verbose_name='标题')),
                ('link', models.CharField(max_length=64, verbose_name='链接')),
                ('image', models.ImageField(upload_to='banner', verbose_name='图片链接')),
                ('info', models.TextField(verbose_name='轮播图简介')),
                ('order', models.IntegerField(verbose_name='显示顺序')),
            ],
            options={
                'verbose_name_plural': '轮播图表',
                'db_table': 'zx_banner',
            },
        ),
    ]
