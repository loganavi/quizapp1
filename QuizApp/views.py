from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from QuizApp.form import SignUpForm,contactform
from QuizApp.models import contact_form
# Create your views here.
def home(request):
	#mydict={"Welcome To SVIMQuiz...!"}
	#return(HttpResponse("hello world"))
	return render(request,'QuizApp/home.html')

def Signup_Form(request):
	if request.method=='GET':
		sform=SignUpForm()
		return render(request,"QuizApp/signup.html",{'sform':sform})
	if request.method=='POST':
		sform=SignUpForm(request.POST)
		user=sform.save()
		user.set_password(user.password)
		user.save()
		sform=SignUpForm()
		mydict={'msg':'Registration Successful...Welcome to SVIMQuiz !!!'}
		return render(request,'QuizApp/signup.html',context=mydict)


@login_required
def contact(request):
	if request.method=='GET':
		cForm=contactform()
		return render(request,'QuizApp/contact.html',{'cForm':cForm})
	
	if request.method=='POST':
		cForm=contactform(request.POST)
		cform=cForm.save()
		cform.save()
		cForm=contactform
		mydict={'msg':'Message Sent.','cForm':cForm}
		return render(request,'QuizApp/contact.html',context=mydict)


@login_required
def task(request):
	if request.method=='POST':
		if request.POST.get('action')=='submit':
			return render(request,'QuizApp/task.html')

@login_required
def game(request):
	return render(request,'QuizApp/game.html')

@login_required
def programming(request):
	return render(request,'QuizApp/programming.html')