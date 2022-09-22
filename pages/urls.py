from django.urls import path

from users.views import UserCreate
from .views import Index
from .views import SpriteCreate, ElementCreate, EquipmentCreate, SpellCreate
from .views import SpriteUpdate, ElementUpdate, EquipmentUpdate, SpellUpdate
from .views import ElementDelete, EquipmentDelete
from .views import ElementList, EquipmentList

urlpatterns = [
    path('', Index.as_view(), name='index'),
    # ----------------- USER -----------------
    path('register/user', UserCreate.as_view(), name='register-user'),
    # ----------------- SPRITE -----------------
    path('register/sprite', SpriteCreate.as_view(), name='register-sprite'),
    path('edit/sprite/<int:pk>', SpriteUpdate.as_view(), name='edit-sprite'),
    # ----------------- ELEMENT -----------------
    path('register/element', ElementCreate.as_view(), name='register-element'),
    path('edit/element/<int:pk>', ElementUpdate.as_view(), name='edit-element'),
    path('list/element', ElementList.as_view(), name='list-element'),
    path('delete/element/<int:pk>', ElementDelete.as_view(), name='delete-element'),
    # ----------------- EQUIPMENT -----------------
    path('register/equipment', EquipmentCreate.as_view(), name='register-equipment'),
    path('edit/equipment/<int:pk>', EquipmentUpdate.as_view(), name='edit-equipment'),
    path('list/equipment', EquipmentList.as_view(), name='list-equipment'),
    path('delete/equipment/<int:pk>', EquipmentDelete.as_view(), name='delete-equipment'),
    # ----------------- SPELL -----------------
    path('register/spell', SpellCreate.as_view(), name='register-spell'),
    path('edit/spell/<int:pk>', SpellUpdate.as_view(), name='edit-spell'),
    # ----------------- EFFECT -----------------
    path('register/effect', SpellCreate.as_view(), name='register-effect'),
    path('edit/effect/<int:pk>', SpellUpdate.as_view(), name='edit-effect'),

]
