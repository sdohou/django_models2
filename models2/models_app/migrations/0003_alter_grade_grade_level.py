# Generated by Django 3.2.3 on 2021-05-20 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('models_app', '0002_rename_grade_type_grade_grade_level'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grade',
            name='grade_level',
            field=models.CharField(max_length=50),
        ),
    ]
