# Generated by Django 5.0.6 on 2025-01-30 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0002_alter_legacysubjects_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='description',
            field=models.CharField(blank=True, null=True),
        ),
    ]
