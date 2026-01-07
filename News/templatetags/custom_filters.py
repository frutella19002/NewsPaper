import re
from django import template

register = template.Library()

BAD_WORDS = [
    'редиска',
]

@register.filter(name='censor')
def censor(value):
    if not isinstance(value, str):
        raise ValueError('Фильтр censor применяется только к строкам')

    result = value

    for word in BAD_WORDS:
        pattern = re.compile(rf'\b{word}\b', re.IGNORECASE)
        def replace(match):
            w = match.group()
            return w[0] + '*' * (len(w) - 1)

        result = pattern.sub(replace, result)

    return result