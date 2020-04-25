from django.contrib import admin
from django.urls import include, path

urlpatterns = [
 	path('', include('home.urls')),
	path('articles/', include('articles.urls')),
	#path('posts/', admin.site.urls),
	#path('about/', admin.site.urls),
    path('admin/', admin.site.urls),
]
