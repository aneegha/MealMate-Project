from django import template

register = template.Library()

@register.filter
def to_stars(value):
    """
    Converts a numeric value (0-5) into a range of numbers for star rendering.
    Example: 3 -> [1, 2, 3]
    We can't easily return complex objects, so we'll just return a range 
    and let the template handle filled/empty logic or just simple stars.
    
    Actually, a better approach for the template is to return a string of stars
    or a list of booleans like [True, True, True, False, False].
    Let's return a list where True=Full Star, False=Empty Star.
    """
    try:
        rating = float(value)
        stars = []
        for i in range(1, 6):
            if rating >= i:
                stars.append('full')
            elif rating >= i - 0.5:
                 stars.append('half')
            else:
                stars.append('empty')
        return stars
    except (ValueError, TypeError):
        return ['empty'] * 5
