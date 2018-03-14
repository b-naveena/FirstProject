from django.conf.urls import url
from login.views import Delete,Register,Update,ListAll, Login,DownloadLog

urlpatterns = [
    url(r'^register', Register.as_view()),
    url(r'^update', Update.as_view()),
    url(r'^delete', Delete.as_view()),
    url(r'^list', ListAll.as_view()),
    url(r'^login', Login.as_view()),
    url(r'^download',DownloadLog.as_view()),
]
