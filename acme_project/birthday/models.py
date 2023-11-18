from django.db import models

# Импортируется функция-валидатор.
from .validators import real_age


class Birthday(models.Model):
    first_name = models.CharField('Имя', max_length=20)
    last_name = models.CharField(
        'Фамилия', max_length=20, help_text='Необязательное поле', blank=True
    )
    # Валидатор указывается в описании поля.
    birthday = models.DateField('Дата рождения', validators=(real_age,))
    # для работы с картинками нужна сперва установка: pip install Pillow==9.3.0
    image = models.ImageField('Фото', blank=True, upload_to='birthdays_images')

    # Валидатор на уникальность записи:
    # совокупность значений полей «Имя», «Фамилия» и «Дата рождения»
    # не должна повторяться в БД.
    class Meta:
        constraints = (
            models.UniqueConstraint(
                fields=('first_name', 'last_name', 'birthday'),
                name='Unique person constraint',
            ),
        )
