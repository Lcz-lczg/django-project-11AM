from django.urls import path
from . import views
urlpatterns=[
   path('',views.home,name='home'),
   path('aboutus',views.aboutus,name='aboutus'),
   path('editstudent',views.editstudent,name='editstudent'),
   path('deletestudent',views.deletestudent,name='deletestudent'),
   path('services',views.services,name='services'),
   path('gallery',views.gallery,name='gallery'),
   path('contactus',views.contactus,name='contactus'),
   path('signup',views.signup,name='signup'),
   path('signin',views.signin,name='signin'),
   path('dashboard',views.dashboard,name='dashboard')

]