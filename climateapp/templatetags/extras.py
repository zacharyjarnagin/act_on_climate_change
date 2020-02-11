from django import template
from ..models import Politician

register = template.Library()


@register.filter(name='get_by_state')
def get_by_state(state):
    """get all models based on state"""
    if state == '':
        return Politician.objects.all()
    return Politician.objects.filter(state=state)


register.filter('get_by_state', get_by_state)
