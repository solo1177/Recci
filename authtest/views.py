from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

# Create your views here.


from django.contrib.auth.forms import UserCreationForm

from django.urls import reverse_lazy

from django.views.generic import CreateView

 
from django.contrib.auth import login
from django.http import HttpResponseRedirect


class SignUpView(CreateView):

    form_class = UserCreationForm

    success_url = reverse_lazy('Top')

    template_name = 'authtest/signup.html'

    def form_valid(self, form):
        user = form.save() # formの情報を保存
        login(self.request, user) # 認証
        self.object = user 
        return HttpResponseRedirect(self.get_success_url()) 


    

