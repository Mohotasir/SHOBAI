from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as signIn, logout as signOut
from django.db.models import Q
from .models import User, Zone
from .forms import UserRegistrationForm, UserSignInForm, BecomeMerchantForm
from .decorators import role_required


def register(request):
    """
    This view handles the registration of a new user.
    """
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            # Save the user and set the password correctly
            user = form.save(commit=False)
            user.set_password(form.cleaned_data.get("password"))
            user.save()

            # Automatically log in the user
            user = authenticate(
                request, email=user.email, password=form.cleaned_data.get("password")
            )
            if user:
                signIn(request, user)
                messages.success(request, "Account created successfully!")
                return redirect("home")
    else:
        form = UserRegistrationForm()

    return render(request, "register.html", {"form": form})


def login(request):
    """
    This view handles the login of a user.
    """
    if request.method == "POST":
        form = UserSignInForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password")
            user = authenticate(request, email=email, password=password)

            if user is not None:
                signIn(request, user)
                messages.success(request, "Successfully logged in!")
                return redirect("home")
            else:
                messages.error(request, "Invalid email or password.")
    else:
        form = UserSignInForm()

    return render(request, "login.html", {"form": form})


def logout(request):
    """
    This handles the logout of a user.
    """
    signOut(request)
    return redirect(request.META.get("HTTP_REFERER", "/"))


@login_required
def become_merchant(request):
    """
    This view handles the request to become a merchant.
    """
    if request.method == "POST":
        form = BecomeMerchantForm(request.POST, request.FILES)
        if form.is_valid():
            application = form.save(commit=False)
            application.user = request.user
            application.save()
            messages.success(request, "Successfully submitted!")
            return redirect("home")
        else:
            print(form.errors)

    else:
        form = BecomeMerchantForm()

    return render(request, "become_merchant.html", {"form": form})


@login_required
def address_book(request):
    """
    This view handles the address book of a user.
    """
    user = request.user
    addresses = user.addresses.all()
    return render(request, "address_book.html", {"addresses": addresses})


def zones(request):
    zones = Zone.objects.all()
    zones_data = [{"id": zone.pk, "name": zone.name} for zone in zones]
    return JsonResponse({"data": zones_data})


def areas(request):
    zone_id = request.GET.get("zone")
    if zone_id:
        try:
            zone = Zone.objects.get(pk=zone_id)
            areas = zone.thanas.all()
            areas_data = [{"id": area.pk, "name": area.name} for area in areas]
            return JsonResponse({"zone": zone.name, "areas": areas_data})
        except Zone.DoesNotExist:
            return JsonResponse({"error": "Zone not found"}, status=404)
    else:
        return JsonResponse({"error": "Zone ID not provided"}, status=400)


@role_required(["ADMIN"])
def manage_user(request):
    role = request.GET.get("role", "all")
    query = request.GET.get("q", "")

    # Filter users based on role except superusers
    if role == "all":
        users = User.objects.filter(is_superuser=False)
    else:
        users = User.objects.filter(role=role.upper(), is_superuser=False)

    # Apply search filter if query exists
    if query:
        users = users.filter(Q(name__icontains=query) | Q(email__icontains=query))

    return render(request, "manage-users.html", {"users": users})


@role_required(["ADMIN"])
def update_role(request, id):
    role = request.GET.get("role", "").lower()

    if not role or role not in ("admin", "user"):
        return redirect("manage-users")

    try:
        user = User.objects.get(pk=id)
        user.role = role.upper()
        user.save(update_fields=["role"])
        return redirect("manage-users")
    except User.DoesNotExist:
        return redirect("manage-users")
