from django.shortcuts import redirect
from functools import wraps


# Decorator to check if the user is authenticated and has the required role
def role_required(allowed_roles, redirect_url="dashboard"):
    def decorator(view_func):
        @wraps(view_func)
        def wrapper(request, *args, **kwargs):
            if not request.user.is_authenticated:
                return redirect("login")
            if request.user.role not in allowed_roles:
                return redirect(redirect_url)
            return view_func(request, *args, **kwargs)

        return wrapper

    return decorator
