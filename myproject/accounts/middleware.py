from django.shortcuts import redirect
from django.urls import reverse

class LoginRequiredMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.protected_paths = [
            '/categories/',
            '/Product/',
        ]

    def __call__(self, request):
        if any(request.path.startswith(path) for path in self.protected_paths):
            if not request.user.is_authenticated:
                return redirect(reverse('login'))
        return self.get_response(request)