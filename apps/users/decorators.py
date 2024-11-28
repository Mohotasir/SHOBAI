from django.shortcuts import redirect
from functools import wraps


# Decorator to redirect authenticated users to the previous page
def redirect_authenticated_user(view_func, redirect_url="dashboard"):
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated:
            previous_url = request.META.get("HTTP_REFERER", redirect_url)
            return redirect(previous_url)
        return view_func(request, *args, **kwargs)

    return wrapper


# Decorator to check if the user is authenticated and has the required role
def role_required(allowed_roles, redirect_url="dashboard"):
    def decorator(view_func):
        @wraps(view_func)
        def wrapper(request, *args, **kwargs):
            if not request.user.is_authenticated:
                return redirect("login")
            if request.user.role not in allowed_roles:
                if redirect_url == "CURRENT":
                    return redirect(request.META.get("HTTP_REFERER"))
                return redirect(redirect_url)
            return view_func(request, *args, **kwargs)

        return wrapper

    return decorator
