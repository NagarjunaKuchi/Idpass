# Generated by Django 3.2.15 on 2022-09-08 04:25

import django.core.validators
from django.db import migrations, models
import django.utils.timezone
import model_utils.fields
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('title', models.CharField(max_length=50, verbose_name='Title')),
                ('front_svg', models.FileField(upload_to='cards/', validators=[django.core.validators.FileExtensionValidator(['svg'])])),
                ('back_svg', models.FileField(upload_to='cards/', validators=[django.core.validators.FileExtensionValidator(['svg'])])),
                ('uuid', models.UUIDField(db_index=True, default=uuid.uuid4)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
