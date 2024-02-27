from django.shortcuts import render,redirect
from crmapp.models import Projects
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
# Create your views here.
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')

def nextpage(request):
    pro = Projects.objects.all()
    return render(request,'index2.html',{'pro':pro})
def nextpage2(request):
    return render(request,'index3.html')
def archived(request):
    pro = Projects.objects.all()
    return render(request,'archived.html',{'pro':pro})
def new(request):
    return render(request,'new.html')
def new_data(request):
    if request.method == 'POST':


        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        profile=request.FILES.get('file')

        project_name = request.POST['project']
        amount = request.POST['amount']
        

        
        
        
        new = Projects(first_name=first_name,last_name=last_name,profile=profile,project_name=project_name,amount=amount)
                            
                                
        new.save()

                           
    return render(request,'new.html')

def updatetoarchived(request,data):


 
        # proid = request.GET.get('id')
        # data = json.loads(request.body)
        # pk = data.get('data')
        pro = Projects.objects.get(id=data)
        pro.status="ARCHIVED";
        pro.save()

   
   
        return redirect('nextpage')


def updatetounarchived(request,data):


 
        # proid = request.GET.get('id')
        # data = json.loads(request.body)
        # pk = data.get('data')
        pro = Projects.objects.get(id=data)
        pro.status="UNARCHIVED";
        pro.save()

   
   
        return redirect('nextpage')