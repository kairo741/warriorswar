from django.urls import path

from users.views import UserCreate
from .views import Index
from .views import CidadeCreate, PessoaCreate
from .views import CidadeUpdate, PessoaUpdate

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('register/cidade', CidadeCreate.as_view(), name='register-cidade'),
    path('register/pessoa', PessoaCreate.as_view(), name='register-pessoa'),
    path('register/user', UserCreate.as_view(), name='register-user'),
    path('edit/cidade/<int:pk>', CidadeUpdate.as_view(), name='edit-cidade'),
    path('edit/pessoa/<int:pk>', PessoaUpdate.as_view(), name='edit-pessoa'),
]
