from django.shortcuts import render
import pymongo

def HomeView(request):
    return(render(request,'index.html'))

def mongo(request):
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["Corto"]
    mycol=mydb["URLS"]
    url=request.POST.get("name_url")
    
    return(render(request,"New-URL.html",{"url_value":url}))