# Generated by Django 4.1.3 on 2022-12-27 01:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chessengine', '0002_rename_chessboard_chessboardmodel_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='gamestatemodel',
            name='totalMoves',
            field=models.PositiveSmallIntegerField(default=0),
        ),
    ]