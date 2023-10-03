from django.contrib import admin


class AdminStylesSite(admin.AdminSite):
    enable_nav_sidebar = True

    def each_context(self, request):
        context = super().each_context(request)
        # context["show_save_as_new"] = False
        # context["show_save_and_add_another"] = False
        # context["show_save_and_continue"] = False
        return context
