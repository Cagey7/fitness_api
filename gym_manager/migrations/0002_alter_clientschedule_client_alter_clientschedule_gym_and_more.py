# Generated by Django 5.0.2 on 2024-04-07 16:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gym_manager', '0001_initial'),
        ('users', '0005_alter_client_height_alter_client_weight'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientschedule',
            name='client',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.client'),
        ),
        migrations.AlterField(
            model_name='clientschedule',
            name='gym',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='gym_manager.gym'),
        ),
        migrations.AlterField(
            model_name='clientschedule',
            name='trainer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.trainer'),
        ),
        migrations.AlterField(
            model_name='trainerschedule',
            name='gym',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='gym_manager.gym'),
        ),
        migrations.AlterField(
            model_name='trainerschedule',
            name='trainer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.trainer'),
        ),
        migrations.AlterUniqueTogether(
            name='trainerschedule',
            unique_together={('trainer', 'week_day')},
        ),
    ]