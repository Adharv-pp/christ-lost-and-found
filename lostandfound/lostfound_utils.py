# lostandfound/lostfound_utils.py

def get_category_breadcrumb(category):
    """
    **RECURSION CONCEPT**
    Traces the parent categories of a given category to create a breadcrumb trail.
    e.g., [Electronics, Phones, iPhone]
    """
    if category is None:
        return []
    
    # Base Case: The category has no parent.
    if category.parent is None:
        return [category.name]
    
    # Recursive Step: Call the function on the parent and append the current category name.
    return get_category_breadcrumb(category.parent) + [category.name]