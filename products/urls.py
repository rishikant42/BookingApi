from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from products import views

urlpatterns = [
    url(r'^products/$', views.ProductList.as_view()),
    url(r'^products/(?P<pk>[0-9]+)/$', views.ProductDetail.as_view()),
    url(r'^bookticket/$', views.BookTicket.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
