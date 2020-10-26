import bootstrap_datepicker_plus as datetimepicker
from django import forms
from .models import List
from .models import Item

class ListForm(forms.ModelForm):
    class Meta:
        model = List
        fields = ["item", "completed"]

class ItemForm(forms.ModelForm):

    class Meta:
        model = Item
        fields = ('sample_1', 'sample_2', 'sample_3', 'sample_4_start', 'sample_4_end')
        widgets = {
            'sample_1': datetimepicker.DatePickerInput(
                format='%Y-%m-%d',
                options={
                    'locale': 'ja',
                    'dayViewHeaderFormat': 'YYYY年 MMMM',
                }
            ),

            'sample_2': datetimepicker.DateTimePickerInput(
                format='%Y-%m-%d %H:%M:%S',
                options={
                    'locale': 'ja',
                    'dayViewHeaderFormat': 'YYYY年 MMMM',
                }
            ),

            'sample_3': datetimepicker.TimePickerInput(
                format='%H:%M:%S',
                options={
                    'locale': 'ja',
                }

            ),

            'sample_4_start': datetimepicker.DatePickerInput(
                format='%Y-%m-%d',
                options={
                    'locale': 'ja',
                    'dayViewHeaderFormat': 'YYYY年 MMMM',
                }
            ).start_of('期間'),

            'sample_4_end': datetimepicker.DatePickerInput(
                format='%Y-%m-%d',
                options={
                    'locale': 'ja',
                    'dayViewHeaderFormat': 'YYYY年 MMMM',
                }
            ).end_of('期間'),
        }
