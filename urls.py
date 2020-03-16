from django.urls import path

from .views import index, all_by_manufacturer, load_models

urlpatterns = [
    path('', index, name='index'),
    path('<int:manufacturer_id>', all_by_manufacturer, name='all_by_manufacturer'),
    path('ajax/load-models/', load_models, name='ajax_load_models'),
]
