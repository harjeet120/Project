from django.http import HttpResponse
from django.shortcuts import render
def addition(request):
    return render(request,'addition.html')
def result(request):
    if request.method=="POST":
        a=int(request.POST['no1'])
        b=int(request.POST['no2'])
        c=a+b
        return render(request,'result.html',{"result":c})
    else:
        return render(request, 'addition.html')



