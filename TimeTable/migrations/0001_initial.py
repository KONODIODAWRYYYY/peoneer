# Generated by Django 2.2.7 on 2019-12-18 17:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('SchoolMap', '0004_auto_20191218_2228'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=30, verbose_name='Урок')),
                ('day', models.CharField(choices=[('Понедельник', 'Понедельник'), ('Вторник', 'Вторник'), ('Среда', 'Среда'), ('Четверг', 'Четверг'), ('Пятница', 'Пятница'), ('Суббота', 'Суббота')], default='Понедельник', max_length=20, verbose_name='День')),
                ('course', models.CharField(default='', max_length=3, verbose_name='Класс')),
                ('time', models.TimeField(verbose_name='Время')),
                ('room', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='SchoolMap.Room')),
            ],
        ),
    ]