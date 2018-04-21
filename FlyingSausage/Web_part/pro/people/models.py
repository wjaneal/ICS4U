from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django.utils import timezone
import hashlib
import random
import string
from django.conf import settings
SALT = getattr(settings,'EMAIL_TOKEN_SALT')

# Create your models here.
class MyUserManager(BaseUserManager):
	def create_user(self, username, email, password=None):
		if not email :
			raise ValueError('Users must have an email address')
		if not username:
			raise ValueError('Users must have an username')
		now = timezone.now()
		user = self.model(
			username=username,
			email=self.normalize_email(email),
			date_joined=now,
			last_login=now
			)
		user.set_password(password)
		user.save(using=self._db)
		return user
	def create_superuser(self, username, email, password):
		user = self.create_user(username,
			email,
			password=password,
			)
		user.is_admin = True
		user.save(using=self._db)
		return user

class Member(AbstractBaseUser):
	email = models.EmailField(verbose_name='email',max_length=255,unique=True,)
	username = models.CharField(verbose_name="username", max_length=16, unique=True)
	email_verified = models.BooleanField(verbose_name="if email is verified", default=False)
	is_active = models.BooleanField(default=True)
	is_admin = models.BooleanField(default=False)

	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ['username']

	objects = MyUserManager()

	def __str__(self):
		return self.username

	def calculate_au(self):
		self.au = self.topic_num * 5 + self.comment_num * 1
		return self.au

	def is_email_verified(self):
		return self.email_verified	

	def get_email(self):
		return self.email


	def get_username(self):
		return self.username

	def get_full_name(self):
		return self.email

	def get_short_name(self):
		return self.username

	def has_perm(self, perm, obj=None):
		return True

	def has_module_perms(self, app_label):
		return True

	def is_staff(self):
		return self.is_admin


class EmailVerified(models.Model):
	user = models.OneToOneField(Member, related_name="user")
	token = models.CharField("Email verify token", max_length=32, default=None)
	timestamp = models.DateTimeField(default=timezone.now)
#DateTimeField . datetime.datetime.now
	def __str__(self):
		return "%s@%s" % (self.user, self.token)

	def generate_token(self):
		year = self.timestamp.year
		month = self.timestamp.month
		day = self.timestamp.day
		date = "%s-%s-%s" % (year, month, day)
		token = hashlib.md5((self.ran_str()+data).encode('utf-8')).hexdigest()
		return token
	def ran_str(self):
		salt = ''.join(random.sample(string.ascii_letters + string.digits, 8))
		return salt + SALT

class FindPass(models.Model):
	user = models.OneToOneField(Member, verbose_name="user")
	token = models.CharField(max_length=32, blank=True)
	timestamp = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return "%s@%s" % (self.user, self.token)

	def generate_token(self):
		year = self.timestamp.year
		month = self.timestamp.month
		day = self.timestamp.day
		date = "%s-%s-%s" % (year, month, day)
		token = hashlib.md5((self.ran_str()+data).encode('utf-8')).hexdigest()
		return token
	def ran_str(self):
		salt = ''.join(random.sample(string.ascii_letters + string.digits, 8))
		return salt + SALT

