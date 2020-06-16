# Generated by Django 3.0.5 on 2020-04-18 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
                ('energy_class', models.IntegerField(blank=True, choices=[(10, 'A+++'), (9, 'A++'), (8, 'A+'), (7, 'A'), (6, 'B'), (5, 'C'), (4, 'D'), (3, 'E'), (2, 'F'), (1, 'G')], null=True)),
                ('price', models.IntegerField()),
                ('note', models.TextField(blank=True, max_length=500, null=True)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('last_mod', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['create_date'],
            },
        ),
    ]
