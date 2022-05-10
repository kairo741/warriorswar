from django.urls import path
from .views import Index
from .views import CidadeCreate, PessoaCreate
from .views import CidadeUpdate, PessoaUpdate

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('register/cidade', CidadeCreate.as_view(), name='register-cidade'),
    path('register/pessoa', PessoaCreate.as_view(), name='register-pessoa'),
    path('edit/cidade/<int:pk>', CidadeUpdate.as_view(), name='edit-cidade'),
    path('edit/pessoa/<int:pk>', PessoaUpdate.as_view(), name='edit-pessoa'),
]
