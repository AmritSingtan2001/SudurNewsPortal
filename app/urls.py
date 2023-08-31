from django.urls import path
from django.urls import re_path
from django.conf import settings
from django.views.static import serve
from django.conf.urls.static import static
from . import views
from . views import (IndexListView,
                     NewsDetailsView,
                     CategorieRelatedNews,
                     CategorieSubNews,
                     OurTeamView,
                     PrivacyPolicyView,
                     ContactView,
                     PostJosnListView
                     )

urlpatterns = [
    path('', IndexListView.as_view(), name='index'),
    path('news-details/<slug:news_slug>', NewsDetailsView.as_view(), name='newsDetails'),
    path('content/<slug:main_ctg_slug>', CategorieRelatedNews.as_view(), name='ctgRelatedNews'),
    path('news/content/<slug:subctgslug>', CategorieSubNews.as_view(), name='subCtgNews'),
    path('ourteam', OurTeamView.as_view(), name='ourteam'),
    path('privacy-policy', PrivacyPolicyView.as_view(), name='privacypolicy'),
    path('morenews',views.moreListView, name='ajax_more_news'),

    path('post-json/<int:num_news>/',PostJosnListView.as_view(), name='postJosnlist'),

    path('contact-us', ContactView.as_view(), name='contact'),
    re_path(r"^media/(?P<path>.*)$", serve, {"document_root": settings.MEDIA_ROOT}),
    re_path(r"^static/(?P<path>.*)$", serve, {"document_root": settings.STATIC_ROOT}),
    path('home', views.home)
]
