from django.shortcuts import render, redirect
from .models import Student
from .forms import StudentForm


def students(request):
    students=Student.objects.all()
    return render (request,'students.html',{
        'students':students
    })



def add(request):
  students=Student.objects.all()  
  form=StudentForm()
  if request.method=='POST':
      form=StudentForm(request.POST)
      if form.is_valid():
         form.save()
         return redirect('/')
  return render(request,'add.html',{'form':form})


def edit(request,pk):
   student=Student.objects.get(id=pk)
   form=StudentForm(instance=student)
   if request.method =='POST':
       form=StudentForm(request.POST,instance=student)
       if form.is_valid():
          form.save()
          return redirect('/')
       
   return render (request,'edit.html',{'form':form})


def delete(request,pk):
   student=Student.objects.get(id=pk)
   student.delete()
   return redirect ('/')
   

