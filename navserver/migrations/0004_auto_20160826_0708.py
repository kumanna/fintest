# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-26 07:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('navserver', '0003_auto_20160826_0708'),
    ]

    operations = [
        migrations.CreateModel(
            name='MutualFund',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amfisymbol', models.CharField(max_length=10, unique=True)),
            ],
        ),
        migrations.AlterField(
            model_name='mutualfundnav',
            name='mf',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='nav', to='navserver.MutualFund'),
        ),
        migrations.DeleteModel(
            name='MutualFund2',
        ),
    ]
