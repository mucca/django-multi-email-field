import os
import six

from django.forms.widgets import Textarea
from django.core.exceptions import ValidationError
from django.core import validators

MULTI_EMAIL_FIELD_EMPTY_VALUES = validators.EMPTY_VALUES + ('[]', )


class MultiEmailWidget(Textarea):

    is_hidden = False
    separator = os.linesep

    def __init__(self, **kwargs):
        if 'separator' in kwargs:
            self.separator = kwargs['separator']
            del kwargs['separator']
        return super(MultiEmailWidget, self).__init__(**kwargs)

    def prep_value(self, value):
        """ Prepare value before effectively render widget """
        if value in MULTI_EMAIL_FIELD_EMPTY_VALUES:
            return ""
        elif isinstance(value, six.string_types):
            return value
        elif isinstance(value, list):
            return self.separator.join(value)
        raise ValidationError('Invalid format.')

    def render(self, name, value, attrs=None):
        value = self.prep_value(value)
        return super(MultiEmailWidget, self).render(name, value, attrs)
