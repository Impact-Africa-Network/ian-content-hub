# Generated by Django 4.1 on 2022-08-05 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0002_alter_contenttype_options_remove_contentcategory_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='contenttype',
            name='thumbnail',
            field=models.ImageField(default=1, upload_to=''),
            preserve_default=False,
        ),
    ]