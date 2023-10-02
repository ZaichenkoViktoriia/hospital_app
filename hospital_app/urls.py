"""
URL configuration for hospital_app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from authentication.views import CustomLoginView, CustomLogoutView
from hospital.views import index, DepartmentListView, MedicamentListView, RoomListView, \
    DepartmentCreateView, DepartmentDeleteView, DepartmentUpdateView, MedicamentUpdateView, MedicamentDeleteView, \
    AssistantListView, AssistantCreateView, RoomUpdateView, RoomDeleteView, MedicamentCreateView, AssistantUpdateView, \
    AssistantDeleteView, PatientCreateView, PatientListView, PatientUpdateView, PatientDeleteView, PatientDetailView, \
    DepartmentDetailView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(('hospital.urls', 'hospital'), namespace='hospital')),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('', index, name="index"),
    path("departments/", DepartmentListView.as_view(),
         name="department-list"),
    path("departments/<int:pk>/", DepartmentDetailView.as_view(), name="department-detail"),

    path(
        "departments/create/",
        DepartmentCreateView.as_view(),
        name="department-create"
    ),
    path(
        "departments/<int:pk>/update/",
        DepartmentUpdateView.as_view(),
        name="department-update"
    ),
    path(
        "departments/<int:pk>/delete/",
        DepartmentDeleteView.as_view(),
        name="department-delete"
    ),
    path("rooms/", RoomListView.as_view(), name="room-list"),
    path(
        "rooms/<int:pk>/update/",
        RoomUpdateView.as_view(),
        name="room-update"
    ),
    path(
        "rooms/<int:pk>/delete/",
        RoomDeleteView.as_view(),
        name="room-delete"
    ),


    path("medicaments/", MedicamentListView.as_view(), name="medicament-list"),
    path("medicaments/create/",MedicamentCreateView.as_view(),name="medicament-create"),
    path("medicaments/<int:pk>/update/", MedicamentUpdateView.as_view(), name="medicament-update"),
    path("medicaments/<int:pk>/delete/", MedicamentDeleteView.as_view(), name="medicament-delete"),




    path("assistants/", AssistantListView.as_view(), name="assistant-list"),
    path("assistants/create/", AssistantCreateView.as_view(), name="assistant-create"),
    path("assistants/<int:pk>/update/", AssistantUpdateView.as_view(), name="assistant-update"),
    path("assistants/<int:pk>/delete/", AssistantDeleteView.as_view(), name="assistant-delete"),

    path("patients/", PatientListView.as_view(), name="patient-list"),
    path("patients/create/", PatientCreateView.as_view(), name="patient-create"),
    path("patients/<int:pk>/update/", PatientUpdateView.as_view(), name="patient-update"),
    path("patients/<int:pk>/delete/", PatientDeleteView.as_view(), name="patient-delete"),
    path("patients/<int:pk>/", PatientDetailView.as_view(), name="patient-detail"),

    path("/", include("django.contrib.auth.urls")),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

app_name = "hospital"
