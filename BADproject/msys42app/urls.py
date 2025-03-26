from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('CreateChildProfile/', views.create_child_profile, name='create_child_profile'),
    path('view/<int:pk>/', views.view_child_profile, name='view_child_profile'),
    path('edit/<int:pk>/', views.edit_child_profile, name='edit_child_profile'),

    # Medical History Paths
    path('medical-history/add/<int:child_id>/', views.add_medical_history, name='create_medical_history'),
    path('medical-history/view/<int:child_id>/', views.view_medical_history, name='view_medical_history'), 

    #Physician's Exam
    path('physician-exam/home/<int:pk>/', views.home_physicians_exam, name='home_physicians_exam'),
    path('physician-exam/add/<int:pk>/', views.create_physicians_exam, name='create_physicians_exam'),
    path('physician-exam/view/<int:pk>/<int:id>/', views.view_physicians_exam, name='view_physicians_exam'),

    path('child/<int:child_id>/annual-medical-check/', views.annual_medical_check_list, name='annual_medical_check_list'),
    path('child/<int:child_id>/annual-medical-check/create/', views.create_annual_medical_check, name='create_annual_medical_check'),
    path('child/<int:child_id>/annual-medical-check/<int:year>/', views.view_annual_medical_check, name='view_annual_medical_check'),

]
