from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import login 
from django.contrib.auth import authenticate
from django.contrib import messages

def index(request):
    return render(request,'index.html',{
})
    
def admin(request):
    return render(request,'admin',{
})