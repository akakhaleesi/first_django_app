# Generated by Django 2.0.5 on 2019-06-13 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_auto_20190613_0903'),
    ]

    operations = [
        migrations.AddField(
            model_name='instructor',
            name='password',
            field=models.CharField(default='toto', max_length=200),
        ),
        migrations.AddField(
            model_name='secretary',
            name='password',
            field=models.CharField(default='toto', max_length=200),
        ),
        migrations.AddField(
            model_name='student',
            name='password',
            field=models.CharField(default='toto', max_length=200),
        ),
    ]