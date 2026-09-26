from django.contrib import messages
from django.contrib.auth.views import LoginView
from django.http import HttpResponseBadRequest
from django.shortcuts import redirect, render

from .forms import ContactForm, DashboardLoginForm
from .media_utils import store_image
from .models import (
    Achievement,
    Certification,
    CodingProfile,
    Education,
    Experience,
    Project,
    SiteSettings,
    Skill,
)


def home(request):
    settings = SiteSettings.load()

    if settings.coming_soon:
        return render(request, "portfolio/coming_soon.html", {"settings": settings})

    context = {
        "settings": settings,
        "skills": Skill.objects.filter(visible=True),
        "projects": Project.objects.filter(visible=True),
        "featured_projects": Project.objects.filter(visible=True, featured=True)[:3],
        "experiences": Experience.objects.filter(visible=True),
        "educations": Education.objects.filter(visible=True),
        "certifications": Certification.objects.filter(visible=True),
        "coding_profiles": CodingProfile.objects.filter(visible=True),
        "achievements": Achievement.objects.filter(visible=True),
    }
    return render(request, "portfolio/home.html", context)


class PortfolioLoginView(LoginView):
    template_name = "portfolio/login.html"
    authentication_form = DashboardLoginForm
    redirect_authenticated_user = True


def login_view(request):
    return PortfolioLoginView.as_view()(request)


def resume_redirect(request):
    settings = SiteSettings.load()
    if not settings.resume_url:
        messages.info(request, "A resume link has not been added yet.")
        return redirect("home")
    return redirect(settings.resume_url)


def contact(request):
    settings = SiteSettings.load()
    if settings.coming_soon:
        return redirect("home")

    if request.method != "POST":
        return HttpResponseBadRequest("Use the contact form on the portfolio page.")

    form = ContactForm(request.POST)
    if form.is_valid():
        form.save()
        messages.success(request, "Your message has been sent.")
        return redirect("/#contact")

    context = {
        "settings": settings,
        "skills": Skill.objects.filter(visible=True),
        "projects": Project.objects.filter(visible=True),
        "featured_projects": Project.objects.filter(visible=True, featured=True)[:3],
        "experiences": Experience.objects.filter(visible=True),
        "educations": Education.objects.filter(visible=True),
        "certifications": Certification.objects.filter(visible=True),
        "coding_profiles": CodingProfile.objects.filter(visible=True),
        "achievements": Achievement.objects.filter(visible=True),
        "contact_form": form,
        "contact_has_errors": True,
    }
    return render(request, "portfolio/home.html", context)
