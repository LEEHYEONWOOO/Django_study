from django import forms
from django.db import models

from general.models import GeneralInfo, Office
from seoulsoft.val import text_widget, date_widget, file_widget


class GeneralInfoUpdateForm(forms.ModelForm):
   safety_management_top_position = forms.CharField(max_length=10,
                                                    required=False,
                                                    widget=forms.TextInput(
                                                       attrs={'class': 'border-0 w-100 text-center',
                                                              'autocomplete': 'off', 'placeholder': '부서/직책'}))

   safety_management_middle_position = forms.CharField(max_length=10,
                                                       required=False,
                                                       widget=forms.TextInput(
                                                          attrs={'class': 'border-0 w-100 text-center',
                                                                 'autocomplete': 'off', 'placeholder': '부서/직책'}))

   safety_management_bottom_position = forms.CharField(max_length=10,
                                                       required=False,
                                                       widget=forms.TextInput(
                                                          attrs={'class': 'border-0 w-100 text-center',
                                                                 'autocomplete': 'off', 'placeholder': '부서/직책'}))

   traffic_manager_position = forms.CharField(max_length=10,
                                              required=False,
                                              widget=forms.TextInput(
                                                 attrs={'class': 'border-0 w-100 text-center',
                                                        'autocomplete': 'off', 'placeholder': '부서/직책'}))

   lead_manager_position = forms.CharField(max_length=10,
                                           required=False,
                                           widget=forms.TextInput(
                                              attrs={'class': 'border-0 w-100 text-center',
                                                     'autocomplete': 'off', 'placeholder': '부서/직책'}))

   accident_manager_position = forms.CharField(max_length=10,
                                               required=False,
                                               widget=forms.TextInput(
                                                  attrs={'class': 'border-0 w-100 text-center',
                                                         'autocomplete': 'off', 'placeholder': '부서/직책'}))

   operate_manager_position = forms.CharField(max_length=10,
                                              required=False,
                                              widget=forms.TextInput(
                                                 attrs={'class': 'border-0 w-100 text-center',
                                                        'autocomplete': 'off', 'placeholder': '부서/직책'}))

   dispatch_manager_position = forms.CharField(max_length=10,
                                               required=False,
                                               widget=forms.TextInput(
                                                  attrs={'class': 'border-0 w-100 text-center',
                                                         'autocomplete': 'off', 'placeholder': '부서/직책'}))

   safety_management_top_name = forms.CharField(max_length=10,
                                                required=False,
                                                widget=forms.TextInput(
                                                   attrs={'class': 'border-0 w-100 text-center',
                                                          'autocomplete': 'off', 'placeholder': '이름'}))

   safety_management_middle_name = forms.CharField(max_length=10,
                                                   required=False,
                                                   widget=forms.TextInput(
                                                      attrs={'class': 'border-0 w-100 text-center',
                                                             'autocomplete': 'off', 'placeholder': '이름'}))

   safety_management_bottom_name = forms.CharField(max_length=10,
                                                   required=False,
                                                   widget=forms.TextInput(
                                                      attrs={'class': 'border-0 w-100 text-center',
                                                             'autocomplete': 'off', 'placeholder': '이름'}))

   traffic_manager_name = forms.CharField(max_length=10,
                                          required=False,
                                          widget=forms.TextInput(
                                             attrs={'class': 'border-0 w-100 text-center',
                                                    'autocomplete': 'off', 'placeholder': '이름'}))

   lead_manager_name = forms.CharField(max_length=10,
                                       required=False,
                                       widget=forms.TextInput(
                                          attrs={'class': 'border-0 w-100 text-center',
                                                 'autocomplete': 'off', 'placeholder': '이름'}))

   accident_manager_name = forms.CharField(max_length=10,
                                           required=False,
                                           widget=forms.TextInput(
                                              attrs={'class': 'border-0 w-100 text-center',
                                                     'autocomplete': 'off', 'placeholder': '이름'}))

   operate_manager_name = forms.CharField(max_length=10,
                                          required=False,
                                          widget=forms.TextInput(
                                             attrs={'class': 'border-0 w-100 text-center',
                                                    'autocomplete': 'off', 'placeholder': '이름'}))

   dispatch_manager_name = forms.CharField(max_length=10,
                                           required=False,
                                           widget=forms.TextInput(
                                              attrs={'class': 'border-0 w-100 text-center',
                                                     'autocomplete': 'off', 'placeholder': '이름'}))

   class Meta:
      model = GeneralInfo
      fields = '__all__'
      widgets = {
         'name': text_widget,
         'representative': text_widget,
         'founding_date': date_widget,
         'business_number': text_widget,
         'corporate_number': text_widget,
         'email': text_widget,
         'tell': text_widget,
         'fax': text_widget,
         'address': text_widget,
         'main_img1': file_widget,
         'main_img2': file_widget,
         'main_img3': file_widget,
      }

class OfficeCreateForm(forms.ModelForm):
    class Meta:
        model = Office
        fields = '__all__'
        widgets = {
            'office_name': text_widget,
            'office_address': text_widget,
            'office_tell': text_widget,
        }

class OfficeUpdateForm(forms.ModelForm):
    class Meta:
        model = Office
        fields = ['office_name', 'office_address', 'office_tell']
        widgets = {
            'office_name': text_widget,
            'office_address': text_widget,
            'office_tell': text_widget,
        }