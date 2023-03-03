from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View


class TestView(View):
    template_name = "blank.html"

    def get(self, request, *args, **kwargs):
        messages.warning(request, 'Your account is about to expire.')

        return render(request, self.template_name, {"a": 2})
