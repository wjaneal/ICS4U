from django import forms
from people.models import Member
from django.core.validators import URLValidator

class RegisterForm(forms.Form):
	username = forms.CharField(label="username", min_length=2, max_length=16,required=True,)
	password = forms.CharField(label="password", min_length=6,max_length=30, widget=forms.PasswordInput(), required=True)
	password2 = forms.CharField(label="repeat password", min_length=6, max_length=30,widget=forms.PasswordInput(), required=True)
	email = forms.EmailField(label="email", max_length=255, required=True)

	def clean_password2(self):
		password = self.cleaned_data.get("password")
		password2 = self.cleaned_data.get("password2")
		if password and password2 and password != password2:
			raise forms.ValidationError("the two password are not the same")
		return password2

	def clean_username(self):
		username = self.cleaned_data.get("username").strip()
		if username[:1] == '_':
			raise forms.ValidationError("user name can not begin with dash")
		try:
			Member._default_manager.get(username=username)
		except Member.DoesNotExist:
			return username
		raise forms.ValidationError("username %s has been existed" % username)

	def clean_email(self):
		email = self.cleaned_data.get("email").strip()
		try:
			Member._default_manager.get(email=email)
		except Member.DoesNotExist:
			return email
		raise forms.ValidationError("email %s has been existed" % email)

class LoginForm(forms.Form):
	username = forms.CharField(label="username",required=True,)
	password = forms.CharField(label="password", widget=forms.PasswordInput(),required=True)
	def clean_username(self):
		username = self.cleaned_data.get("username").strip()
		username_exist = True
		email_exits = True
		try:
			Member._default_manager.get(username=username)
		except Member.DoesNotExist:
			username_exist = False
		try:
			Member._default_manager.get(email=username)
		except Member.DoesNotExist:	
			email_exits = False
		if username_exist or email_exits:
			return username
		raise forms.ValidationError("username of emil does not exist")

class ProfileForm(forms.ModelForm):

	email = forms.EmailField(label="email", required=True, max_length=255,widget=forms.TextInput(attrs={'class':'disabled form-control',}))

	def __init__(self, *args, **kwargs):
		super(ProfileForm, self).__init__(*args, **kwargs)
		user = kwargs.pop('instance',None)
		self.old_email = user.email

	def clean_email(self):
		cleaned_data = super(ProfileForm, self).clean()
		email = cleaned_data.get("email").strip()
		try:
			user = Member.objects.get(email=email)
		except (Member.DoesNotExist,ValueError):
			return email
		else:
			if user.email == self.old_email:
				return email
			else:
				raise forms.ValidationError(u"email %s has been existed" % email)



class PasswordChangeForm(forms.Form):  #let the user to reset the password
	old_password = forms.CharField(label="old password", widget=forms.PasswordInput(attrs={'class':'form-control'}),required=True)
	password = forms.CharField(label="new password", min_length=6, max_length=30,widget=forms.PasswordInput(attrs={'class':'form-control'}),required=True)
	password2 = forms.CharField(label="repeat your new password", min_length=6,max_length=30, widget=forms.PasswordInput(attrs={'class':'form-control'}),required=True)

	def clean_password2(self):
		password = self.cleaned_data.get("password")
		password2 = self.cleaned_data.get("password2")
		if password and password2 and password != password2:
			raise forms.ValidationError("the two password are not the same")
		return password2
