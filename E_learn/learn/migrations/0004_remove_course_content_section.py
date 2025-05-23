# Generated by Django 5.2 on 2025-05-12 05:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learn', '0003_course_content'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='content',
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('section', models.CharField(max_length=255)),
                ('content', models.TextField(blank=True)),
                ('order', models.PositiveIntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sections', to='learn.course')),
            ],
            options={
                'ordering': ['order'],
                'unique_together': {('course', 'order')},
            },
        ),
    ]
