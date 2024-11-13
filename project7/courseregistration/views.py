

from django.shortcuts import render
from courseregistration.models import Student, Course

#Create your views here.

def register(request):

    st = Student.objects.create(name = 'Hrishikesh', usn='4MK21CS017')

    cr = Course.objects.create(name='Python', code='cs1')

    cr.enrolment.add(st)

    s=Student.objects.all()

    c=Course.objects.all()

    return render(request, 'course_reg.html', {'student_list':s, 'course_list':c})