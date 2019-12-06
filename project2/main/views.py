from django.shortcuts import render



from django.views import View
class MyFormView(View):
    template_name = 'home.html'

    def get(self, request):
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/success/')
        return render(request, self.template_name, {'form': form})




from django.core.files.storage import FileSystemStorage
def upload(request):
    if request.method == 'POST' and request.FILES['fileToUpload']:
        myfile = request.FILES['fileToUpload']
        fs = FileSystemStorage()

        #File will be saved on MEDIA_ROOT path and access using MEDIA_URL
        filename = fs.save(myfile.name, myfile) 
    
    template_name='home.html'
    context={}
    return render( request , template_name , context )






from main.models import UsersAccounts,LoginForm

def login(request):
    template_name='main/login.html'
    username = None
   
    if request.method == "POST":
        MyLoginForm = LoginForm(request.POST)
        
        if MyLoginForm.is_valid():
            username = MyLoginForm.cleaned_data['username']
   
    return render(request, template_name, {"username" : username})



def home(request):
    template_name='home.html'
    context={}
    return render( request , template_name , context )


















from django.contrib import messages
from django.shortcuts import redirect
from main.models import UserForm
from django.db import transaction
@transaction.atomic
def NewUser(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST or None)   
        if user_form.is_valid():
            user_form.save() 
            messages.success(request, 'Your profile was successfully updated!')
            return redirect('main:newuser')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        user_form = UserForm() 
    
    return render(request, 'main/newuser.html', {'user_form': user_form, })





       
"""
from django.db import connection
def custom_sql_insert(SQL):
    try:
        cursor = connection.cursor()
        cursor.execute(SQL)
        return cursor.lastrowid
    except Exception as e:
        return 0


def custom_sql_insert_update_delete(SQL):
    cursor = connection.cursor()
    cursor.execute(SQL)


def custom_sql_select(SQL):
    with connection.cursor() as cursor:
        cursor.execute(SQL)
        rows = cursor.fetchall()
        return rows








#Select All Records
RecordType=MarcRecordType.objects.all()

#Select One Record  
bibliographies = marc_bibliographies.objects.get(pk=100)

#Select Record
Marc = RawMarc.objects.filter(BibID=BibID).order_by('Treeid')   
if Marc.count()<=0:
    print('No records')

#Select Raw SQL
people = Person.objects.raw('SELECT id, first_name,age FROM myapp_person')
  

#Delete Record
marc_Dump.objects.filter(BibID=BibID).delete()

  
#Insert in two tables in Transaction
with transaction.atomic():
    rootObj = marc_bibliographies.objects.create(title_ar='',biblio_type_id=recordType,price=price,source_id=Providerid,created_by=userid,created_at=timestamp)
    rootObj.save()


    marc=RawMarc.objects.create(BibID=rootObj.pk,Type='0',Treeid=str(Treeid),Key=tags.tag,Value=tags.data)
    marc.save() 

#Update Record
rootObj = marc_bibliographies.objects.get(pk=BibID)
rootObj.price=price
rootObj.parent_id=parent_id
rootObj.save()

"""