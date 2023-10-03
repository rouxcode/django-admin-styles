from django.contrib.admin.apps import AdminConfig


class ProjectAdminConfig(AdminConfig):
    default_site = "testproject.admin.ProjectAdminSite"
