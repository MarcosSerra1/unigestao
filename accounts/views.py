from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse_lazy
from django.views.generic import FormView, RedirectView
from django.shortcuts import redirect


class LoginView(FormView):
    template_name = 'accounts/login.html'
    form_class = AuthenticationForm
    success_url = reverse_lazy('cars_list')

    def form_valid(self, form):
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(self.request, username=username, password=password)
        if user is not None:
            login(self.request, user)
            return redirect(self.get_success_url())
        else:
            return self.form_invalid(form)


class LogoutView(RedirectView):
    pattern_name = 'login'

    def get(self, request, *args, **kwargs):
        logout(request)
        return super().get(request, *args, **kwargs)
