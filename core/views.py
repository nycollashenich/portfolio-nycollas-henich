from django.shortcuts import render
from django.views.generic import FormView, ListView
from .models import Project
from .forms import ContactMe
from django.core.mail import send_mail
from django.urls import reverse_lazy

class IndexView(ListView, FormView):
    template_name = 'index.html'
    model = Project
    context_object_name = 'projects'
    form_class = ContactMe
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        message = "{name} / {email} said: ".format(
            name=form.cleaned_data.get('name'),
            email=form.cleaned_data.get('email')
        )
        message += "\n\n{0}".format(form.cleaned_data.get('message'))

        send_mail(
            subject=form.cleaned_data.get('subject').strip(),
            message=message,
            from_email='portifoliohenichteste@gmail.com',
            recipient_list=['nhhenich@gmail.com'], 
        )

        return super().form_valid(form)