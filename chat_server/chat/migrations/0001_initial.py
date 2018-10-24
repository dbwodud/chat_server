# Generated by Django 2.1.2 on 2018-10-24 22:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chat', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_name', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='chat',
            name='room_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chat.Room'),
        ),
    ]