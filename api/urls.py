from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.BookCreateApiView.as_view()),
    path('', views.book_list),
    path('<int:pk>/', views.book_detail),
    # function based
    # path('author/', views.book_author),
    # class based
    # path('author', views.AuthorsApiView.as_view()),
    # get author byid
    path('<int:id>/', views.AuthorsApiView.as_view()),

]
