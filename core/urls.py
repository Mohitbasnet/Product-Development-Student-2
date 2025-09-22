from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.home, name='home'),
    # path('solutions/', views.solutions, name='solutions'),
    path('services/', views.services, name='services'),
    path('past-solutions/', views.past_solutions, name='past_solutions'),
    path('solutions/<slug:slug>/', views.solution_detail, name='solution_detail'),
    path('services/<slug:slug>/', views.service_detail, name='service_detail'),
    path('testimonials/submit/', views.submit_testimonial, name='submit_testimonial'),
    path('articles/', views.articles, name='articles'),
    path('articles/<slug:slug>/', views.article_detail, name='article_detail'),
    path('testimonials/', views.testimonials, name='testimonials'),
    path('events/', views.events, name='events'),
    path('events/<slug:slug>/', views.event_detail, name='event_detail'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('gallery/', views.gallery, name='gallery'),
] 