# Generated by Django 2.0.13 on 2020-09-10 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_usercommunicationlayermodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserInformationLayerModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('metadata', models.CharField(max_length=100)),
                ('storagesystems', models.CharField(max_length=100)),
                ('schemaregistry', models.BooleanField()),
                ('da', models.BooleanField()),
                ('cdate', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'InformationTable',
            },
        ),
    ]