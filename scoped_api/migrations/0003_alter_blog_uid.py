# Generated by Django 4.1.6 on 2023-03-23 22:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('scoped_api', '0002_alter_invite_company_alter_invite_uid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='uid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scoped_api.user'),
        ),
    ]
