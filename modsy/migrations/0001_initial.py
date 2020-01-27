# Generated by Django 3.0.1 on 2020-01-06 09:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='design',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('image', models.ImageField(upload_to='images')),
                ('content', models.CharField(default='0000000', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='furniture',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('phrase', models.CharField(default='111111', max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='goal',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('goal', models.CharField(default='0000000', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='room',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('image', models.ImageField(upload_to='images')),
                ('content', models.CharField(default='0000000', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=50, unique=True)),
                ('password', models.CharField(default='0000000', max_length=50)),
                ('furn', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='modsy.furniture')),
                ('goal', models.ManyToManyField(to='modsy.goal')),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='modsy.room')),
                ('style', models.ManyToManyField(to='modsy.design')),
            ],
        ),
    ]
