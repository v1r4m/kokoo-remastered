# Generated by Django 4.1.3 on 2022-11-13 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kokooremaster', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='result',
            name='whole_id',
            field=models.IntegerField(default=0, primary_key=True, serialize=False),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='result',
            name='id',
            field=models.IntegerField(),
        ),
    ]