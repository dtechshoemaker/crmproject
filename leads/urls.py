from django.urls import include, path
from django.contrib.auth import views as auth_view
from . import views
from .forms import LoginForm

app_name = 'core'


urlpatterns = [
    path('', views.leads_list, name='leads_list'),
    path('lead/<str:new_test>/', views.lead_detail, name='lead'),

    path('create_lead/', views.createLead, name='create_lead'),
    path('update_lead/<str:pk>/', views.updateLead, name='update_lead'),
    path('delete_lead/<str:pk>/', views.deleteLead, name='delete_lead'),

    #Auth Urls
    path('signup/', views.signup, name='signup'),
    path('login/', auth_view.LoginView.as_view(
        template_name='auth/login.html', 
        authentication_form=LoginForm), name='login'),

]
