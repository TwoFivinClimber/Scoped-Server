# Generated by Django 4.1.6 on 2023-02-09 03:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('scoped_api', '0002_alter_userskill_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='job',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='job_messages', to='scoped_api.job'),
        ),
    ]
