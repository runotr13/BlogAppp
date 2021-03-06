# Generated by Django 4.0.4 on 2022-05-31 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfiletwo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=30)),
                ('Image', models.ImageField(blank=True, upload_to='profile_pics')),
                ('bio', models.TextField(blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='userprofile',
            name='avatar',
            field=models.ImageField(default='default.jpg', upload_to='profile_images'),
        ),
    ]
