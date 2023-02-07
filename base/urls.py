from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('found', views.found, name='found'),
    path('missing', views.missing, name='missing'),
    path('after-found', views.after_found, name='after_found'),
    path("child/'<int:pk>'", views.after_missing_sccuess, name='after_missing_sccuess'),
    path("parent-child/'<int:pk>'", views.after_found_sccuess, name='after_found_sccuess'),
    path('notFound', views.after_mising_fail, name='after_mising_fail'),
    path('about-us', views.about_us, name='about_us'),
]
