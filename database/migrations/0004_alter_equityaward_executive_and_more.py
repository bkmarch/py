# Generated by Django 5.1.3 on 2024-12-04 21:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0003_companies_alter_equityaward_executive_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equityaward',
            name='executive',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='equityaward', to='database.executive'),
        ),
        migrations.AlterField(
            model_name='executive',
            name='companies',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='executive', to='database.companies'),
        ),
    ]