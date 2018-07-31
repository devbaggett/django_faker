from django.conf.urls import url
from appTwo import views

urlpatterns = [
    url(r'^users$',views.users),
]
