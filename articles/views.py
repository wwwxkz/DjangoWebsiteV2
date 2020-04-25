from django.shortcuts import get_object_or_404, render

from .models import Article

def index(request):
    latest_article_list = Article.objects.order_by('-pub_date')[:5]
    context = {'latest_article_list': latest_article_list}
    return render(request, 'articles/index.html', context)

def article(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    return render(request, 'articles/article.html', {'article': article})






#def results(request, article_id):
#    response = "You're looking at the results of question %s."
#    return HttpResponse(response % article_id)

#def vote(request, article_id):
#    return HttpResponse("You're voting on question %s." % article_id)