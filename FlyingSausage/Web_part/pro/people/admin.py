from django import forms
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from people.models import Member, Follower


class UserCreationForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    password1 = forms.CharField(label='password', widget=forms.PasswordInput)  # let the user to enter the password
    password2 = forms.CharField(label='comfirm password', widget=forms.PasswordInput)# let the user to enter the password for the second time
    class Meta:
        model = Member
        fields = ('email', 'username')

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("verify failed")
        return password2
    #clean the password
    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])

        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()
    class Meta:
        model = Member
        fields = ('email', 'password', 'username', 'is_active', 'is_admin',)
    def clean_password(self):
        return self.initial["password"]
    #clean the password



admin.site.register(Member, MyUserAdmin)
admin.site.register(Follower)
