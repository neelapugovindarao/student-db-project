from django.shortcuts import render
from .models import Student

def student_form(request):
    if request.method == "POST":
        roll = request.POST.get('roll')
        name = request.POST.get('name')
        student_class = request.POST.get('student_class')
        total = request.POST.get('total')
        paid = request.POST.get('paid')
        balance = request.POST.get('balance')

        Student.objects.create(
            roll=roll,
            name=name,
            student_class=student_class,
            total=total,
            paid=paid,
            balance=balance
        )

    return render(request, 'student.html')