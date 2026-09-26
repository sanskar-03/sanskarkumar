from django.db import migrations, models


def set_contact_defaults(apps, schema_editor):
    SiteSettings = apps.get_model("portfolio", "SiteSettings")
    obj, _ = SiteSettings.objects.get_or_create(pk=1)
    if not obj.email:
        obj.email = "sanskarkumar838383@gmail.com"
    if not obj.location:
        obj.location = "Chennai"
    obj.save(update_fields=["email", "location", "updated_at"])


class Migration(migrations.Migration):
    dependencies = [("portfolio", "0001_initial")]

    operations = [
        migrations.AlterField(
            model_name="sitesettings",
            name="email",
            field=models.EmailField(blank=True, default="sanskarkumar838383@gmail.com", max_length=254),
        ),
        migrations.AlterField(
            model_name="sitesettings",
            name="location",
            field=models.CharField(blank=True, default="Chennai", max_length=120),
        ),
        migrations.RunPython(set_contact_defaults, migrations.RunPython.noop),
    ]
