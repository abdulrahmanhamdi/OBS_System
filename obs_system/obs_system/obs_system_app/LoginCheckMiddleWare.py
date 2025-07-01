from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils.deprecation import MiddlewareMixin

class LoginCheckMiddleWare(MiddlewareMixin):

    def process_view(self, request, view_func, view_args, view_kwargs):
        modulename = view_func.__module__
        print(f"Module Name: {modulename}, Path: {request.path}")  # Debugging
        
        user = request.user
        if user.is_authenticated:
            if user.user_type == "1":
                if modulename in [
                    "obs_system_app.HodViews",
                    "obs_system_app.views",
                    "django.views.static",
                    "django.contrib.auth.views",
                    "django.contrib.admin.sites"
                ]:
                    pass
                else:
                    return HttpResponseRedirect(reverse("admin_home"))
            elif user.user_type == "2":
                if modulename in [
                    "obs_system_app.StaffViews",
                    "obs_system.EditResultVIewClass",
                    "obs_system_app.views",
                    "django.views.static"
                ]:
                    pass
                else:
                    return HttpResponseRedirect(reverse("staff_home"))
            elif user.user_type == "3":
                if modulename in [
                    "obs_system_app.StudentViews",  # Updated module name
                    "django.views.static",
                    "obs_system_app.views"
                ]:
                    pass
                else:
                    return HttpResponseRedirect(reverse("student_home"))
            else:
                return HttpResponseRedirect(reverse("show_login"))
        else:
            if request.path in [
                reverse("show_login"),
                reverse("do_login")
            ] or modulename in [
                "django.contrib.auth.views",
                "django.contrib.admin.sites",
                "obs_system_app.views"
            ]:
                pass
            else:
                return HttpResponseRedirect(reverse("show_login"))
