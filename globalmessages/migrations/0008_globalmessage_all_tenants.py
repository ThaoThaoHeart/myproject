# Generated by Django 3.2.14 on 2022-10-14 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('globalmessages', '0007_globalmessage_optional'),
    ]

    operations = [
        migrations.AddField(
            model_name='globalmessage',
            name='all_tenants',
            field=models.BooleanField(default=False),
        ),
    ]
