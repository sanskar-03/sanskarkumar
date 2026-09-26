from django import template


register = template.Library()


@register.filter
def get_field(value, field_name):
    if value is None:
        return ""
    try:
        result = getattr(value, field_name)
    except AttributeError:
        return ""
    if callable(result):
        try:
            return result()
        except TypeError:
            return ""
    return result


@register.filter
def pretty_value(value):
    if value in {True, False}:
        return "Yes" if value else "No"
    return value if value not in (None, "") else "—"
