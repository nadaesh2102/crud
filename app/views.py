from django.shortcuts import render, redirect, get_object_or_404
from .models import Student

# Create your views here.
def index(request):
    data = Student.objects.all()
    context = {"data": data}
    return render(request, "index.html", context)

def insertData(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        print(name, email, age, gender)
        query = Student(name=name, email=email, age=age, gender=gender)
        query.save()
        return redirect("/")

    return render(request, "index.html")

def updateData(request, id):
    student = get_object_or_404(Student, id=id)  # Fetch the student or return 404 if not found

    if request.method == "POST":
        student.name = request.POST['name']
        student.email = request.POST['email']
        student.age = request.POST['age']
        student.gender = request.POST['gender']
        student.save()
        return redirect("/")

    context = {"d": student}  # Pass the fetched student object
    return render(request, "edit.html", context)

def deleteData(request, id):
    student = get_object_or_404(Student, id=id)  # Fetch the student or return 404 if not found
    student.delete()  # Delete the student object
    return redirect("/")  # Redirect to the index page after deletion

def about(request):
    return render(request, "about.html")
