# Generated by Django 4.2.11 on 2024-03-10 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app3', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mynews',
            fields=[
                ('title', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('image', models.ImageField(upload_to='mynews_images/')),
                ('pdf', models.FileField(blank=True, null=True, upload_to='mynews_pdfs/')),
            ],
        ),
    ]
