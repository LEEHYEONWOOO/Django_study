from django import forms
from .models import Question, Choice


class question_form(forms.Form):
    another_question_select = forms.ModelChoiceField(queryset=Question.objects.all(),
                                                     to_field_name='pk',
                                                     empty_label='질문을 선택하세요')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.initial:
            if self.initial.get('queryset'):
                self.fields['another_question_select'] = forms.ModelChoiceField(queryset=self.initial.get('queryset'),
                                                                                to_field_name='pk',
                                                                                empty_label='질문을 선택하세요'
                                                                                )


class choice_form(forms.Form):
    Choice_select = forms.ModelChoiceField(queryset=Choice.objects.all())


class question_model_form(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['question_text']