from rest_framework import serializers
from table.models import Attendance


class AttendanceSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    login = serializers.DateTimeField(required=True)
    firstname = serializers.CharField(required=True)
    lastname = serializers.CharField(required=True)
    gate = serializers.CharField(required=False)

    def create(self, validated_data):
        return Attendance.objects.create(**validated_data)


class AttendanceObjectsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        fields = '__all__'
