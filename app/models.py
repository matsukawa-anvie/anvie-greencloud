# coding:utf-8
from django.db import models


class Corp(models.Model):
    user_name = models.CharField(u'会社名', max_length=150, null=True)
    user_email = models.EmailField(u'E-mail アドレス', max_length=256, null=True)
    user_password = models.CharField(u'パスワード', max_length=8, null=True)
    user_tel = models.CharField(u'電話番号', max_length=11, null=True)
    user_img = models.ImageField(u'会社アイコン', upload_to=None, height_field=None, width_field=None, max_length=100, null=True)
    user_ceo_name = models.CharField(u'代表取締役', max_length=20, null=True)
    user_employee_num = models.CharField(u'従業員数', max_length=7, null=True)
    user_register_date = models.DateTimeField(u'登録日時', auto_now=False, auto_now_add=True, null=True)
    user_last_logined_date = models.DateTimeField(u'最終ログイン日時', auto_now=True, auto_now_add=False, null=True)
    user_login_times = models.IntegerField(u'ログイン回数', null=True)

    def __unicode__(self):
        return self.name
