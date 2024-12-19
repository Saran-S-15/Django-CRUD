from django.shortcuts import render, redirect
from practiseApp.models import Register
# Create your views here.
def home(request):
    query = Register.objects.all()
    context ={"data": query}
    return render(request, "index.html", context)

def register(request):
    if request.method=="POST":
        name=request.POST.get("name")
        email=request.POST.get("email")
        mobile=request.POST.get("mobile")
        course=request.POST.get("course")
        query = Register(Full_Name=name,Email=email,Phone_Number=mobile,Course=course)
        query.save()
        return redirect("/")

    return render(request, "index.html")

def update(request, id):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        mobile=request.POST.get('mobile')
        course=request.POST.get('course')
        edit=Register.objects.get(id=id)
        edit.Full_Name=name
        edit.Email=email
        edit.Phone_Number=mobile
        edit.Course=course
        edit.save()
        return redirect("/")
    
    data = Register.objects.get(id=id)
    context = {"data":data}
    return render(request, "update.html", context)

def delete(request, id):
    data = Register.objects.get(id=id)
    data.delete()
    return redirect("/")