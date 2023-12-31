# Generated by Django 4.2.4 on 2023-08-06 13:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=64)),
                ('last_name', models.CharField(max_length=64)),
                ('contact', models.CharField(max_length=14)),
            ],
        ),
        migrations.CreateModel(
            name='address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street', models.CharField(max_length=100)),
                ('landmark', models.CharField(blank=True, max_length=100, null=True)),
                ('state', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=100)),
                ('belongs_to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.user')),
            ],
        ),
    ]
