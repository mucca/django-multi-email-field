import os
import re

from django import forms
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

from multi_email_field.widgets import MultiEmailWidget


class MultiEmailField(forms.Field):
    message = _('Enter valid email addresses.')
    code = 'invalid'
    widget = MultiEmailWidget

    separator = os.linesep

    def __init__(self, **kwargs):
        if 'separator' in kwargs:
            self.separator = kwargs['separator']
            del kwargs['separator']
        return super(MultiEmailField, self).__init__(**kwargs)

    def to_python(self, value):
        "Normalize data to a list of strings."
        # Return None if no input was given.
        if not value:
            return []

        return [re.sub(r'[\s]*', "", v)  for v in value.split(self.separator) if re.sub(r'[\s]*', "", v)  != ""]

    def validate(self, value):
        "Check if value consists only of valid emails."

        # Use the parent's handling of required fields, etc.
        super(MultiEmailField, self).validate(value)
        try:
            for email in value:
                validate_email(email)
        except ValidationError:
            raise ValidationError(self.message, code=self.code)
