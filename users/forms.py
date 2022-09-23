from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Column, Field, ButtonHolder, Div, HTML
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserForm(UserCreationForm):
    # password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ["first_name", "last_name", "username", "password1", "password2"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.helper = FormHelper()

        self.helper.layout = Layout(
            Row(
                Column(Field('first_name', css_class='form-control form-control-user'),
                       css_class='col-lg mb-0'),
                Column(Field('last_name', css_class='form-control form-control-user'),
                       css_class='col-lg mb-0'),
            ),
            Row(Column(Field('username', css_class='form-control form-control-user'),
                       css_class='col-lg mb-0'), ),
            Row(Column(Field('password1', css_class='form-control form-control-user'),
                       css_class='col-lg mb-0'), ),
            Row(Column(Field('password2', css_class='form-control form-control-user'),
                       css_class='col-lg mb-0'), ),
            ButtonHolder(
                Div(
                    HTML("""
                            <button type="submit" class="btn btn-primary btn-user btn-block">
                            Cadastrar
                            </button>
                        """),
                ))

        )
