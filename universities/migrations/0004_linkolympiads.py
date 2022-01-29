# Generated by Django 4.0.1 on 2022-01-29 12:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('universities', '0003_delete_linkolympiads'),
    ]

    operations = [
        migrations.CreateModel(
            name='LinkOlympiads',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('olymp', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='universities.olympiad')),
                ('univer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='universities.university')),
            ],
        ),
    ]
