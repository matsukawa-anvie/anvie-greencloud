from django.conf.urls import url
from app import views

urlpatterns = [
    url(r'^agreement', views.agreement, name='agreement'),
    url(r'^base', views.base, name='base'),
    url(r'^corp_confirm', views.corp_confirm, name='corp_confirm'),
    url(r'^corp_detail', views.corp_detail, name='corp_detail'),
    url(r'^corp_info', views.corp_info, name='corp_info'),
    url(r'^corp_search_result', views.corp_search_result, name='corp_search_result'),
    url(r'^corp_top', views.corp_top, name='corp_top'),
    url(r'^doc_detail', views.doc_detail, name='doc_detail'),
    url(r'^doc_edit', views.doc_edit, name='doc_edit'),
    url(r'^doc_kind', views.doc_kind, name='doc_kind'),
    url(r'^doc_list', views.doc_list, name='doc_list'),
    url(r'^login', views.login, name='login'),
    url(r'^make_project', views.make_project, name='make_project'),
    url(r'^partner_list', views.partner_list, name='partner_list'),
    url(r'^partner_request_agreement', views.partner_request_agreement, name='partner_request_agreement'),
    url(r'^partner', views.partner, name='partner'),
    url(r'^project_agreement', views.project_agreement, name='project_agreement'),
    url(r'^project_detail', views.project_detail, name='project_detail'),
    url(r'^project_list', views.project_list, name='project_list'),
    url(r'^select_partner', views.select_partner, name='select_partner'),
    url(r'^thanks', views.thanks, name='thanks'),
    url(r'^top', views.top, name='top'),
]