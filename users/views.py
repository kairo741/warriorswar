from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from users.forms import UserForm


class UserCreate(CreateView):
    form_class = UserForm
    template_name = 'register/register_account.html'
    success_url = reverse_lazy('index')
