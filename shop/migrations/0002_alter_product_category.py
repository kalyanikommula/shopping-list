# Generated by Django 4.2.13 on 2024-07-08 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('CU', 'Curd'), ('ML', 'Milk'), ('BU', 'Butter'), ('MS', 'Milkshake'), ('PN', 'Panner'), ('GH', 'Ghee'), ('CZ', 'Cheese'), ('IC', 'Ice-creams')], max_length=2),
        ),
    ]
