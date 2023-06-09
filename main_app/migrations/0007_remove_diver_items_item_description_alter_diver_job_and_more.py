# Generated by Django 4.2 on 2023-05-08 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0006_item_diver_items'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='diver',
            name='items',
        ),
        migrations.AddField(
            model_name='item',
            name='description',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='diver',
            name='job',
            field=models.CharField(choices=[('F', 'Fighter'), ('C', 'Cleric'), ('P', 'Paladin'), ('R', 'Rogue'), ('S', 'Sorcerer')], default='F', max_length=10),
        ),
        migrations.AlterField(
            model_name='item',
            name='name',
            field=models.CharField(default='', max_length=50),
        ),
    ]
