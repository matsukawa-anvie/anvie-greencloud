# coding:utf-8
from django import forms


class CorpInfoForm(forms.Form):
    user_name = forms.CharField(label=u'会社名', max_length=150)
    user_email = forms.EmailField(label=u'E-mail アドレス', max_length=256)
    user_password = forms.CharField(label=u'パスワード', max_length=8, widget=forms.PasswordInput)
    user_tel = forms.RegexField(label=u'電話番号', regex=r'\d{2,4}\-\d{2,4}\-\d{3,4}', max_length=11, min_length=9)
    user_img = forms.ImageField(label=u'会社アイコン')
    user_ceo_name = forms.CharField(label=u'代表取締役', max_length=20)
    user_employee_num = forms.CharField(label=u'従業員数', max_length=7)
    user_register_date = forms.DateTimeField(label=u'登録日時')
    user_last_logined_date = forms.DateTimeField(label=u'最終ログイン日時')
    user_login_times = forms.IntegerField(label=u'ログイン回数')