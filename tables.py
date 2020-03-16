from django.utils.html import format_html

import django_tables2 as tables
from django_tables2.utils import A

from .models import Device

class DeviceTable(tables.Table):
    manufacturer = tables.LinkColumn("all_by_manufacturer", args=[A("manufacturer.id")])
    selection = tables.CheckBoxColumn(accessor="pk", orderable=False)

    class Meta:
        model = Device
        exclude = ('id',)
        
        # template_name = "django_tables2/semantic.html"
    
    # def render_manufacturer(self, value):
    #     return format_html('<a href="""{% url "manufacturer" value.id %}""">{}</a>', value)