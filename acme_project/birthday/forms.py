from django import forms
# Импортируем класс ошибки валидации.
from django.core.exceptions import ValidationError
# Импорт функции для отправки почты.
from django.core.mail import send_mail

# Импортируем класс модели Birthday.
from .models import Birthday, Congratulation


# Множество с именами участников Ливерпульской четвёрки.
BEATLES = {'Джон Леннон', 'Пол Маккартни', 'Джордж Харрисон', 'Ринго Старр'}


# Для использования формы с моделями меняем класс на forms.ModelForm.
class BirthdayForm(forms.ModelForm):
    # Удаляем все описания полей.

    # Все настройки задаём в подклассе Meta.
    class Meta:
        # Указываем модель, на основе которой должна строиться форма.
        model = Birthday
        # Указываем, что надо отобразить все поля.
        fields = '__all__'
        # Указываем, какие поля не отображать в форме.
        exclude = ('author',)
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
    
    # Clean-метод для валидации имени (не должно входить в список):
    def clean(self):
        # Вызов родительского метода clean с проверкой уникальности записи.
        super().clean()
        # Получаем имя и фамилию из очищенных полей формы.
        first_name = self.cleaned_data['first_name']
        last_name = self.cleaned_data['last_name']
        # Если кто-то представился участником Beatles:
        if f'{first_name} {last_name}' in BEATLES:
            send_mail(
                subject='Another Beatles member',
                message=f'{first_name} {last_name} пытался опубликовать запись!',
                from_email='birthday_form@acme.not',
                recipient_list=['admin@acme.not'],
                fail_silently=True,
            )
            raise ValidationError(
                'Мы тоже любим Битлз, но введите, пожалуйста, настоящее имя!'
            )


# Форма для текста поздравления.
class CongratulationForm(forms.ModelForm):
    
    class Meta:
        model = Congratulation
        fields = ('text',)
