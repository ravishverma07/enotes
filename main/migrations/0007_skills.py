# Generated by Django 4.2.5 on 2024-01-26 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_note_is_public'),
    ]

    operations = [
        migrations.CreateModel(
            name='Skills',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('heading', models.TextField()),
                ('paragraph', models.TextField()),
                ('question', models.TextField()),
                ('answer', models.TextField()),
            ],
        ),
    ]
