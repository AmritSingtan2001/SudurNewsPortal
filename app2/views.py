from django.shortcuts import render,HttpResponse, HttpResponseRedirect,redirect,get_object_or_404
from account.models import User
from django.contrib.auth import authenticate, login, logout
from . decorators import login_required
from django.contrib import messages
from django.contrib import auth
from . forms import *
from app.models import *
from django.core.paginator import Paginator
from . new_file_handler import validate_file


def login(request):
    try:
        if request.user.is_authenticated:
            return render(request,'app2/index.html')

        if request.method =="POST":
            email = request.POST['useremail']
            print(email)
            password = request.POST['password']
            user_obj = User.objects.filter(email= email)
            if not user_obj.exists():
                messages.warning(request,"Invalid username...")
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
                
            
            user_obj = authenticate(email=email, password=password)
            if user_obj and user_obj.is_superuser or user_obj.is_editor:
                auth.login(request, user_obj)
                return redirect('dashboard:index')
            
            messages.warning(request,'Inavlid Password')
            return redirect('dashboard:login')
            
        return render(request,'app2/login.html')
            

    except Exception as e:
        print(e)
        messages.warning(request,'something wrong...')
        return redirect('dashboard:login')


@login_required
def userlogout(request):
    auth.logout(request)
    messages.info(request,"logout successfully..")
    return redirect('dashboard:login')


@login_required
def index(request):
    return render(request,'app2/index.html')


