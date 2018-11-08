#coding:utf-8
#from django.conf.urls import patterns, include, url
from django.conf.urls import include, url
# from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from emensageriapro.r2020.views import r2020_nfs as r2020_nfs_views
from emensageriapro.r2020.views import r2020_infotpserv as r2020_infotpserv_views
from emensageriapro.r2020.views import r2020_infoprocretpr as r2020_infoprocretpr_views
from emensageriapro.r2020.views import r2020_infoprocretad as r2020_infoprocretad_views





urlpatterns = [



url(r'^r2020-nfs/apagar/(?P<hash>.*)/$', 
        r2020_nfs_views.apagar, 
        name='r2020_nfs_apagar'),

url(r'^r2020-nfs/api/$',
            r2020_nfs_views.r2020nfsList.as_view() ),

        url(r'^r2020-nfs/api/(?P<pk>[0-9]+)/$',
            r2020_nfs_views.r2020nfsDetail.as_view() ),

url(r'^r2020-nfs/listar/(?P<hash>.*)/$', 
        r2020_nfs_views.listar, 
        name='r2020_nfs'),

url(r'^r2020-nfs/salvar/(?P<hash>.*)/$', 
        r2020_nfs_views.salvar, 
        name='r2020_nfs_salvar'),



url(r'^r2020-infotpserv/apagar/(?P<hash>.*)/$', 
        r2020_infotpserv_views.apagar, 
        name='r2020_infotpserv_apagar'),

url(r'^r2020-infotpserv/api/$',
            r2020_infotpserv_views.r2020infoTpServList.as_view() ),

        url(r'^r2020-infotpserv/api/(?P<pk>[0-9]+)/$',
            r2020_infotpserv_views.r2020infoTpServDetail.as_view() ),

url(r'^r2020-infotpserv/listar/(?P<hash>.*)/$', 
        r2020_infotpserv_views.listar, 
        name='r2020_infotpserv'),

url(r'^r2020-infotpserv/salvar/(?P<hash>.*)/$', 
        r2020_infotpserv_views.salvar, 
        name='r2020_infotpserv_salvar'),



url(r'^r2020-infoprocretpr/apagar/(?P<hash>.*)/$', 
        r2020_infoprocretpr_views.apagar, 
        name='r2020_infoprocretpr_apagar'),

url(r'^r2020-infoprocretpr/api/$',
            r2020_infoprocretpr_views.r2020infoProcRetPrList.as_view() ),

        url(r'^r2020-infoprocretpr/api/(?P<pk>[0-9]+)/$',
            r2020_infoprocretpr_views.r2020infoProcRetPrDetail.as_view() ),

url(r'^r2020-infoprocretpr/listar/(?P<hash>.*)/$', 
        r2020_infoprocretpr_views.listar, 
        name='r2020_infoprocretpr'),

url(r'^r2020-infoprocretpr/salvar/(?P<hash>.*)/$', 
        r2020_infoprocretpr_views.salvar, 
        name='r2020_infoprocretpr_salvar'),



url(r'^r2020-infoprocretad/apagar/(?P<hash>.*)/$', 
        r2020_infoprocretad_views.apagar, 
        name='r2020_infoprocretad_apagar'),

url(r'^r2020-infoprocretad/api/$',
            r2020_infoprocretad_views.r2020infoProcRetAdList.as_view() ),

        url(r'^r2020-infoprocretad/api/(?P<pk>[0-9]+)/$',
            r2020_infoprocretad_views.r2020infoProcRetAdDetail.as_view() ),

url(r'^r2020-infoprocretad/listar/(?P<hash>.*)/$', 
        r2020_infoprocretad_views.listar, 
        name='r2020_infoprocretad'),

url(r'^r2020-infoprocretad/salvar/(?P<hash>.*)/$', 
        r2020_infoprocretad_views.salvar, 
        name='r2020_infoprocretad_salvar'),





]