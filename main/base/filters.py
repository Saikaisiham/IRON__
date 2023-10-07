from categories.models import Category
import django_filters

class CategoryFilter(django_filters.FilterSet):
    class Meta :
        model = Category
        fields = ['category_name']