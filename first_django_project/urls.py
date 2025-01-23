from django.urls import path
from . import views

urlpatterns = [
    path('post-example/', views.post_example, name='post_example'),
    path('person-info/<str:name>/<int:age>/', views.person_info, name='person_info'),
    path('endpoint/', views.my_endpoint, name='my-endpoint'),

]
