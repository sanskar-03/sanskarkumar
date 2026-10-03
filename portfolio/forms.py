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
        help_text="JPG, PNG, WEBP or GIF. Maximum 5 MB.",
        widget=forms.ClearableFileInput(
            attrs={
                "accept": "image/jpeg,image/png,image/webp,image/gif",
            }
        ),
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
        labels = {
            "role_line": "Main title / Role",
            "intro": "Short headline",
            "about": "About / Bio",
        }
        widgets = {
            "site_title": forms.TextInput(attrs={"placeholder": "Sanskar Kumar | Portfolio"}),
            "owner_name": forms.TextInput(attrs={"placeholder": "Sanskar Kumar"}),
            "role_line": forms.TextInput(attrs={"placeholder": "Computer Science Engineering Student & Developer"}),
            "intro": forms.Textarea(attrs={"rows": 5, "placeholder": "Short introduction for the hero section."}),
            "about": forms.Textarea(attrs={"rows": 8, "placeholder": "Longer professional/about description."}),
            "email": forms.EmailInput(attrs={"placeholder": "you@example.com"}),
            "phone": forms.TextInput(attrs={"placeholder": "+91 ..."}),
            "location": forms.TextInput(attrs={"placeholder": "Chennai, Tamil Nadu, India"}),
            "github_url": forms.URLInput(attrs={"placeholder": "https://github.com/..."}),
            "linkedin_url": forms.URLInput(attrs={"placeholder": "https://linkedin.com/in/..."}),
            "resume_url": forms.URLInput(attrs={"placeholder": "https://..."}),
            "availability": forms.TextInput(attrs={"placeholder": "Open to internships and junior roles."}),
            "coming_soon_title": forms.TextInput(attrs={"placeholder": "A new portfolio is on its way."}),
            "coming_soon_message": forms.Textarea(attrs={"rows": 5}),
            "footer_note": forms.TextInput(attrs={"placeholder": "Built with Django."}),
        }


class ProjectForm(StyledFormMixin, forms.ModelForm):
    image_upload = forms.ImageField(
        required=False,
        label="Upload project image",
        help_text="JPG, PNG, WEBP or GIF. Maximum 5 MB.",
        widget=forms.ClearableFileInput(
            attrs={
                "accept": "image/jpeg,image/png,image/webp,image/gif",
            }
        ),
    )

    class Meta:
        model = Project
        fields = "__all__"
        labels = {
            "summary": "Short description",
            "description": "Detailed description",
            "features": "Features",
        }
        widgets = {
            "title": forms.TextInput(attrs={"placeholder": "StudyForge", "autocomplete": "off"}),
            "slug": forms.TextInput(attrs={"placeholder": "studyforge", "autocomplete": "off"}),
            "summary": forms.Textarea(attrs={"rows": 3, "maxlength": 240, "placeholder": "One concise sentence describing the project."}),
            "description": forms.Textarea(attrs={"rows": 9, "placeholder": "Explain what the project does, how it works and what you built."}),
            "features": forms.Textarea(attrs={"rows": 6, "placeholder": "Bullet point list of main features..."}),
            "tech_stack": forms.TextInput(attrs={"placeholder": "Python, Django, PostgreSQL, JavaScript"}),
            "github_url": forms.URLInput(attrs={"placeholder": "https://github.com/username/project", "autocomplete": "url"}),
            "live_demo_url": forms.URLInput(attrs={"placeholder": "https://example.com", "autocomplete": "url"}),
            "image_url": forms.URLInput(attrs={"placeholder": "Optional external image URL"}),
        }


class SkillForm(StyledFormMixin, forms.ModelForm):
    class Meta:
        model = Skill
        fields = "__all__"
        widgets = {
            "level": forms.NumberInput(attrs={"type": "range", "min": "0", "max": "100", "step": "5"}),
        }


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
    image_upload = forms.ImageField(
        required=False,
        label="Upload certificate image",
        help_text="JPG, PNG, WEBP or GIF. Maximum 5 MB.",
        widget=forms.ClearableFileInput(attrs={"accept": "image/jpeg,image/png,image/webp,image/gif"}),
    )

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
        widgets = {
            "icon_key": forms.Select(choices=[
                ("github", "GitHub"),
                ("linkedin", "LinkedIn"),
                ("mail", "Email"),
                ("link", "Website"),
            ])
        }


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
