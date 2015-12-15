Field and widget to store a list of e-mail addresses in a `Django <https://www.djangoproject.com>`_ projects.

It provides:

* A form field and a form widget to edit a list of e-mails in a Django form;
* A model field to store the captured list of e-mails with custom separator;

==================
COMPATIBILITY
==================

* Python 2.6/2.7/3.2/3.3/3.4
* Django 1.4/1.5/1.6/1.7

==================
USAGE
==================

* Add ``multi_email_field`` to your ``INSTALLED_APPS``:

::

    # settings.py
    INSTALLED_APPS = (
    ...
    'multi_email_field',
    )

* Use provided form field and widget:

::

    # forms.py
    from django import forms
    from multi_email_field.forms import MultiEmailField

    class SendMessageForm(forms.Form):
        emails = MultiEmailField([, separator='string'])

==================
IN YOUR MODELS
==================

If you wan to store list of e-mails, you can use this:

::

    from django.db import models
    from multi_email_field.fields import MultiEmailField

    class ContactModel(models.Model):
        emails = MultiEmailField([, separator='string'])


==================
AUTHORS
==================

    * Ivan Bettarini <ivan.bettarini@gmail.com>

    * forked from https://github.com/fle/django-multi-email-field

    * by Florent Lebreton <florent.lebreton@makina-corpus.com>


