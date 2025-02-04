from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,redirect
from django.contrib import messages
from django.db.models import Q
from .models import Student
from django.core.mail import send_mail,EmailMessage
from django.template.loader import render_to_string
from datetime import datetime


# Create your views here.
def home(request):
    searched=request.GET.get('searched')
    if searched:
        data=Student.objects.filter(Q(name__icontains=searched)|Q(age__icontains=searched))
        data=data.filter(isdelete=False)
    else:
      data=Student.objects.filter(isdelete=False)
    return render(request, 'crud_app/home.html',{"data":data})
   

def form(request):
    if request.method == 'POST' and request.FILES:
        data = request.POST
        name = data.get('name')
        age = data.get('age') 
        email = data.get('email')
        password = data.get('password')
        message = data.get('message')
        image=request.FILES.get('image')

       
        try:
            age = int(age)
        except ValueError:
           
            messages.error(request, "Invalid age. Please enter a number between 0 and 100.")
            return redirect('form')

        # Validate the age range
        if age < 0 or age > 100:
            messages.error(request, "Your age should be between 0 and 100.")
            return redirect('form')

      
        try:
            user = Student(name=name, age=age, email=email, password=password, message=message,image=image)
            user.full_clean() 
            user.save()

          
            
          

            subject = "Django Training"
            message = render_to_string('crud_app/msg.html',{'name':name ,'date':datetime.now})
            from_email = 'rojikc764@gmail.com'
            recipient_list = [email,'rojikc764@gmail.com','adhikarialan723@gmail.com']

            # send_mail(subject, message, from_email, recipient_list,fail_silently=True)
            email_msg=EmailMessage(subject,message,from_email,recipient_list)
            email_msg.attach_file('email.pdf')
            email_msg.send(fail_silently=True)

            messages.success(request, f"Hi {name}, your form has been successfully submitted and Please Check your email for Confirmation!")
            return redirect('form')
        except Exception as e:
            messages.error(request, f"An error occurred: {str(e)}")
            return redirect('form')

    
    return render(request, 'crud_app/form.html')


def about(request):
    return render(request ,'crud_app/about.html')

def contact(request):
    return render(request ,'crud_app/contact.html')


def delete_data(request,id):
    data=Student.objects.get(id=id)
    data.isdelete=True
    data.save()
    return redirect('home')

def clear(request):
    Student.objects.all().update(isdelete=True)
    # for student in data:
    #   student.isdelete=True
    #   student.save()
    return redirect('home')


def recycle(request):
    data = Student.objects.filter(isdelete=True)
    return render(request,'crud_app/recycle.html',{'data':data})


def restore(request,id):
    data=Student.objects.get(id=id)
    data.isdelete=False
    data.save()
    return redirect('home')

def edit(request,id):
    data=Student.objects.get(id=id)

    if request.method=="POST":
        
        data=Student.objects.get(id=id)
        data.name=request.POST.get('name')
        data.age=request.POST.get('age')
        data.email=request.POST.get('email')
        data.message=request.POST.get('message')
        data.save()
        return redirect('home')
    return render(request,'crud_app/edit.html',{'data':data})