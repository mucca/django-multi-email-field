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

# class CharField(WritableField):
#     type_name = 'CharField'
#     type_label = 'string'
#     form_field_class = forms.CharField

#     def __init__(self, max_length=None, min_length=None, *args, **kwargs):
#         self.max_length, self.min_length = max_length, min_length
#         super(CharField, self).__init__(*args, **kwargs)
#         if min_length is not None:
#             self.validators.append(validators.MinLengthValidator(min_length))
#         if max_length is not None:
#             self.validators.append(validators.MaxLengthValidator(max_length))

#     def from_native(self, value):
#         if isinstance(value, six.string_types) or value is None:
#             return value
#         return smart_text(value)


ModelSerializer.field_mapping.update({fields.MultiEmailField: MultiEmailField})
