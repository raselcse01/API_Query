from django.shortcuts import render
from .models import Student, Teacher
from django.db.models import Q

# Create your views here.
def home(request):
    student_data = Student.objects.all()

    # student_data = Student.objects.filter(marks=70)
    # student_data = Student.objects.exclude(marks=70)
    # student_data = Student.objects.order_by('marks')
    # student_data = Student.objects.order_by('-marks')
    # student_data = Student.objects.order_by('?')
    # student_data = Student.objects.order_by('name') 
    # student_data = Student.objects.order_by('id').reverse()[0:5]
    # student_data = Student.objects.values()
    # student_data = Student.objects.values('name', 'city')
    # student_data = Student.objects.values_list()
    # student_data = Student.objects.values_list('id','name', named=True)
    # student_data = Student.objects.using('default')
    # student_data = Student.objects.detes('pass_date', 'year')
# union
    # qs1 = Student.objects.values_list('id', 'name', named=True)
    # qs2 = Teacher.objects.values_list('id', 'name', named=True)

    # student_data = qs1.union(qs2, all=True)

# intersection
    # qs1 = Student.objects.values_list('id', 'name', named=True)
    # qs2 = Teacher.objects.values_list('id', 'name', named=True)

    # student_data = qs2.intersection(qs1)

# difference
    # qs1 = Student.objects.values_list('id', 'name', named=True)
    # qs2 = Teacher.objects.values_list('id', 'name', named=True)

    # student_data = qs2.difference(qs1)

    # student_data = Student.objects.filter(id=2, roll=101)
    # student_data = Student.objects.filter(id=3) & Student.objects.filter(roll=104)
    # student_data = Student.objects.filter(Q(id=3) & Q(roll=104))
    # student_data = Student.objects.filter(id=3) | Student.objects.filter(roll=104)

    return render(request, 'app/home.html', {'students':student_data})