@login_required
def aboutUs(request):
    instance = None
    try:
        if id:
            instance = AboutUS.objects.first()
    except Exception as e:
        messages.warning(request, 'An error occurred while retrieving the AboutUS.')
        return redirect('dashboard:aboutUs')

    if request.method == 'POST':
        form = AboutUSForm(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            form.save()
            if instance:  # Edit operation
                messages.success(request, 'AboutUS edited successfully.')
                return redirect('dashboard:aboutUs')  # Redirect to the edited AboutUS's details page
            else:  # Add operation
                messages.success(request, 'AboutUS added successfully.')
                return redirect('dashboard:aboutUs')  # Redirect to the page for adding new AboutUSs
        else:
            messages.warning(request, 'Form is not valid. Please correct the errors.')
    else:
        form = AboutUSForm(instance=instance)

    context = {'form': form, 'instance': instance}
    return render(request, 'app2/create_about_us.html', context)


#news categorei
@login_required
def add_edit_MainCategorie(request, id=None):
    instance = None
    try:
        if id:
            instance = MainCategorie.objects.get(pk=id)
    except Exception as e:
        messages.warning(request, 'An error occurred while retrieving the MainCategorie.')
        return redirect('dashboard:add_MainCategorie')

    if request.method == 'POST':
        form = MainCategorieForm(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            form.save()
            if instance:  # Edit operation
                messages.success(request, 'MainCategorie edited successfully.')
                return redirect('dashboard:edit_MainCategorie', id=instance.id)  # Redirect to the edited MainCategorie's details page
            else:  # Add operation
                messages.success(request, 'MainCategorie added successfully.')
                return redirect('dashboard:add_MainCategorie')  # Redirect to the page for adding new MainCategories
        else:
            messages.warning(request, 'Form is not valid. Please correct the errors.')
    else:
        form = MainCategorieForm(instance=instance)

    context = {'form': form, 'instance': instance}
    return render(request, 'app2/create_MainCategorie.html', context)

@login_required
def mainCategories(request):
    MainCategories=MainCategorie.objects.all()
    p=Paginator(MainCategories,10)
    page_number= request.GET.get('page')
    MainCategories=p.get_page(page_number)
    return render(request, 'app2/MainCategorie.html',{'details':MainCategories})

@login_required
def deleteMainCategorie(request, id):
    record = get_object_or_404(MainCategorie, id=id)

    if request.method == 'POST':
        record.delete()
        return redirect('dashboard:mainCategorie')  # Redirect to a list view after deletion
    else:
        return render(request, 'app2/MainCategorie.html', {'details': record})



#news subcategorie
@login_required
def add_edit_SubCategories(request, id=None):
    instance = None
    try:
        if id:
            instance = SubCategorie.objects.get(pk=id)
    except Exception as e:
        messages.warning(request, 'An error occurred while retrieving the SubCategories.')
        return redirect('dashboard:add_SubCategories')

    if request.method == 'POST':
        form = SubCategorieForm(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            form.save()
            if instance:  # Edit operation
                messages.success(request, 'SubCategories edited successfully.')
                return redirect('dashboard:edit_SubCategories', id=instance.id)  # Redirect to the edited SubCategories's details page
            else:  # Add operation
                messages.success(request, 'SubCategories added successfully.')
                return redirect('dashboard:add_SubCategories')  # Redirect to the page for adding new SubCategoriess
        else:
            messages.warning(request, 'Form is not valid. Please correct the errors.')
    else:
        form = SubCategorieForm(instance=instance)

    context = {'form': form, 'instance': instance}
    return render(request, 'app2/create_SubCategories.html', context)

@login_required
def subCategories(request):
    SubCategories=MainCategorie.objects.all()
    p=Paginator(SubCategories,4)
    page_number= request.GET.get('page')
    SubCategories=p.get_page(page_number)
    return render(request, 'app2/SubCategories.html',{'details':SubCategories})

@login_required
def deleteSubCategories(request, id):
    record = SubCategorie.objects.get(pk=id)
    if request.method == 'POST':
        record.delete()
        messages.success(request,'Sub Categorie Deleted Successfully !')
        return redirect('dashboard:subCategorie')  # Redirect to a list view after deletion
    else:
        return render(request, 'app2/SubCategories.html', {'details': record})



@login_required 
def newsList(request):
    allnews = News.objects.all()
    return render(request,'app2/news_table.html',{'allNews':allnews})


@login_required
def createNews(request):
    allcategorie= MainCategorie.objects.all()
    user= request.user
    if request.method=="POST":
        newstitle = request.POST['title']
        maincategorie= request.POST['categoryselect']
        mainctg = MainCategorie.objects.get(id=maincategorie)
        subcategorie = request.POST['subcategory']
        if subcategorie:
            subctg = SubCategorie.objects.get(id =subcategorie)
        else:
            subctg =None
        reporter = request.POST['reporter']
        news_reporter =User.objects.get(id=reporter)
        trending_status=request.POST['trending']
        features_status = request.POST['feature']
        news_description = request.POST['description']
        news_image = request.FILES['newsimage']
        highlight = request.POST['highlight']
        new_news= News.objects.create( 
                                      categorie=mainctg,
                                      subCategorie=subctg,
                                      title=newstitle,
                                      discriptions=news_description,
                                      image =news_image,
                                      repoter =news_reporter,
                                      trending= trending_status,
                                      feature=features_status,
                                      highlight= highlight
                                      )
        new_news.save()
        messages.success(request,'News added successfully !')
        return redirect('dashboard:createnews')

    else:
        return render(request,'app2/create_news.html',{'allcategorie':allcategorie,
                                                       'user':user
                                                       })
@login_required
def editeNews(request, slug=None):
    news = News.objects.get(news_slug =slug)
    allcategorie= MainCategorie.objects.all()
    user= request.user
    if request.method=="POST":
        news.title = request.POST['title']
        maincategorie= request.POST['categoryselect']
        news.categorie = MainCategorie.objects.get(id=maincategorie)
        subcategorie = request.POST['subcategory']
        if subcategorie:
            news.subCategorie = SubCategorie.objects.get(id =subcategorie)
        else:
            news.subCategorie =None
        reporter = request.POST['reporter']
        news.repoter =User.objects.get(id=reporter)
        news.trending=request.POST['trending']
        news.feature = request.POST['feature']
        news.discriptions = request.POST['description']
        if 'newsimage' in request.FILES:
            news.image = request.FILES['newsimage']
    
        news.highlight = request.POST['highlight']
        
        news.save()
        messages.success(request,'News updated successfully !')
        return redirect('dashboard:edite_news', slug=news.news_slug)

    
    return render(request,'app2/edite_news.html',{'news':news,
                                                  'allcategorie':allcategorie,
                                                    'user':user
                                                  })

@login_required
def deletenews(request, slug):
    relatedNews= News.objects.get(news_slug=slug)
    relatedNews.delete()
    messages.success(request,"News deleted successfullY !")
    return redirect('dashboard:allnews')

@login_required
def load_sub_category(request):
    main_ctg_id = request.GET.get('programming')
    print(main_ctg_id)
    sub_category = SubCategorie.objects.filter(maincategorie=main_ctg_id)
    return render(request,'app2/listdropdow.html',{'sub_category':sub_category})

# def createNews(request, id= None):
#     instance = None
#     newscategorie = MainCategorie.objects.all()
#     try:
#         if id:
#             instance = News.objects.get(pk=id)
#     except Exception as e:
#         messages.warning(request, 'An error occurred while retrieving the SubCategories.')
#         return HttpResponse('news list')

#     if request.method == 'POST':
#         form = NewsForm(request.POST, request.FILES, instance=instance)
#         if form.is_valid():
#             form.save()
#             if instance:  # Edit operation
#                 messages.success(request, 'SubCategories edited successfully.')
#                 # return redirect('dashboard:edit_SubCategories', id=instance.id)  # Redirect to the edited SubCategories's details page
#                 return HttpResponse("edite ..")
#             else:  # Add operation
#                 messages.success(request, 'News added successfully.')
#                 return HttpResponse("Added successfully..")  # Redirect to the page for adding new SubCategoriess
#         else:
#             messages.warning(request, 'Form is not valid. Please correct the errors.')
#     else:
#         form = NewsForm(instance=instance)

#     context = {'form': form, 'instance': instance}
#     return render(request, 'app2/create_news.html', context)



# ads sections
@login_required
def add_edit_HorizontalAds(request, id=None):
    instance = None
    try:
        if id:
            instance = HorizontalAds.objects.get(pk=id)
    except Exception as e:
        print(e)
        messages.warning(request, 'An error occurred while retrieving the HorizontalAds.')
        return redirect('dashboard:add_HorizontalAds')

    if request.method == 'POST':
        form = HorizontalAdsForm(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            form.save()
            if instance:  # Edit operation
                messages.success(request, 'HorizontalAds edited successfully.')
                return redirect('dashboard:edit_HorizontalAds', id=instance.id)  # Redirect to the edited HorizontalAds's details page
            else:  # Add operation
                messages.success(request, 'HorizontalAds added successfully.')
                return redirect('dashboard:add_HorizontalAds')  # Redirect to the page for adding new HorizontalAdss
        else:
            messages.warning(request, 'Form is not valid. Please correct the errors.')
    else:
        form = HorizontalAdsForm(instance=instance)

    context = {'form': form, 'instance': instance}
    return render(request, 'app2/create_horizontal_ads.html', context)

@login_required
def horizontalAds(request):
    horizontalAds=HorizontalAds.objects.all()
    p=Paginator(horizontalAds,10)
    page_number= request.GET.get('page')
    horizontalAds=p.get_page(page_number)
    return render(request, 'app2/horizontalAds.html',{'details':horizontalAds})

@login_required
def deletehorizontalAds(request, id):
    record = get_object_or_404(HorizontalAds, id=id)

    if request.method == 'POST':
        record.delete()
        return redirect('dashboard:horizontalAds')  # Redirect to a list view after deletion

    return render(request, 'app2/horizontalAds.html', {'details': record})



@login_required
def add_edit_VerticalAds(request, id=None):
    instance = None
    try:
        if id:
            instance = VerticalAds.objects.get(pk=id)
    except Exception as e:
        print(e)
        messages.warning(request, 'An error occurred while retrieving the VerticalAds.')
        return redirect('dashboard:add_VerticalAds')

    if request.method == 'POST':
        form = VerticalAdsForm(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            form.save()
            if instance:  # Edit operation
                messages.success(request, 'VerticalAds edited successfully.')
                return redirect('dashboard:edit_VerticalAds', id=instance.id)  # Redirect to the edited VerticalAds's details page
            else:  # Add operation
                messages.success(request, 'VerticalAds added successfully.')
                return redirect('dashboard:add_VerticalAds')  # Redirect to the page for adding new VerticalAdss
        else:
            messages.warning(request, 'Form is not valid. Please correct the errors.')
    else:
        form = VerticalAdsForm(instance=instance)

    context = {'form': form, 'instance': instance}
    return render(request, 'app2/create_verticalAds.html', context)


@login_required
def verticalAds(request):
    verticalAds=VerticalAds.objects.all()
    p=Paginator(verticalAds,10)
    page_number= request.GET.get('page')
    verticalAds=p.get_page(page_number)
    return render(request, 'app2/verticalAds.html',{'details':verticalAds})

@login_required
def deleteverticalAds(request, id):
    record = get_object_or_404(VerticalAds, id=id)

    if request.method == 'POST':
        record.delete()
        return redirect('dashboard:verticalAds')  # Redirect to a list view after deletion

    return render(request, 'app2/verticalAds.html', {'details': record})


@login_required
def contactUs(request):
    instance = None
    try:
        if id:
            instance = ContactUs.objects.first()
    except Exception as e:
        print(e)
        messages.warning(request, 'An error occurred while retrieving the VerticalAds.')
        return redirect('dashboard:contactUs')

    if request.method == 'POST':
        form = ContactUsForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            if instance:  # Edit operation
                messages.success(request, 'Contact updated successfully.')
                return redirect('dashboard:contactUs')  # Redirect to the edited VerticalAds's details page
            else:  # Add operation
                messages.success(request, 'Contact added successfully.')
                return redirect('dashboard:contactUs')  # Redirect to the page for adding new VerticalAdss
        else:
            messages.warning(request, 'Form is not valid. Please correct the errors.')
    else:
        form = ContactUsForm(instance=instance)

    context = {'form': form, 'instance': instance}
    return render(request, 'app2/contactUs.html', context)


@login_required
def ourteam(request):
    instance = None
    try:
        if id:
            instance = OurTeam.objects.first()
    except Exception as e:
        print(e)
        messages.warning(request, 'An error occurred while retrieving the VerticalAds.')
        return redirect('dashboard:ourteam')

    if request.method == 'POST':
        form = OurTeamForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            if instance:  # Edit operation
                messages.success(request, 'Our team updated successfully.')
                return redirect('dashboard:ourteam')  # Redirect to the edited VerticalAds's details page
            else:  # Add operation
                messages.success(request, 'Team added successfully.')
                return redirect('dashboard:ourteam')  # Redirect to the page for adding new VerticalAdss
        else:
            messages.warning(request, 'Form is not valid. Please correct the errors.')
    else:
        form = OurTeamForm(instance=instance)

    context = {'form': form, 'instance': instance}
    return render(request, 'app2/ourteam.html', context)




