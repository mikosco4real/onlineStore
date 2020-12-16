from django.shortcuts import render
from django.views import View

# Create your views here.
class home(View):
    template_name = 'home.html'

    def get(self, request):
        args = {'name': "Michael Okolo"}
        
        return render(request, self.template_name, args)

    def post(self, request):
        pass