from django.conf.urls import url
from django.conf import settings
from . import views
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$',views.home,name='home'),
    url(r'^accounts/profile/', views.my_profile, name='my_profile'),
    url(r'^index',views.index,name='index'),
    url(r'^join/(\d+)', views.join, name='join'),
    url(r'^register/',views.register, name='register'),
    url(r'^my_profile',views.my_profile,name = 'my_profile'),
    url(r'^leave',views.leave,name = 'leave'),
    url(r'^search/', views.search_results, name='search_results'),
    url(r'^business/(\d+)', views.business, name='business'),
    url(r'^newbusiness/',views.newbusiness, name='newbusiness'),

]
# if settings.DEBUG:
#     urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)