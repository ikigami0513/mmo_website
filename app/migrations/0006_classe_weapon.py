# Generated by Django 4.2.1 on 2023-10-04 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_classe_icon_race_icon'),
    ]

    operations = [
        migrations.AddField(
            model_name='classe',
            name='weapon',
            field=models.CharField(choices=[('epees', 'Épées'), ('arcs', 'Arcs'), ('lances', 'Lances')], max_length=30, null=True),
        ),
    ]