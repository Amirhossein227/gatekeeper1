from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import PasswordChangeForm
from core.models import UserAccount, Subscription


class UserEmailChangeForm(forms.ModelForm):
    class Meta:
        model = UserAccount
        fields = ['email']

    old_password = forms.CharField(
        label='Current Password',
        widget=forms.PasswordInput(attrs={
            'class': 'form-control form-control-lg form-control-solid',
            'id': 'confirmemailpassword',
            'autocomplete': 'off',
        })
    )

    def clean_old_password(self):
        old_password = self.cleaned_data.get('old_password')
        user = self.instance
        if not user.check_password(old_password):
            raise forms.ValidationError('Incorrect password')
        return old_password

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['email'].widget.attrs.update({
            'class': 'form-control form-control-lg form-control-solid',
            'id': 'emailaddress',
            'autocomplete': 'off',
        })


class UserPasswordChangeForm(PasswordChangeForm):
    class Meta:
        model = UserAccount

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['old_password'].widget.attrs.update({
            'class': 'form-control form-control-lg form-control-solid',
            'id': "currentpassword",
            'autocomplete': "off",
        })

        self.fields['new_password1'].widget.attrs.update({
            'class': 'form-control form-control-lg form-control-solid',
            'id': "newpassword",
            'autocomplete': "off",
        })

        self.fields['new_password2'].widget.attrs.update({
            'class': 'form-control form-control-lg form-control-solid',
            'id': "confirmpassword",
            'autocomplete': "off",
        })


class UserCreationForm(UserCreationForm):
    class Meta:
        model = UserAccount
        fields = ("first_name", "last_name", "username", "email", "password1", "password2")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['first_name'].widget.attrs.update({
            'class': 'form-control form-control-lg form-control-solid',
            'placeholder': 'Name',
            'autocomplete': "off",
        })

        self.fields['last_name'].widget.attrs.update({
            'class': 'form-control form-control-lg form-control-solid',
            'placeholder': 'Name',
            'autocomplete': "off",
        })

        self.fields['username'].widget.attrs.update({
            'class': 'form-control form-control-lg form-control-solid',
            'placeholder': 'Username',
            'autocomplete': "off",
        })

        self.fields['email'].widget.attrs.update({
            'class': 'form-control form-control-lg form-control-solid',
            'placeholder': 'E-mail Address',
            'autocomplete': "off",
        })

        self.fields['password1'].widget.attrs.update({
            'class': 'form-control form-control-lg form-control-solid',
            'placeholder': 'Password',
            'autocomplete': "off",
        })

        self.fields['password2'].widget.attrs.update({
            'class': 'form-control form-control-lg form-control-solid',
            'placeholder': 'Repeat Password',
            'autocomplete': "off",
        })


class AdminUserCreationForm(UserCreationForm):
    class Meta:
        model = UserAccount
        fields = ("first_name", "last_name", "username", "email", "account_type")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['first_name'].widget.attrs.update({
            'class': 'form-control form-control-solid mb-3 mb-lg-0',
            'placeholder': 'Name',
            'autocomplete': "off",
        })

        self.fields['last_name'].widget.attrs.update({
            'class': 'form-control form-control-solid mb-3 mb-lg-0',
            'placeholder': 'Name',
            'autocomplete': "off",
        })

        self.fields['username'].widget.attrs.update({
            'class': 'form-control form-control-solid mb-3 mb-lg-0',
            'placeholder': 'Username',
            'autocomplete': "off",
        })

        self.fields['email'].widget.attrs.update({
            'class': 'form-control form-control-solid mb-3 mb-lg-0',
            'placeholder': 'E-mail Address',
            'autocomplete': "off",
        })

        self.fields['account_type'].widget.attrs.update({
            'class': 'form-check form-check-custom form-check-solid',
            'autocomplete': "off",
        })

        # Set password fields as not required
        self.fields['last_name'].required = False
        self.fields['password1'].required = False
        self.fields['password2'].required = False

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password('Gatekeeper2024@')  # Set a fixed password
        if commit:
            user.save()
        return user


class AdminUserEditForm(forms.ModelForm):
    class Meta:
        model = UserAccount
        fields = ("first_name", "last_name", "username", "email", "account_type", "is_active")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['first_name'].widget.attrs.update({
            'class': 'form-control form-control-solid mb-3 mb-lg-0',
            'placeholder': 'Name',
            'autocomplete': "off",
        })

        self.fields['last_name'].widget.attrs.update({
            'class': 'form-control form-control-solid mb-3 mb-lg-0',
            'placeholder': 'Name',
            'autocomplete': "off",
        })

        self.fields['username'].widget.attrs.update({
            'class': 'form-control form-control-solid mb-3 mb-lg-0',
            'placeholder': 'Username',
            'autocomplete': "off",
        })

        self.fields['email'].widget.attrs.update({
            'class': 'form-control form-control-solid mb-3 mb-lg-0',
            'placeholder': 'E-mail Address',
            'autocomplete': "off",
        })

        self.fields['account_type'].widget.attrs.update({
            'class': 'form-check form-check-custom form-check-solid',
            'autocomplete': "off",
        })

        self.fields['is_active'].widget.attrs.update({
            'class': 'form-check-input w-45px h-30px',
            'autocomplete': "off",
        })

        # Set password fields as not required
        self.fields['last_name'].required = False


class UserEditForm(forms.ModelForm):
    class Meta:
        model = UserAccount
        fields = ("first_name", "last_name", "username", "email")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['first_name'].widget.attrs.update({
            'class': 'form-control form-control-solid mb-3 mb-lg-0',
            'placeholder': 'Name',
            'autocomplete': "off",
        })

        self.fields['last_name'].widget.attrs.update({
            'class': 'form-control form-control-solid mb-3 mb-lg-0',
            'placeholder': 'Name',
            'autocomplete': "off",
        })

        self.fields['username'].widget.attrs.update({
            'class': 'form-control form-control-solid mb-3 mb-lg-0',
            'placeholder': 'Username',
            'autocomplete': "off",
        })

        self.fields['email'].widget.attrs.update({
            'class': 'form-control form-control-solid mb-3 mb-lg-0',
            'placeholder': 'E-mail Address',
            'autocomplete': "off",
        })

        # Set password fields as not required
        self.fields['last_name'].required = False
