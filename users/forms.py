from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Column, Field
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class UserForm(UserCreationForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ["first_name", "last_name", "email", "password1", "password2"]

    # template_name = 'register/register_account.html'
    # success_url = reverse_lazy('index')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.helper = FormHelper()

        self.helper.layout = Layout(
            Row(
                Column(Field('first_name', css_class='form-control form-control-user'),
                       css_class='col-lg mb-0'),
                Column(Field('last_name', css_class='form-control form-control-user'),
                       css_class='col-lg-4 mb-0'),
            ),
            Row(Column(Field('password1', css_class='form-control form-control-user'),
                       css_class='col-lg mb-0'), ),
            Row(Column(Field('password2', css_class='form-control form-control-user'),
                       css_class='col-lg mb-0'), )

            # Fieldset(
            #     'Endereço',
            #     Row(
            #         Column('cep', css_class='form-group col-lg mb-0'),
            #         Column('numero', css_class='form-group col-lg mb-0'),
            #         Column('bairro', css_class='form-group col-lg-4 mb-0'),
            #     ),
            #     Row(
            #         Column('rua', css_class='form-group col-lg mb-0'),
            #         Column('cidade', css_class='form-group col-lg mb-0'),
            #     ),
            #     css_class="mb-5"
            # ),
            # Fieldset(
            #     'Características do imóvel',
            #     Row(
            #         Column('tipo', css_class='form-group col-sm mb-0'),
            #
            #     ),
            #     Row(
            #         Column('quantidade_quartos', css_class='form-group col-lg mb-0'),
            #         Column('quantidade_banheiros', css_class='form-group col-lg mb-0'),
            #         Column('area', css_class='form-group col-sm mb-0'),
            #     ),
            #     css_class="mb-5",
            # ),
            # Fieldset(
            #     "Fotos do imóvel",
            #     Column('fotos', css_class='form-group col-sm mb-0'),
            #     css_class="mb-5",
            # ),
            # ButtonHolder(
            #     Div(
            #         HTML("""
            #             <button type="submit" class="btn btn-lg btn-success w-100 fs-4">
            #                 Salvar
            #             </button>
            #         """),
            #         css_class="w-50 mx-auto"
            #     ),
            # )
        )
