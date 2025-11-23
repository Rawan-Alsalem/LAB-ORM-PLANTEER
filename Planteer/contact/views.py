from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .forms import ContactForm
from .models import ContactMessage

def contact_view(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/contact/?success=1")  # ← redirect so modal works
    else:
        form = ContactForm()

    success = request.GET.get("success") == "1"

    return render(request, "contact/contact.html", {"form": form, "success": success})



def contact_messages(request):
    msgs = ContactMessage.objects.all().order_by('-id')
    return render(request, "contact/contact_messages.html", {"messages": msgs})
