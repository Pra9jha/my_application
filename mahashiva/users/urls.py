from rest_framework.urlpatterns import format_suffix_patterns
from django.urls import path
from . import views ,view_request_response as vrr, view_classed_based as vcb
from . import view_Article
from  .view_Article import  ArticalAPIView,ArticalDetails
urlpatterns = [
    # //To call view_basic uncommnet below
    # path('',views.snippet_list),
    # path('<int:pk>/',views.snippet_detail),
    # //To call view_request_response uncommnet below
    path('snippet/', vrr.snippet_list),
    path('snippet/<str:pk>/', vrr.snippet_detail),
    #//To call class based view uncomment below
    # path('',vcb.SnippetList.as_view()),
    # path('<str:pk>/', vcb.SnippetDetail.as_view()),
    #Method based article view
    # path('article/',view_Article.article_list),
    # path('article/<str:pk>/',view_Article.article_detail)
    #Class based Article view
    path('article/',ArticalAPIView.as_view()),
    path('article/<int:pk>/',ArticalDetails.as_view())
]
urlpatterns = format_suffix_patterns(urlpatterns)







