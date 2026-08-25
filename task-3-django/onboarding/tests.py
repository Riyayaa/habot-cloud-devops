from django.test import TestCase


from .dcyn import to_dcyn
from .serializers import StudentOnboardingSerializer


class DCYNTests(TestCase):
    def test_true_returns_yes(self):
        self.assertEqual(to_dcyn(True), "Yes")

    def test_false_returns_no(self):
        self.assertEqual(to_dcyn(False), "No")

    def test_invalid_dcyn_value_is_rejected(self):
        with self.assertRaises(ValueError):
            to_dcyn("maybe")


class StudentOnboardingSerializerTests(TestCase):
    def valid_payload(self):
        return {
            "student_id": "STU001",
            "student_name": "Riya",
            "region": "Mumbai",
            "requires_support": True,
        }

    def test_valid_payload(self):
        serializer = StudentOnboardingSerializer(data=self.valid_payload())
        self.assertTrue(serializer.is_valid(), serializer.errors)

    def test_student_id_over_20_characters_is_rejected(self):
        data = self.valid_payload()
        data["student_id"] = "A" * 21

        serializer = StudentOnboardingSerializer(data=data)

        self.assertFalse(serializer.is_valid())
        self.assertIn("student_id", serializer.errors)

    def test_student_name_over_100_characters_is_rejected(self):
        data = self.valid_payload()
        data["student_name"] = "A" * 101

        serializer = StudentOnboardingSerializer(data=data)

        self.assertFalse(serializer.is_valid())
        self.assertIn("student_name", serializer.errors)

    def test_region_over_50_characters_is_rejected(self):
        data = self.valid_payload()
        data["region"] = "A" * 51

        serializer = StudentOnboardingSerializer(data=data)

        self.assertFalse(serializer.is_valid())
        self.assertIn("region", serializer.errors)
