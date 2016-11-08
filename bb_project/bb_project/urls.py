"""bb_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from core.views import *
from django.views.generic import *

urlpatterns = [
    
    url(r'^$', TemplateView.as_view(template_name='core/template.html')),

    # List URLs
    url(r'^clients$', ClientList.as_view()),
    url(r'^brands$', BrandList.as_view()),
    url(r'^brand_ambassadors$', BrandAmbassadorList.as_view()),
    url(r'^stores$', StoreList.as_view()),
    url(r'^store_contacts$', StoreContactList.as_view()),

    # Create URLs
    url(r'^clients/new$', CreateClient.as_view()),
    url(r'^brands/new$', CreateBrand.as_view()),
    url(r'^brand_ambassadors/new$', CreateBrandAmbassador.as_view()),
    url(r'^stores/new$', CreateStore.as_view()),
    url(r'^store_contacts/new$', CreateStoreContact.as_view()),

    # Update URLs
    url(r'^clients/(?P<pk>\d+)/update$', UpdateClient.as_view()),
    url(r'^brands/(?P<pk>\d+)/update$', UpdateBrand.as_view()),
    url(r'^brand_ambassadors/(?P<pk>\d+)/update$', UpdateBrandAmbassador.as_view()),
    url(r'^stores/(?P<pk>\d+)/update$', UpdateStore.as_view()),
    url(r'^store_contacts/(?P<pk>\d+)/update$', UpdateStoreContact.as_view()),

    # Demos
    url(r'^schedule_demos/$', ScheduleDemos.as_view()),

    #Ajax Calls
    url(r'^ajax/stores$', ajax_stores),
    url(r'^ajax/dropdowns/clients$', ajax_clients),
    url(r'^ajax/dropdowns/demo_types$', ajax_demo_types),
    url(r'^ajax/dropdowns/clients/(?P<client_id>\d+)/brands$', ajax_brands),
    url(r'^ajax/dropdowns/brands/(?P<brand_id>\d+)/products$', ajax_products),
]
