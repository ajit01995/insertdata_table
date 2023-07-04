from django.shortcuts import render

# Create your views here.
from app.models import*
from django.http import HttpResponse


def top(request):
    if request.method=='POST':
        Topic_name=request.POST['topic']
        tn=Topic.objects.get_or_create(Topic_name=Topic_name)[0]
        tn.save()
        return HttpResponse('Topic insert succefully')

    return render(request,'topic.html')



def web(request):
    LTO=Topic.objects.all()
    d={'LTO' : LTO}
    if request.method=='POST':
        Topic_name=request.POST['tn']
        tn=Topic.objects.get(Topic_name=Topic_name)
        Name=request.POST['na']
        url=request.POST['ur']
        Wo=Webpage.objects.get_or_create(Topic_name=tn,name=Name,url=url)[0]
        Wo.save()
        return HttpResponse('data insert succefully')

    return render(request,'web.html',d)




def retrive_webpage(request):
    LTO=Topic.objects.all()
    d={'LTO' : LTO}
    if request.method=='POST':
        MSTS=request.POST.getlist('topic')
        RWOS=Webpage.objects.none()
        for i in MSTS:
            RWOS=RWOS|Webpage.objects.filter(Topic_name=i)
        d1={'RWOS': RWOS}
        return render(request,'display_webpage.html',d1)
    return render(request,'retrive_webpage.html',d)




def checkbox(request):
    LTO=Topic.objects.all()
    d={'LTO' : LTO}

    return render(request,'checkbox.html',d)

