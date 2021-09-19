from django.shortcuts import render,redirect
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.contrib import messages
from .forms import DocumentForm
from .models import Document

# Create your views here.

def Simple_upload(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        template_name='Imageapp/simple_upload.html'
        context={'uploaded_file_url':uploaded_file_url}
        return render(request,template_name,context)
    
    template_name='Imageapp/simple_upload.html'
    context={}
    return render(request,template_name,context)

def model_form_upload(request):
    form = DocumentForm()
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('show_upload')
    template_name='Imageapp/model_form_upload.html'
    context={'form':form}
    return render(request,template_name,context)

def show_upload_view(request):
    file=Document.objects.all()
    template_name='Imageapp/show_uplaod.html'
    context={'file':file}
    return render(request,template_name,context)

    
    
    
    


