# -*- coding: utf-8 -*-

from django import template
from django.contrib.auth.models import Group

register = template.Library()

# -----------------------------------------------------------------------------
# Inclusion Tags
# -----------------------------------------------------------------------------


@register.inclusion_tag("customadmin/partials/list_boolean.html")
def show_check(value):
    return {"bool_val": value}


@register.inclusion_tag("customadmin/partials/list_lock.html")
def show_lock(value):
    return {"bool_val": value}


@register.inclusion_tag("customadmin/partials/input_datetime_bootstrap.html")
def input_datetime_bs(field, show_label=True, disabled=False, auto_now=True):
    """Return HTML markup for a datetime input."""
    return {
        "field": field,
        "show_label": show_label,
        "disabled": disabled,
        "auto_now": auto_now,
    }

@register.inclusion_tag("customadmin/partials/input_date_bootstrap.html")
def input_date_bs(field, show_label=True, disabled=False):
    """Return HTML markup for a date input."""
    return {"field": field, "show_label": show_label, "disabled": disabled}


@register.inclusion_tag("customadmin/partials/input_icheck.html")
def input_icheck(field):
    """Return HTML markup for a icheck checkbox."""
    return {"field": field}


@register.inclusion_tag("customadmin/partials/input_upload_video.html")
def input_upload_video(field, preview=True, mime_types="video/mp4"):
    """Return HTML markup for a video upload input."""
    return {"field": field, "preview": preview, "mime_types": mime_types}


@register.inclusion_tag("customadmin/partials/input_upload_image.html")
def input_upload_image(field, mime_types="image/jpg,image/jpeg,image/png"):
    """Return HTML markup for a image upload input."""
    return {"field": field, "mime_types": mime_types}


@register.inclusion_tag("customadmin/partials/input_upload_file.html")
def input_upload_file(field, mime_types="image/jpg,image/jpeg,image/png,video/mp4"):
    """Return HTML markup for a file upload input."""
    return {"field": field, "mime_types": mime_types}


@register.inclusion_tag("customadmin/partials/bulk_actions.html")
def bulk_actions(name):
    """Return HTML markup for table bulk actions."""
    return {"action_item": name}


@register.inclusion_tag("customadmin/partials/input_trix.html")
def input_trix(field):
    """Return HTML markup for a trix editor. https://github.com/basecamp/trix"""
    return {"field": field}


@register.inclusion_tag("customadmin/partials/input_colorpicker.html")
def input_colorpicker(field):
    """Return HTML markup for a color picker."""
    return {"field": field}


@register.inclusion_tag("customadmin/partials/input_readonly.html")
def input_readonly(field):
    """Return HTML markup for a readonly input."""
    return {"field": field}


@register.inclusion_tag("customadmin/partials/read_only.html")
def readonly(label, value):
    """Return HTML markup for a readonly display like a form input."""
    return {"label": label, "value": value}


@register.inclusion_tag("customadmin/partials/input_group_typeahead.html")
def input_group_typeahead(field, icon_class=None):
    """Return HTML markup for a input group."""
    return {"field": field, "icon_class": icon_class}


# -----------------------------------------------------------------------------
# Filters
# -----------------------------------------------------------------------------


# @register.filter
# def has_perm(user, perm):
#     if user.is_authenticated:
#         if user.is_superuser or user.is_staff or user.has_perm(perm):
#             return True
#         return False
#     return False


# @register.filter
# def has_group(user, group_name):
#     try:
#         group = Group.objects.get(name=group_name)
#     except Group.DoesNotExist:
#         return False
#     if group in user.groups.all():
#         return True
#     return False
