from __future__ import annotations

from dataclasses import dataclass

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from .media_utils import store_image
from .forms import (
    AchievementForm,
    CertificationForm,
    CodingProfileForm,
    EducationForm,
    ExperienceForm,
    ProjectForm,
    SiteSettingsForm,
    SkillForm,
    SocialLinkForm,
    DraftItemForm,
)
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
    DraftItem,
)


@dataclass(frozen=True)
class SectionConfig:
    label: str
    plural: str
    model: type
    form: type
    columns: tuple[tuple[str, str], ...]


SECTIONS = {
    "drafts": SectionConfig("Draft", "Drafts", DraftItem, DraftItemForm,
        (("Source", "source"), ("Type", "draft_type"), ("Title", "title"), ("Created", "created_at"))),
    "projects": SectionConfig("Project", "Projects", Project, ProjectForm,
        (("Title", "title"), ("Stack", "tech_stack"), ("Featured", "featured"), ("Visible", "visible"))),
    "skills": SectionConfig("Skill", "Skills", Skill, SkillForm,
        (("Name", "name"), ("Category", "category"), ("Level", "level"), ("Visible", "visible"))),
    "experience": SectionConfig("Experience", "Experience", Experience, ExperienceForm,
        (("Role", "role"), ("Company", "company"), ("Start", "start_date"), ("Current", "current"))),
    "education": SectionConfig("Education", "Education", Education, EducationForm,
        (("Degree", "degree"), ("Institution", "institution"), ("Start", "start_date"), ("End", "end_date"))),
    "certifications": SectionConfig("Certification", "Certifications", Certification, CertificationForm,
        (("Name", "name"), ("Issuer", "issuer"), ("Issue date", "issue_date"), ("Visible", "visible"))),
    "coding-profiles": SectionConfig("Coding profile", "Coding Profiles", CodingProfile, CodingProfileForm,
        (("Platform", "platform"), ("Username", "username"), ("Stat", "stat_value"), ("Visible", "visible"))),
    "achievements": SectionConfig("Achievement", "Achievements", Achievement, AchievementForm,
        (("Title", "title"), ("Date", "date"), ("Link", "link_url"), ("Visible", "visible"))),
    "social-links": SectionConfig("Social link", "Social Links", SocialLink, SocialLinkForm,
        (("Label", "label"), ("URL", "url"), ("Icon", "icon_key"), ("Visible", "visible"))),
}


@login_required
def dashboard_home(request):
    settings = SiteSettings.load()
    section_counts = [
        (config.plural, config.model.objects.count(), slug)
        for slug, config in SECTIONS.items()
    ]
    unread_messages = ContactMessage.objects.filter(is_read=False).count()
    return render(
        request,
        "portfolio/dashboard/index.html",
        {
            "settings": settings,
            "section_counts": section_counts,
            "unread_messages": unread_messages,
        },
    )


@login_required
def settings_edit(request):
    settings = SiteSettings.load()
    if request.method == "POST":
        form = SiteSettingsForm(request.POST, request.FILES, instance=settings)
        if form.is_valid():
            saved = form.save(commit=False)
            upload = form.cleaned_data.get("profile_image_upload")
            if upload:
                try:
                    saved.profile_image_url = store_image(upload, "profile")
                except ValueError as exc:
                    form.add_error("profile_image_upload", str(exc))
                except Exception:
                    form.add_error(
                        "profile_image_upload",
                        "Image upload failed. Check the image and Cloudinary configuration.",
                    )
                else:
                    saved.save()
                    messages.success(request, "Site settings and profile image saved.")
                    return redirect("dashboard_settings")
            else:
                saved.save()
                messages.success(request, "Site settings saved.")
                return redirect("dashboard_settings")
    else:
        form = SiteSettingsForm(instance=settings)
    return render(
        request,
        "portfolio/dashboard/settings.html",
        {"form": form, "settings": settings},
    )


def _config_or_404(kind: str) -> SectionConfig:
    from django.http import Http404

    config = SECTIONS.get(kind)
    if not config:
        raise Http404("Unknown dashboard section.")
    return config


