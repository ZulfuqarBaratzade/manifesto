# Generated by Django 4.2.1 on 2023-06-23 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MainBanner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated_date', models.DateTimeField(auto_now=True, verbose_name='update_date')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='created_date')),
                ('name', models.CharField(blank=True, default='', max_length=254, verbose_name='name')),
                ('file', models.ImageField(blank=True, default='', upload_to='images/mainbanner', verbose_name='Image')),
            ],
            options={
                'verbose_name': 'Main Banner',
                'verbose_name_plural': 'Main Banner',
                'ordering': ('name',),
            },
        ),
    ]