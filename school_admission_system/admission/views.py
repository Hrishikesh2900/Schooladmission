from django.shortcuts import render, HttpResponseRedirect 
from .forms import StudentRegistration
from .models import User

# Create your views here.
def add_show(request):
    if request.method == 'POST':
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            ad = fm.cleaned_data['address']
            mk = fm.cleaned_data['marks']
            pw = fm.cleaned_data['password']
            reg = User(name=nm, email=em, address=ad, marks=mk, password=pw)
            reg.save()
            fm = StudentRegistration()
    else:
        fm = StudentRegistration()
    stud = User.objects.all()
    return render(request, 'admission/addandshow.html',{'form':fm, 'stu':stud})

def eligible_stu(request, marks):
    stude = User.objects.get(marks>='55')
    stude.get()
    return HttpResponse('<h1>LIST OF ELIGIBLE STUDENTS</h1>')

def update_data(request, id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        fm = StudentRegistration(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi = User.objects.get(pk=id)
        fm = StudentRegistration(instance=pi)
    return render(request, 'admission/updatestudent.html', {'form':fm})

def delete_data(request, id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')