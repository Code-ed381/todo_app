from django.shortcuts import render,redirect
# from django.http import HttpResponse
from django.template import loader
from .models import Todo
from .forms import TodoForm
from .models import Com
from .forms import ComForm
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def godwin(request):
    # template=loader.get_template("index.html")
    # return HttpResponse(template.render())

    #sellecting all data from the database
 
    context={}
    context["todo"]=Todo.objects.all()
    return render(request,"index.html",context)

@csrf_exempt
def create(request):
    form= TodoForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect("/")
    # form= TodoForm()
    # return render(request,"index.html",{"form":form})

def delete(request,id):
    todo= Todo.objects.get(id=id)
    todo.delete()
    return redirect("/")

def update(request,id):
    todo=Todo.objects.get(id=id)
    form=TodoForm(request.POST,instance=todo)
    if form.is_valid():
        form.save()
        return redirect("/")
    
    return render(request,"update.html",{'todos':todo})

def completed(request,id):
    todo=Com.objects.get(id=id)
    form=ComForm(request.POST,instance=todo)
    if form.is_valid():
        form.save()   
        return redirect("/")
    
    todo= Todo.objects.get(id=id)
    todo.delete()
    
    