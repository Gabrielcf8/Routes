from django.urls import re_path

from Routes.views import ListPoint, CreatePoint, CreateCategory, ListCategory, ListCity, CreateCity, CreateRoute, \
    ListRoute
from . import views

urlpatterns = [
    re_path(r'^$', views.firstview),
    re_path(r'^cities', views.cityview),
    re_path(r'^route', views.routeview),
    re_path(r'^generate', views.generaterouteview),
    re_path(r'^categories', views.categoryview),
    re_path(r'^points', views.pointview, name='points'),
    re_path(r'^map', views.mapview),
    re_path(r'^user_profile/$', views.user_profile),
    re_path(r'^user_form/$', views.create_profile),
    re_path(r'^createpoint/$', CreatePoint.as_view(), name='cadastroPoint'),
    re_path(r'^listpoint/$', ListPoint.as_view(), name='listaPoint'),
    re_path(r'^createcategory/$', CreateCategory.as_view(), name='cadastroCategory'),
    re_path(r'^listcategory/$', ListCategory.as_view(), name='listaCategory'),
    re_path(r'^createcity/$', CreateCity.as_view(), name='cadastroCity'),
    re_path(r'^listcity/$', ListCity.as_view(), name='listaCity'),
    re_path(r'^createroute/$', CreateRoute.as_view(), name='cadastroRoute'),
    re_path(r'^listroute/$', ListRoute.as_view(), name='listaRoute'),
]
