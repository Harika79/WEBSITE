# Generated by Django 4.2.11 on 2024-03-13 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app2', '0004_remove_book_url_book_pdf_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchasedetail',
            name='credit_card',
            field=models.CharField(default=123566, max_length=16),
        ),
    ]
