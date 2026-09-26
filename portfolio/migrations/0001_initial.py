from django.db import migrations, models
import django.core.validators


def create_default_settings(apps, schema_editor):
    SiteSettings = apps.get_model("portfolio", "SiteSettings")
    SiteSettings.objects.get_or_create(
        pk=1,
        defaults={
            "site_title": "Your Name — CSE Portfolio",
            "owner_name": "Your Name",
            "role_line": "Computer Science Engineering Student & Developer",
            "intro": (
                "I build practical software, learn by shipping projects, "
                "and keep improving the details that make a product easy to use."
            ),
            "about": (
                "I enjoy working across the stack, from designing a clean interface "
                "to wiring up the database and deployment. This portfolio is where I "
                "keep my recent work, education and the things I am learning."
            ),
            "availability": "Open to internships, junior roles and useful side projects.",
            "coming_soon": True,
            "coming_soon_title": "A new portfolio is on its way.",
            "coming_soon_message": (
                "I am putting the final pieces together. The projects, "
                "experience, education and links will be here soon."
            ),
            "footer_note": "Built with Django, plain CSS and a lot of coffee.",
        },
    )


class Migration(migrations.Migration):
    initial = True
    dependencies = []
    operations = [
        migrations.CreateModel(
            name="Achievement",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("title", models.CharField(max_length=160)),
                ("date", models.DateField(blank=True, null=True)),
                ("description", models.TextField()),
                ("link_url", models.URLField(blank=True)),
                ("order", models.PositiveIntegerField(default=0)),
                ("visible", models.BooleanField(default=True)),
            ],
            options={"ordering": ["order", "-date"]},
        ),
        migrations.CreateModel(
            name="Certification",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=160)),
                ("issuer", models.CharField(max_length=140)),
                ("issue_date", models.DateField(blank=True, null=True)),
                ("credential_url", models.URLField(blank=True)),
                ("credential_id", models.CharField(blank=True, max_length=120)),
                ("description", models.TextField(blank=True)),
                ("order", models.PositiveIntegerField(default=0)),
                ("visible", models.BooleanField(default=True)),
            ],
            options={"ordering": ["order", "-issue_date"]},
        ),
        migrations.CreateModel(
            name="CodingProfile",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("platform", models.CharField(choices=[("LeetCode", "LeetCode"), ("HackerRank", "HackerRank"), ("GitHub", "GitHub"), ("CodeChef", "CodeChef"), ("Other", "Other")], max_length=30)),
                ("username", models.CharField(max_length=120)),
                ("profile_url", models.URLField()),
                ("stat_value", models.CharField(blank=True, max_length=80)),
                ("stat_label", models.CharField(blank=True, max_length=120)),
                ("note", models.CharField(blank=True, max_length=220)),
                ("order", models.PositiveIntegerField(default=0)),
                ("visible", models.BooleanField(default=True)),
            ],
            options={"ordering": ["order", "platform"]},
        ),
        migrations.CreateModel(
            name="ContactMessage",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=100)),
                ("email", models.EmailField(max_length=254)),
                ("subject", models.CharField(max_length=180)),
                ("message", models.TextField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("is_read", models.BooleanField(default=False)),
            ],
            options={"ordering": ["is_read", "-created_at"]},
        ),
        migrations.CreateModel(
            name="Education",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("institution", models.CharField(max_length=180)),
                ("degree", models.CharField(max_length=140)),
                ("field_of_study", models.CharField(max_length=140)),
                ("location", models.CharField(blank=True, max_length=120)),
                ("start_date", models.DateField()),
                ("end_date", models.DateField(blank=True, null=True)),
                ("grade", models.CharField(blank=True, max_length=80)),
                ("description", models.TextField(blank=True)),
                ("order", models.PositiveIntegerField(default=0)),
                ("visible", models.BooleanField(default=True)),
            ],
            options={"ordering": ["order", "-start_date"]},
        ),
        migrations.CreateModel(
            name="Experience",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("company", models.CharField(max_length=140)),
                ("role", models.CharField(max_length=140)),
                ("location", models.CharField(blank=True, max_length=120)),
                ("start_date", models.DateField()),
                ("end_date", models.DateField(blank=True, null=True)),
                ("current", models.BooleanField(default=False)),
                ("description", models.TextField()),
                ("tech_stack", models.CharField(blank=True, max_length=400)),
                ("order", models.PositiveIntegerField(default=0)),
                ("visible", models.BooleanField(default=True)),
            ],
            options={"ordering": ["order", "-start_date"]},
        ),
        migrations.CreateModel(
            name="Project",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("title", models.CharField(max_length=140)),
                ("slug", models.SlugField(blank=True, max_length=160, unique=True)),
                ("summary", models.CharField(max_length=240)),
                ("description", models.TextField()),
                ("tech_stack", models.CharField(help_text="Comma-separated, for example: Django, PostgreSQL, JavaScript", max_length=400)),
                ("github_url", models.URLField(blank=True)),
                ("live_demo_url", models.URLField(blank=True)),
                ("image_url", models.URLField(blank=True)),
                ("featured", models.BooleanField(default=False)),
                ("order", models.PositiveIntegerField(default=0)),
                ("visible", models.BooleanField(default=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
            options={"ordering": ["order", "-featured", "-created_at"]},
        ),
        migrations.CreateModel(
            name="SiteSettings",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("site_title", models.CharField(default="Your Name — CSE Portfolio", max_length=120)),
                ("owner_name", models.CharField(default="Your Name", max_length=80)),
                ("role_line", models.CharField(default="Computer Science Engineering Student & Developer", max_length=160)),
                ("intro", models.TextField(default="I build practical software, learn by shipping projects, and keep improving the details that make a product easy to use.")),
                ("about", models.TextField(default="I enjoy working across the stack, from designing a clean interface to wiring up the database and deployment. This portfolio is where I keep my recent work, education and the things I am learning.")),
                ("email", models.EmailField(blank=True, max_length=254)),
                ("phone", models.CharField(blank=True, max_length=40)),
                ("location", models.CharField(blank=True, max_length=120)),
                ("github_url", models.URLField(blank=True)),
                ("linkedin_url", models.URLField(blank=True)),
                ("leetcode_url", models.URLField(blank=True)),
                ("hacker_rank_url", models.URLField(blank=True)),
                ("resume_url", models.URLField(blank=True)),
                ("profile_image_url", models.URLField(blank=True)),
                ("availability", models.CharField(default="Open to internships, junior roles and useful side projects.", max_length=180)),
                ("coming_soon", models.BooleanField(default=True)),
                ("coming_soon_title", models.CharField(default="A new portfolio is on its way.", max_length=140)),
                ("coming_soon_message", models.TextField(default="I am putting the final pieces together. The projects, experience, education and links will be here soon.")),
                ("footer_note", models.CharField(default="Built with Django, plain CSS and a lot of coffee.", max_length=180)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
            options={"verbose_name": "Site settings", "verbose_name_plural": "Site settings"},
        ),
        migrations.CreateModel(
            name="Skill",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("category", models.CharField(default="Development", max_length=80)),
                ("name", models.CharField(max_length=80)),
                ("level", models.PositiveSmallIntegerField(default=70, help_text="Optional visual confidence level, 0–100.", validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
                ("order", models.PositiveIntegerField(default=0)),
                ("visible", models.BooleanField(default=True)),
            ],
            options={"ordering": ["order", "category", "name"]},
        ),
        migrations.CreateModel(
            name="SocialLink",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("label", models.CharField(max_length=80)),
                ("url", models.URLField()),
                ("icon_key", models.CharField(default="link", help_text="Use github, linkedin, mail, or link.", max_length=30)),
                ("order", models.PositiveIntegerField(default=0)),
                ("visible", models.BooleanField(default=True)),
            ],
            options={"ordering": ["order", "label"]},
        ),
        migrations.RunPython(create_default_settings, migrations.RunPython.noop),
    ]
