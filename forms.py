from django import forms

from .models import Manufacturer, Model, Device

class SelectManufacturer(forms.Form):
    manufacturer = forms.ModelChoiceField(Manufacturer.objects.all(), label="Производитель")

class SelectModel(forms.Form):
    manufacturer = forms.ModelChoiceField(Model.objects.all(), label="Модель")

class selectDevice(forms.ModelForm):
    class Meta:
        model = Device
        fields = ('manufacturer', 'model', 'serial_number', 'delivery_year')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['model'].queryset = Model.objects.none()
        
        # if 'manufacturer' in self.data:
        #     self.fields['serial_number'].label = "fsdfsdfsdf"
            # self.fields['model'].queryset = Model.objects.all()
        #     try:
        #         model_id = int(self.data.get('model'))
        #         self.fields['model'].queryset = Model.objects.filter(manufacturer=manufacturer).order_by('model')
        #     except (ValueError, TypeError):
        #         pass  # invalid input from the client; ignore and fallback to empty City queryset
        # elif self.instance.pk:
        
        #     self.fields['model'].queryset = self.instance.model.manufacturer.order_by('name')
            