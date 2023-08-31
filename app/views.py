from django.shortcuts import render, HttpResponse, get_object_or_404
from django.http import JsonResponse
from django.views import generic
from datetime import datetime
from . models import News,MainCategorie,HorizontalAds, VerticalAds,SubCategorie, OurTeam,PrivacyPolicy,ContactUs
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def custom_404_view(request, exception):
    return render(request, 'app/404.html')


class IndexListView(generic.ListView):
    model= News
    template_name='app/index.html'

    def get_context_data(self, *args, **kwargs):
        context = super(IndexListView,self).get_context_data(*args, **kwargs)
        newsCategorie = MainCategorie.objects.all().order_by('ordering')
        allNews =News.objects.all()
        allHorizontalAds = HorizontalAds.objects.all()
        context['firstnews']= allNews.filter(highlight=True)[:2]
        context['secondthirdNews'] = allNews.filter(highlight=True)[2:3]
        context['allnews']= allNews[2:]
        context['firstCategorieNews'] = News.objects.filter(categorie =newsCategorie.first())
        context['firstCategorie'] =newsCategorie.first()
        context['scondNewsSection'] =News.objects.filter(categorie = newsCategorie[1:2])
        context['secondCategorie'] = newsCategorie[1:2]
        context['thirdSectionNews'] = News.objects.filter(categorie = newsCategorie[2:3])
        context['thirdCategorie'] = newsCategorie[2:3]
        context['treandingNews'] =News.objects.filter(trending=True)[:10]
        context['featuresNews'] =News.objects.filter(feature=True).order_by('-id')[:10]
        context['firstads'] = allHorizontalAds.filter(positionNumber="first").first()
        context['horizontalSecondAds'] = allHorizontalAds.filter(positionNumber="second").first()
        context['horizontalThirdAds'] = allHorizontalAds.filter(positionNumber="third").first()
        context['horizontalFourthAds'] = allHorizontalAds.filter(positionNumber="fourth").first()
        context['horizontalFifthAds'] = allHorizontalAds.filter(positionNumber="fifth").first()
        context['horizontalSixthAds'] = allHorizontalAds.filter(positionNumber="six").first()
        context['verticalAds'] = VerticalAds.objects.all().order_by('-id')[:10]
        return context
    


class NewsDetailsView(generic.DetailView):
    model= News
    template_name= 'app/desc.html'
    slug_field = 'news_slug'
    slug_url_kwarg = 'news_slug'

    def get_context_data(self, *args, **kwargs):
        context = super(NewsDetailsView,self).get_context_data(*args, **kwargs)
        newsDetails= get_object_or_404(News, news_slug=self.kwargs['news_slug']) 
        categorie = MainCategorie.objects.get(categorie_name = newsDetails.categorie)  
        context['newsDetails']  = newsDetails
        context['relatedNews'] = News.objects.filter(categorie =categorie)[1:10]
        # context['verticalAds']=print(VerticalAds.objects.filter(page='news_details')[:5])
        return context
    
class CategorieRelatedNews(generic.ListView):
    model = News
    template_name = 'app/categorydescription.html'
    slug_field = 'main_ctg_slug'
    slug_url_kwarg = 'main_ctg_slug'

    def get_context_data(self, *args, **kwargs):
        context = super(CategorieRelatedNews,self).get_context_data(*args, **kwargs)
        newsCategories= get_object_or_404(MainCategorie, main_ctg_slug=self.kwargs['main_ctg_slug']) 
        allRelatedNews = News.objects.filter(categorie = newsCategories)
        context['categorie']= newsCategories
        context['firstNews']  = allRelatedNews.first()
        allNews= allRelatedNews[1:]
        p = Paginator(allNews, 15)
        page_number = self.request.GET.get('page')
        allNews = p.get_page(page_number)
        context['allNews']  = allNews
        return context
    

class CategorieSubNews(generic.ListView):
    model = News
    template_name = 'app/subCategorie.html'
    slug_field = 'subctgslug'
    slug_url_kwarg = 'subctgslug'
    paginate_by =3

    def get_context_data(self, *args, **kwargs):
        context = super(CategorieSubNews,self).get_context_data(*args, **kwargs)
        subcategorie= SubCategorie.objects.get(subctgslug=self.kwargs['subctgslug'])
        allSubcategoreiNews =subcategorie.subCtg.all()
        context['firstSubNews'] = allSubcategoreiNews.first()
        context['allNews'] = allSubcategoreiNews[1:]
        return context
    

class OurTeamView(generic.ListView):
    model = OurTeam
    template_name = 'app/ourteam.html'
    content_objects_name  = 'ourteams'

    def get_context_data(self, *args, **kwargs):
        context = super(OurTeamView,self).get_context_data(*args, **kwargs)
        context['ourteams'] = OurTeam.objects.first()
        return context
    

class PrivacyPolicyView(generic.ListView):
    model = PrivacyPolicy
    template_name = 'app/privacypolicy.html'
    content_objects_name  = 'privacypolicy'

    def get_context_data(self, *args, **kwargs):
        context = super(PrivacyPolicyView,self).get_context_data(*args, **kwargs)
        context['privacypolicy'] = PrivacyPolicy.objects.first()
        return context
    
class ContactView(generic.ListView):
    model = ContactUs
    template_name = 'app/contact.html'
    content_objects_name  = 'contact'

    def get_context_data(self, *args, **kwargs):
        context = super(ContactView,self).get_context_data(*args, **kwargs)
        context['contact'] = ContactUs.objects.first()
        return context
    





def moreListView(request):
    visible = request.GET['data']
    newsCategorie = MainCategorie.objects.all().order_by('ordering')[3:4]
    for ctg in newsCategorie:
        allnews= News.objects.filter(categorie=ctg.id)
        print(ctg.id)
    print(allnews)
    return render(request,'app/morenews.html',{'allmorenews':allnews[1:],
                                               'singlemorenews':allnews[:1],
                                               'newscategorie':newsCategorie
                                               })


class PostJosnListView(generic.View):
    def get(self, *args, **kwargs):
        print(kwargs)
        upper = kwargs.get('num_news')
        print(upper)
        lower =upper-3
        news= list(News.objects.values()[lower:upper])
        news_size =len(News.objects.all())
        size = True if upper >= news_size else False
        return JsonResponse({'data':news, 'max':size}, safe=False)

# class MoreListView(generic.ListView):
#     model= News
#     template_name='app/index.html'
#     paginate_by =4

#     def get_context_data(self, *args, **kwargs):
#         context = super(MoreListView,self).get_context_data(*args, **kwargs)
#         moreNewslist =News.objects.all()
#         return context
    


#testing 
def home(request):
    numbers_list = range(1, 1000)
    page = request.GET.get('page', 1)
    paginator = Paginator(numbers_list, 20)
    try:
        numbers = paginator.page(page)
    except PageNotAnInteger:
        numbers = paginator.page(1)
    except EmptyPage:
        numbers = paginator.page(paginator.num_pages)
    return render(request, 'app/home.html', {'numbers': numbers})