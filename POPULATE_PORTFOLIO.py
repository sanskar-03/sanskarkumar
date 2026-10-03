import os
import sys
import django
from datetime import date

def populate_portfolio():
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
    django.setup()

    from portfolio.models import (
        SiteSettings, Skill, Project, Experience, 
        Education, Certification, CodingProfile, 
        Achievement, SocialLink
    )

    print("Clearing database...")
    Skill.objects.all().delete()
    Project.objects.all().delete()
    Experience.objects.all().delete()
    Education.objects.all().delete()
    Certification.objects.all().delete()
    CodingProfile.objects.all().delete()
    Achievement.objects.all().delete()
    SocialLink.objects.all().delete()
    SiteSettings.objects.all().delete()

    print("Populating SiteSettings...")
    SiteSettings.objects.create(
        site_title="Sanskar Kumar",
        owner_name="Sanskar Kumar",
        role_line="Computer Science Engineering Student & Developer",
        intro="Building full-stack applications, AI/ML systems, automation tools, and developer-focused software.",
        about="I am a Computer Science Engineering student at Aarupadai Veedu Institute of Technology, building software across full-stack web development, AI/ML, automation, and intelligent developer tools. My work includes Django and FastAPI applications, machine-learning systems, automation workflows, data-driven platforms, and modern web products.",
        location="Chennai, Tamil Nadu, India",
        email="",
        phone="",
        github_url="https://github.com/sanskar-03",
        linkedin_url="https://www.linkedin.com/in/sanskar-kumar-2810502b2/",
        footer_note="Built with Django."
    )

    print("Populating Projects...")
    Project.objects.create(
        title="StudyForge",
        summary="AI-powered smart study and productivity platform developed during an AI/ML internship.",
        description="StudyForge is an AI-assisted learning and focus-management platform that combines study assistance, focused study sessions, interactive quizzes, and learning analytics in a Django-based application.",
        tech_stack="Python, Django, Django REST Framework, AI, Machine Learning",
        github_url="https://github.com/sanskar-03/Codemax_Digital_Solution_AI-ML_Intership_projects",
        order=1, featured=True
    )
    Project.objects.create(
        title="TravelBridge",
        summary="AI-powered marketplace for trusted travel-based package exchange.",
        description="TravelBridge connects travelers with spare baggage capacity and people who need trusted item transport. The platform combines intelligent matching, verification, communication, agreement workflows, escrow-style payments, delivery tracking, notifications, reviews, and operational management.",
        tech_stack="Django, Python, PostgreSQL, Redis, REST APIs, WebSockets, Docker, JavaScript",
        github_url="https://github.com/sanskar-03/TravelBridge",
        order=2, featured=True
    )
    Project.objects.create(
        title="Naukri Job Scraper",
        summary="Django and Playwright application for automated Naukri job collection and Excel-based tracking.",
        description="A web-based job scraping system that searches Naukri listings using Playwright and Chromium, extracts structured job information, prevents duplicates, preserves historical Excel records, and provides downloadable search-specific and master job datasets.",
        tech_stack="Python, Django, Playwright, Chromium, openpyxl, HTML, CSS, JavaScript",
        github_url="https://github.com/sanskar-03/naukri-job-scraper",
        order=3, featured=True
    )
    Project.objects.create(
        title="ScaleDown",
        summary="Intelligent context optimization and prompt compression framework.",
        description="ScaleDown is a developer-focused context optimization framework designed to reduce unnecessary LLM token usage while preserving relevant code and semantic context through intelligent retrieval, optimization, and prompt compression.",
        tech_stack="Python, Tree-sitter, BM25, FAISS, Transformer embeddings, Semantic Search, LLM APIs, Pytest",
        github_url="https://github.com/sanskar-03/scaledown",
        order=4, featured=True
    )
    Project.objects.create(
        title="Fake News Detection using NLP",
        summary="Evidence-assisted news and claim verification system using NLP, web evidence, retrieval, and structured reasoning.",
        description="An evidence-assisted verification system that combines claim extraction, NLP analysis, retrieval, live web evidence, optional image analysis, source credibility signals, and deterministic evidence-weighted reasoning.",
        tech_stack="Python, FastAPI, NLP, ChromaDB, DuckDuckGo Search, Ollama, Llama 3.1, AsyncIO, Machine Learning",
        github_url="https://github.com/sanskar-03/fakenewsdetector",
        order=5, featured=True
    )

    print("Populating Skills...")
    skills = [
        ("Languages", ["Python", "JavaScript", "HTML", "CSS"]),
        ("Backend", ["Django", "Django REST Framework", "FastAPI", "REST APIs"]),
        ("AI / ML / Data", ["Machine Learning", "Scikit-Learn", "Pandas", "NumPy", "NLP", "ChromaDB", "FAISS", "Transformer Models"]),
        ("Automation / Developer Tools", ["Playwright", "Chromium", "Tree-sitter", "BM25", "Pytest", "Git", "GitHub", "Docker"]),
        ("Databases / Infrastructure", ["PostgreSQL", "Redis"])
    ]
    for order_cat, (cat, items) in enumerate(skills, 1):
        for order_item, name in enumerate(items, 1):
            Skill.objects.create(category=cat, name=name, level=90, order=order_cat * 100 + order_item)

    print("Populating Experience...")
    Experience.objects.create(
        company="HCLTech",
        role="AI Code Labs Intern",
        description="Completed an internship with HCLTech as part of AI Code Labs, working with Python and gaining practical experience in AI-focused development and technical problem solving.",
        start_date=date(2025, 12, 1),
        end_date=date(2026, 3, 1),
        current=False
    )
    Experience.objects.create(
        company="Codemax Digital Solution",
        role="AI/ML Intern",
        description="Completed a structured AI and machine learning internship covering Python fundamentals, automation, data analysis, machine learning, AI tools, StudyForge, and the TravelShield capstone.",
        tech_stack="Python, Pandas, NumPy, Matplotlib, Seaborn, Scikit-Learn, Django, Django REST Framework, Celery, Redis, Docker"
    )

    print("Populating Education...")
    Education.objects.create(
        institution="Aarupadai Veedu Institute Of Technology",
        degree="B.E. / B.Tech",
        field_of_study="Computer Science Engineering",
        start_date=date(2023, 1, 1),
        end_date=date(2027, 5, 1)
    )

    print("Populating Certifications...")
    Certification.objects.create(
        name="YUVA AI for ALL — Foundational",
        issuer="IndiaAI"
    )

    print("Populating Coding Profiles...")
    CodingProfile.objects.create(
        platform="GitHub",
        username="sanskar-03",
        profile_url="https://github.com/sanskar-03"
    )
    CodingProfile.objects.create(
        platform="LinkedIn",
        username="sanskar-kumar-2810502b2",
        profile_url="https://www.linkedin.com/in/sanskar-kumar-2810502b2/"
    )

    print("Populating Achievements...")
    Achievement.objects.create(
        title="iTech Hackathon — Team Win",
        description="Secured a team win at the iTech Hackathon."
    )
    Achievement.objects.create(
        title="Speaker — 15th Global Webinar on Applied ...",
        description="Served as a speaker at the 15th Global Webinar on Applied ..."
    )

    print("Populating Social Links...")
    SocialLink.objects.create(label="GitHub", url="https://github.com/sanskar-03", icon_key="github")
    SocialLink.objects.create(label="LinkedIn", url="https://www.linkedin.com/in/sanskar-kumar-2810502b2/", icon_key="linkedin")

    print("Done! Portfolio has been successfully populated with your data.")

if __name__ == "__main__":
    populate_portfolio()
