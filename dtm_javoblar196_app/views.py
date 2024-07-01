from django.shortcuts import *
from django.urls import *
# from .tests import idjavob
import pandas as pd
from django.contrib.auth import *
from .models import *
from .forms import *




# Create your views here.
def home(request):
    errors=''
    if request.method=="POST":
        id=request.POST.get('user_id')
        return redirect(reverse('dtm_javoblar196_app:javob',kwargs=dict(id=id)))
    return render(request,'index.html')



def javob(request,id):
    df = pd.read_excel("excel.xlsx")
    olish=df[df['ID (QRcode)']==int(id)]
    cols1 = olish.values[0][14:14+50]
    reverse1 = ''.join(cols1)
    cols3 = f"{olish.values[0][3:3+5]} {olish.values[0][9:9+1]} {olish.values[0][11:11+1]}"
    reverse3 = cols3.replace('[','').replace(']','').replace(',','').replace("'",'').replace('"','')
    cols4 = eval(f"{int(olish.values[0][167:167+1] )}+{int(olish.values[0][171:171+1])}")
    lis=[]
    for i in olish.values[0][114:114+50]:
        if i==1:
            lis.append('✅')
        elif i==0:
            lis.append('❌')
    
    data = zip(reverse1,lis)
    return render(request,'javob.html', 
                  {
                      'javob': reverse1,
                      'malumot':reverse3,
                      'topdi':lis,
                      'topladi':cols4,
                      "id":id,
                      "data":data
                      })