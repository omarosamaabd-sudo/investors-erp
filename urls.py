from django.contrib import admin
from django.urls import path,include
from django.contrib.auth import views as auth_views
from core import views
urlpatterns=[path('admin/',admin.site.urls),path('login/',auth_views.LoginView.as_view(template_name='core/login.html'),name='login'),path('logout/',auth_views.LogoutView.as_view(),name='logout'),path('',views.dashboard,name='dashboard'),path('investors/',views.investors,name='investors'),path('plots/',views.plots,name='plots'),path('contractors/',views.contractors,name='contractors'),path('finance/',views.finance,name='finance'),path('reports/',views.reports,name='reports')]
