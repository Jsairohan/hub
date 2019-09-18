from django import template

register = template.Library()

@register.filter()
def to_int(value):
    return int(value)

@register.filter(name='split')
def split(value, key):
    print "ddsdss"
    """
        Returns the value turned into a list.
    """
    return value.split(key)

@register.filter(name = "zipping")
def zipping(value,key):
    print value,key
    value =value.split(",")
    key = key.split(",")

    return zip(value,key)
