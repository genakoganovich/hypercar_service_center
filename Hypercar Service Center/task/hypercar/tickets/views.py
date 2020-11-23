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
    ticket_number = 1
    line_of_cars = {'change_oil': list(), 'inflate_tires': list(), 'diagnostic': list()}
    service_time = {'change_oil': 2, 'inflate_tires': 5, 'diagnostic': 30}
    service_menu = ['change_oil', 'inflate_tires', 'diagnostic']

    @staticmethod
    def get_service_time(service):
        return len(TicketView.line_of_cars[service]) * TicketView.service_time[service]

    @staticmethod
    def get_total_time(ticket):
        total_time = 0
        for i in range(0, TicketView.service_menu.index(ticket) + 1):
            total_time += TicketView.get_service_time(TicketView.service_menu[i])
        return total_time

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        ticket = kwargs['ticket']
        context['ticket_number'] = TicketView.ticket_number
        minutes_to_wait = TicketView.get_total_time(ticket)
        context['minutes_to_wait'] = minutes_to_wait
        TicketView.line_of_cars[ticket].append(TicketView.ticket_number)

        TicketView.ticket_number += 1
        return context
