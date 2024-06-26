# Generated by Django 4.2.1 on 2023-10-03 07:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0002_alter_armor_options_alter_boots_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Amulet',
            fields=[
                ('stuff_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='app.stuff')),
            ],
            options={
                'verbose_name': 'Amulette',
                'verbose_name_plural': 'Amulettes',
            },
            bases=('app.stuff',),
        ),
        migrations.CreateModel(
            name='Belt',
            fields=[
                ('stuff_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='app.stuff')),
            ],
            options={
                'verbose_name': 'Ceinture',
                'verbose_name_plural': 'Ceintures',
            },
            bases=('app.stuff',),
        ),
        migrations.CreateModel(
            name='Ring',
            fields=[
                ('stuff_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='app.stuff')),
            ],
            options={
                'verbose_name': 'Anneau',
                'verbose_name_plural': 'Anneaux',
            },
            bases=('app.stuff',),
        ),
        migrations.AddField(
            model_name='stuff',
            name='picture',
            field=models.ImageField(null=True, upload_to='items/'),
        ),
        migrations.AlterField(
            model_name='character',
            name='armor',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.armor', verbose_name='armure'),
        ),
        migrations.AlterField(
            model_name='character',
            name='boots',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.boots', verbose_name='bottes'),
        ),
        migrations.AlterField(
            model_name='character',
            name='classe',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.classe', verbose_name='classe'),
        ),
        migrations.AlterField(
            model_name='character',
            name='helmet',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.helmet', verbose_name='casque'),
        ),
        migrations.AlterField(
            model_name='character',
            name='left_gantelet',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='left_gantelet', to='app.gantelet', verbose_name='gant gauche'),
        ),
        migrations.AlterField(
            model_name='character',
            name='level',
            field=models.PositiveIntegerField(verbose_name='niveau'),
        ),
        migrations.AlterField(
            model_name='character',
            name='name',
            field=models.CharField(max_length=50, verbose_name='nom'),
        ),
        migrations.AlterField(
            model_name='character',
            name='pant',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.pant', verbose_name='pantalon'),
        ),
        migrations.AlterField(
            model_name='character',
            name='race',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.race', verbose_name='race'),
        ),
        migrations.AlterField(
            model_name='character',
            name='right_gantelet',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='right_gantelet', to='app.gantelet', verbose_name='gant droit'),
        ),
        migrations.AlterField(
            model_name='character',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='characters', to=settings.AUTH_USER_MODEL, verbose_name='utilisateur'),
        ),
        migrations.AlterField(
            model_name='classe',
            name='name',
            field=models.CharField(max_length=50, verbose_name='classe'),
        ),
        migrations.AlterField(
            model_name='race',
            name='name',
            field=models.CharField(max_length=50, verbose_name='nom'),
        ),
        migrations.AlterField(
            model_name='stats',
            name='attack',
            field=models.IntegerField(verbose_name='attaque'),
        ),
        migrations.AlterField(
            model_name='stats',
            name='defense',
            field=models.IntegerField(verbose_name='défense'),
        ),
        migrations.AlterField(
            model_name='stats',
            name='hp',
            field=models.IntegerField(verbose_name='points de vie'),
        ),
        migrations.AlterField(
            model_name='stats',
            name='luck',
            field=models.IntegerField(verbose_name='chance'),
        ),
        migrations.AlterField(
            model_name='stats',
            name='mana',
            field=models.IntegerField(verbose_name='mana'),
        ),
        migrations.AlterField(
            model_name='stats',
            name='speed',
            field=models.IntegerField(verbose_name='vitesse'),
        ),
        migrations.AlterField(
            model_name='stuff',
            name='name',
            field=models.CharField(max_length=50, verbose_name='nom'),
        ),
        migrations.AlterField(
            model_name='stuff',
            name='required_level',
            field=models.PositiveIntegerField(verbose_name='niveau requis'),
        ),
    ]
