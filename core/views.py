from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Service, Solution, Testimonial, Article, Event, ContactInquiry, GalleryImage
from .forms import ContactForm
from django.utils import timezone
from django import forms
from django.db.models import Count
import logging

# Configure logging
logger = logging.getLogger(__name__)

def home(request):
    solutions = Solution.objects.all()[:6]
    services = Service.objects.all()[:6]
    testimonials = Testimonial.objects.all()[:3]
    articles = Article.objects.all()[:3]
    events = Event.objects.all()[:3]
    return render(request, 'core/home.html', {
        'solutions': solutions,
        'services': services,
        'testimonials': testimonials,
        'articles': articles,
        'events': events,
    })




def services(request):
    services_qs = Service.objects.annotate(review_count=Count('testimonials'))
    return render(request, 'core/services.html', {'services': services_qs})

def solution_detail(request, slug):
    solution = get_object_or_404(Solution, slug=slug)
    # Get related solutions (excluding current solution)
    related_solutions = Solution.objects.exclude(id=solution.id)[:3]
    return render(request, 'core/solution_detail.html', {
        'solution': solution,
        'related_solutions': related_solutions,
        'is_past': True,
    })


def service_detail(request, slug):
    service = get_object_or_404(Service, slug=slug)
    related_services = Service.objects.exclude(id=service.id)[:3]
    return render(request, 'core/service_detail.html', {
        'service': service,
        'related_services': related_services,
    })


class TestimonialForm(forms.Form):
    client_name = forms.CharField(max_length=100, label='Client name *')
    company = forms.CharField(max_length=100, label='Company *')
    testimonial = forms.CharField(widget=forms.Textarea, label='Testimonial *')
    rating = forms.IntegerField(min_value=1, max_value=5, initial=5, label='Rating *')
    client_position = forms.CharField(max_length=100, required=False, label='Client position (optional)')
    client_image = forms.ImageField(required=False, label='Client image (optional)')


def submit_testimonial(request):
    # Preselect service via URL parameter (e.g., ?service=slug)
    initial = {}
    service_slug = request.GET.get('service')
    if service_slug:
        svc = Service.objects.filter(slug=service_slug).first()
        if svc:
            initial['service'] = svc.id
    if request.method == 'POST':
        form = TestimonialForm(request.POST, request.FILES)
        if form.is_valid():
            Testimonial.objects.create(
                client_name=form.cleaned_data['client_name'],
                company=form.cleaned_data['company'],
                testimonial=form.cleaned_data['testimonial'],
                rating=form.cleaned_data['rating'],
                client_position=form.cleaned_data.get('client_position') or '',
                client_image=form.cleaned_data.get('client_image'),
                service=Service.objects.filter(slug=service_slug).first() if service_slug else None,
            )
            messages.success(request, 'Thank you for your feedback! Your testimonial has been submitted.')
            return redirect('core:testimonials')
    else:
        form = TestimonialForm(initial=initial)
    return render(request, 'core/submit_testimonial.html', {'form': form})

def articles(request):
    articles = Article.objects.all()
    return render(request, 'core/articles.html', {'articles': articles})

def article_detail(request, slug):
    article = get_object_or_404(Article, slug=slug)
    return render(request, 'core/article_detail.html', {'article': article})

def testimonials(request):
    testimonials = Testimonial.objects.all()
    return render(request, 'core/testimonials.html', {'testimonials': testimonials})

def events(request):
    current_date = timezone.now().date()
    upcoming_events = Event.objects.filter(date__gte=current_date).order_by('date')
    past_events = Event.objects.filter(date__lt=current_date).order_by('-date')
    return render(request, 'core/events.html', {
        'upcoming_events': upcoming_events,
        'past_events': past_events,
        'now': current_date,
    })

def event_detail(request, slug):
    event = get_object_or_404(Event, slug=slug)
    return render(request, 'core/event_detail.html', {'event': event})

def about(request):
    return render(request, 'core/about.html')

def contact(request):
    if request.method == 'POST':
        logger.info("Received POST request to contact view")
        form = ContactForm(request.POST)
        if form.is_valid():
            logger.info("Form is valid, attempting to save")
            try:
                contact_inquiry = form.save()
                logger.info(f"Successfully saved contact inquiry with ID: {contact_inquiry.id}")
                messages.success(request, 'Thank you for your inquiry. We will get back to you soon!')
                return redirect('core:contact')
            except Exception as e:
                logger.error(f"Error saving contact inquiry: {e}")
                messages.error(request, 'Sorry, there was an error submitting your inquiry. Please try again.')
        else:
            logger.error(f"Form validation failed: {form.errors}")
            messages.error(request, 'Please correct the errors below.')
    else:
        logger.info("Received GET request to contact view")
        form = ContactForm()
    return render(request, 'core/contact.html', {'form': form})


def past_solutions(request):
    # Show legacy solutions only (exclude items that were migrated to Services)
    service_titles = Service.objects.values_list('title', flat=True)
    solutions_qs = (
        Solution.objects.exclude(title__in=service_titles)
        .order_by('created_at')
    )
    return render(request, 'core/past_solutions.html', {
        'solutions': solutions_qs,
    })


def gallery(request):
    # Use admin-managed gallery images
    gallery_images = GalleryImage.objects.all().order_by('-created_at')
    return render(request, 'core/gallery.html', {
        'gallery_images': gallery_images,
    })
