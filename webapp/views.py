from django.shortcuts import render, redirect
from .forms import CreateUserForm, LoginForm, CreateRecordForm, UpdateRecordForm, CreateChildForm, BriefNoteForm, IntitialVisitsForm, TreatmentPlanForm, InitialPsychiatricEvaluationAdultForm, PsychiatricProgressNoteForm

from django.contrib.auth.models import auth
from django.contrib.auth import authenticate

from django.contrib.auth.decorators import login_required

from .models import Record

from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q    



# - Homepage 

def home(request):

    return render(request, 'webapp/index.html')


# - Register a user

#def register(request):

    #form = CreateUserForm()

    #if request.method == "POST":

       # form = CreateUserForm(request.POST)

      #  if form.is_valid():

     #       form.save()

     #       messages.success(request, "Account created successfully!")

    #        return redirect("my-login")

   # context = {'form':form}

   # return render(request, 'webapp/register.html', context=context)


# - Login a user

def my_login(request):

    form = LoginForm()

    if request.method == "POST":

        form = LoginForm(request, data=request.POST)

        if form.is_valid():

            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:

                auth.login(request, user)

                return redirect("dashboard")

    context = {'form':form}

    return render(request, 'webapp/my-login.html', context=context)


# - Dashboard

@login_required(login_url='my-login')
def dashboard(request):

    my_records = Record.objects.all().order_by('-id')
    #Set up pagination

    p = Paginator(Record.objects.all().order_by('-id'), 20)
    page = request.GET.get('page')

    clients = p.get_page(page)

    context = {'records': clients} 

    return render(request, 'webapp/dashboard.html', context=context)



# - Create a record 

@login_required(login_url='my-login')
def create_record(request):

    form = CreateRecordForm()

    if request.method == "POST":

        form = CreateRecordForm(request.POST)

        if form.is_valid():

            form.save()

            messages.success(request, "Your record was created!")

            return redirect("dashboard")

    context = {'form': form}

    return render(request, 'webapp/create-record.html', context=context)

@login_required(login_url='my-login')
def create_child_form_record(request):

    form = CreateChildForm()

    if request.method == "POST":

        form = CreateChildForm(request.POST)

        if form.is_valid():

            form.save()

            messages.success(request, "Your record was created!")

            return redirect("dashboard")

    context = {'form': form}

    return render(request, 'webapp/childform.html', context=context)

@login_required(login_url='my-login')
def create_BriefNote_record(request):

    form = BriefNoteForm()

    if request.method == "POST":

        form = BriefNoteForm(request.POST)

        if form.is_valid():

            form.save()

            messages.success(request, "Your record was created!")

            return redirect("appointmentSession")

    context = {'form': form}

    return render(request, 'webapp/briefNote.html', context=context)


#create initial visits record 
@login_required(login_url='my-login')
def create_InitialVisitsForm_record(request):

    form = IntitialVisitsForm()

    if request.method == "POST":

        form = IntitialVisitsForm(request.POST)

        if form.is_valid():

            form.save()

            messages.success(request, "Your record was created!")

            return redirect("appointmentSession")

    context = {'form': form}

    return render(request, 'webapp/initialVisitsForm.html', context=context)

#create progress note record 
@login_required(login_url='my-login')
def create_ProgressNoteForm_record(request):

    form = IntitialVisitsForm()

    if request.method == "POST":

        form = IntitialVisitsForm(request.POST)

        if form.is_valid():

            form.save()

            messages.success(request, "Your record was created!")

            return redirect("appointmentSession")

    context = {'form': form}

    return render(request, 'webapp/progressNote.html', context=context)

#create progress note record 
@login_required(login_url='my-login')
def create_TreatmentPlan_record(request):

    form = TreatmentPlanForm()

    if request.method == "POST":

        form = TreatmentPlanForm(request.POST)

        if form.is_valid():

            form.save()

            messages.success(request, "Your record was created!")

            return redirect("appointmentSession")

    context = {'form': form}

    return render(request, 'webapp/treatmentPlanForm.html', context=context)

#create progress note record 
@login_required(login_url='my-login')
def create_InitialPsychiatric_record(request):

    form = InitialPsychiatricEvaluationAdultForm()

    if request.method == "POST":

        form = InitialPsychiatricEvaluationAdultForm(request.POST)

        if form.is_valid():

            form.save()

            messages.success(request, "Your record was created!")

            return redirect("appointmentSession")

    context = {'form': form}

    return render(request, 'webapp/intialPsychiatricEvaluationAdultForm.html', context=context)

#create progress note record 
@login_required(login_url='my-login')
def create_PsychiatricProgressNote_record(request):

    form = PsychiatricProgressNoteForm()

    if request.method == "POST":

        form = PsychiatricProgressNoteForm(request.POST)

        if form.is_valid():

            form.save()

            messages.success(request, "Your record was created!")

            return redirect("appointmentSession")

    context = {'form': form}

    return render(request, 'webapp/psychiatricProgressNote.html', context=context)

# - Update a record  

@login_required(login_url='my-login')
def update_record(request, pk):

    record = Record.objects.get(id=pk)

    form = UpdateRecordForm(instance=record)

    if request.method == 'POST':

        form = UpdateRecordForm(request.POST, instance=record)

        if form.is_valid():

            form.save()

            messages.success(request, "Your record was updated!")

            return redirect("dashboard")
        
    context = {'form':form}

    return render(request, 'webapp/update-record.html', context=context)


@login_required(login_url='my-login')
def search_client(request):

    if request.method == "POST":
        searched  = request.POST['searched']
        
        my_record = Record.objects.filter(Q(first_name__contains = searched)|Q(last_name__contains =searched)).order_by('-id')

    #context = {'records': my_records}

    return render(request, 'webapp/search-record.html',{'searched': searched, 'my_record':my_record})

@login_required(login_url='my-login')
def search_clinicians(request):

    if request.method == "POST":
        searched  = request.POST['searched']
        
        my_record = Record.objects.filter(talk_therapy_doc_name__contains = searched).order_by('-id')

    #context = {'records': my_records}

    return render(request, 'webapp/search-clinicians.html',{'searched': searched, 'my_record':my_record})

@login_required(login_url='my-login')
def search_facility(request):

    if request.method == "POST":
        searched  = request.POST['searched']
        
        my_record = Record.objects.filter(facility_name__contains = searched).order_by('-id')



    #context = {'records': my_records}

    return render(request, 'webapp/search-facility.html',{'searched': searched, 'my_record':my_record})

# - Read / View a singular record

@login_required(login_url='my-login')
def singular_record(request, pk):

    all_records = Record.objects.get(id=pk)

    context = {'record':all_records}

    return render(request, 'webapp/view-record.html', context=context)


def appointment_session(request):
    return render(request, 'webapp/appointmentSession.html')
# - Delete a record

@login_required(login_url='my-login')
def delete_record(request, pk):

    record = Record.objects.get(id=pk)

    record.delete()

    messages.success(request, "Your record was deleted!")

    return redirect("dashboard")



# - User logout

def user_logout(request):

    auth.logout(request)

    messages.success(request, "Logout success!")

    return redirect("my-login")





