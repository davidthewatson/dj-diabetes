# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-06 10:39
from __future__ import unicode_literals

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('body', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('date_appointments', models.DateField(null=True)),
                ('hour_appointments', models.TimeField(null=True)),
                ('recall_one_duration', models.IntegerField(null=True)),
                ('recall_two_duration', models.IntegerField(null=True)),
                ('recall_one_unit', models.IntegerField(null=True)),
                ('recall_two_unit', models.IntegerField(null=True)),
            ],
            options={
                'verbose_name_plural': 'Appointments',
                'verbose_name': 'Appointments',
            },
        ),
        migrations.CreateModel(
            name='AppointmentTypes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, unique=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Appointment Types',
                'verbose_name': 'Appointment Types',
            },
        ),
        migrations.CreateModel(
            name='ExaminationDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('value', models.DecimalField(decimal_places=5, max_digits=15)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Examination Details',
                'verbose_name': 'Examination Details',
            },
        ),
        migrations.CreateModel(
            name='Examinations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comments', models.TextField()),
                ('date_examinations', models.DateField()),
                ('hour_examinations', models.TimeField(null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Examinations',
                'verbose_name': 'Examinations',
            },
        ),
        migrations.CreateModel(
            name='ExaminationTypes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, unique=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Examination Types',
                'verbose_name': 'Examination Types',
            },
        ),
        migrations.CreateModel(
            name='Exercises',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('duration', models.FloatField()),
                ('date_exercises', models.DateField(null=True)),
                ('hour_exercises', models.TimeField(null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Foods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, unique=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Foods',
                'verbose_name': 'Foods',
            },
        ),
        migrations.CreateModel(
            name='Glucoses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('moment', models.IntegerField(null=True)),
                ('glucose', models.DecimalField(decimal_places=2, max_digits=5)),
                ('insulin', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
                ('comment', models.TextField()),
                ('date_glucoses', models.DateField()),
                ('hour_glucoses', models.TimeField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Glucoses',
                'verbose_name': 'Glucose',
            },
        ),
        migrations.CreateModel(
            name='Issues',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField()),
                ('question_to', models.CharField(max_length=255)),
                ('answer', models.TextField(blank=True, null=True)),
                ('date_answer', models.DateField(blank=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Issues',
                'verbose_name': 'Issues',
            },
        ),
        migrations.CreateModel(
            name='Meals',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('food', models.TextField()),
                ('breakfast_lunch_diner', models.CharField(max_length=2)),
                ('date_meals', models.DateField(null=True)),
                ('hour_meals', models.TimeField(null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Meals',
                'verbose_name': 'Meal',
            },
        ),
        migrations.CreateModel(
            name='Preferences',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(max_length=255)),
                ('title', models.CharField(max_length=255)),
                ('value', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Preferences',
                'verbose_name': 'Preference',
            },
        ),
        migrations.CreateModel(
            name='Sports',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, unique=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Sports',
                'verbose_name': 'Sports',
            },
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100)),
                ('birth_date', models.DateField(blank=True, null=True)),
                ('phone', models.CharField(blank=True, max_length=15)),
                ('address', models.TextField(blank=True, null=True)),
                ('zipcode', models.CharField(blank=True, max_length=50)),
                ('town', models.CharField(blank=True, max_length=255)),
                ('role', models.CharField(blank=True, max_length=250)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Weights',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weight', models.FloatField()),
                ('date_weights', models.DateField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Weights',
                'verbose_name': 'Weight',
            },
        ),
        migrations.AddField(
            model_name='exercises',
            name='sports',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dj_diabetes.Sports'),
        ),
        migrations.AddField(
            model_name='exercises',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='examinations',
            name='examination_types',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dj_diabetes.ExaminationTypes'),
        ),
        migrations.AddField(
            model_name='examinations',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='examinationdetails',
            name='examination',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dj_diabetes.Examinations'),
        ),
        migrations.AddField(
            model_name='appointments',
            name='appointment_types',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dj_diabetes.AppointmentTypes'),
        ),
        migrations.AddField(
            model_name='appointments',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
