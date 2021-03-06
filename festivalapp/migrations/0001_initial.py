# Generated by Django 2.1.8 on 2019-05-21 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=20)),
                ('contents', models.TextField(verbose_name='contents')),
                ('pwd', models.CharField(default='', max_length=8, verbose_name='password')),
                ('posted_date', models.DateTimeField(auto_now_add=True, verbose_name='posted_date')),
                ('commented_post', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=100, verbose_name='title')),
                ('owner_name', models.CharField(default='', max_length=20)),
                ('contents', models.TextField(verbose_name='contents')),
                ('owner_pwd', models.CharField(default='', max_length=8, verbose_name='password')),
                ('posted_date', models.DateTimeField(auto_now_add=True, verbose_name='posted_date')),
                ('image_url', models.URLField(default='', max_length=1000, verbose_name='imageurl')),
                ('image', models.FileField(blank=True, null=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Pub',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=100, verbose_name='title')),
                ('description', models.TextField(verbose_name='description')),
                ('section', models.CharField(max_length=2)),
                ('location', models.CharField(max_length=10)),
                ('time', models.CharField(max_length=10)),
                ('date', models.CharField(max_length=10)),
                ('image_booth', models.FileField(blank=True, null=True, upload_to='')),
            ],
        ),
    ]
