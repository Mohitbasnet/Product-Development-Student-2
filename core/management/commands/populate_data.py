from django.core.management.base import BaseCommand
from django.utils import timezone
from django.contrib.auth.models import User
from core.models import Service, Solution, Article, Testimonial, Event
from datetime import timedelta

class Command(BaseCommand):
    help = 'Populates the database with dummy data'

    def handle(self, *args, **kwargs):
        self.stdout.write('Creating dummy data...')

        # Create admin user if not exists
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser('admin', 'admin@example.com', 'admin123')
            self.stdout.write('Created admin user')

        # Create Solutions
        solutions_data = [
            {
                'title': 'AI-Powered Employee Onboarding',
                'description': 'Streamline your onboarding process with our intelligent AI solution that personalizes the experience for each new hire.',
                'icon': 'fa-user-plus',
            },
            {
                'title': 'Smart Performance Management',
                'description': 'Transform your performance reviews with AI-driven insights and real-time feedback systems.',
                'icon': 'fa-chart-line',
            },
            {
                'title': 'Intelligent Learning Platform',
                'description': 'Personalized learning paths and skill development powered by advanced AI algorithms.',
                'icon': 'fa-graduation-cap',
            },
            {
                'title': 'Employee Engagement Analytics',
                'description': 'Gain deep insights into employee engagement and satisfaction with our AI-powered analytics platform.',
                'icon': 'fa-heart',
            },
            {
                'title': 'Smart HR Assistant',
                'description': '24/7 AI-powered HR support that handles employee queries and automates routine tasks.',
                'icon': 'fa-robot',
            },
            {
                'title': 'Workforce Planning AI',
                'description': 'Optimize your workforce planning with predictive analytics and AI-driven insights.',
                'icon': 'fa-users',
            }
        ]

        for data in solutions_data:
            Solution.objects.get_or_create(
                title=data['title'],
                defaults={
                    'description': data['description'],
                    'icon': data['icon'],
                }
            )

        # Create Services
        services_data = [
            {
                'title': 'AI Strategy Consulting',
                'summary': 'Define your AI roadmap and prioritize high-impact opportunities.',
                'description': 'Our consultants partner with your stakeholders to identify strategic AI use cases, assess readiness, and build a pragmatic execution plan.',
                'icon': 'fa-compass',
            },
            {
                'title': 'Custom AI Development',
                'summary': 'End-to-end design and delivery of AI applications.',
                'description': 'Full lifecycle development from discovery through deployment, including model selection, MLOps, and ongoing optimization.',
                'icon': 'fa-cogs',
            },
            {
                'title': 'Data Engineering & Pipelines',
                'summary': 'Reliable data foundations for analytics and AI.',
                'description': 'We design and build robust data ingestion, transformation, and governance pipelines to power enterprise AI initiatives.',
                'icon': 'fa-database',
            },
            {
                'title': 'AI in HR Enablement',
                'summary': 'Use AI to elevate employee experience and productivity.',
                'description': 'Services tailored for HR: onboarding assistants, performance insights, learning personalization, and engagement analytics.',
                'icon': 'fa-user-tie',
            },
            {
                'title': 'Analytics & BI Modernization',
                'summary': 'Modern dashboards and self-serve analytics at scale.',
                'description': 'We modernize legacy BI stacks, implement semantic layers, and enable governed self-serve analytics across teams.',
                'icon': 'fa-chart-bar',
            },
            {
                'title': 'MLOps & Model Governance',
                'summary': 'Operationalize models with confidence and compliance.',
                'description': 'CI/CD for ML, monitoring, drift detection, lineage, and governance to keep models accurate and auditable.',
                'icon': 'fa-project-diagram',
            },
            {
                'title': 'GenAI Assistants',
                'summary': 'Domain-specific copilots for employees and customers.',
                'description': 'We build safe, grounded assistants with retrieval, guardrails, and analytics tuned to your domain.',
                'icon': 'fa-robot',
            },
            {
                'title': 'Training & Enablement',
                'summary': 'Upskill your teams to deliver and operate AI solutions.',
                'description': 'Curriculum and hands-on workshops for product, data, and engineering teams to adopt AI sustainably.',
                'icon': 'fa-chalkboard-teacher',
            },
        ]

        for data in services_data:
            Service.objects.get_or_create(
                title=data['title'],
                defaults={
                    'summary': data.get('summary', ''),
                    'description': data['description'],
                    'icon': data.get('icon', 'fa-briefcase'),
                }
            )

        # Create Articles
        articles_data = [
            {
                'title': 'The Future of AI in HR',
                'content': 'Artificial Intelligence is revolutionizing the way we approach human resources. From recruitment to employee engagement, AI is transforming every aspect of HR management.',
                'author': 'John Smith',
            },
            {
                'title': '5 Ways AI is Improving Employee Experience',
                'content': 'Discover how artificial intelligence is enhancing employee experience through personalized learning, smart onboarding, and intelligent performance management.',
                'author': 'Sarah Johnson',
            },
            {
                'title': 'Digital Transformation in the Workplace',
                'content': 'Learn about the key trends in digital transformation and how organizations are leveraging technology to create better workplaces.',
                'author': 'Michael Brown',
            },
            {
                'title': 'Building Responsible GenAI for the Enterprise',
                'content': 'Enterprises adopting GenAI must balance velocity with responsibility. This guide covers data governance, retrieval augmentation, prompt hygiene, evaluation frameworks, red‑teaming, and human‑in‑the‑loop review to keep systems safe and effective at scale. We include concrete blueprints and KPIs to measure business outcomes.',
                'author': 'Priya Kapoor',
            },
            {
                'title': 'From POCs to Platform: Industrializing AI Delivery',
                'content': 'Many teams get stuck in prototype purgatory. We outline an operating model for AI: product pods, shared MLOps, CI/CD for ML, model registry, observability, drift detection, and cost governance. Real customer stories show how to reduce time‑to‑value while improving reliability.',
                'author': 'Diego Alvarez',
            },
            {
                'title': 'Designing AI Assistants Employees Actually Use',
                'content': 'Adoption requires trust and usability. We share design patterns for copilots: grounding, confidence overlays, clarifying questions, graceful failure, and analytics loops. Includes UI patterns, prompt architectures, and measurement techniques to drive net productivity gains.',
                'author': 'Emily Chen',
            },
        ]

        for data in articles_data:
            Article.objects.get_or_create(
                title=data['title'],
                defaults={
                    'content': data['content'],
                    'author': data['author'],
                }
            )

        # Create Testimonials
        testimonials_data = [
            {
                'client_name': 'Emma Wilson',
                'company': 'TechCorp',
                'testimonial': 'AI-Solutions has transformed our employee experience. The onboarding process is now seamless, and our team engagement has increased significantly.',
                'rating': 5,
                'client_position': 'HR Director',
            },
            {
                'client_name': 'David Chen',
                'company': 'Global Solutions',
                'testimonial': 'The AI-powered learning platform has revolutionized how we train our employees. The personalized approach has led to better retention and skill development.',
                'rating': 5,
                'client_position': 'Learning & Development Manager',
            },
            {
                'client_name': 'Lisa Anderson',
                'company': 'Innovate Inc',
                'testimonial': 'Implementing AI-Solutions has streamlined our HR processes and improved employee satisfaction. The analytics insights are invaluable for decision-making.',
                'rating': 5,
                'client_position': 'Chief People Officer',
            }
        ]

        for data in testimonials_data:
            Testimonial.objects.get_or_create(
                client_name=data['client_name'],
                defaults={
                    'company': data['company'],
                    'testimonial': data['testimonial'],
                    'rating': data['rating'],
                    'client_position': data['client_position'],
                }
            )

        # Create Events
        events_data = [
            {
                'title': 'AI in HR Summit 2024',
                'description': 'Join industry leaders and experts to explore the latest trends in AI-powered HR solutions.',
                'date': timezone.now() + timedelta(days=30),
                'time': '09:00 AM - 05:00 PM',
                'location': 'Virtual Event',
            },
            {
                'title': 'Digital Employee Experience Workshop',
                'description': 'Hands-on workshop on implementing AI solutions for better employee experience.',
                'date': timezone.now() + timedelta(days=45),
                'time': '10:00 AM - 03:00 PM',
                'location': 'London Business Center',
            },
            {
                'title': 'Future of Work Conference',
                'description': 'Explore how AI and automation are shaping the future of work and employee experience.',
                'date': timezone.now() + timedelta(days=60),
                'time': '09:00 AM - 06:00 PM',
                'location': 'Manchester Convention Center',
            },
            {
                'title': 'GenAI Platform Deep Dive',
                'description': 'Technical deep dive on retrieval, orchestration, evaluation, and guardrails for GenAI apps. Live demos and code walkthroughs.',
                'date': timezone.now() + timedelta(days=15),
                'time': '01:00 PM - 04:00 PM',
                'location': 'Berlin Tech Hub',
            },
            {
                'title': 'AI Adoption Roundtable',
                'description': 'Executive roundtable discussing change management, skills, and ROI measurement for enterprise AI programs.',
                'date': timezone.now() - timedelta(days=10),
                'time': '02:00 PM - 05:00 PM',
                'location': 'Virtual Event',
            },
            {
                'title': 'Secure AI Engineering Bootcamp',
                'description': 'Hands‑on training on secure prompt design, policy enforcement, and auditability for regulated industries.',
                'date': timezone.now() - timedelta(days=25),
                'time': '09:30 AM - 05:30 PM',
                'location': 'New York Innovation Lab',
            },
        ]

        for data in events_data:
            Event.objects.get_or_create(
                title=data['title'],
                defaults={
                    'description': data['description'],
                    'date': data['date'],
                    'time': data['time'],
                    'location': data['location'],
                }
            )

        self.stdout.write(self.style.SUCCESS('Successfully populated database with dummy data')) 