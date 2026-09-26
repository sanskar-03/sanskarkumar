from __future__ import annotations

import os
from pathlib import Path
from uuid import uuid4

from django.conf import settings
from django.core.files.storage import FileSystemStorage


MAX_IMAGE_BYTES = 5 * 1024 * 1024
ALLOWED_EXTENSIONS = {".jpg", ".jpeg", ".png", ".webp", ".gif"}


def store_image(uploaded_file, folder: str) -> str:
    """Store an uploaded image locally or on Cloudinary and return its URL."""
    if not uploaded_file:
        return ""

    if uploaded_file.size > MAX_IMAGE_BYTES:
        raise ValueError("Image must be 5 MB or smaller.")

    content_type = getattr(uploaded_file, "content_type", "") or ""
    if not content_type.startswith("image/"):
        raise ValueError("Please upload an image file.")

    suffix = Path(uploaded_file.name).suffix.lower()
    if suffix not in ALLOWED_EXTENSIONS:
        raise ValueError("Allowed image types: JPG, PNG, WEBP or GIF.")

    cloudinary_url = os.getenv("CLOUDINARY_URL", "").strip()
    if cloudinary_url:
        import cloudinary
        import cloudinary.uploader

        cloudinary.config(secure=True)
        result = cloudinary.uploader.upload(
            uploaded_file,
            folder=f"cse-portfolio/{folder}",
            resource_type="image",
            use_filename=False,
            unique_filename=True,
        )
        return result["secure_url"]

    if getattr(settings, "VERCEL", False) or os.getenv("VERCEL"):
        raise ValueError(
            "Image upload on Vercel requires CLOUDINARY_URL. "
            "Add your Cloudinary connection string in Vercel Environment Variables."
        )

    storage = FileSystemStorage(location=settings.MEDIA_ROOT, base_url=settings.MEDIA_URL)
    name = f"uploads/{folder}/{uuid4().hex}{suffix}"
    saved_name = storage.save(name, uploaded_file)
    return storage.url(saved_name)
