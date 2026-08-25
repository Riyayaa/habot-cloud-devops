from django.contrib import admin
from django.urls import path

from onboarding.views import StudentOnboardingCreateView

urlpatterns = [
    path("admin/", admin.site.urls),
    path(
        "api/students/onboard/",
        StudentOnboardingCreateView.as_view(),
        name="student-onboarding",
    ),
]
