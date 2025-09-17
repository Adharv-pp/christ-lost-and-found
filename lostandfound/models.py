# lostandfound/models.py
from django.db import models
from django.utils import timezone

class Category(models.Model):
    name = models.CharField(max_length=100)
    # This allows for nested categories (e.g., Electronics -> Phone)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    class Meta:
        # Ensures better naming in the admin panel
        verbose_name_plural = "Categories"

    def __str__(self):
        # Shows the full path, e.g., "Electronics > Phone"
        full_path = [self.name]
        k = self.parent
        while k is not None:
            full_path.append(k.name)
            k = k.parent
        return ' > '.join(full_path[::-1])


class LostItem(models.Model):
    # Defining choices for fields
    LOCATION_CHOICES = [
        ('library', 'Library'),
        ('cafeteria', 'Cafeteria'),
        ('quad', 'Main Quad'),
        ('audi', 'Auditorium'),
        ('other', 'Other'),
    ]
    STATUS_CHOICES = [
        ('lost', 'Lost'),
        ('found', 'Found'),
        ('claimed', 'Claimed'),
    ]

    item_name = models.CharField(max_length=200)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    location = models.CharField(max_length=50, choices=LOCATION_CHOICES)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='lost')
    reported_on = models.DateTimeField(default=timezone.now)
    # For now, simple text fields. Later, this could be a ForeignKey to a Student model.
    reported_by = models.CharField(max_length=100, help_text="Your Name / Student ID")

    def __str__(self):
        return f"{self.item_name} (Lost in {self.get_location_display()})"