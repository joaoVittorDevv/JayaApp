import os
from django.db import migrations


def add_default_superuser(apps, schema_editor):
    User = apps.get_model("users", "User")

    if not User.objects.filter(username='admin').exists():
        User.objects.create_superuser(username='admin', email='admin@mail.com', password='admin')

class Migration(migrations.Migration):

    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(add_default_superuser),
    ]
