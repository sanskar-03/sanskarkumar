# CSE Portfolio — Django CMS + Vercel Ready v2

A polished, responsive Computer Science portfolio built with Django, plain CSS and a custom CMS dashboard.

## What changed in v2

- Premium black / off-white / electric-blue visual system
- Light and dark mode with persistent browser preference
- Responsive mobile navigation
- Scroll progress indicator
- Scroll-reveal animation with reduced-motion support
- Hover motion and subtle glow/ambient grid effects
- Refined project, skill, profile, timeline and contact cards
- Responsive dashboard with the same theme switcher
- Python 3.12 pinned for predictable Vercel builds
- Vercel-ready `pyproject.toml` build hook for migrations + `collectstatic`
- Production PostgreSQL via `DATABASE_URL` (Neon recommended)
- Cloudinary support for persistent image uploads

## Local development

```bash
python -m venv .venv
```

Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

Install:

```powershell
pip install -r requirements.txt
Copy-Item .env.example .env
```

Then:

```powershell
python manage.py migrate
python manage.py create_portfolio_user
python manage.py runserver
```

Open `http://127.0.0.1:8000/`.

## First-time content setup

The public site starts in **Coming Soon** mode.

Open `/login/`, sign in, then use `/dashboard/` to manage:

- Site Settings
- Projects
- Skills
- Experience
- Education
- Certifications
- Coding Profiles
- Achievements
- Social Links
- Contact messages

Turn off **Coming Soon** in Site Settings when the content is ready.

## Theme

Use the round theme button in the top-right on the public site or the Theme button in the dashboard. The selected light/dark mode is stored in `localStorage`, so it remains when you return.

## Vercel

This package is prepared for Vercel's current zero-configuration Django support. Vercel detects `manage.py` and the Django WSGI entrypoint; no old `/api` rewrite is needed.

The deployment guide is in **`DEPLOY_VERCEL.md`**. The short flow is:

1. Put the extracted project root (the folder containing `manage.py`) in GitHub.
2. Import the repository into Vercel.
3. Add `DJANGO_SECRET_KEY`, `DJANGO_DEBUG=0`, `DATABASE_URL` from Neon, `DJANGO_ALLOWED_HOSTS`, and `CSRF_TRUSTED_ORIGINS`.
4. Deploy.
5. Run `python manage.py create_portfolio_user` against the production database.
6. Log in at `/login/` and finish Site Settings.
7. Turn off Coming Soon.

Vercel's current Django examples use PostgreSQL for production and run migrations from `pyproject.toml`; Neon branches are useful to isolate preview migrations from production.

## Edit after deployment

Content changes made from the dashboard are database changes and appear on the live site without a Vercel rebuild.

Code/design changes are made locally, committed to Git, and pushed to the GitHub branch connected to Vercel. Vercel then creates a new deployment.

## Images

Local images use the local `media/` directory.

On Vercel, configure `CLOUDINARY_URL` before using the dashboard upload fields so profile and project images persist outside the serverless filesystem.
