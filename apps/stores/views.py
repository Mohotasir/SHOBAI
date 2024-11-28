from django.shortcuts import render, redirect
from apps.users.decorators import role_required
from .forms import CreateStoreForm
from .models import Store, StoreFollow


# Create your views here.
def store(request, slug):
    try:
        store = Store.objects.get(slug=slug)
        collections = store.collections.all().prefetch_related("products")
        is_following = StoreFollow.objects.filter(user=request.user, store=store).exists()
        return render(
            request,
            "store.html",
            {"store": store, "collections": collections, "is_following": is_following},
        )
    except Store.DoesNotExist:
        return redirect(request.META.get("HTTP_REFERER", "home"))


def manage_inventory(request):
    return render(request, "manage_inventory.html")


def manage_orders(request):
    return render(request, "manage_orders.html")


@role_required(["MERCHANT"])
def create_store(request):
    if request.method == "POST":
        form = CreateStoreForm(request.POST, request.FILES)
        if form.is_valid():
            store = form.save(commit=False)
            store.merchant = request.user
            store.save()
            return redirect("dashboard")
    else:
        form = CreateStoreForm()
    return render(request, "create_store.html", {"form": form})


@role_required(["USER", "MERCHANT"], redirect_url="CURRENT")
def toggle_follow_store(request, slug):
    try:
        store = Store.objects.get(slug=slug)
        if store.merchant != request.user:
            follow, created = StoreFollow.objects.get_or_create(user=request.user, store=store)
            if not created:
                follow.delete()
    except Store.DoesNotExist:
        pass

    return redirect(request.META.get("HTTP_REFERER"))
