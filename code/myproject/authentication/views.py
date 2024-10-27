from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from authentication.forms import AuthenticationForm, SignUpForm
from authentication.models import Authentication

class LoginView(FormView):
    
    template_name = 'login.html'
    form_class = AuthenticationForm
    success_url = reverse_lazy('success_url')
    
    def form_valid(self, form):

        email = form.cleaned_data['email']
        password = form.cleaned_data['password']

        model = Authentication(email, password)
        user_exist = model.get_user_credentials()

        if not user_exist:
            form.add_error(None, model.user_not_exist())
            return self.form_invalid(form)

        return HttpResponse(model.user_exist())

class SignUpView(FormView):

    template_name = 'signup.html'
    form_class = SignUpForm
    success_url = reverse_lazy('success_url')

    def form_valid(self, form):
        email = form.cleaned_data['email']
        password = form.cleaned_data['password']
        return super().form_valid(form)