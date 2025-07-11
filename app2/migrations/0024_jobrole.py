# Generated by Django 5.0.2 on 2025-06-17 08:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app2', '0023_department'),
    ]

    operations = [
        migrations.CreateModel(
            name='JobRole',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(help_text='Separate each point with a new line')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app2.department')),
            ],
        ),
    ]
