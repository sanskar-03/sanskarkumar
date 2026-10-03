from django import forms
from django.contrib.auth.forms import AuthenticationForm

from .models import (
    Achievement,
    Certification,
    CodingProfile,
    ContactMessage,
    Education,
    Experience,
    Project,
    SiteSettings,
    Skill,
    SocialLink,
)


class StyledFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            existing = field.widget.attrs.get("class", "")
            field.widget.attrs["class"] = f"{existing} field-control".strip()


class SiteSettingsForm(StyledFormMixin, forms.ModelForm):
    profile_image_upload = forms.ImageField(
        required=False,
        label="Upload profile image",
        help_text="JPG, PNG, WEBP or GIF; up to 5 MB. Uploading replaces the profile image URL.",
        widget=forms.ClearableFileInput(attrs={"accept": "image/*"}),
    )

    class Meta:
        model = SiteSettings
        fields = [
            "site_title", "owner_name", "role_line", "intro", "about",
            "email", "phone", "location",
            "github_url", "linkedin_url", "leetcode_url", "hacker_rank_url",
            "resume_url", "profile_image_url", "availability",
            "coming_soon", "coming_soon_title", "coming_soon_message",
            "footer_note",
        ]
        widgets = {
            "intro": forms.Textarea(attrs={"rows": 4}),
            "about": forms.Textarea(attrs={"rows": 6}),
            "coming_soon_message": forms.Textarea(attrs={"rows": 5}),
        }


class ProjectForm(StyledFormMixin, forms.ModelForm):
    image_upload = forms.ImageField(
        required=False,
        label="Upload project image",
        help_text="JPG, PNG, WEBP or GIF; up to 5 MB. Uploading replaces the image URL.",
        widget=forms.ClearableFileInput(attrs={"accept": "image/*"}),
    )

    class Meta:
        model = Project
        fields = "__all__"
        widgets = {
            "summary": forms.TextInput(attrs={"placeholder": "One clear sentence about the project"}),
            "description": forms.Textarea(attrs={"rows": 7}),
            "tech_stack": forms.TextInput(attrs={"placeholder": "Django, PostgreSQL, JavaScript"}),
        }


class SkillForm(StyledFormMixin, forms.ModelForm):
    class Meta:
        model = Skill
        fields = "__all__"


class ExperienceForm(StyledFormMixin, forms.ModelForm):
    class Meta:
        model = Experience
        fields = "__all__"
        widgets = {
            "description": forms.Textarea(attrs={"rows": 7}),
            "tech_stack": forms.TextInput(attrs={"placeholder": "Python, Django, SQL"}),
            "start_date": forms.DateInput(attrs={"type": "date"}),
            "end_date": forms.DateInput(attrs={"type": "date"}),
        }


class EducationForm(StyledFormMixin, forms.ModelForm):
    class Meta:
        model = Education
        fields = "__all__"
        widgets = {
            "description": forms.Textarea(attrs={"rows": 5}),
            "start_date": forms.DateInput(attrs={"type": "date"}),
            "end_date": forms.DateInput(attrs={"type": "date"}),
        }


class CertificationForm(StyledFormMixin, forms.ModelForm):
    class Meta:
        model = Certification
        fields = "__all__"
        widgets = {
            "description": forms.Textarea(attrs={"rows": 4}),
            "issue_date": forms.DateInput(attrs={"type": "date"}),
        }


class CodingProfileForm(StyledFormMixin, forms.ModelForm):
    class Meta:
        model = CodingProfile
        fields = "__all__"


class AchievementForm(StyledFormMixin, forms.ModelForm):
    class Meta:
        model = Achievement
        fields = "__all__"
        widgets = {
            "description": forms.Textarea(attrs={"rows": 5}),
            "date": forms.DateInput(attrs={"type": "date"}),
        }


class SocialLinkForm(StyledFormMixin, forms.ModelForm):
    class Meta:
        model = SocialLink
        fields = "__all__"


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ["name", "email", "subject", "message"]
        widgets = {
            "name": forms.TextInput(attrs={"placeholder": "Your name"}),
            "email": forms.EmailInput(attrs={"placeholder": "you@example.com"}),
            "subject": forms.TextInput(attrs={"placeholder": "What should we talk about?"}),
            "message": forms.Textarea(attrs={"rows": 6, "placeholder": "A short message is enough."}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs["class"] = "field-control"


class DashboardLoginForm(AuthenticationForm):
    username = forms.CharField(
        label="Username",
        widget=forms.TextInput(attrs={"class": "field-control", "autocomplete": "username", "autofocus": True}),
    )
    password = forms.CharField(
        label="Password",
        strip=False,
        widget=forms.PasswordInput(attrs={"class": "field-control", "autocomplete": "current-password"}),
    )

from .models import DraftItem

class DraftItemForm(forms.ModelForm):
    class Meta:
        model = DraftItem
        fields = ["source", "draft_type", "title", "description", "link_url"]
        widgets = {
            "source": forms.Select(attrs={"class": "field-control"}),
            "draft_type": forms.TextInput(attrs={"class": "field-control"}),
            "title": forms.TextInput(attrs={"class": "field-control"}),
            "description": forms.Textarea(attrs={"class": "field-control", "rows": 4}),
            "link_url": forms.URLInput(attrs={"class": "field-control"}),
        }
