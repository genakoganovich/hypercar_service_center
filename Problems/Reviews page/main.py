from django.shortcuts import render
from django.views import View


class ReviewView(View):
    reviews = ['review1', 'review2', 'review3']  # List of reviews as plain strings

    def get(self, request, *args, **kwargs):
        return render(request, "book/reviews.html", context={'reviews': self.reviews})
