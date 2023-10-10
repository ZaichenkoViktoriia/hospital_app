from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from hospital.models import Medicament, Room, Patient, Doctor


class ModelTests(TestCase):
    def test_medicament_str(self) -> None:
        medicament = Medicament.objects.create(
            name="test "
        )
        self.assertEqual(
            str(medicament), medicament.name
        )

    def test_patient_str(self):
        room = Room.objects.create(name="Room 101")
        patient = Patient.objects.create(
            full_name="John Doe",
            diagnosis="Some Diagnosis",
            home_address="123 Main St",
            phone_number="555-123-4567",
            room=room,
            )
        medicament = Medicament.objects.create(name="Medicine 1")
        patient.medicament.add(medicament)

        expected_str = f"{patient.full_name} {patient.room} {patient.diagnosis}"
        self.assertEqual(str(patient), expected_str)

    def test_room_str(self):
        room = Room.objects.create(number="3")

        expected_str = room.number
        self.assertEqual(str(room), expected_str)


ROOM_URL = reverse("hospital:room-list")
PATIENT_URL = reverse("hospital:patient-list")
MEDICAMENT_URL = reverse("hospital:medicament-list")


class PublicTaxiTests(TestCase):
    def test_room_status_code(self):
        response = self.client.get(ROOM_URL)
        self.assertEqual(response.status_code, 200)

    def test_patient_status_code(self):
        response = self.client.get(PATIENT_URL)
        self.assertEqual(response.status_code, 200)

    def test_medicament_status_code(self):
        response = self.client.get(MEDICAMENT_URL)
        self.assertEqual(response.status_code, 200)


CREATE_URL = reverse("hospital:patient-create")


class PrivateModelTests(TestCase):
    def setUp(self):
        self.room = Room.objects.create(name="Room 3")
        self.medicament = Medicament.objects.create(name="Medicament")
        self.admin = Doctor.objects.create_user(
            username="admin", password="password"
        )

    def test_admin_can_create_patient(self):
        self.client.force_login(self.admin)
        response = self.client.post(
            CREATE_URL,
            {
                "full_name": "Test",
                "diagnosis": "Test",
                "home_address": "Test",
                "phone_number": "111",
                "room": self.room.pk,
                "medicament": self.medicament.pk,
            },
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Patient.objects.last().full_name, "Test")
