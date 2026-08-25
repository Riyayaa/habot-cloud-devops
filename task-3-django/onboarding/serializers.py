from rest_framework import serializers

from .dcyn import from_raw_input, requires_support_dcyn
from .models import StudentOnboarding


class StudentOnboardingSerializer(serializers.ModelSerializer):
    support_decision = serializers.SerializerMethodField()

    class Meta:
        model = StudentOnboarding
        fields = [
            "student_id",
            "student_name",
            "region",
            "requires_support",
            "support_decision",
        ]

    def to_internal_value(self, data):
        data = data.copy()

        if "requires_support" in data:
            try:
                data["requires_support"] = from_raw_input(data["requires_support"])
            except ValueError as exc:
                raise serializers.ValidationError({"requires_support": str(exc)})

        return super().to_internal_value(data)

    def validate_student_id(self, value):
        value = value.strip()
        if not value:
            raise serializers.ValidationError("student_id cannot be empty.")
        if len(value) > 20:
            raise serializers.ValidationError(
                "student_id must be 20 characters or fewer."
            )
        return value

    def validate_student_name(self, value):
        value = value.strip()
        if not value:
            raise serializers.ValidationError("student_name cannot be empty.")
        if len(value) > 100:
            raise serializers.ValidationError(
                "student_name must be 100 characters or fewer."
            )
        return value

    def validate_region(self, value):
        valid_regions = {code for code, _ in StudentOnboarding.REGION_CHOICES}
        if value not in valid_regions:
            raise serializers.ValidationError(
                f"region must be one of {sorted(valid_regions)}."
            )
        return value

    def get_support_decision(self, obj):
        return requires_support_dcyn(obj.requires_support)
