from django.contrib import admin


from .models import Device, Manufacturer, Model, System, Objects, Responsible


# Register your models here.
class DeviceAdmin(admin.ModelAdmin):
    list_display = ('manufacturer', 'model', 'serial_number', 'delivery_year', 'system', 'to_object', 'responsible')
    list_display_links = ('serial_number',)
    search_fields = ('manufacturer', 'model', 'serial_number', 'delivery_year', 'system', 'to_object', 'responsible')
    list_select_related = True
admin.site.register(Device, DeviceAdmin)


class ManufacturerAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_display_links = ('name',)
    search_fields = ('name',)
admin.site.register(Manufacturer, ManufacturerAdmin)


class ModelAdmin(admin.ModelAdmin):
    list_display = ('manufacturer', 'model')
    list_display_links = ('manufacturer', 'model')
    search_fields = ('manufacturer', 'model')
admin.site.register(Model, ModelAdmin)


class SystemAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_display_links = ('name',)
    search_fields = ('name',)
admin.site.register(System, SystemAdmin)


class ObjectsAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_display_links = ('name',)
    search_fields = ('name',)
admin.site.register(Objects, ObjectsAdmin)


class ResponsibleAdmin(admin.ModelAdmin):
    list_display = ('FIO', 'Position')
    list_display_links = ('FIO',)
    search_fields = ('FIO', 'Position')
admin.site.register(Responsible, ResponsibleAdmin)





