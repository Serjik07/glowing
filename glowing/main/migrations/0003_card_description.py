# Generated by Django 4.2.3 on 2023-09-10 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_card_img_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='card',
            name='description',
            field=models.TextField(default=1, verbose_name='Description'),
            preserve_default=False,
        ),
    ]