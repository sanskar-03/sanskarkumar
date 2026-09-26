from .models import SiteSettings


def site_context(request):
    return {"site_settings": SiteSettings.load()}


def dashboard_context(request):
    from .dashboard_views import SECTIONS
    return {"dashboard_nav": [(slug, config.plural) for slug, config in SECTIONS.items()]}
