from django.db import models

# Create your models here.
Category_choice = [
    ("EC", "Electronics"),
    ("KA", "Kitchen Appliances"),
    ("BF", "Bedroom Furniture"),
    ("HD", "Home Decor"),
    ("OE", "Outdoor Equipment"),
    ("CA", "Clothing & Accessories"),
    ("BP", "Beauty & Personal Care"),
    ("SF", "Sports & Fitness"),
    ("BS", "Books & Stationery"),
    ("TG", "Toys & Games")
]

class Category(models.Model):
    name =models.TextField(max_length=50)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    category = models.CharField(max_length=2, choices=Category_choice)
    image = models.ImageField(upload_to='category_images/', blank=True, null=True)
    # Add more relevant fields as needed    

    def __str__(self) -> str:
        return Category.name