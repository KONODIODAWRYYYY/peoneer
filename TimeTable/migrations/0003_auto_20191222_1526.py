# Generated by Django 2.2.7 on 2019-12-22 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TimeTable', '0002_auto_20191219_2108'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='course',
            field=models.SmallIntegerField(choices=[(50, '50А'), (51, '51Б'), (52, '52В'), (53, '53Г'), (54, '54А'), (55, '55Б'), (56, '56В'), (57, '57Г'), (58, '58А'), (59, '59Б'), (60, '60А'), (61, '61Б'), (62, '62В'), (63, '63Г'), (64, '64А'), (65, '65Б'), (66, '66В'), (67, '67Г'), (68, '68А'), (69, '69Б'), (70, '70А'), (71, '71Б'), (72, '72В'), (73, '73Г'), (74, '74А'), (75, '75Б'), (76, '76В'), (77, '77Г'), (78, '78А'), (79, '79Б'), (80, '80А'), (81, '81Б'), (82, '82В'), (83, '83Г'), (84, '84А'), (85, '85Б'), (86, '86В'), (87, '87Г'), (88, '88А'), (89, '89Б'), (90, '90А'), (91, '91Б'), (92, '92В'), (93, '93Г'), (94, '94А'), (95, '95Б'), (96, '96В'), (97, '97Г'), (98, '98А'), (99, '99Б'), (100, '100А'), (101, '101Б'), (102, '102В'), (103, '103Г'), (104, '104А'), (105, '105Б'), (106, '106В'), (107, '107Г'), (108, '108А'), (109, '109Б'), (110, '110А'), (111, '111Б')], default=100, max_length=3, verbose_name='Класс'),
        ),
    ]
