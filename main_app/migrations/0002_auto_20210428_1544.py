# Generated by Django 3.2 on 2021-04-28 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CSV_FILE',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(blank=True)),
                ('file_name', models.FileField(upload_to='data_files')),
            ],
        ),
        migrations.DeleteModel(
            name='CSV',
        ),
    ]
