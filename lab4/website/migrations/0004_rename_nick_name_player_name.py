# Generated by Django 4.0 on 2024-05-03 05:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_rename_avatars_avatar_rename_persons_person_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='player',
            old_name='nick_name',
            new_name='name',
        ),
    ]
