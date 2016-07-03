# import random
# from django import forms
# from django.contrib.auth.models import User
# from django.contrib.auth.forms import UserCreationForm, UserChangeForm
# from website.models import ItemCategories
# from django.forms import ModelForm, CharField, TextInput, Select
# from website.models import CustomUser, ShipprBooking, ShippingAddress
# from django.contrib.auth import authenticate

# class LoginForm(forms.Form):
#     username = forms.EmailField(max_length=255, required=True)
#     password = forms.CharField(widget=forms.PasswordInput, required=True)

#     def clean(self):
#         username = self.cleaned_data.get('username')
#         password = self.cleaned_data.get('password')
#         user = authenticate(username=username, password=password)
#         if not user or not user.is_active:
#             raise forms.ValidationError("Sorry, that login was invalid. Please try again.")
#         return self.cleaned_data

#     def login(self, request):
#         username = self.cleaned_data.get('username')
#         password = self.cleaned_data.get('password')
#         user = authenticate(username=username, password=password)
#         return user

# class CustomUserCreationForm(UserCreationForm):
#     """
#     A form that creates a user, with no privileges, from the given email and
#     password.
#     """

#     def __init__(self, *args, **kargs):
#         super(CustomUserCreationForm, self).__init__(*args, **kargs)
#         del self.fields['username']

#     class Meta:
#         model = CustomUser
#         fields = ("email","name")

# class CustomUserChangeForm(UserChangeForm):
#     """A form for updating users. Includes all the fields on
#     the user, but replaces the password field with admin's
#     password hash display field.
#     """

#     def __init__(self, *args, **kargs):
#         super(CustomUserChangeForm, self).__init__(*args, **kargs)
#         del self.fields['username']

#     class Meta:
#         model = CustomUser

# class UserRegistrationForm(UserCreationForm):
#     email = forms.EmailField(required=True)
#     name = forms.CharField(required=True)
#     class Meta:
#         model = User
#         fields = ('email','name','password1','password2')

#     def save(self, commit=True) :
#         user = super(UserCreationForm,self).save(commit=False)
#         user.email = self.cleaned_data['email']
#         user.name = self.cleaned_data['name']

#         if commit:
#             user.save()
#         return user

# # class BookingAddressForm(forms.Form) :


# class SearchShipprForm(forms.Form):
#     ### TODO: Add proper classes and other attributes if required.
#     fromLoc = forms.CharField(max_length=100,required=True, label = 'Pick up location',
#         widget=TextInput(attrs={'class':'source input-icon',
#             'onkeyup':'suggestSource()'}))
#     toLoc = forms.CharField(max_length=100,required=True, label = 'Delivery location',
#         widget=TextInput(attrs={'class':'destination input-icon',
#             'onkeyup':'suggestDestination()'}))
#     pickupDate = forms.CharField(required=True, label = 'Pick up date',
#         widget=TextInput(attrs={'class':' datepicker-input','data-date-format':'dd/mm/yyyy'}))
#     itemName = forms.CharField(max_length=200, required=True , label = 'Item Name',
#         widget=TextInput(attrs={'class':' cube'}))

#     ### TODO: Load categories with ModelChoiceField
#     category = forms.ChoiceField(initial='1',label = 'Category',required=True)
#     dimensionUnit = forms.ChoiceField(initial='1', label='Dimensions',required=True, choices=(('1', 'Inches',), ('2', 'CM',)))
#     length = forms.CharField(required=True, label = '',
#      widget=TextInput(attrs={'type':'number','placeholder':'Length','class':'length','step':'any'}))
#     breadth = forms.CharField( required=True, label = '',
#      widget=TextInput(attrs={'type':'number','placeholder':'Breadth','step':'any'}))
#     height = forms.CharField( required=True, label = '',
#      widget=TextInput(attrs={'type':'number','placeholder':'Height','step':'any'}))
#     value = forms.CharField( widget=TextInput(attrs={'type':'number'}), label = 'Invoice Value')
#     itemUnit = forms.CharField( widget=TextInput(attrs={'type':'number'}), label = 'Number of items')
#     weight = forms.CharField( widget=TextInput(attrs={'type':'number','step':'any'}), label = 'Weight')

#     def __init__(self, *args, **kwargs):
#         custom_choices = ItemCategories.objects.all().values_list('id','name')
#         super(SearchShipprForm, self).__init__(*args, **kwargs)
#         if custom_choices:
#             self.fields['category'].choices = custom_choices

#     def clean_itemName(self):
#         if(self.cleaned_data.get('itemName', '').endswith('abc')):
#             raise forms.ValidationError("Invalid item name.")

#         return self.cleaned_data.get('itemName', '')

# class ShipprBookingForm(forms.ModelForm) :
#     class Meta:
#         model = ShipprBooking
#         fields = ('source', 'destination', 'phone')

#     def clean_source(self):
#         if(self.cleaned_data['source'].endswith(', India')):
#             self.cleaned_data['source'] = self.cleaned_data['source'].replace(", India", "")
#             if len(self.cleaned_data['source']) >= 200 :
#                 self.cleaned_data['source'] = self.cleaned_data['source'][:199]
#             return self.cleaned_data['source']
#         else:
#             return self.cleaned_data['source']

#     def clean_destination(self):
#         if(self.cleaned_data['destination'].endswith(', India')):
#             self.cleaned_data['destination'] = self.cleaned_data['destination'].replace(", India", "")
#             if len(self.cleaned_data['destination']) >= 200 :
#                 self.cleaned_data['destination'] = self.cleaned_data['destination'][:199]
#             return self.cleaned_data['destination']
#         else:
#             return self.cleaned_data['destination']

# class ShippingAddressFrom(forms.ModelForm) :
#     class Meta :
#         model = ShippingAddress
#         fields = ('name', 'company','phone', 'address1', 'address2', 'city', 'state','email','vat')

