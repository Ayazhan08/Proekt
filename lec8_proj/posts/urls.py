from django.urls import path
from .  views import *



urlpatterns=[
    path('', hello, name ='hello'),
    path('index/', index, name ='index'),
    # path('post/<int:post_id>',views.show_post, name='post'),
    # path('post/<slug:post_slug>',views.show_post1, name='post'),

    path('send/', EmailAttachementView.as_view(), name='emailattachment'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout')
]