# Generated by Django 3.1 on 2020-08-25 07:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0003_auto_20200825_1317'),
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('docID', models.IntegerField(default=1, primary_key=True, serialize=False, unique=True)),
                ('docTitle', models.CharField(max_length=20)),
                ('docDescription', models.CharField(max_length=50)),
                ('docLink', models.CharField(max_length=100)),
                ('docCreatedon', models.DateTimeField()),
                ('docStatus', models.CharField(max_length=20)),
                ('docRemark', models.CharField(max_length=50)),
                ('usrID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.user')),
            ],
        ),
    ]
