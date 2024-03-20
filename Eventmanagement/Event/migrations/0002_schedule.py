# Generated by Django 4.2.2 on 2023-07-05 16:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Speaker', '0002_remove_speaker_created_remove_speaker_updated'),
        ('Event', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic', models.CharField(max_length=200)),
                ('startDate', models.DateTimeField()),
                ('endDate', models.DateTimeField()),
                ('speaker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Speaker.speaker')),
            ],
        ),
    ]
