from xml.etree.ElementInclude import include
from django.urls import path, include
from .views import IndexView

urlpatterns = [
    path('', IndexView),
    path('captcha/', include('captcha.urls'))
]