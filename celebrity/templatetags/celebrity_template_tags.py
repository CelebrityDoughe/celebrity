# -*- coding: utf-8 -*-
from django import template
from django.forms.widgets import CheckboxInput, RadioInput, TextInput, FileInput


register = template.Library()


@register.filter
def label_as_placeholder(field):
    """
    Set label as placeholder
    """
    if isinstance(field.field.widget, TextInput):
        return field.as_widget(attrs={'placeholder': field.label})
    return field.as_widget()


@register.filter
def add_attrs(field, attrs_str):
    """
    Add attribute to the html tag.
    Exclude checkbox and radiobox
    """
    # exclude widgets
    exclude_widgets = (CheckboxInput, RadioInput, FileInput,)
    for widget in exclude_widgets:
        if isinstance(field.field.widget, widget):
            return field.as_widget()

    attrs = {}
    for attr in attrs_str.split(';'):
        attr_name, attr_value = attr.split(':')
        attrs[attr_name] = attr_value
    return field.as_widget(attrs=attrs)
