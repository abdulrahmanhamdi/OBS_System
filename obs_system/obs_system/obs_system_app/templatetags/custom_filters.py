from django import template

register = template.Library()

@register.filter
def get_component_score(components, component_name):
    for comp in components:
        if comp.grade_component.name.lower() == component_name.lower():
            return comp.score
    return None
