from .models import Notes
from django.forms import ModelForm, TextInput, SelectDateWidget, Textarea

class NotesForm(ModelForm):
    class Meta:
        model = Notes
        fields = ['title', 'anons', 'full_text','current_value', 'date']

        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Привычка'}),
            "anons": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Цель'}),
            "current_value": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Нынешнее значение'}),
            "date": SelectDateWidget(attrs={
                'class': 'form-control',
                'placeholder': 'Дата'}),
            "full_text": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Описание'}),
        }
