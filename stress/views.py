from django.shortcuts import render
from django.http import HttpResponse
from stress.models import StressDetection





# Create your views here.
# def index(request):
#     context={'a':'helloworld'}
#     # return render(request,'index.html',)
#     # return render(request,'indexgrid.html',)
#     return render(request,'new 1.html',)
#     #return render(request,'index.html',)
#     #return render(request,'about us.html',)
#     return render(request,'work.html',)
#     return HttpResponse()


def new_1(request):
    return render(request,'new 1.html')

def home(request):
    return render(request,'home.html')


def about_us(request):
    return render(request,'work.html')

def click_here(request):
    return render(request,'ques.html')

def data(request):
    ques1=request.POST['question4']
    ques2=request.POST['When']
    ques3=request.POST['feel']
    ques4=request.POST['question7']
    ques5=request.POST['uestion8']
    ques6=request.POST['find']
    ques7=request.POST['spend']
    ques8=request.POST['goal']
    ques9=request.POST['learn']
    ques10=request.POST['psychological']
    ques11=request.POST['relief']
    ques12=request.POST['cognitive']
    ques13=request.POST['work']
    

    ins=StressDetection(question1=ques1,
    question2=ques2,
    question3=ques3,
    question4=ques4,
    question5=ques5,
    question6=ques6,
    question7=ques7,
    question8=ques8,
    question9=ques9,
    question10=ques10,
    question11=ques11,
    question12=ques12,
    question13=ques13)

    ins.save()

    
    return render(request,'ques.html')

     
