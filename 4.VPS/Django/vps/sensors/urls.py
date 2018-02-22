from django.conf.urls import url 
from . import views

urlpatterns = [
    # post views
        url(r'^$', views.data_list, name='data_list'), 
        # url(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/'r'(?P<    post>[-\w]+)/$',views.post_detail,name='post_detail'),
]


