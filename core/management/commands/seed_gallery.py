import os
import shutil
from pathlib import Path

from django.core.management.base import BaseCommand
from django.conf import settings

from core.models import GalleryImage


class Command(BaseCommand):
    help = "Seed GalleryImage entries by copying existing media images into gallery/."

    def add_arguments(self, parser):
        parser.add_argument("--count", type=int, default=10, help="Number of images to add (default 10)")

    def handle(self, *args, **options):
        count = options["count"]
        media_root = Path(settings.MEDIA_ROOT)

        # Source folders to look for images
        source_dirs = [
            media_root / "solutions",
            media_root / "articles",
            media_root / "events",
            media_root / "testimonials",
        ]

        gallery_dir = media_root / "gallery"
        gallery_dir.mkdir(parents=True, exist_ok=True)

        # Collect existing image paths
        candidates = []
        for d in source_dirs:
            if d.exists() and d.is_dir():
                for p in d.iterdir():
                    if p.suffix.lower() in {".jpg", ".jpeg", ".png", ".gif", ".webp"} and p.is_file():
                        candidates.append(p)

        if not candidates:
            self.stdout.write(self.style.WARNING("No source images found under media/solutions|articles|events|testimonials"))
            return

        added = 0
        for src in candidates:
            if added >= count:
                break

            # Compose destination file path (avoid collisions)
            dest_name = f"{src.stem}_{added}{src.suffix}"
            dest_path = gallery_dir / dest_name
            try:
                shutil.copyfile(src, dest_path)
                # Save a GalleryImage pointing to gallery/<dest_name>
                rel_path = f"gallery/{dest_name}"
                GalleryImage.objects.create(label=src.stem.replace("_", " "), image=rel_path)
                added += 1
            except Exception as e:
                self.stdout.write(self.style.WARNING(f"Skip {src.name}: {e}"))

        self.stdout.write(self.style.SUCCESS(f"Added {added} gallery images"))


