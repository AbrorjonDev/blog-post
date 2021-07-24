from django.contrib.auth.forms import UserCreationForm,UserChangeForm

from .models import CustomUser

class CustomCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('username','first_name','last_name','email','age','address',)


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('username','first_name','last_name','email','age','address',)



