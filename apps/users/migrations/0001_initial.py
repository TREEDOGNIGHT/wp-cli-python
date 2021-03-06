# Generated by Django 2.2.7 on 2019-12-04 15:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_login', models.CharField(max_length=50)),
                ('user_pass', models.CharField(max_length=50)),
                ('user_display_name', models.CharField(max_length=20)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('user_email', models.CharField(max_length=50)),
                ('user_status', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Options',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('op_value', models.CharField(max_length=50)),
                ('op_name', models.CharField(max_length=20)),
                ('User', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='users.User')),
            ],
        ),
    ]
