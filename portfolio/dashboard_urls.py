from django.urls import path

from . import dashboard_views


urlpatterns = [
    path("", dashboard_views.dashboard_home, name="dashboard_home"),
    path("settings/", dashboard_views.settings_edit, name="dashboard_settings"),
    path("messages/", dashboard_views.messages_list, name="dashboard_messages"),
    path("messages/<int:pk>/read/", dashboard_views.message_read, name="dashboard_message_read"),
    path("messages/<int:pk>/delete/", dashboard_views.message_delete, name="dashboard_message_delete"),
    path("drafts/fetch/", dashboard_views.trigger_external_fetch, name="dashboard_trigger_fetch"),
    path("drafts/<int:pk>/approve/", dashboard_views.approve_draft, name="dashboard_approve_draft"),
    path("<slug:kind>/", dashboard_views.crud_list, name="dashboard_list"),
    path("<slug:kind>/new/", dashboard_views.crud_edit, name="dashboard_create"),
    path("<slug:kind>/<int:pk>/edit/", dashboard_views.crud_edit, name="dashboard_edit"),
    path("<slug:kind>/<int:pk>/delete/", dashboard_views.crud_delete, name="dashboard_delete"),
]
