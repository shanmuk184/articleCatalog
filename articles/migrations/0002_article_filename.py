# Generated by Django 2.2.1 on 2019-06-02 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='filename',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
