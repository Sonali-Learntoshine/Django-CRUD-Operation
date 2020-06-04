from django.contrib import messages
from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from django.views.generic import ListView
from .models import Profile
from .forms import Add_Stud


def index(request):
    return HttpResponse("<h1><center>I m index</h1>")


class View_user(ListView):
    model = Profile
    template_name = 'App/view_users.html'
    context_object_name = 'users'

    def view_user(self, request):
        if request.POST.get('add_student'):
            print("i m working")
            return HttpResponse("U r not eligible")
        return HttpResponse("U r eligible")


def profile(request, id):
    obj = Profile.objects.get(id=id)
    print(obj)
    return render(request, 'App/profile.html', {'data': obj})


def add_student(request):
    form = Add_Stud()
    if request.method == 'POST':
        form = Add_Stud(request.POST, request.FILES)

        if form.is_valid():
            name = form.cleaned_data.get('name')
            img = form.cleaned_data.get('img')
            caption = form.cleaned_data.get('caption')
            dob = form.cleaned_data.get('dob')
            designation = form.cleaned_data.get('designation')

            obj = Profile(name=name, img=img, caption=caption, dob=dob, designation=designation)
            obj.save()
            return HttpResponse("Student Added successfully")
        else:
            return render(request, 'App/add_student.html', {'form': form})
    return render(request, 'App/add_student.html', {'form': form})


def del_student(request, id):
    obj = Profile.objects.get(id=id)
    if request.method == 'POST':
        obj.delete()
        messages.success(request, "Data deleted Successfully")
        return redirect('users')
    return render(request, 'App/delete.html', {'obj': obj})


def update(request, id):
    obj = Profile.objects.get(id=id)
    form = Add_Stud(request.POST or None)

    if form.is_valid():
        form = Add_Stud(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form}
    return render(request, 'App/edit.html', context)
