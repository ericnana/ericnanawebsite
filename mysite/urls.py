# mysite/urls.py
from django.conf.urls import url
from django.urls import path
from mysite import views
from django.conf import settings
from django.views.generic.base import RedirectView
from django.conf.urls.static import static
from django.contrib import admin








urlpatterns = [
   
    url(r'^$', views.HomePageView.as_view()),
    url(r'^about/$', views.AboutPageView.as_view()), # Add this /about/ route
    url(r'^home/$', views.HomePageView.as_view()),
    url(r'^work/$', views.WorkPageView.as_view()),
    url(r'^home/$', views.HomePageViewReal.as_view(), name='home'),
    #url(r'^success/$', views.SuccessPageView.as_view()),
    #url(r'^success/$', views.SuccessView,name='success'),
    #url(r'^contact/$', views.ContactPageView.as_view()),
    #url(r'^contact/$', views.ContactPageViewReal.as_view(), name='contact'),
    #url(r'^ajax.php/$', views.SubmitMessagePageView, name='ajax'),
    #url(r'^contact/$', views.ContactPageView.emailView),
    #url(r'^success/$', views.SuccessPageView.as_view()),
    # url(r'^about/aboutme/$', views.pdf_view),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^impressum/$', views.ImpressumPageView.as_view()),
    url(r'^work/automationtesting/$', views.AutomationTestingPageView.as_view(), name='automationtesting'),
    url(r'^work/naturallanguage/$', views.NaturalLanguagePageView.as_view(), name='naturallanguage'),
    url(r'^work/tradingstock/$', views.TradingStockPageView.as_view(), name='tradingstock'),
    url(r'^work/markovprocess/$', views.MarkovProcessPageView.as_view(), name='markovprocess'),

]


