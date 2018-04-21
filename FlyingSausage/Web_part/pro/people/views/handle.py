from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from people.forms import RegisterForm, LoginForm
from people.models import Member, Follower, EmailVerified as Email, FindPass
from question.models import Topic, Comment
from django.views.decorators.csrf import csrf_protect
from django.core.urlresolvers import reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.core.cache import cache
from pro.settings import NUM_TOPICS_PER_PAGE,NUM_COMMENT_PER_PAGE
from django.conf import settings
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.core.mail import send_mail
import datetime
from django.contrib.auth import logout as auth_logout, authenticate, login as auth_login

SITE_URL = getattr(settings,'SITE_URL')

@csrf_protect
def register(request):
	if  request.method == 'POST':
		form = RegisterForm(request.POST)
		if form.is_valid():
			data = form.cleaned_data
			new_user = Member.objects.create_user(username=data['username'],
				                                  email=data['email'],
				                                  password=data['password'])	

			new_user.save()

			email_verified = Email(user=new_user)
			email_verified.token = email_verified.generate_token()
			email_verified.save()

			#email_verified
			send_mail("Welcome","%s Hello：\r\nplease click the link below to verify your email：%s%s"%(new_user.username,SITE_URL,reverse('user:email_verified',args=(new_user.id,email_verified.token))),
				"kashun.712@gmail.com",[data['email']]
				)
			messages.success(request,'congratulations，please check the message in your email address.')
			user = authenticate(email=data['email'],password=data['password'])
			#check
			auth_login(request,user)
			#login
			go =reverse('question:index')
			is_auto_login = request.POST.get('auto')
			if not is_auto_login:
				request.session.set_expiry(0)
			else:
				request.session.set_expiry(60)

			return HttpResponseRedirect(go)
	else:
		form = RegisterForm()
	return render(request,'people/register.html',{'form':form})

@csrf_protect
def login(request):
	if request.user.is_authenticated():
	#check if the user is logged in or not
		return HttpResponseRedirect(request.META.get('HTTP_PEFERER','/'))
		#HTTP REFERER header 
		#
	if request.method == 'POST':
		form = LoginForm(request.POST)
		if form.is_valid():
			#clean_fileds
			data = form.cleaned_data
			username = data['username']
			if '@' in username:
				email = username

			else:
				user = Member.objects.get(username=username)
				email = user.email
			user = authenticate(email=email,password=data['password'])
			if user is not None:
				auth_login(request,user)
				go = reverse('question:index')
				is_auto_login = request.POST.get('auto')
				if not is_auto_login:
					request.session.set_expiry(0)
				return HttpResponseRedirect(go)
			else:
				messages.error(request,'password is not correct')
				return render(request,'people/login.html',locals())
	else:
		form = LoginForm()
		return render(request,'people/login.html',{'form':form})

def logout(request):
	auth_logout(request)
	return HttpResponseRedirect(reverse('question:index'))


