from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from hospital.models import Department, Doctor, Medicament, Room, Patient, Assistant


@admin.register(Doctor)
class DoctorAdmin(UserAdmin):
    list_display = UserAdmin.list_display


admin.site.register(Medicament)
admin.site.register(Department)
admin.site.register(Room)
admin.site.register(Patient)
admin.site.register(Assistant)