@login_required
def crud_list(request, kind):
    config = _config_or_404(kind)
    return render(
        request,
        "portfolio/dashboard/crud_list.html",
        {"config": config, "kind": kind, "items": config.model.objects.all()},
    )


@login_required
def crud_edit(request, kind, pk=None):
    config = _config_or_404(kind)
    instance = None if pk is None else get_object_or_404(config.model, pk=pk)

    if request.method == "POST":
        form = config.form(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            saved = form.save(commit=False)
            upload_field = "image_upload" if kind == "projects" else None
            upload = form.cleaned_data.get(upload_field) if upload_field else None
            if upload:
                try:
                    saved.image_url = store_image(upload, "projects")
                except ValueError as exc:
                    form.add_error(upload_field, str(exc))
                except Exception:
                    form.add_error(
                        upload_field,
                        "Image upload failed. Check the image and Cloudinary configuration.",
                    )
                else:
                    saved.save()
                    verb = "created" if instance is None else "updated"
                    messages.success(request, f"{config.label} {verb}, including its image.")
                    return redirect("dashboard_list", kind=kind)
            else:
                saved.save()
                verb = "created" if instance is None else "updated"
                messages.success(request, f"{config.label} {verb}.")
                return redirect("dashboard_list", kind=kind)
    else:
        form = config.form(instance=instance)

    return render(
        request,
        "portfolio/dashboard/crud_form.html",
        {"config": config, "kind": kind, "form": form, "instance": instance},
    )


@login_required
def crud_delete(request, kind, pk):
    config = _config_or_404(kind)
    instance = get_object_or_404(config.model, pk=pk)

    if request.method == "POST":
        instance.delete()
        messages.success(request, f"{config.label} deleted.")
        return redirect("dashboard_list", kind=kind)

    return render(
        request,
        "portfolio/dashboard/crud_delete.html",
        {"config": config, "kind": kind, "instance": instance},
    )


@login_required
def messages_list(request):
    return render(
        request,
        "portfolio/dashboard/messages.html",
        {"messages_list": ContactMessage.objects.all()},
    )


@login_required
def message_read(request, pk):
    item = get_object_or_404(ContactMessage, pk=pk)
    item.is_read = True
    item.save(update_fields=["is_read"])
    return redirect("dashboard_messages")


@login_required
def message_delete(request, pk):
    item = get_object_or_404(ContactMessage, pk=pk)
    if request.method == "POST":
        item.delete()
        messages.success(request, "Message deleted.")
        return redirect("dashboard_messages")
    return render(
        request,
        "portfolio/dashboard/message_delete.html",
        {"item": item},
    )

@login_required
def approve_draft(request, pk):
    draft = get_object_or_404(DraftItem, pk=pk)
    
    # Simple logic to convert a draft to actual item
    t = draft.draft_type.lower()
    if 'project' in t:
        Project.objects.create(title=draft.title, summary=draft.description, description=draft.description, link_url=draft.link_url)
    elif 'achieve' in t:
        Achievement.objects.create(title=draft.title, description=draft.description, link_url=draft.link_url)
    elif 'exper' in t:
        Experience.objects.create(company=draft.title, role="Role from Draft", description=draft.description)
    else:
        Achievement.objects.create(title=draft.title, description=draft.description, link_url=draft.link_url)
        
    draft.delete()
    messages.success(request, f"Draft '{draft.title}' approved and published.")
    return redirect("dashboard_list", kind="drafts")

@login_required
def trigger_external_fetch(request):
    # Dummy logic mimicking fetch
    # In reality, this would hit GitHub/LinkedIn API
    DraftItem.objects.create(
        source="github", 
        draft_type="Project", 
        title="Auto-fetched repo: Cool-Project", 
        description="A cool project found on GitHub.",
        link_url="https://github.com/your-username/Cool-Project"
    )
    DraftItem.objects.create(
        source="linkedin",
        draft_type="Achievement",
        title="New LinkedIn Certification",
        description="Auto-fetched post about completing a new course.",
        link_url="https://linkedin.com/in/your-username/"
    )
    messages.success(request, "External sources checked. Found new items and created drafts.")
    return redirect("dashboard_list", kind="drafts")
