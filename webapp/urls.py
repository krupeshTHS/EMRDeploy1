
from django.urls import path

from . import views

urlpatterns = [

    path('', views.home, name=""),

    #path('register', views.register, name="register"),

    path('my-login', views.my_login, name="my-login"),

    path('user-logout', views.user_logout, name="user-logout"),

    # CRUD

    path('dashboard', views.dashboard, name="dashboard"),

    path('create-record', views.create_record, name="create-record"),

    path('search-record', views.search_client, name="search-record"),

    path('search-clinicians', views.search_clinicians, name="search-clinicians"),

    path('search-facility', views.search_facility, name="search-facility"),

    path('update-record/<int:pk>', views.update_record, name='update-record'),

    path('record/<int:pk>', views.singular_record, name="record"),

    path('delete-record/<int:pk>', views.delete_record, name="delete-record"),

    path('childform', views.create_child_form_record, name="childform"),

    path('appointmentSession', views.appointment_session, name="appointmentSession"),

    path('briefNote', views.create_BriefNote_record, name="briefNote"),

    path('initialVistisForm', views.create_InitialVisitsForm_record, name="initialVisitsForm"),

    path('progressNote', views.create_ProgressNoteForm_record, name="progressNote"),

    path('treatmentPlanForm', views.create_TreatmentPlan_record, name = "treatmentPlanForm"),

    path('intialPsychiatricEvaluationAdultForm', views.create_InitialPsychiatric_record, name = "intialPsychiatricEvaluationAdultForm"),

    path('psychiatricProgressNote', views.create_PsychiatricProgressNote_record, name = "psychiatricProgressNote"),

]






