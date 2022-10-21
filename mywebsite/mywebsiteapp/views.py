from django.shortcuts import render
from .models import place, people


# Create your views here.
def demo(request):
    obj= place.objects.all()
    task = people.objects.all()
    return render(request,'index.html',{'result':obj,'change':task})
