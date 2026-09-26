from getpass import getpass

from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    help = "Create a user for the custom portfolio dashboard."

    def handle(self, *args, **options):
        User = get_user_model()
        username = input("Username: ").strip()

        if not username:
            raise CommandError("Username is required.")

        if User.objects.filter(username=username).exists():
            raise CommandError("That username already exists.")

        password = getpass("Password: ")
        confirm = getpass("Confirm password: ")

        if not password:
            raise CommandError("Password cannot be empty.")

        if password != confirm:
            raise CommandError("Passwords do not match.")

        try:
            validate_password(password)
        except ValidationError as exc:
            raise CommandError("Password is not strong enough: " + " ".join(exc.messages)) from exc

        user = User.objects.create_user(
            username=username,
            password=password,
            is_staff=True,
            is_superuser=False,
        )

        self.stdout.write(
            self.style.SUCCESS(
                f"Created dashboard user '{user.username}'. "
                "Use /login/ for the custom CMS."
            )
        )
