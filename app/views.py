from django.shortcuts import render,redirect
from .import models
from django.contrib import messages

# Create your views here.
def index(request):
    contact = models.Contact.objects.all().order_by('-id')
    context = {
        'contacts':contact
    }
    return render(request,'index.html',context)


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        contact = models.Contact(name=name,email=email,subject=subject,message=message)
        contact.save()
        messages.success(request,'Your contact is sended successfully')
        return redirect('index')
    return render(request,'contact.html')


def delete_contact(request,contact_id):
    contact = models.Contact.objects.get(id = contact_id)
    if request.method == "POST":
        contact.delete()
        messages.success(request=request,message=f'Your data is deleted successfully ')
        return redirect('index')
    
    return render(request,'delete_contact.html',{'contact':contact})


def edit_contact(request,contact_id):
    contact = models.Contact.objects.get(id = contact_id)
    if request.method == 'POST':
        contact.name = request.POST['name']
        contact.email = request.POST['email']
        contact.subject = request.POST['subject']
        contact.message = request.POST['message']
        contact.save()
        messages.success(request=request,message=f'You contact updated successfully')
        return redirect('index')
    context = {
        'contact':contact
    }
    return render(request,'edit_contact.html',context)


def view_contact(request,contact_id):
    contact = models.Contact.objects.get(id = contact_id)
    context = {
        'contact':contact
    }
    return render(request,'view_contact.html',context)