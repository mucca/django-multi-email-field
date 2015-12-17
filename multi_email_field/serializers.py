import os

from multi_email_field import forms
from multi_email_field import widgets
from multi_email_field import fields


from rest_framework.serializers import CharField
from rest_framework.serializers import ModelSerializer


class MultiEmailField(CharField):

    type_name = 'CharField'
    form_field_class = forms.MultiEmailField
    widget = widgets.MultiEmailWidget

    def __init__(self, max_length=None, min_length=None, separator=os.linesep, *args, **kwargs):
        self.separator = separator
        super(MultiEmailField, self).__init__(*args, **kwargs)

    def to_native(self, value):
        if isinstance(value, str):
            return value
        elif isinstance(value, type([])):
            return '{} '.format(self.separator).join(value)
        return value

    def validate(self, value):
        super(MultiEmailField, self).validate(value)
        form = self.form_field_class(separator=self.separator)
        form.validate(form.to_python(value))


ModelSerializer.field_mapping.update({fields.MultiEmailField: MultiEmailField})
