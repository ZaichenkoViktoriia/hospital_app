from django.urls import path

from .views import index, DepartmentListView, DepartmentUpdateView, DepartmentDeleteView, MedicamentListView, \
    MedicamentUpdateView, MedicamentDeleteView, RoomListView, AssistantListView, AssistantCreateView, \
    DepartmentCreateView

urlpatterns = [
    path("", index, name="index"),
    path('', index),
]

app_name = "hospital"
