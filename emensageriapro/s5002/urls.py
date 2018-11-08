#coding:utf-8
#from django.conf.urls import patterns, include, url
from django.conf.urls import include, url
# from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from emensageriapro.s5002.views import s5002_infodep as s5002_infodep_views
from emensageriapro.s5002.views import s5002_infoirrf as s5002_infoirrf_views
from emensageriapro.s5002.views import s5002_basesirrf as s5002_basesirrf_views
from emensageriapro.s5002.views import s5002_irrf as s5002_irrf_views
from emensageriapro.s5002.views import s5002_idepgtoext as s5002_idepgtoext_views





urlpatterns = [



url(r'^s5002-infodep/apagar/(?P<hash>.*)/$', 
        s5002_infodep_views.apagar, 
        name='s5002_infodep_apagar'),

url(r'^s5002-infodep/api/$',
            s5002_infodep_views.s5002infoDepList.as_view() ),

        url(r'^s5002-infodep/api/(?P<pk>[0-9]+)/$',
            s5002_infodep_views.s5002infoDepDetail.as_view() ),

url(r'^s5002-infodep/listar/(?P<hash>.*)/$', 
        s5002_infodep_views.listar, 
        name='s5002_infodep'),

url(r'^s5002-infodep/salvar/(?P<hash>.*)/$', 
        s5002_infodep_views.salvar, 
        name='s5002_infodep_salvar'),



url(r'^s5002-infoirrf/apagar/(?P<hash>.*)/$', 
        s5002_infoirrf_views.apagar, 
        name='s5002_infoirrf_apagar'),

url(r'^s5002-infoirrf/api/$',
            s5002_infoirrf_views.s5002infoIrrfList.as_view() ),

        url(r'^s5002-infoirrf/api/(?P<pk>[0-9]+)/$',
            s5002_infoirrf_views.s5002infoIrrfDetail.as_view() ),

url(r'^s5002-infoirrf/listar/(?P<hash>.*)/$', 
        s5002_infoirrf_views.listar, 
        name='s5002_infoirrf'),

url(r'^s5002-infoirrf/salvar/(?P<hash>.*)/$', 
        s5002_infoirrf_views.salvar, 
        name='s5002_infoirrf_salvar'),



url(r'^s5002-basesirrf/apagar/(?P<hash>.*)/$', 
        s5002_basesirrf_views.apagar, 
        name='s5002_basesirrf_apagar'),

url(r'^s5002-basesirrf/api/$',
            s5002_basesirrf_views.s5002basesIrrfList.as_view() ),

        url(r'^s5002-basesirrf/api/(?P<pk>[0-9]+)/$',
            s5002_basesirrf_views.s5002basesIrrfDetail.as_view() ),

url(r'^s5002-basesirrf/listar/(?P<hash>.*)/$', 
        s5002_basesirrf_views.listar, 
        name='s5002_basesirrf'),

url(r'^s5002-basesirrf/salvar/(?P<hash>.*)/$', 
        s5002_basesirrf_views.salvar, 
        name='s5002_basesirrf_salvar'),



url(r'^s5002-irrf/apagar/(?P<hash>.*)/$', 
        s5002_irrf_views.apagar, 
        name='s5002_irrf_apagar'),

url(r'^s5002-irrf/api/$',
            s5002_irrf_views.s5002irrfList.as_view() ),

        url(r'^s5002-irrf/api/(?P<pk>[0-9]+)/$',
            s5002_irrf_views.s5002irrfDetail.as_view() ),

url(r'^s5002-irrf/listar/(?P<hash>.*)/$', 
        s5002_irrf_views.listar, 
        name='s5002_irrf'),

url(r'^s5002-irrf/salvar/(?P<hash>.*)/$', 
        s5002_irrf_views.salvar, 
        name='s5002_irrf_salvar'),



url(r'^s5002-idepgtoext/apagar/(?P<hash>.*)/$', 
        s5002_idepgtoext_views.apagar, 
        name='s5002_idepgtoext_apagar'),

url(r'^s5002-idepgtoext/api/$',
            s5002_idepgtoext_views.s5002idePgtoExtList.as_view() ),

        url(r'^s5002-idepgtoext/api/(?P<pk>[0-9]+)/$',
            s5002_idepgtoext_views.s5002idePgtoExtDetail.as_view() ),

url(r'^s5002-idepgtoext/listar/(?P<hash>.*)/$', 
        s5002_idepgtoext_views.listar, 
        name='s5002_idepgtoext'),

url(r'^s5002-idepgtoext/salvar/(?P<hash>.*)/$', 
        s5002_idepgtoext_views.salvar, 
        name='s5002_idepgtoext_salvar'),





]