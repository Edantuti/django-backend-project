# Generated by Django 4.1 on 2022-08-13 11:17

import apps.courses.models
import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_alter_enroll_managers'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='enroll',
            options={'verbose_name': 'enroll'},
        ),
        migrations.AlterField(
            model_name='course',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 13, 11, 17, 0, 65816, tzinfo=datetime.timezone.utc)),
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('video', models.FileField(upload_to='videos')),
                ('created_at', models.DateTimeField(default=datetime.datetime(2022, 8, 13, 11, 17, 0, 67299, tzinfo=datetime.timezone.utc))),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.course')),
            ],
            options={
                'verbose_name': 'video',
            },
            managers=[
                ('objects', apps.courses.models.VideoManager()),
            ],
        ),
    ]
