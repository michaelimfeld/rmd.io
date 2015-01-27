from django.conf.urls import patterns, url
from mails import views

handler404 = 'maildelay.views.page_not_found_view'

urlpatterns = patterns(
    '',
    url(r'^$',       views.BaseView.as_view()),
    url(r'^help/$',  views.HelpView.as_view()),
    url(r'^login/$', views.LoginView.as_view()),
    url(r'^terms/$', views.TermsView.as_view()),
    url(r'^mails/$', views.MailView.as_view()),
    url(r'^mails/delete/$', views.mail_delete_view),
    url(
        r'^mails/delete/confirm/(?P<id>\d+)/$',
        views.mail_delete_confirm_view
    ),
    url(
        r'^mails/table/$',
        views.MailView.as_view(template_name="mails/mails_table.html")
    ),
    url(r'^mails/edit/(?P<id>\d+)/$', views.mail_edit_view),
    url(r'^mails/update/$', views.mail_update_view),
    url(r'^mails/info/(?P<id>\d+)/$', views.mail_info_view),
    url(r'^download/maildelay.vcf', views.download_vcard_view),
    url(r'^settings/$', views.settings_view),
    url(r'^calendar/(?P<secret>\w+)/$', views.download_calendar_view),
    url(r'^statistic/$', views.statistic_view),
    url(r'^user/add/$', views.user_add_view),
    url(r'^user/delete/confirm/(?P<id>\d+)/$', views.user_delete_confirm_view),
    url(r'^user/delete/$', views.user_delete_view),
    url(r'^user/activate/send/$', views.user_send_activation_view),
    url(r'^user/activate/(?P<key>\w+)/$', views.user_activate_view),
    url(r'^user/connect/(?P<account_id>\d+)/(?P<key>\w+)/$', views.user_connect_view),
)
