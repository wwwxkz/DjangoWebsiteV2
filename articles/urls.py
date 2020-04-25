from django.urls import path

from . import views

urlpatterns = [
	path('', views.index, name='index'),
 	path('<int:article_id>/', views.article, name='article'),
   	#path('<int:article_id>/results/', views.results, name='results'),
   	#path('<int:article_id>/vote/', views.vote, name='vote'),
]