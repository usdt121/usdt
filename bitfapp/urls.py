from django.urls import path
from . import views

urlpatterns = [

    path('', views.home),
    path('signup/', views.signup ),
    path('login/', views.login ),
    path('account/', views.acc),
    path('withdraw/', views.withd),
    path('deposit/', views.depo),

    path('verify/', views.verify),
    path('profile/', views.profile),
    path('plan/', views.plan),
    path('ref/', views.ref),
    path('livetrade/', views.livetrade),

    path('admin/', views.admin),
    path('edit/', views.edit),
    path('site/', views.site),
    path('act/', views.act),

]
