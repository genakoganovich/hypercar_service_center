from django.views import View
from django.http.response import HttpResponse
from django.shortcuts import render
from django.views.generic.base import TemplateView


template_name = 'tickets/menu.html'
tickets = {
    'change_oil': 'Change oil',
    'inflate_tires': 'Inflate tires',
    'diagnostic': 'Diagnostic',
}


class WelcomeView(View):
    def get(self, request, *args, **kwargs):
        html = "<h2>Welcome to the Hypercar Service!</h2>"
        return HttpResponse(html)


class MenuView(View):
    def get(self, request, *args, **kwargs):
        return render(request, template_name=template_name, context={'tickets': tickets})


class TicketView(TemplateView):
    template_name = 'tickets/ticket.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        ticket = kwargs['ticket']
        context['content'] = tickets[ticket]
        return context
