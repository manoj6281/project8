from django.shortcuts import render

# Create your views here.

def data_render(request):
    data='this is our assumption'
    d={'assumption':data}
    return render(request,'data_render.html',context=d)




def login(request):
    data1='Manojkumar'
    data2='23'
    d={'username':data1,'Age':data2}
    return render(request,'login.html',context=d)