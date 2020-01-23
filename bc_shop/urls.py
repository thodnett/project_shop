"""bc_shop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from home.views import index
from accounts import urls as urls_accounts 
from products import urls as urls_products
from products.views import all_products 
from reviews import urls as urls_reviews
from reviews.views import all_reviews
from cart import urls as urls_cart
from search import urls as urls_search 
from checkout import urls as urls_checkout
from django.views import static
from .settings import MEDIA_ROOT


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', index,  name='index'),
    url(r'^all_products', all_products,  name='all_products'),
    url(r'^all_reviews/', all_reviews, name="reviews"),
    url(r'^accounts/', include(urls_accounts)),
    url(r'^products/', include(urls_products)),
    url(r'^cart/', include(urls_cart)),
    url(r'^search/', include(urls_search)),
    url(r'^checkout/', include(urls_checkout)),
    url(r'media/(?P<path>.*)$', static.serve,{'document_root' : MEDIA_ROOT})
]

