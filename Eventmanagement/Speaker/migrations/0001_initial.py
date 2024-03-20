# Generated by Django 4.2.2 on 2023-07-02 06:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Speaker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('title', models.CharField(max_length=200)),
                ('biograph', models.TextField(blank=True, null=True)),
                ('profile_pic', models.ImageField(upload_to='speakerphoto/')),
                ('email', models.EmailField(max_length=254)),
                ('socialmedialink', models.URLField()),
                ('phone', models.IntegerField()),
                ('updated', models.DateTimeField(auto_now_add=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
