from django.core.management.base import BaseCommand
from core.models import GalleryImage


DEFAULT_LABELS = [
    "AI Strategy Workshop",
    "GenAI Assistant Prototype",
    "Data Pipeline Architecture",
    "MLOps Monitoring Dashboard",
    "Analytics & BI Modernization",
    "HR Enablement Session",
    "Training & Enablement Workshop",
    "Employee Onboarding Bot",
    "Performance Insights Report",
    "Engagement Analytics Overview",
    "Conference Keynote",
    "Innovation Summit",
    "Team Collaboration",
    "Customer Support Assistant",
    "Model Governance Review",
    "Design Sprint",
    "Product Prototype UI",
    "Secure Deployment",
    "Post‑Launch Monitoring",
    "Project Retrospective",
]


class Command(BaseCommand):
    help = "Relabel all GalleryImage records with professional labels (idempotent)."

    def add_arguments(self, parser):
        parser.add_argument(
            "--prefix",
            type=str,
            default="",
            help="Optional prefix to add before each label",
        )

    def handle(self, *args, **options):
        prefix = options.get("prefix", "").strip()
        labels = [f"{prefix} {l}".strip() for l in DEFAULT_LABELS]

        qs = GalleryImage.objects.order_by("-created_at")
        if not qs.exists():
            self.stdout.write(self.style.WARNING("No GalleryImage records to relabel."))
            return

        updated = 0
        for idx, item in enumerate(qs):
            new_label = labels[idx % len(labels)]
            if item.label != new_label:
                item.label = new_label
                item.save(update_fields=["label"])
                updated += 1

        self.stdout.write(self.style.SUCCESS(f"Relabeled {updated} gallery items."))


