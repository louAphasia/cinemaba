# Generated by Django 3.0.1 on 2020-01-14 21:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('worker', '0014_auto_20191229_1922'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='showtime',
            name='end_time',
        ),
        migrations.RemoveField(
            model_name='showtime',
            name='start_time',
        ),
        migrations.AlterField(
            model_name='reservation',
            name='showtime_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='worker.Showtime'),
        ),
        migrations.AlterField(
            model_name='showtime',
            name='end_date',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='showtime',
            name='start_date',
            field=models.DateTimeField(null=True),
        ),
    ]
