from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth.models import Group
from users.forms import UserForm


class UserCreate(CreateView):
    form_class = UserForm
    template_name = 'register/register_account.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        url = super().form_valid(form)
        user_group = Group.objects.get_or_create(name="summoners")
        self.object.groups.add(user_group[0])
        self.object.save()
        return url
