from users.views import dashboard,help
from django.conf.urls import include,url
from django.contrib import admin

urlpatterns = [
    url(r"^dashboard/", dashboard, name="dashboard"),
    url(r"^help/", help, name="help"),
    url(r"^accounts/", include("django.contrib.auth.urls")),
    url(r"^admin/", admin.site.urls),


]





