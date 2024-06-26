# Generated by Django 5.0.1 on 2024-01-09 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0002_outgoingdoc'),
    ]

    operations = [
        migrations.RenameField(
            model_name='outgoingdoc',
            old_name='archive_no',
            new_name='dossier_no',
        ),
        migrations.RemoveField(
            model_name='incomingdoc',
            name='archive_no',
        ),
        migrations.RemoveField(
            model_name='incomingdoc',
            name='branch_no',
        ),
        migrations.RemoveField(
            model_name='outgoingdoc',
            name='branch_no',
        ),
        migrations.AddField(
            model_name='incomingdoc',
            name='archive',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='incomingdoc',
            name='branch',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='outgoingdoc',
            name='archive',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='outgoingdoc',
            name='branch',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='outgoingdoc',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='outgoingdoc',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='records/outgoingdocs/images'),
        ),
        migrations.AlterField(
            model_name='incomingdoc',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='records/incomingdocs/images'),
        ),
        migrations.AlterField(
            model_name='incomingdoc',
            name='year',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='outgoingdoc',
            name='year',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
