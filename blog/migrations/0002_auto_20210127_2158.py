# Generated by Django 3.1.5 on 2021-01-27 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plan',
            name='status',
            field=models.CharField(choices=[('-', 'note'), ('○', 'event'), ('·', 'todo'), ('>', 'delay'), ('<', 'migrate'), ('x', 'done')], max_length=5),
        ),
    ]