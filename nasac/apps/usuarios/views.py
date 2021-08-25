from django.shortcuts import render
from django.views.generic import CreateView
from django.urls import reverse_lazy
# Create your views here.


class SignUpView(CreateView):
    model = Usuario
    form_class = SignUpForm
    template_name="registrar.html"
    success_url = reverse_lazy('home')