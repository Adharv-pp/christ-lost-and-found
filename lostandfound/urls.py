# lostandfound/urls.py
from django.urls import path
from . import views

urlpatterns = [
    # Main page showing the list of items
    path('', views.list_items, name='list_items'),
    
    # URL to trigger the claim action for a specific item
    path('claim/<int:item_id>/', views.claim_item, name='claim_item'),
    
    # You would add URLs for reporting and viewing details here
    # path('report/', views.report_lost_item, name='report_item'),
    # path('item/<int:item_id>/', views.item_detail, name='item_detail'),
]