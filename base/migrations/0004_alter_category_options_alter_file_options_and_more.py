# Generated by Django 5.0.4 on 2024-05-05 14:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_remove_historicalfile_tags_remove_file_tags_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterModelOptions(
            name='file',
            options={'verbose_name_plural': 'Files'},
        ),
        migrations.AlterModelOptions(
            name='folder',
            options={'verbose_name_plural': 'Folders'},
        ),
        migrations.AlterModelOptions(
            name='historicalcategory',
            options={'get_latest_by': ('history_date', 'history_id'), 'ordering': ('-history_date', '-history_id'), 'verbose_name': 'historical category', 'verbose_name_plural': 'historical Categories'},
        ),
        migrations.AlterModelOptions(
            name='historicalfile',
            options={'get_latest_by': ('history_date', 'history_id'), 'ordering': ('-history_date', '-history_id'), 'verbose_name': 'historical file', 'verbose_name_plural': 'historical Files'},
        ),
        migrations.AlterModelOptions(
            name='historicalfolder',
            options={'get_latest_by': ('history_date', 'history_id'), 'ordering': ('-history_date', '-history_id'), 'verbose_name': 'historical folder', 'verbose_name_plural': 'historical Folders'},
        ),
        migrations.AlterModelOptions(
            name='historicaltag',
            options={'get_latest_by': ('history_date', 'history_id'), 'ordering': ('-history_date', '-history_id'), 'verbose_name': 'historical tag', 'verbose_name_plural': 'historical Tags'},
        ),
        migrations.AlterModelOptions(
            name='tag',
            options={'verbose_name_plural': 'Tags'},
        ),
        migrations.RemoveField(
            model_name='file',
            name='file_size',
        ),
        migrations.RemoveField(
            model_name='historicalfile',
            name='file_size',
        ),
    ]