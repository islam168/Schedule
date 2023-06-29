# Generated by Django 4.2.2 on 2023-06-28 21:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0009_alter_schedule_course_end_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedule',
            name='course_end_date',
            field=models.DateField(default=datetime.datetime(2023, 6, 28, 21, 17, 23, 355842, tzinfo=datetime.timezone.utc), verbose_name='День окончания курса'),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='course_start_date',
            field=models.DateField(default=datetime.datetime(2023, 6, 28, 21, 17, 23, 355842, tzinfo=datetime.timezone.utc), verbose_name='День начала курса'),
        ),
        migrations.AlterModelTable(
            name='schedule',
            table='schedule',
        ),
    ]