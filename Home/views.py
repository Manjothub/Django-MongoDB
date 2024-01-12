from django.shortcuts import render,redirect
from .models import *
# Create your views here.
def Home(request):
    todo = TODO.objects.all()  
    data ={
        'data':todo
    }
    return render(request,'table.html',data)

def SAVETODO(request):
    if request.method == 'POST':
        name =  request.POST.get('task_name')
        details =  request.POST.get('task_details')
        date =  request.POST.get('task_date')
        status =  request.POST.get('status') =='on'
        
        todo = TODO.objects.create(task_name=name, task_detail=details, task_date=date, status=status)
        if todo is not None:
            todo.save()
            return redirect('todo')
        else:
            context ={
                'error':'Please Fill Details Properly'
            }
            return render(request,'table.html',context)
        
        
def UPDATETODO(request,id):
    todo = TODO.objects.get(id=id)
    if todo is not None:
            todo.status = True
            todo.save()
            return redirect('todo')

def DELETETODO(request,id):
    todo = TODO.objects.get(id=id)  
    todo.delete()
    return redirect('todo')
