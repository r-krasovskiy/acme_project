from django.shortcuts import render

# Импортируем класс BirthdayForm, чтобы создать экземпляр формы.
from .forms import BirthdayForm
# Импортируем из utils.py функцию для подсчёта дней.
from .utils import calculate_birthday_countdown
# Импортируем модель дней рождения.
from .models import Birthday


def birthday(request):
    # Создаём экземпляр класса формы.
    form = BirthdayForm(request.POST or None)
    # Создаём словарь контекста сразу после инициализации формы.
    context = {'form': form}
    # Если в GET-запросе были переданы параметры — значит,
    # объект request.GET не пуст и этот объект передаётся в форму;
    # если же объект request.GET пуст — срабатывает условиe or
    # и форма создаётся без параметров, через BirthdayForm(None)
    # — это идентично обычному BirthdayForm()
    # Если форма валидна...
    if form.is_valid():
        # Сохраняем в базу введенные данные.
        form.save()
        # ...вызовем функцию подсчёта дней:
        birthday_countdown = calculate_birthday_countdown(
            # ...и передаём в неё дату из словаря cleaned_data.
            form.cleaned_data['birthday']
        )
        # Обновляем словарь контекста: добавляем в него новый элемент.
        context.update({'birthday_countdown': birthday_countdown})
    # Указываем нужный шаблон и передаём в него словарь контекста.
    return render(request, 'birthday/birthday.html', context)


def birthday_list(request):
    # Получаем все объекты модели Birthday из БД.
    birthdays = Birthday.objects.all()
    # Передаём их в контекст шаблона.
    context = {'birthdays': birthdays}
    return render(request, 'birthday/birthday_list.html', context) 
