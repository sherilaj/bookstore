# Generated by Django 5.0.2 on 2024-03-01 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookapp', '0005_message'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='EmailId',
            field=models.CharField(default=55, max_length=150),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='message',
            name='Message',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='message',
            name='Name',
            field=models.CharField(max_length=300),
        ),
    ]
