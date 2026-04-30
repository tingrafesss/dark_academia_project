from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

def home(request):
    return HttpResponse("Сайт работает, приложение core пока отключено для отладки.")
    
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    # path('', include('core.urls')),
]
