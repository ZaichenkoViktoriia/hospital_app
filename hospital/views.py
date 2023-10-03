from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from hospital.models import (
    Department,
    Medicament,
    Room,
    Patient,
    Assistant
)


def index(request: HttpRequest) -> render:
    return render(request, "hospital/index.html")


class DepartmentListView(LoginRequiredMixin, generic.ListView):
    model = Department
    paginate_by = 5
    fields = "__all__"
    queryset = Department.objects.order_by("name")

    def get_queryset(self):
        query = self.request.GET.get("q")
        if query is not None:
            return Department.objects.filter(name__icontains=query).order_by("name")
        return Department.objects.order_by("name")


class DepartmentDetailView(LoginRequiredMixin, generic.DetailView):
    model = Department
    fields = "__all__"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rooms'] = self.object.rooms.all()
        return context


class DepartmentCreateView(LoginRequiredMixin, generic.CreateView):
    model = Department
    fields = "__all__"
    success_url = reverse_lazy("department-list")


class DepartmentUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Department
    fields = "__all__"
    success_url = reverse_lazy("department-list")


class DepartmentDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Department
    fields = "__all__"
    success_url = reverse_lazy("department-list")


class RoomListView(LoginRequiredMixin, generic.ListView):
    model = Room
    paginate_by = 5
    fields = "__all__"
    queryset = Room.objects.select_related("department")

    def get_queryset(self):
        query = self.request.GET.get("q")
        if query is not None:
            return Room.objects.filter(number__icontains=query).all()
        return Room.objects.all()


class RoomUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Room
    fields = "__all__"
    success_url = reverse_lazy("room-list")


class RoomDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Room
    fields = "__all__"
    success_url = reverse_lazy("room-list")


class MedicamentListView(LoginRequiredMixin, generic.ListView):
    model = Medicament
    paginate_by = 5
    queryset = Medicament.objects.order_by("name")

    def get_queryset(self):
        query = self.request.GET.get("q")
        if query is not None:
            return Medicament.objects.filter(name__icontains=query).order_by("name")
        return Medicament.objects.order_by("name")


class MedicamentCreateView(LoginRequiredMixin, generic.CreateView):
    model = Medicament
    fields = "__all__"
    success_url = reverse_lazy("medicament-list")


class MedicamentUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Medicament
    fields = "__all__"
    success_url = reverse_lazy("medicament-list")


class MedicamentDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Medicament
    fields = "__all__"
    success_url = reverse_lazy("medicament-list")


class MedicamentSearchView(LoginRequiredMixin, generic.ListView):
    model = Medicament

    def get_queryset(self):
        query = self.request.GET.get("q")
        return Medicament.objects.filter(name__icontains=query).order_by("name")


class PatientListView(LoginRequiredMixin,generic.ListView):
    model = Patient
    paginate_by = 5
    queryset = Patient.objects.select_related("room")

    def get_queryset(self):
        query = self.request.GET.get("q")
        if query is not None:
            return Patient.objects.filter(full_name__icontains=query).order_by("full_name")
        return Patient.objects.order_by("full_name")


class PatientCreateView(LoginRequiredMixin, generic.CreateView):
    model = Patient
    fields = "__all__"
    success_url = reverse_lazy("patient-list")


class PatientDetailView(LoginRequiredMixin, generic.DetailView):
    model = Patient
    queryset = Patient.objects.select_related("medicament")


class PatientUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Patient
    fields = "__all__"
    success_url = reverse_lazy("patient-list")


class PatientDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Patient
    fields = "__all__"
    success_url = reverse_lazy("patient-list")


class AssistantListView(LoginRequiredMixin, generic.ListView):
    model = Assistant
    paginate_by = 5
    queryset = Assistant.objects.select_related("room")

    def get_queryset(self):
        query = self.request.GET.get("q")
        if query is not None:
            return Assistant.objects.filter(name__icontains=query).order_by("name")
        return Assistant.objects.order_by("name")


class AssistantCreateView(LoginRequiredMixin,generic.CreateView):
    model = Assistant
    success_url = reverse_lazy("assistant-list")
    fields = "__all__"


class AssistantUpdateView(LoginRequiredMixin,generic.UpdateView):
    model = Assistant
    success_url = reverse_lazy("assistant-list")
    fields = "__all__"


class AssistantDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Assistant
    success_url = reverse_lazy("assistant-list")
    fields = "__all__"

