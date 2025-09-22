from django.core.management.base import BaseCommand
import os
import requests
from django.conf import settings
from pathlib import Path

class Command(BaseCommand):
    help = 'Downloads placeholder images for dummy data'

    def handle(self, *args, **kwargs):
        self.stdout.write('Downloading placeholder images...')

        # Create media directories
        media_dirs = [
            'solutions',
            'articles',
            'testimonials',
            'events'
        ]

        for dir_name in media_dirs:
            dir_path = os.path.join(settings.MEDIA_ROOT, dir_name)
            os.makedirs(dir_path, exist_ok=True)

        # Image URLs (using placeholder.com)
        image_urls = {
            'solutions': {
                'onboarding.jpg': 'https://placehold.co/800x600/2563eb/ffffff?text=AI+Onboarding',
                'performance.jpg': 'https://placehold.co/800x600/2563eb/ffffff?text=Performance+Management',
                'learning.jpg': 'https://placehold.co/800x600/2563eb/ffffff?text=Learning+Platform',
                'engagement.jpg': 'https://placehold.co/800x600/2563eb/ffffff?text=Engagement+Analytics',
                'assistant.jpg': 'https://placehold.co/800x600/2563eb/ffffff?text=HR+Assistant',
                'planning.jpg': 'https://placehold.co/800x600/2563eb/ffffff?text=Workforce+Planning'
            },
            'articles': {
                'ai-hr.jpg': 'https://placehold.co/800x600/2563eb/ffffff?text=AI+in+HR',
                'employee-exp.jpg': 'https://placehold.co/800x600/2563eb/ffffff?text=Employee+Experience',
                'digital-trans.jpg': 'https://placehold.co/800x600/2563eb/ffffff?text=Digital+Transformation'
            },
            'testimonials': {
                'client1.jpg': 'https://placehold.co/400x400/2563eb/ffffff?text=Emma+Wilson',
                'client2.jpg': 'https://placehold.co/400x400/2563eb/ffffff?text=David+Chen',
                'client3.jpg': 'https://placehold.co/400x400/2563eb/ffffff?text=Lisa+Anderson'
            },
            'events': {
                'summit.jpg': 'https://placehold.co/800x600/2563eb/ffffff?text=AI+Summit',
                'workshop.jpg': 'https://placehold.co/800x600/2563eb/ffffff?text=Workshop',
                'conference.jpg': 'https://placehold.co/800x600/2563eb/ffffff?text=Conference'
            }
        }

        # Download images
        for category, images in image_urls.items():
            for filename, url in images.items():
                file_path = os.path.join(settings.MEDIA_ROOT, category, filename)
                if not os.path.exists(file_path):
                    try:
                        response = requests.get(url)
                        response.raise_for_status()
                        with open(file_path, 'wb') as f:
                            f.write(response.content)
                        self.stdout.write(f'Downloaded {filename}')
                    except Exception as e:
                        self.stdout.write(self.style.ERROR(f'Error downloading {filename}: {str(e)}'))

        self.stdout.write(self.style.SUCCESS('Successfully downloaded placeholder images')) 