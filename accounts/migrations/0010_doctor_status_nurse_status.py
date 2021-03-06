# Generated by Django 4.0.4 on 2022-06-06 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_patient_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='status',
            field=models.SmallIntegerField(choices=[(0, 'New'), (1, 'Approved'), (2, 'Rejected')], default=0),
        ),
        migrations.AddField(
            model_name='nurse',
            name='status',
            field=models.SmallIntegerField(choices=[(0, 'New'), (1, 'Approved'), (2, 'Rejected')], default=0),
        ),
    ]
