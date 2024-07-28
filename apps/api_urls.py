from django.urls import include, path

urlpatterns = [
    path("notif/", include("apps.notification.api.urls")),
]
