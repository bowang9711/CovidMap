# Generated by Django 4.0.2 on 2022-02-05 13:18

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('covidmap', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Marker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('location', django.contrib.gis.db.models.fields.PointField(srid=4326)),
            ],
        ),
        migrations.AlterField(
            model_name='covidinfor',
            name='activecases',
            field=models.TextField(blank=True, db_column='ActiveCases', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='covidinfor',
            name='country',
            field=models.TextField(blank=True, db_column='Country', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='covidinfor',
            name='deaths_1m_pop',
            field=models.TextField(blank=True, db_column='Deaths_1M_pop', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='covidinfor',
            name='newcases',
            field=models.TextField(blank=True, db_column='NewCases', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='covidinfor',
            name='newdeaths',
            field=models.TextField(blank=True, db_column='NewDeaths', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='covidinfor',
            name='newrecovered',
            field=models.TextField(blank=True, db_column='NewRecovered', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='covidinfor',
            name='seriouscritical',
            field=models.TextField(blank=True, db_column='SeriousCritical', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='covidinfor',
            name='totalcases',
            field=models.TextField(blank=True, db_column='TotalCases', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='covidinfor',
            name='totaldeaths',
            field=models.TextField(blank=True, db_column='TotalDeaths', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='covidinfor',
            name='totalrecovered',
            field=models.TextField(blank=True, db_column='TotalRecovered', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='covidinfor',
            name='totaltests',
            field=models.TextField(blank=True, db_column='TotalTests', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='covidinfor',
            name='totcases_1m_pop',
            field=models.TextField(blank=True, db_column='TotCases_1M_pop', max_length=20, null=True),
        ),
    ]