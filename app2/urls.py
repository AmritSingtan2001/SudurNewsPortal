from django.urls import path
from . import views 
from django.contrib.auth import views as auth_views

from .views import *


app_name ='dashboard'
urlpatterns = [
        path('',views.index,name='index'),
        path('login', views.login, name='login'),
        path('logout', views.userlogout, name='logout'),
        path('about-us', views.aboutUs, name='aboutUs'),
        path('contact-us', views.contactUs, name='contactUs'),
        path('our-team',views.ourteam, name="ourteam"),



        path('news', views.newsList, name='allnews'),
        path('news/delete/<slug:slug>', views.deletenews, name='deletenews'),
        path('news/categorie', views.mainCategories, name='mainCategorie'),
        path('news/add', views.createNews, name='createnews'),
        path('news/edite/<slug:slug>',views.editeNews, name="edite_news"),
        path('news/categorie/main-categorie',views.add_edit_MainCategorie,name='add_MainCategorie'),
        path('news/categorie/edit_main-categorie/<int:id>/',views.add_edit_MainCategorie,name='edit_MainCategorie'),
        path('news/categorie/delete/main-ategorie/<int:id>/',views.deleteMainCategorie,name='deleteMainCategorie'),
    
        path('news/categorie/sub-categorie',views.subCategories,name='subCategorie'),
        path('news/categorie/add/sub-categories',views.add_edit_SubCategories,name='add_SubCategories'),
        path('news/categorie/edit/sub-categories/<int:id>/',views.add_edit_SubCategories,name='edit_SubCategories'),
        path('news/categorie/delete/sub-categories/<int:id>/',views.deleteSubCategories,name='deleteSubCategories'),


        path('advertisement/horizontal-ads',views.horizontalAds,name='horizontalAds'),
        path('advertisement/add/horizontal-ads',views.add_edit_HorizontalAds,name='add_HorizontalAds'),
        path('advertisement/edit/horizontal-ads/<int:id>/',views.add_edit_HorizontalAds,name='edit_HorizontalAds'),
        path('advertisement/delete/horizontal-ads/<int:id>/',views.deletehorizontalAds,name='deletehorizontalAds'),

        path('advertisement/vertical-ads',views.verticalAds,name='verticalAds'),
        path('advertisement/add/vertical-ads',views.add_edit_VerticalAds,name='add_VerticalAds'),
        path('advertisement/edit/vertical-ads/<int:id>/',views.add_edit_VerticalAds,name='edit_VerticalAds'),
        path('advertisement/delete/vertical-ads/<int:id>/',views.deleteverticalAds,name='deleteverticalAds'),


        path('subcategories', views.load_sub_category, name="ajax_load_courses"),


]