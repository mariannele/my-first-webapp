from django.urls import path
from . import views
from .views import list_businesstrips, create_businesstrip, update_businesstrip, delete_businesstrip, weather

urlpatterns = [
    path('', views.HomePageView, name='home'),
    path('weather', weather, name='weatherview'),
    path('list', list_businesstrips, name='list_businesstrips'),
    path('new', create_businesstrip, name="create_businesstrip"),
    path('update/<int:id>/', update_businesstrip, name='update_businesstrip'),
    path('delete/<int:id>/', delete_businesstrip, name='delete_businesstrip'),
]
