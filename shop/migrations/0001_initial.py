# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('name', models.CharField(verbose_name='name', max_length=100)),
                ('slogan', models.CharField(null=True, blank=True, verbose_name='slogan', max_length=150)),
                ('address', models.CharField(null=True, blank=True, verbose_name='address', max_length=75)),
                ('city', models.CharField(null=True, blank=True, verbose_name='city', max_length=20)),
                ('town_ship', models.CharField(null=True, blank=True, verbose_name='town ship', max_length=20)),
                ('zip_code', models.CharField(null=True, blank=True, verbose_name='zip code', max_length=10)),
                ('country', models.CharField(null=True, blank=True, verbose_name='country', max_length=20)),
                ('tax_number', models.CharField(verbose_name='utr', max_length=20)),
                ('phone', models.CharField(null=True, blank=True, verbose_name='phone', max_length=15)),
                ('email', models.EmailField(null=True, blank=True, verbose_name='email', max_length=75)),
                ('terms_use_privacy', models.TextField(null=True, blank=True, verbose_name='terms of use and privacy')),
                ('return_policy', models.TextField(null=True, blank=True, verbose_name='return policy')),
            ],
            options={
                'verbose_name': 'shop information',
            },
            bases=(models.Model,),
        ),
    ]
