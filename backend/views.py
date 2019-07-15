from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from django.http import HttpResponse
# from django.core.mail import send_mail
from django.conf import settings
from backend.forms import loginForm,RegisterForm
from backend.models import user
from django import forms
from django.contrib import messages 

def login(request):
	if request.method=='POST':
		form=loginForm(request.POST)
		if form.is_valid():
			obj=form.cleaned_data
			email=obj['EmailAddress']
			password=obj['Password']
			if (user.objects.filter(EmailAddress=email).exists()  and user.objects.filter(Password=password).exists()):
				template = '../bluecredit'
				return redirect(template)

			else:
				messages.error(request, "Error")
				return redirect('login')
				#raise forms.ValidationError('Incorrect Email or password')
	else:
		form = loginForm()
		return render(request, 'account/signin.html', {'form' : form})


def register(request):
	if request.method == 'POST':
		messages.info(request, 'Your information was sent successfully!')
		form = RegisterForm(request.POST)
		if form.is_valid():
			userObj = form.cleaned_data
			Firstname = userObj['FirstName']
			Surname=userObj['Surname']
			role=userObj['Role']
			email =  userObj['EmailAddress']
			mobilenumber=userObj['MobileNumber']
			password =  userObj['Password']
			confirmpassword=userObj['ConfirmPassword']
			if not (user.objects.filter(EmailAddress=email).exists()):
				user.objects.create(FirstName=Firstname,Surname=Surname,Role=role, EmailAddress = email, MobileNumber=mobilenumber,Password=password,ConfirmPassword=confirmpassword)
				# users = authenticate(EmailAddress = email, Password = password)
				# login(request)
				context = {
					'form':form
	              }
				template='../pending'
				return redirect (template)
			else:
				messages.error(request, "Error")
				return redirect('register')
	else:
		form = RegisterForm()
		return render(request, 'account/signup.html', {'form' : form})


def pending(request):
	context = {}
	template = 'account/pending.html'
	return render(request, template, context)


def index(request):
	context = {}
	template = 'dashboard/index.html'
	return render(request, template, context)


def results(request):
	context = {}
	template = 'dashboard/results.html'
	return render(request, template, context)


def personal(request):
	context = {}
	template = 'dashboard/personal.html'
	return render(request, template, context)

def loandetails(request):
	context = {}
	template = 'dashboard/loandetails.html'
	return render(request, template, context)
