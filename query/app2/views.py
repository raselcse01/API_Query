from django.shortcuts import render
from .models import Student
from datetime import date, time

# Create your views here.

def home(request):
    student_data = Student.objects.all()
    # student_data = Student.objects.filter(name__exact='Rasel')
    # student_data = Student.objects.filter(name__iexact='sasel')
    # student_data = Student.objects.filter(name__iexact='p')
    # student_data = Student.objects.filter(name_contains='p')
    # student_data = Student.objects.filter(name_icontains='P')
    # student_data = Student.objects.filter(id__in=[1,5,7])
    # student_data = Student.objects.filter(marks__in=[90])
    # student_data = Student.objects.filter(marks__in=[60, 90])
    # student_data = Student.objects.filter(marks__gt=60)
    # student_data = Student.objects.filter(marks__gte=60)
    # student_data = Student.objects.filter(marks__lt=60)
    # student_data = Student.objects.filter(marks__lte=60)
    # student_data = Student.objects.filter(passdate__range=('2020-05-13', '2023-05-04'))
    # student_data = Student.objects.filter(admdatetime__date=date('2020, 5, 13'))
    # student_data = Student.objects.filter(admdatetime__date__gte=date('2020, 5, 13'))
    # student_data = Student.objects.filter(passdate__year=2019)
    # student_data = Student.objects.filter(passdate__year__get=2019)
    # student_data = Student.objects.filter(passdate__month=4)
    # student_data = Student.objects.filter(passdate__month__gte=4)
    # student_data = Student.objects.filter(passdate__day=12)
    # student_data = Student.objects.filter(passdate__week=12)
    # student_data = Student.objects.filter(passdate__week__gt=12)
    # student_data = Student.objects.filter(passdate__week__day=12)

    print("Returns",student_data)

    print("Sql query",student_data.query)
    return render(request, 'app2/home.html', {'students':student_data})
