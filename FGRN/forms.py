from django import forms
#from .models import GRN, GRNItem
from .models import *


class FGRNForm(forms.ModelForm):
    
    
    class Meta:
   
        model = FGRN
        fields = ['FGRN_no','date','recieved_from', 'recieved_by']
   
class FGRNItemForm(forms.ModelForm):
    
    item_name = forms.CharField(
        widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Item Name'})
    )
    quantity = forms.IntegerField(
        widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'quantity'})
    )
    remarks = forms.CharField(
        required = False,
        widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Add Description'})
    )
    class Meta:
   
        model = FGRN_item
        fields = ['item_name','quantity','remarks']
       