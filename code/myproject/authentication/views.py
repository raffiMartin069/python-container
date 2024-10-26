from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from authentication.forms import AuthenticationForm

class LoginView(FormView):
    
    template_name = 'login.html'
    form_class = AuthenticationForm
    success_url = reverse_lazy('success_url')
    
    def form_valid(request, form):
        email = form.cleaned_data['email']
        password = form.cleaned_data['password']

        return super().form_valid(form)