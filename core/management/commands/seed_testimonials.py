from django.core.management.base import BaseCommand
from django.db import transaction
from core.models import Testimonial, Service


TESTIMONIALS = [
    {
        'client_name': 'Ava Thompson',
        'company': 'Northwind Bank',
        'testimonial': 'The AI roadmap workshop clarified priorities and avoided months of churn.',
        'rating': 5,
        'client_position': 'Head of Strategy',
        'service_title': 'AI Strategy Consulting',
    },
    {
        'client_name': 'Ravi Patel',
        'company': 'Helios Manufacturing',
        'testimonial': 'Our assistant reduced ticket volume by 38% in the first month.',
        'rating': 5,
        'client_position': 'Operations Director',
        'service_title': 'GenAI Assistants',
    },
    {
        'client_name': 'Sophia Martinez',
        'company': 'Acme Health',
        'testimonial': 'Clean MLOps practices let us deploy models weekly with confidence.',
        'rating': 5,
        'client_position': 'VP Data Science',
        'service_title': 'MLOps & Model Governance',
    },
    {
        'client_name': 'Daniel Kim',
        'company': 'UrbanTel',
        'testimonial': 'Custom AI features shipped on time and exceeded user adoption goals.',
        'rating': 4,
        'client_position': 'Product Lead',
        'service_title': 'Custom AI Development',
    },
    {
        'client_name': 'Grace Lee',
        'company': 'Vista Retail',
        'testimonial': 'Data pipelines are reliable and governance-ready. Huge quality lift.',
        'rating': 5,
        'client_position': 'Data Engineering Manager',
        'service_title': 'Data Engineering & Pipelines',
    },
    {
        'client_name': 'Michael Brown',
        'company': 'Orbit Logistics',
        'testimonial': 'Modern BI stack enabled self-serve analytics for 200+ users.',
        'rating': 5,
        'client_position': 'Analytics Director',
        'service_title': 'Analytics & BI Modernization',
    },
    {
        'client_name': 'Lena Novak',
        'company': 'BlueSky HR',
        'testimonial': 'HR enablement program delivered measurable improvements in onboarding time.',
        'rating': 4,
        'client_position': 'People Ops Manager',
        'service_title': 'AI in HR Enablement',
    },
    {
        'client_name': 'Oliver Smith',
        'company': 'Nova Energy',
        'testimonial': 'Workshops were practical and immediately applicable to our teams.',
        'rating': 5,
        'client_position': 'Engineering Manager',
        'service_title': 'Training & Enablement',
    },
    {
        'client_name': 'Isabella Rossi',
        'company': 'Finova',
        'testimonial': 'The migration cut dashboard load times by 65% with better governance.',
        'rating': 5,
        'client_position': 'BI Lead',
        'service_title': 'Analytics & BI Modernization',
    },
    {
        'client_name': 'Noah Johnson',
        'company': 'CloudPeak',
        'testimonial': 'Their design reviews helped us de-risk our GenAI rollout.',
        'rating': 5,
        'client_position': 'CTO',
        'service_title': 'AI Strategy Consulting',
    },
]


class Command(BaseCommand):
    help = 'Seeds 10 testimonials and links them to existing services (idempotent).'

    def handle(self, *args, **options):
        created_count = 0
        with transaction.atomic():
            for data in TESTIMONIALS:
                service = None
                title = data.get('service_title')
                if title:
                    service = Service.objects.filter(title=title).first()
                obj, created = Testimonial.objects.get_or_create(
                    client_name=data['client_name'],
                    company=data['company'],
                    defaults={
                        'testimonial': data['testimonial'],
                        'rating': data['rating'],
                        'client_position': data.get('client_position', ''),
                        'service': service,
                    }
                )
                if created:
                    created_count += 1
        self.stdout.write(self.style.SUCCESS(f'Seeded {created_count} testimonials (idempotent).'))


