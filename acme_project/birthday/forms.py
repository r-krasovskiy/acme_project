from django import forms

# Импортируем класс модели Birthday.
from .models import Birthday


# Для использования формы с моделями меняем класс на forms.ModelForm.
class BirthdayForm(forms.ModelForm):
    # Удаляем все описания полей.

    # Все настройки задаём в подклассе Meta.
    class Meta:
        # Указываем модель, на основе которой должна строиться форма.
        model = Birthday
        # Указываем, что надо отобразить все поля.
        fields = '__all__'
        # Указываем, что для поля с датой рождения
        # используется виджет с типом данных date.
        widgets = {
            'birthday': forms.DateInput(attrs={'type': 'date'})
        }

        # Clean-метод для валидации имени (если юзер ввел несколько слов):
        def clean_first_name(self):
            # Получаем значение имени из словаря очищенных данных.
            first_name = self.cleaned_data['first_name']
            # Разбиваем полученную строку по пробелам
            # и возвращаем только первое имя.
            return first_name.split()[0]
