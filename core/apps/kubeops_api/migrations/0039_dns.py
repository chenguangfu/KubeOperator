# Generated by Django 2.1.11 on 2019-11-04 09:38

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('kubeops_api', '0038_auto_20191031_1052'),
    ]

    operations = [
        migrations.CreateModel(
            name='DNS',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('dns1', models.CharField(max_length=128, null=True)),
                ('dns2', models.CharField(max_length=128, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='Date created')),
            ],
            options={
                'ordering': ('-date_created',),
                'get_latest_by': 'date_created',
            },
        ),
    ]
