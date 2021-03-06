# Generated by Django 4.0.1 on 2022-02-02 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Covidinfor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.TextField(blank=True, db_column='Country', null=True)),
                ('totalcases', models.TextField(blank=True, db_column='TotalCases', null=True)),
                ('newcases', models.TextField(blank=True, db_column='NewCases', null=True)),
                ('totaldeaths', models.TextField(blank=True, db_column='TotalDeaths', null=True)),
                ('newdeaths', models.TextField(blank=True, db_column='NewDeaths', null=True)),
                ('totalrecovered', models.TextField(blank=True, db_column='TotalRecovered', null=True)),
                ('newrecovered', models.TextField(blank=True, db_column='NewRecovered', null=True)),
                ('activecases', models.TextField(blank=True, db_column='ActiveCases', null=True)),
                ('seriouscritical', models.TextField(blank=True, db_column='SeriousCritical', null=True)),
                ('totcases_1m_pop', models.TextField(blank=True, db_column='TotCases_1M_pop', null=True)),
                ('deaths_1m_pop', models.TextField(blank=True, db_column='Deaths_1M_pop', null=True)),
                ('totaltests', models.TextField(blank=True, db_column='TotalTests', null=True)),
            ],
        ),
    ]
