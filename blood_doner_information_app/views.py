from multiprocessing import context
from re import L
import requests
from rest_framework import generics
from django.shortcuts import render,redirect
from django.contrib import messages
from .models import blood_doner_createForm,blood_doner_info

#for serializer
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import blood_doner_info
from .forms import SearchForm
from .serializers import doner_Serializer
from rest_framework import filters




# Create your views here

def Home(request):

    context={

    }

    return render(request,'page 5.html',context)

#your data details
def your_data_details(request):

    context={

    }

    return render(request,'page 6 (your data part 1).html',context)




#all data details
def all_data_details(request):

    context={

    }

    return render(request,'page 9.html',context)



#your data json view
@csrf_exempt
def your_data_json_view(request):

    if request.method == 'GET':
        creator = request.user
        my_data=blood_doner_info.objects.filter(author=creator)
        serializer = doner_Serializer(my_data, many=True)
        return JsonResponse(serializer.data,safe=False)


    context={

    }

    return render(request,'page 7 (api view).html',context)


#your data template view
def your_data_template_view(request):
    creator = request.user
    my_data=blood_doner_info.objects.filter(author=creator)

    context={
        'my_data': my_data 

    }

    return render(request,'page 8 (template view).html',context)


#all data json view

@csrf_exempt
def all_data_json_view(request):

    if request.method == 'GET':
        all_doner_api = blood_doner_info.objects.all()
        serializer = doner_Serializer(all_doner_api, many=True)
        return JsonResponse(serializer.data,safe=False)



    context={
        

    }

    return render(request,'page 10 (api view).html',context)


#all data template view
def all_data_template_view(request):
    doner_show = blood_doner_info.objects.all()
    

    context={
        'doner_show' : doner_show

    }

    return render(request,'page 11 (template view).html',context)


#create data
def create_doner(request):
    if request.method == 'POST':
        pos = blood_doner_createForm(request.POST)
        if pos.is_valid():
            data = blood_doner_info()
            data.name = pos.cleaned_data['name']
            data.email = pos.cleaned_data['email']
            data.phone = pos.cleaned_data['phone']
            data.age = pos.cleaned_data['age']
            data.gender = pos.cleaned_data['gender']
            data.blood_group = pos.cleaned_data['blood_group']
            data.author = request.user

            data.save()
            messages.success(request, 'Your informative comment has been sent')
            return redirect('all_data_template_view')
        return redirect('create_doner')


    context={

    }

    return render(request,'page 12 (create form).html',context)


#get data from api

#def get_data_from_api(request):
#    url="http://127.0.0.1:8000/information/json_view_all/"


#    r = requests.get(url).json()
   # print(r)

#    doner_list=[]


#    for pp in r:

#    doner_info ={
#        'Name': pp['name'],
#        'Email': pp['email'],
#        'Phone': pp['phone'],
#        'Age': pp['age'],
#        'Gender': pp['gender'],
#        'Blood_group': pp['blood_group'],
#        'author' :pp['author'],
#     }
    # print("the temp value is ",doner_info)

#     doner_list.append(doner_info)
   # print("the doner list is : ",doner_list)


#    context={
#        'doner_info': doner_info,
#        'doner_list': doner_list

#    }

#    return render(request,'page 13 (get data from api).html',context)



#search data from api

class search_data_from_api(generics.ListAPIView):
    queryset = blood_doner_info.objects.all()
    serializer_class = doner_Serializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['blood_group']

        

    


        

