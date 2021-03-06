# Generated by Django 2.2.7 on 2019-12-27 12:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('SchoolMap', '0006_auto_20191223_1731'),
        ('TimeTable', '0009_auto_20191226_2010'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subject',
            name='room',
        ),
        migrations.AlterModelOptions(
            name='lesson',
            options={'ordering': ['-day', 'course', 'time']},
        ),
        migrations.RemoveField(
            model_name='lesson',
            name='subject',
        ),
        migrations.AddField(
            model_name='lesson',
            name='is_extra',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='lesson',
            name='room',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='SchoolMap.Room', verbose_name='Кабинет'),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='course',
            field=models.SmallIntegerField(choices=[(51040, '5А'), (51041, '5Б'), (51042, '5В'), (51043, '5Г'), (61040, '6А'), (61041, '6Б'), (61042, '6В'), (61043, '6Г'), (71040, '7А'), (71041, '7Б'), (71042, '7В'), (71043, '7Г'), (81040, '8А'), (81041, '8Б'), (81042, '8В'), (81043, '8Г'), (91040, '9А'), (91041, '9Б'), (91042, '9В'), (91043, '9Г'), (101040, '10А'), (101041, '10Б'), (111040, '11А'), (111041, '11Б')], verbose_name='Класс'),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='day',
            field=models.CharField(choices=[(0, 'Понедельник'), (1, 'Вторник'), (2, 'Среда'), (3, 'Четверг'), (4, 'Пятница'), (5, 'Суббота')], max_length=20, verbose_name='День'),
        ),
        migrations.DeleteModel(
            name='Course',
        ),
        migrations.DeleteModel(
            name='Subject',
        ),
    ]
