# Generated by Django 3.2.5 on 2021-07-15 01:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=400)),
                ('title', models.CharField(max_length=400)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='photos/')),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=400)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('activity_list', models.CharField(choices=[('completed', 'completed'), ('ongoing', 'ongoing'), ('stalled', 'stalled')], max_length=50)),
                ('description', models.TextField()),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.team')),
            ],
        ),
    ]
