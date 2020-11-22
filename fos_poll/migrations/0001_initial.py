# Generated by Django 2.2.10 on 2020-11-22 00:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Poll',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('date_of_begin', models.DateField()),
                ('date_of_end', models.DateField()),
                ('description', models.TextField(blank=True, max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length=200)),
                ('answer_type', models.CharField(choices=[('o', 'Выбрать один'), ('f', 'Выбрать несколько'), ('t', 'Текст')], default='Выбрать один', max_length=50)),
                ('poll', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='fos_poll.Poll')),
            ],
        ),
    ]
