from django.urls import path
from .views import *

app_name='dtm_javoblar196_app'

urlpatterns = [
    path('',home,name='home'),
    path('javob/<int:id>/',javob,name='javob')
]
