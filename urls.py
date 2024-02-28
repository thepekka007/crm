from . import views
from django.urls import path,re_path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.index,name='index'),
    path('nextpage',views.nextpage,name='nextpage'),
    path('nextpage2',views.nextpage2,name='nextpage2'),
    path('archived',views.archived,name='archived'),
    path('new',views.new,name='new'),
    path('new_data',views.new_data,name='new_data'),
    path('updatetoarchived/<str:data>/',views.updatetoarchived,name='updatetoarchived'),
    path('updatetounarchived/<str:data>/',views.updatetounarchived,name='updatetounarchived'),


    path('newdesign',views.newdesign,name='newdesign'),

    
]