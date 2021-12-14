from django.urls import path,include
from .views import homePage, newQuestionPage,questionPage, replyPage

urlpatterns = [
    path('',homePage,name='forum-home'),
    path('new-question',newQuestionPage,name='new-question'),
    path('question/<int:id>',questionPage,name = 'question'),
    path('reply/',replyPage,name='reply')
]
