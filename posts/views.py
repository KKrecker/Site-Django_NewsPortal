from django.contrib.admin.templatetags.admin_list import pagination, paginator_number
from django.http import HttpResponse, HttpResponseRedirect,HttpRequest
from django.shortcuts import render
from posts.models import News, Advertisement
from django.core.paginator import Paginator
from posts.forms import AdvertisementForm, OfferForm
from django.urls import reverse
from .bot import bot

# Create your views here.

def news(request, page_number=1):
    new = News.objects.all()
    per_page = 3
    paginator = Paginator(new,per_page)
    page = paginator.page(page_number)
    context = {
    "news": page
    }
    return render(request,"posts/news.html", context)

def advertisements(request):
    advertisement = Advertisement.objects.all()
    context = {
        "advertisements": advertisement
    }
    return render(request, "posts/advertisements.html", context)

def one_advertisement(request, advertisement_id=4):
    advertisement = Advertisement.objects.get(id=advertisement_id)
    context = {
        "advertisement": advertisement
    }
    return render(request, "posts/advertisement.html", context)

def about(request):
    return render(request,'posts/about.html')

def contacts(request):
    return render(request, 'posts/contacts.html')

def create_advertisements(request):
    if request.method == "POST":
        form = AdvertisementForm(data=request.POST) #форма которую мы заполняем данными
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("posts:advertisements"))
        else:
            return HttpResponseRedirect(reverse("posts:create_advertisements"))
    elif request.method == "GET":
        form = AdvertisementForm() #пустая форма для заполнения данными
    context= {
        "form": form
    }
    return render(request, 'posts/create_advertisements.html',context)

def create_offer(request):
    if request.method == "POST":
        form = OfferForm(data=request.POST) #форма которую мы заполняем данными
        if form.is_valid():
            form.save()
            text = render(HttpRequest(),'posts/message_offer_for_tg_bot.html',{'form':form})
            bot.send_message(6216772256,text,parse_mode="HTML")
            # bot.send_message(6216772256,f'''
            # К вам поступила заявка
            # {form.cleaned_data['title']}
            # {form.cleaned_data['content']}
            # Email: {form.cleaned_data['email']}
            # 📱Номер телефона: {form.cleaned_data['phone']}
            # ''')
            return HttpResponseRedirect(reverse("posts:create_offer"))
        else:
            return HttpResponseRedirect(reverse("posts:create_offer"))
    elif request.method == "GET":
        form = OfferForm() #пустая форма для заполнения данными
    context= {
        "form": form
    }
    return render(request, 'posts/create_offer.html',context)
