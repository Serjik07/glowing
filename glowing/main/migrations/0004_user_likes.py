# Generated by Django 4.2.3 on 2023-09-16 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_card_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='User_likes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField(verbose_name='user_id')),
                ('card_id', models.IntegerField(verbose_name='card_id')),
            ],
            options={
                'verbose_name': 'Like',
                'verbose_name_plural': 'Likes',
            },
        ),
    ]
