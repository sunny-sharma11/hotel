# Generated by Django 3.0.3 on 2020-04-05 02:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20200405_0726'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mainhead', models.CharField(max_length=30)),
                ('head', models.CharField(max_length=30)),
                ('date', models.DateField()),
                ('desc', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='')),
            ],
        ),
        migrations.AddField(
            model_name='hotels',
            name='image',
            field=models.ImageField(default=0, upload_to=''),
            preserve_default=False,
        ),
    ]
