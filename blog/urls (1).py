from django.conf.urls import url, path
from . import views

from django.views.generic import TemplateView, RedirectView

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    path(r'base_layout',views.base_layout,name='base_layout'),
   
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
    url(r'^post/drafts/', views.post_draft_list, name='post_draft_list'),
    url(r'^post/(?P<pk>\d+)/publish/$', views.post_publish, name='post_publish'),
    url(r'^post/(?P<pk>\d+)/remove/$', views.post_remove, name='post_remove'),
    url(r'post/(?P<pk>\d+)/comment/', views.add_comment_to_post, name='add_comment_to_post'),
    url(r'comment/(?P<pk>\d+)/approve/', views.comment_approve, name='comment_approve'),
    url(r'comment/(?P<pk>\d+)/remove/', views.comment_remove, name='comment_remove'),
]

urlpatterns += [
    url(r'^robots\.txt$', TemplateView.as_view(template_name="blog/robots.txt", content_type='text/plain')),
    url(r'^favicon\.ico$',RedirectView.as_view(url='/static/images/favicon.ico')),

]