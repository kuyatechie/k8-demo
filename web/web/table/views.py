from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

from table.models import Attendance
from table.serializers import AttendanceSerializer, AttendanceObjectsSerializer

import socket
from datetime import datetime

def index(request):
    return HttpResponse("Hello, world. I am your Kubernetes Pod Friend, {}. "
                        "You can now use the following APIs. "
                        "/create "
                        "/view/date:YYMMDD".format(socket.gethostbyname(socket.gethostname())))

@csrf_exempt
def create(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        data["login"] = datetime.today()
        serializer = AttendanceSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

    if request.method == 'GET':
        return HttpResponse(status=405)

@csrf_exempt
def view_day_attendance(request, date):
    try:
        if date == "today":
            today = datetime.today()
            date = "{}{}{}".format(today.year, today.month, today.day)
        task = Attendance.objects.filter(login__date=datetime.strptime(date, '%Y%m%d').date())
    except Attendance.DoesNotExist:
        return HttpResponse(status=404)
    except ValueError:
        return HttpResponse("Invalid date. Use YYYYMMDD.", status=400)

    if request.method == 'GET':
        serializer = AttendanceObjectsSerializer(task, many=True)
        return JsonResponse(serializer.data, safe=False)
