
from django.contrib import admin
from django.urls import path
from app.views import ListPeople, CreatePerson, DetailPerson

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', ListPeople.as_view(), name='people' ),
    path('create/',CreatePerson.as_view(), name='create-people' ),
    path('person/<int:person_id>', DetailPerson.as_view(), name='person')
]
