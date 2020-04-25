from django.shortcuts import get_object_or_404, render

#from .models import Article

def index(request):
#    latest_article_list = Article.objects.order_by('-pub_date')[:5]
#    context = {'latest_article_list': latest_article_list}
#    return render(request, 'articles/index.html', context)
  	return render(request, 'home/index.html')


#def article(request, article_id):
#    article = get_object_or_404(Article, pk=article_id)
#    return render(request, 'articles/article.html', {'article': article})

