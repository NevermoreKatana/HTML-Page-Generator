from django.views.generic.base import TemplateView
from django.views import View
from django.shortcuts import render
from page_generator.parser import pars_raw_data

class MainPageView(TemplateView):
    template_name = 'main.html'

class TestGenerationView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'test_generation.html')

    def post(self, request, *args, **kwargs):
        answer = request.POST.dict()
        answer = pars_raw_data(answer)

        return render(request, 'test.html', {'answer': answer})
