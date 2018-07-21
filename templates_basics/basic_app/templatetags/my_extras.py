from django import template

register = template.Library()

#alternate format to registering the custom template tagging
@register.filter(name='cut')

def cut(value,arg):
    """
    This cuts out all values of arg from the string
    """
    return value.replace(arg,'')

# register.filter('cut',cut)
# format for register.filter(word that will be used in html file for template tagging, name of function)
