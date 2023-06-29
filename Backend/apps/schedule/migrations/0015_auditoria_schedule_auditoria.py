# Generated by Django 4.2.2 on 2023-06-29 09:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0014_remove_cancelinggroupclass_group_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Auditoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10, verbose_name='Аудитория')),
            ],
            options={
                'verbose_name': 'Айдитория',
                'verbose_name_plural': 'Аудитории',
            },
        ),
        migrations.AddField(
            model_name='schedule',
            name='auditoria',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='SET_NULL', to='schedule.auditoria', verbose_name='Аудитория'),
        ),
    ]