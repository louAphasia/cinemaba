from django import forms


class ConfirmMail(forms.Form):
    Email = forms.EmailField()

    def __str__(self):
        return self.Email