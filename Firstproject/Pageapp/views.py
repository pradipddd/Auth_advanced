from django.shortcuts import render,redirect
from .forms import LaptopModelForm
from django.core.paginator import Paginator
from .models import Laptop


# Create your views here.

def Laptop_add_view(request):
    form=LaptopModelForm()
    if request.method =='POST':
        form=LaptopModelForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
    template_name='Pageapp/Laptopadd.html'
    context={'form':form}
    return render(request,template_name,context)

def Laptop_show_view(request):
    obj_list = Laptop.objects.all()
    paginator = Paginator(obj_list, 1) # Show 1 laptop per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    template_name='Pageapp/Laptoplist.html'
    context={'page_obj':page_obj}
    return render(request,template_name,context)

