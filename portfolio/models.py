from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.utils.text import slugify


class SiteSettings(models.Model):
    site_title = models.CharField(max_length=120, default="Your Name — CSE Portfolio")
    owner_name = models.CharField(max_length=80, default="Your Name")
    role_line = models.CharField(
        max_length=160,
        default="Computer Science Engineering Student & Developer",
    )
    intro = models.TextField(
        default=(
            "I build practical software, learn by shipping projects, "
            "and keep improving the details that make a product easy to use."
        )
    )
    about = models.TextField(
        default=(
            "I enjoy working across the stack, from designing a clean interface "
            "to wiring up the database and deployment. This portfolio is where I "
            "keep my recent work, education and the things I am learning."
        )
    )
    email = models.EmailField(default="sanskarkumar838383@gmail.com", blank=True)
    phone = models.CharField(max_length=40, blank=True)
    location = models.CharField(max_length=120, default="Chennai", blank=True)
    github_url = models.URLField(blank=True)
    linkedin_url = models.URLField(blank=True)
    leetcode_url = models.URLField(blank=True)
    hacker_rank_url = models.URLField(blank=True)
    resume_url = models.URLField(blank=True)
    profile_image_url = models.URLField(blank=True)
    availability = models.CharField(
        max_length=180,
        default="Open to internships, junior roles and useful side projects.",
    )
    coming_soon = models.BooleanField(default=True)
    coming_soon_title = models.CharField(
        max_length=140,
        default="A new portfolio is on its way.",
    )
    coming_soon_message = models.TextField(
        default=(
            "I am putting the final pieces together. The projects, "
            "experience, education and links will be here soon."
        )
    )
    footer_note = models.CharField(
        max_length=180,
        default="Built with Django, plain CSS and a lot of coffee.",
    )
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Site settings"
        verbose_name_plural = "Site settings"

    def __str__(self):
        return self.owner_name or "Site settings"

    @classmethod
    def load(cls):
        obj, _ = cls.objects.get_or_create(pk=1)
        return obj


class Skill(models.Model):
    category = models.CharField(max_length=80, default="Development")
    name = models.CharField(max_length=80)
    level = models.PositiveSmallIntegerField(
        default=70,
        validators=[MinValueValidator(0), MaxValueValidator(100)],
        help_text="Optional visual confidence level, 0–100.",
    )
    order = models.PositiveIntegerField(default=0)
    visible = models.BooleanField(default=True)

    class Meta:
        ordering = ["order", "category", "name"]

    def __str__(self):
        return self.name


class Project(models.Model):
    title = models.CharField(max_length=140)
    slug = models.SlugField(max_length=160, unique=True, blank=True)
    summary = models.CharField(max_length=240)
    description = models.TextField()
    tech_stack = models.CharField(
        max_length=400,
        help_text="Comma-separated, for example: Django, PostgreSQL, JavaScript",
    )
    github_url = models.URLField(blank=True)
    live_demo_url = models.URLField(blank=True)
    image_url = models.URLField(blank=True)
    featured = models.BooleanField(default=False)
    order = models.PositiveIntegerField(default=0)
    visible = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["order", "-featured", "-created_at"]

    def save(self, *args, **kwargs):
        if not self.slug:
            base = slugify(self.title)[:150]
            candidate = base or "project"
            number = 2
            while Project.objects.filter(slug=candidate).exclude(pk=self.pk).exists():
                candidate = f"{base}-{number}"
                number += 1
            self.slug = candidate
        super().save(*args, **kwargs)

    @property
    def tech_list(self):
        return [item.strip() for item in self.tech_stack.split(",") if item.strip()]

    def __str__(self):
        return self.title


class Experience(models.Model):
    company = models.CharField(max_length=140)
    role = models.CharField(max_length=140)
    location = models.CharField(max_length=120, default="Chennai", blank=True)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    current = models.BooleanField(default=False)
    description = models.TextField()
    tech_stack = models.CharField(max_length=400, blank=True)
    order = models.PositiveIntegerField(default=0)
    visible = models.BooleanField(default=True)

    class Meta:
        ordering = ["order", "-start_date"]

    @property
    def tech_list(self):
        return [item.strip() for item in self.tech_stack.split(",") if item.strip()]

    def __str__(self):
        return f"{self.role} — {self.company}"


class Education(models.Model):
    institution = models.CharField(max_length=180)
    degree = models.CharField(max_length=140)
    field_of_study = models.CharField(max_length=140)
    location = models.CharField(max_length=120, default="Chennai", blank=True)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    grade = models.CharField(max_length=80, blank=True)
    description = models.TextField(blank=True)
    order = models.PositiveIntegerField(default=0)
    visible = models.BooleanField(default=True)

    class Meta:
        ordering = ["order", "-start_date"]

    def __str__(self):
        return f"{self.degree} — {self.institution}"


class Certification(models.Model):
    name = models.CharField(max_length=160)
    issuer = models.CharField(max_length=140)
    issue_date = models.DateField(blank=True, null=True)
    credential_url = models.URLField(blank=True)
    credential_id = models.CharField(max_length=120, blank=True)
    certificate_file = models.FileField(upload_to="certificates/", blank=True, null=True, help_text="Upload your certificate PDF or image.")
    description = models.TextField(blank=True)
    order = models.PositiveIntegerField(default=0)
    visible = models.BooleanField(default=True)

    class Meta:
        ordering = ["order", "-issue_date"]

    def __str__(self):
        return self.name


class CodingProfile(models.Model):
    PLATFORM_CHOICES = [
        ("LeetCode", "LeetCode"),
        ("HackerRank", "HackerRank"),
        ("GitHub", "GitHub"),
        ("CodeChef", "CodeChef"),
        ("Other", "Other"),
    ]

    platform = models.CharField(max_length=30, choices=PLATFORM_CHOICES)
    username = models.CharField(max_length=120)
    profile_url = models.URLField()
    stat_value = models.CharField(max_length=80, blank=True)
    stat_label = models.CharField(max_length=120, blank=True)
    note = models.CharField(max_length=220, blank=True)
    order = models.PositiveIntegerField(default=0)
    visible = models.BooleanField(default=True)

    class Meta:
        ordering = ["order", "platform"]

    def __str__(self):
        return f"{self.platform} — {self.username}"


class Achievement(models.Model):
    title = models.CharField(max_length=160)
    date = models.DateField(blank=True, null=True)
    description = models.TextField()
    link_url = models.URLField(blank=True)
    order = models.PositiveIntegerField(default=0)
    visible = models.BooleanField(default=True)

    class Meta:
        ordering = ["order", "-date"]

    def __str__(self):
        return self.title


class SocialLink(models.Model):
    label = models.CharField(max_length=80)
    url = models.URLField()
    icon_key = models.CharField(
        max_length=30,
        default="link",
        help_text="Use github, linkedin, mail, or link.",
    )
    order = models.PositiveIntegerField(default=0)
    visible = models.BooleanField(default=True)

    class Meta:
        ordering = ["order", "label"]

    def __str__(self):
        return self.label


class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=180)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    class Meta:
        ordering = ["is_read", "-created_at"]

    def __str__(self):
        return f"{self.name} — {self.subject}"

class DraftItem(models.Model):
    SOURCE_CHOICES = [
        ("github", "GitHub"),
        ("linkedin", "LinkedIn"),
    ]
    source = models.CharField(max_length=20, choices=SOURCE_CHOICES)
    draft_type = models.CharField(max_length=50, help_text="e.g. Project, Experience, Achievement")
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    link_url = models.URLField(blank=True)
    raw_data = models.JSONField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"Draft ({self.source}): {self.title}"
