from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.ModelSerializer):

    # serializer's Meta configures how the model is converted to and from JSON.
    class Meta:
        model = Student
        fields = "__all__"
        read_only_fields = ["id"]

    def validate_name(self, value):
        if len(value.strip()) < 3:
            raise serializers.ValidationError(
                "Name must contain atleast 3 characters!!!"
            )
        return value