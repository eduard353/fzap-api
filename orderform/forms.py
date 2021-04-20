from django import forms
from .models import Order, Model, Mark
from datetime import datetime


class OrderForm(forms.Form):
    mark = forms.ModelChoiceField(queryset=Mark.objects.all())
    model = forms.ModelChoiceField(queryset=Model.objects.filter(mark__in=Mark.objects.filter(mark_name=mark)))
    year = forms.ChoiceField(choices=[(i, str(i)) for i in range(1900, int(datetime.now().year)+1, 1)])
    vin = forms.CharField()
    order_details = forms.CharField()
    # class Meta:
    #     model = Order
    #     fields = ['model', 'year', 'vin', 'order_details',]
    #     # widgets = {'year': forms.DateInput(format='%d/%m/%Y')}


    # def __init__(self, *args, **kwargs):
    #     super(OrderForm, self).__init__(*args, **kwargs)
    #     if hasattr(kwargs, 'model_ids'):
    #         self.fields['model'].queryset = Model.objects.filter(model__id__in=kwargs.get('model_ids'))
    #     else:
    #         self.fields['model'].queryset = Model.objects.all()

class MarkForm(forms.ModelForm):
    class Meta:
        model = Model
        fields = ["mark"]
        #widgets = {'mark_name': forms.CheckboxInput, }

# class EmailPostForm(forms.Form):
#     name = forms.CharField(max_length=25)
#     email = forms.EmailField()
#     to = forms.EmailField()
#     comments = forms.CharField(required=False, widget=forms.Textarea)
