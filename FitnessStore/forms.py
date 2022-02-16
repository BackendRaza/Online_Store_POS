from django import forms
from FitnessStore.models import Person, custinfo


class PersonForm(forms.ModelForm):  
    class Meta:  
        model = Person  
        fields = "__all__"
    
'''class loginForm(forms.ModelForm):
    class Meta:
        model = userLogin
        fields = "__all__"'''

class custregister(forms.ModelForm):
    class Meta:
        model = custinfo
        fields = "__all__"