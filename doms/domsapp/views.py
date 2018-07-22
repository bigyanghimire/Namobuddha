from django.shortcuts import render
from django.http import HttpResponse
from .models import File
from django.db.models import Q
from django.shortcuts import redirect
from . import forms



def index(request):
    form=forms.CreateArticle()
    
    file=File.objects.all().order_by('-id')
    context={
'file':file,
'form':form
    }
    return render(request,"index.html",context)

def addfile(request):
    form=forms.CreateArticle()
    if request.method=='POST':
        form=forms.CreateArticle(request.POST,request.FILES)
        if form.is_valid():
            form.save();
            

            return redirect('/')
    else:
        form=CreateArticle()
    return render(request,'index.html',{'form':form})    

def search(request):
    
    template='index.html'
    query=request.GET.get('q')
    if query:
        file=File.objects.all().order_by('-id')
        results=File.objects.filter(Q(title__icontains = query) | Q(category__icontains = query))
        
        context={
        'file':results,
        
         }

        return render(request,template,context)
    else:
        return render(request,template,context)

def searchdate(request):
    template='index.html'
    query=request.GET.get('q')
    if query:
        file=File.objects.all().order_by('-id')
        results=File.objects.filter(Q(uploaded_at__year__icontains= query) | Q(uploaded_at__day__icontains= query)) 
                      
    
        context={
        'file':results,
        
         }



        return render(request,template,context)     
        
'''       
def searchcat(request):
    
    template='index.html'
    query=request.GET.get('q2')
    if query:
        file=File.objects.all().order_by('-id')
        results=File.objects.filter(Q(category__icontains = query))
        
        context={
        'file':results,
        
         }

        return render(request,template,context)
    else:
        return HttpResponse("k ho")

'''        




            

    #if(request.method == 'POST'):
        #title=request.POST['title']
        #comments=request.POST['comments']
        #fileadded=request.POST['fileadded']
        #category=request.POST['category']
        #status=request.POST['status']
        #fileobj=File(title=title,comments=comments,document=fileadded(),category=category,status=status)
        #fileobj.save();

        
        
        

        #return redirect('/')

    #else:
        #return render(request,'index.html')

def DeleteView(request,pk=None):
    object = File.objects.get(id=pk)
    object.delete()
    return redirect('/')


