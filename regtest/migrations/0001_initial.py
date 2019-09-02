# Generated by Django 2.2.4 on 2019-09-02 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserTest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('username', models.CharField(max_length=255)),
                ('password_hash', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('phone_number', models.CharField(max_length=255)),
                ('first_name', models.CharField(default='First_Name', max_length=255)),
                ('last_name', models.CharField(default='Last_Name', max_length=255)),
                ('description', models.CharField(blank=True, max_length=255)),
                ('verification_status', models.CharField(max_length=255)),
                ('profile_picture', models.TextField()),
            ],
            options={
                'ordering': ['created'],
            },
        ),
    ]
