# Generated by Django 2.2 on 2020-08-13 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analyzer', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='word',
            name='frequency',
            field=models.CharField(choices=[('high', 'high'), ('average', 'average'), ('low', 'low')], default='low', max_length=10),
            preserve_default=False,
        ),
    ]
