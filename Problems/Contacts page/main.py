from django.views.generic.base import TemplateView
from django.shortcuts import render


class ContactsView(TemplateView):
    def get(self, request, *args, **kwargs):
        return render(request, "book/contacts.html")
