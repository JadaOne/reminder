# Generated by Django 3.1.4 on 2020-12-08 21:24

import django.contrib.auth.models
from django.db import migrations, models
import django.utils.timezone
import reminder.apps.users.utils.validators
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('updated_at', models.DateTimeField(auto_now=True, db_index=True)),
                ('pub_id', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, unique=True)),
                ('is_active', models.BooleanField(db_index=True, default=True, help_text='If checked, this object is active. Uncheck to soft delete this object but not any child or related objects.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Date joined')),
                ('email', models.EmailField(db_index=True, max_length=254, unique=True, validators=[reminder.apps.users.utils.validators.validate_email], verbose_name='Email address')),
                ('first_name', models.CharField(db_index=True, max_length=32)),
                ('last_name', models.CharField(db_index=True, max_length=32)),
            ],
            options={
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
