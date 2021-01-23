# Generated by Django 3.1.5 on 2021-01-23 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainpage', '0003_auto_20210118_1641'),
    ]

    operations = [
        migrations.CreateModel(
            name='Add_ewaste',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=120)),
                ('Surname', models.CharField(max_length=120)),
                ('Ward', models.PositiveIntegerField()),
                ('Mob_number', models.PositiveBigIntegerField()),
                ('Email', models.CharField(max_length=120)),
                ('Address', models.TextField()),
                ('Image', models.ImageField(upload_to='images/')),
            ],
        ),
        migrations.DeleteModel(
            name='Login',
        ),
        migrations.DeleteModel(
            name='Register',
        ),
    ]
