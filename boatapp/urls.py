from django.urls import path,include
from boatproject import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [
    path('',views.index,name='index'),
    path('book',views.bookings,name='book'),
    path('book2',views.booking2,name='book2'),
    path('booking', views.booking, name='booking'),
]