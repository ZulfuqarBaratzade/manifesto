# Generated by Django 4.2.1 on 2023-06-23 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_drink'),
    ]

    operations = [
        migrations.CreateModel(
            name='TextGoal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated_date', models.DateTimeField(auto_now=True, verbose_name='update_date')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='created_date')),
                ('name', models.CharField(blank=True, default='', max_length=254, verbose_name='name')),
                ('description', models.CharField(blank=True, default='', max_length=254, verbose_name='description')),
            ],
            options={
                'verbose_name': 'Text Goal',
                'verbose_name_plural': 'Text Goal',
                'ordering': ('name',),
            },
        ),
    ]
