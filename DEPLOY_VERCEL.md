# Vercel deployment — Django portfolio v2

This project is prepared for Vercel's current zero-configuration Django deployment flow. Vercel detects `manage.py` and the Django WSGI entrypoint, and static files are served through Vercel's CDN. No `/api` folder or old Django rewrite is required.

## A. Put the project on GitHub

Extract this ZIP. The **project root** is the folder containing `manage.py`, `pyproject.toml`, `requirements.txt`, `vercel.json`, `config/`, and `portfolio/`.

Create a new GitHub repository and upload these root-level files. Do not upload the ZIP itself.

Recommended repository structure:

```text
manage.py
pyproject.toml
requirements.txt
vercel.json
config/
portfolio/
```

## B. Confirm your Neon database

The Django app uses SQLite only for local development. In production it expects `DATABASE_URL`, and the included build step runs migrations automatically.

In Neon, open your project, choose the database/branch you want to use, copy its PostgreSQL connection string, and keep it private. A typical Neon URL looks like:

```text
postgresql://USER:PASSWORD@HOST/DBNAME?sslmode=require
```

Because the connection string is already a PostgreSQL URL, `dj-database-url` reads it and Django uses PostgreSQL in production.

For previews, prefer a Neon branch or other isolated database so preview migrations do not modify production data. Vercel's Django notes example makes the same recommendation for Neon-backed preview deployments.

## C. Import the GitHub repository into Vercel

1. Sign in to Vercel.
2. Click **Add New → Project**.
3. Import the GitHub repository.
4. Make sure the Vercel **Root Directory** is the folder containing `manage.py`. If you uploaded the files directly to the repository root, leave Root Directory at `.`.
5. Let Vercel detect Django. Do not add an `/api` folder or an old `@vercel/python` runtime config; current Django support is zero-config.

## D. Add Vercel environment variables

Open **Project → Settings → Environment Variables** and add these for **Production**. You can also add them for Preview/Development with separate values where appropriate. Vercel requires a redeploy for new environment variables to be used by a deployment.

```text
DJANGO_SECRET_KEY=<long-random-secret>
DJANGO_DEBUG=0
DATABASE_URL=<your-Neon-PostgreSQL-connection-string>
DJANGO_ALLOWED_HOSTS=.vercel.app,your-domain.com
CSRF_TRUSTED_ORIGINS=https://*.vercel.app,https://your-domain.com
```

For production image uploads, also add:

```text
CLOUDINARY_URL=cloudinary://API_KEY:API_SECRET@CLOUD_NAME
```

Generate a Django secret locally with:

```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

Vercel's Django template documents setting `DJANGO_SECRET_KEY` as an environment variable.

## E. Deploy

Click **Deploy**. The project contains this Vercel build hook:

```toml
[tool.vercel.scripts]
build = "python manage.py migrate --noinput && python manage.py collectstatic --noinput"
```

Vercel's current Django examples also use `pyproject.toml` to run migrations during the build.

The project pins Python to 3.12 with `requires-python = "~=3.12.0"`. Vercel currently supports Python 3.12, 3.13 and 3.14 and has announced that the default can move over time, so pinning 3.12 keeps this project reproducible.

## F. Create the dashboard login user

The deployed app includes a custom CMS. There is no `/admin/` route.

After the first deployment, run the management command against your production database from a machine that has the project and the production variables configured:

```bash
python manage.py create_portfolio_user
```

Then open:

```text
https://YOUR-DOMAIN.vercel.app/login/
```

Sign in and open **Dashboard → Site Settings**.

## G. Make the public site live

The first migration intentionally starts with **Coming Soon** enabled.

In **Dashboard → Site Settings**:

1. Fill in your name, role, intro and about text.
2. Add your links and resume URL.
3. Add projects, skills, experience, education, certifications and profiles.
4. Upload a profile/project image after configuring Cloudinary.
5. Turn off **Coming Soon**.
6. Save.

Your content changes are database changes, so you do **not** need to rebuild the frontend for normal dashboard edits.

## H. Make future design/code changes live

For CSS, HTML, JavaScript, Python or migration changes:

```bash
git add .
git commit -m "Update portfolio"
git push origin main
```

With Vercel's Git integration, the push triggers a new deployment. Vercel creates preview deployments from Git changes and deploys the production branch to the live domain.

## I. Important production notes

- Never commit `.env` or your Neon password.
- Keep `DJANGO_DEBUG=0` in production.
- Use HTTPS URLs in `CSRF_TRUSTED_ORIGINS`.
- Use a persistent PostgreSQL database such as Neon for production data.
- Use Cloudinary (or another persistent object store) for uploaded images; do not depend on the serverless filesystem for permanent uploads.
- Keep production and preview databases separated when you can, especially because migrations run during deployment.

## Quick checklist

```text
[ ] GitHub repo contains manage.py at the selected Vercel Root Directory
[ ] Neon DATABASE_URL added to Vercel
[ ] DJANGO_SECRET_KEY added
[ ] DJANGO_DEBUG=0
[ ] CSRF_TRUSTED_ORIGINS set
[ ] Deploy succeeded
[ ] CMS user created
[ ] Login works at /login/
[ ] Site Settings completed
[ ] Coming Soon turned off
[ ] Images tested (only after Cloudinary is configured)
[ ] Production URL opens correctly on mobile
```
