# lostandfound/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import LostItem
from .lostfound_utils import get_category_breadcrumb # Import our recursive function

# **FUNCTION CONCEPT**: Each view is a function that handles a specific web request.

def list_items(request):
    """
    This view lists all lost items and handles filtering and sorting.
    """
    items = LostItem.objects.filter(status='lost')
    locations = LostItem.LOCATION_CHOICES
    
    # **COMPREHENSION CONCEPT**: Filtering items by location.
    location_filter = request.GET.get('location')
    if location_filter:
        # This is a more efficient Django way:
        # items = items.filter(location=location_filter) 
        
        # But to specifically demonstrate a list comprehension as requested:
        all_items = list(items)
        items = [item for item in all_items if item.location == location_filter]

    # **LAMBDA CONCEPT**: Sorting items by date.
    sort_order = request.GET.get('sort', 'desc')
    # While Django's items.order_by('-reported_on') is more efficient,
    # we use a lambda here to meet the specific requirement.
    if sort_order == 'asc':
        items = sorted(items, key=lambda item: item.reported_on)
    else: # Default to descending (newest first)
        items = sorted(items, key=lambda item: item.reported_on, reverse=True)

    context = {
        'items': items,
        'locations': locations,
        'current_location': location_filter,
    }
    return render(request, 'lostandfound/list_items.html', context)


def report_lost_item(request):
    """
    **FUNCTION CONCEPT**: A function to handle the logic for reporting a new item.
    (This would typically be a Django Form, but we'll keep it simple for this example.)
    """
    # This view would be expanded to handle a POST request with form data.
    # For now, it just renders the page.
    return render(request, 'lostandfound/report_form.html')


def claim_item(request, item_id):
    """
    **FUNCTION CONCEPT**: A function to handle the action of claiming an item.
    """
    item = get_object_or_404(LostItem, id=item_id)
    item.status = 'claimed'
    item.save()
    return redirect('list_items') # Redirect back to the main list

# Example of how to use the recursive function in a view (e.g., on an item detail page)
def item_detail(request, item_id):
    item = get_object_or_404(LostItem, id=item_id)
    # Using the recursive function from our custom module
    breadcrumb = get_category_breadcrumb(item.category)
    breadcrumb_str = ' > '.join(breadcrumb)
    
    context = {
        'item': item,
        'breadcrumb': breadcrumb_str,
    }
    return render(request, 'lostandfound/item_detail.html', context)