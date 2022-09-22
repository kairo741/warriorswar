from django.urls import path

from users.views import UserCreate
from .views import Index
from .views import SpriteCreate, PessoaCreate
from .views import CidadeUpdate, PessoaUpdate

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('register/sprite', SpriteCreate.as_view(), name='register-sprite'),
    path('register/pessoa', PessoaCreate.as_view(), name='register-pessoa'),
    path('register/user', UserCreate.as_view(), name='register-user'),
    path('edit/cidade/<int:pk>', CidadeUpdate.as_view(), name='edit-cidade'),
    path('edit/pessoa/<int:pk>', PessoaUpdate.as_view(), name='edit-pessoa'),
]
