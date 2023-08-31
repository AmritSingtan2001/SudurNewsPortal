from . models import MainCategorie, AboutUS,HorizontalAds,VerticalAds,News

def mainCategories(request):
    allCategories = MainCategorie.objects.all().order_by('ordering')
    trendingNews =News.objects.filter(trending=True)[:6]
    alltrendingNews =News.objects.filter(trending=True)[:9]
    recentlyAddedNews= News.objects.all().order_by('-create_date')[:9]
    return({
        'allCategories':allCategories[:7],
        'othermenu': allCategories[7:],
        'trendingNews':trendingNews,
        'recentNews':recentlyAddedNews,
        'alltreandingNews':alltrendingNews
    })

def aboutUs(request):
    aboutus =AboutUS.objects.first()
    return({
        'aboutUS':aboutus
    })

def firstAds(request):
    firstads= HorizontalAds.objects.filter(positionNumber="first", show=True).first()
    verticalAds = VerticalAds.objects.filter(page='news_details', show=True)[:5]
    return({
        'firstads':firstads,
        'verticalAds':verticalAds
    })