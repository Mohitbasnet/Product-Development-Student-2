from django.core.management.base import BaseCommand

from core.models import GalleryImage


class Command(BaseCommand):
    help = "Create N GalleryImage records with labels only (no images)."

    def add_arguments(self, parser):
        parser.add_argument("--count", type=int, default=10, help="Number of label-only items to create (default 10)")
        parser.add_argument("--prefix", type=str, default="Gallery Item", help="Label prefix (default 'Gallery Item')")

    def handle(self, *args, **options):
        count = options["count"]
        prefix = options["prefix"].strip() or "Gallery Item"

        created = 0
        for i in range(1, count + 1):
            label = f"{prefix} {i}"
            obj, made = GalleryImage.objects.get_or_create(label=label, defaults={"image": None})
            if made:
                created += 1
        self.stdout.write(self.style.SUCCESS(f"Created {created} label-only gallery items"))


