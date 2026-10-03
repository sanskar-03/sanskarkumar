import os
import sys
import django

def populate_portfolio():
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
    django.setup()

    from portfolio.models import (
        SiteSettings, Skill, Project, Experience, 
        Education, Certification, CodingProfile, 
        Achievement, SocialLink
    )

    print("Populating portfolio with your data...")

    # Clear existing data first
    Skill.objects.all().delete()
    Project.objects.all().delete()
    Experience.objects.all().delete()
    Education.objects.all().delete()
    Certification.objects.all().delete()
    CodingProfile.objects.all().delete()
    Achievement.objects.all().delete()
    SocialLink.objects.all().delete()
    SiteSettings.objects.all().delete()

    # --- PERSONAL & CONTACT ---
    SiteSettings.objects.create(
        site_title="My Portfolio",
        owner_name="YOUR NAME",
        role_line="YOUR ROLE",
        intro="Your short introduction goes here.",
        about="Detailed about me goes here.",
        email="your.email@example.com",
        location="Your City, Country",
        availability="Available for work",
        footer_note="A brief note or mission statement for the footer.",
        github_url="https://github.com/yourusername",
        linkedin_url="https://linkedin.com/in/yourusername"
    )

    # --- SKILLS ---
    # Add skills here (e.g. Languages, Frontend, Backend)
    # Skill.objects.create(name="Python", category="Backend", level=90, order=1)

    # --- PROJECTS ---
    # Project.objects.create(title="Project Name", summary="Short Description", description="Detailed", featured=True, order=1)

    # --- EXPERIENCE ---
    # Experience.objects.create(company="Company", role="Role", description="Description")

    # --- EDUCATION ---
    # Education.objects.create(degree="Degree", institution="Institution", field_of_study="Field")

    # --- CERTIFICATES ---
    # Certification.objects.create(name="Cert", issuer="Issuer")

    print("Portfolio populated successfully!")

if __name__ == "__main__":
    populate_portfolio()
