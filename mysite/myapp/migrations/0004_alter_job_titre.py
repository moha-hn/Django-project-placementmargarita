# Generated by Django 4.2.7 on 2024-01-06 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_alter_candidat_cv'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='titre',
            field=models.CharField(max_length=20),
        ),
    ]