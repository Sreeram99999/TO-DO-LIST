from django.shortcuts import render,redirect
from .models import *

def home(request):
    if request.method == "POST":
        data = request.POST.get('task')
        des = request.POST.get('description')
        Data.objects.create(Task=data,Desc=des)
    return render(request,'home.html')



def list(request):
    if request.method == 'POST':
        search = request.POST.get('search')
        # print(search)
        data = Data.objects.filter(Task__icontains=search)
    else:
        data = Data.objects.filter(mark__contains = 0)
    con = {'data':data}
    return render(request,'list.html',con)



def details(request,pk):
    data = Data.objects.get(id=pk)
    con = {'data':data}
    return render(request,'details.html',con)


def edit(request,pk):
    data = Data.objects.get(id=pk)
    if request.method == "POST":
        dat = request.POST.get('task')
        des = request.POST.get('description')
        data.Task=dat
        data.Desc=des
        data.save()
        return redirect('list')
    return render(request,'edit.html',{'data':data})

def mark(request,pk):
    data = Data.objects.get(id=pk)
    data.mark = 1
    data.save()
    return list(request)

def history(request):
    data = Data.objects.filter(mark__contains = 1)
    con = {'data':data}
    return render(request,'history.html',con)


def delete(request,pk):
    data = Data.objects.get(id=pk)
    data.delete()
    return history(request)


def contact(request):
    return render(request,'contact.html')