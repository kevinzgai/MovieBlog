# Generated by Django 2.2 on 2019-07-03 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cinema', '0005_auto_20190703_0614'),
    ]

    operations = [
        migrations.CreateModel(
            name='cinema',
            fields=[
                ('names', models.CharField(max_length=256, verbose_name='影院名称')),
                ('cinemaCode', models.CharField(max_length=256, primary_key=True, serialize=False, verbose_name='影城编码')),
                ('systemName', models.CharField(max_length=50, null=True, verbose_name='票务系统')),
                ('maoyanId', models.IntegerField(null=True, verbose_name='猫眼id')),
                ('taopiaopiaoId', models.IntegerField(null=True, verbose_name='淘票票id')),
                ('readme', models.TextField(default='not thing', verbose_name='说明')),
            ],
            options={
                'verbose_name': '影城名称',
                'verbose_name_plural': '影城名称',
                'ordering': ['names'],
            },
        ),
        migrations.DeleteModel(
            name='ciname',
        ),
    ]
