from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse

from app.models import Corp


def agreement(request):
    return render(request,
                  'app/agreement.html',)
def base(request):
    return render(request,
                  'app/templates/base.html', )
def corp_confirm(request):
    return render(request,
                  'app/corp_confirm.html',)
def corp_detail(request):
    return render(request,
                  'app/corp_detail.html',)
def corp_info(request):
    return render(request,
                  'app/corp_info.html',)
def corp_search_result(request):
    return render(request,
                  'app/corp_search_result.html',)
def corp_top(request):
    return render(request,
                  'app/corp_top.html',)
def doc_detail(request):
    return render(request,
                  'app/doc_detail.html', )
def doc_edit(request):
    return render(request,
                  'app/doc_edit.html', )
def doc_kind(request):
    return render(request,
                  'app/doc_kind.html', )
def doc_list(request):
    return render(request,
                  'app/doc_list.html', )
def login(request):
    return render(request,
                  'app/login.html',)
def make_project(request):
    return render(request,
                  'app/make_project.html', )
def partner_list(request):
    return render(request,
                  'app/partner_list.html',)
def partner_request_agreement(request):
    return render(request,
                  'app/partner_request_agreement.html',)
def partner(request):
    return render(request,
                  'app/partner.html',)
def project_agreement(request):
    return render(request,
                  'app/project_agreement.html',)
def project_detail(request):
    return render(request,
                  'app/project_detail.html',)
def project_list(request):
    return render(request,
                  'app/project_list.html',)
def select_partner(request):
    return render(request,
                  'app/select_partner.html',)
def thanks(request):
    return render(request,
                  'app/thanks.html',)
def top(request):
    return render(request,
                  'app/top.html',)