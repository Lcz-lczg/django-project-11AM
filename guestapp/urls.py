from django.urls import path
from . import views
urlpatterns=[
    path('',views.hello,name='hello'),
    path('stuinfo',views.studentinfo,name='studentinfo'),
    path('stuoutput',views.studentoutput,name='studentoutput'),
    path('addition',views.addition,name='addition'),
    path('additionoutput',views.additionoutput,name='additionoutput')
    
]