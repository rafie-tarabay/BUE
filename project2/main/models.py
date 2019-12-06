from django.db import models
class User(models.Model):
    username = models.CharField(max_length=100, blank=True)
    email = models.CharField(max_length=100, blank=True)
    password = models.CharField(max_length=100, blank=True)
    company = models.CharField(max_length=30, blank=True)
    company_site = models.URLField(blank=True)
    Country = models.CharField(
                                max_length=5,
                                choices=[
                                            ('Cairo', 'Cairo'),
                                            ('Alex', 'Alex'),
                                            ('DK', 'Dakahlia'),
                                            ('BA', 'Banha'),
                                        ]   ,
                                default='Cairo',
                              )



from django import forms
class UserForm(forms.ModelForm):
    username = forms.CharField(max_length=100,label='User Name',
                                widget=forms.TextInput(
                                                        attrs={
                                                                "class":"",
                                                                "placeholder":"Your Username"
                                                                }
                                                        )
                               )
    email = forms.EmailField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)


    class Meta:
        model = User
        fields = ['username', 'email', 'password','company', 'company_site','Country']

    def clean_username(self):
        username=self.cleaned_data.get("username")
        qs=User.objects.filter(username=username)
        if qs.exists():
            raise forms.ValidationError("Username is taken")
        return username

    def clean_email(self):
        email=self.cleaned_data.get("email")
        qs=User.objects.filter(email=email)
        if qs.exists():
            raise forms.ValidationError("email is taken")
        return email












#############################################################
class UsersAccounts(models.Model):
    username = models.CharField(max_length=250,default='')
    password = models.CharField(max_length=250,default='')


class LoginForm(forms.Form):
   username = forms.CharField(max_length = 100)
   password = forms.CharField(widget = forms.PasswordInput())
   
   def clean_message(self):
       username = self.cleaned_data.get("username")
       password = self.cleaned_data.get("password")
       dbuser = UsersAccounts.objects.filter(username = username, password=password)
       
       if not dbuser:
           raise forms.ValidationError("User does not exist in our db!")
       return username


####################################################################33333
######################################################################



class phone_book(models.Model):
    phone_name = models.CharField(max_length=250,default='')
    phone_number = models.CharField(max_length=20,default='')
    created_at = models.DateTimeField('date published',auto_now_add=True, blank=True)
    created_by = models.CharField(max_length=7,default='')
    address = models.TextField()
    age = models.IntegerField(default=0)


from django import forms    
class EmpForm(forms.ModelForm):  
    class Meta:  
        model = phone_book  
        fields = "__all__"  