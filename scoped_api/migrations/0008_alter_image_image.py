# Generated by Django 4.1.6 on 2023-02-25 02:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scoped_api', '0007_alter_userskill_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.CharField(max_length=100),
        ),
    ]