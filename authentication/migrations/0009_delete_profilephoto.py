# Generated by Django 5.0.2 on 2024-03-13 13:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0008_customuser_profile_photo_alter_profilephoto_name'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ProfilePhoto',
        ),
    ]
