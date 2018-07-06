# Generated by Django 2.0.7 on 2018-07-06 13:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Parking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_free', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Zone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('zone_id', models.CharField(max_length=1)),
                ('description', models.CharField(max_length=30)),
                ('parking', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parking.Parking')),
            ],
        ),
        migrations.AddField(
            model_name='place',
            name='zone',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parking.Zone'),
        ),
    ]
