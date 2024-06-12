
from django.urls import path
from .import views
urlpatterns = [
    path('',views.index,name='index'),
    path('contact/',views.contact,name='contact'),
    path('delete_contact/<int:contact_id>/',views.delete_contact,name='delete_contact'),
    path('edit_contact/<int:contact_id>/',views.edit_contact,name='edit_contact'),
    path('view_contact/<int:contact_id>/',views.view_contact,name='view_contact')
]
