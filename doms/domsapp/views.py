from django.shortcuts import render
from django.http import HttpResponse
from .models import File
from django.db.models import Q
from django.shortcuts import redirect




def index(request):
	
	file=File.objects.all()[0:]
	context={
'file':file

	}
	return render(request,"index.html",context)

def search(request):
    
    template='index.html'
    query=request.GET.get('q')
    if query:
        file=File.objects.all()[0:]
        results=File.objects.filter(Q(title__icontains = query))
        context={
        'file':results,
         }

        return render(request,template,context)
    else:
        return HttpResponse("<alert>Please enter a search term</alert>")



def addfile(request):
    if(request.method == 'POST'):
        title=request.POST['title']
        comments=request.POST['comments']
        fileadded=request.POST['fileadded']
        category=request.POST['category']
        fileobj=File(title=title,comments=comments,document=fileadded,category=category)
        fileobj.save();

        
        
        

        return redirect('/')

    else:
        return render(request,'index.html')

