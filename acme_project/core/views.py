from django.shortcuts import render


# Кастомизированная страница для ошибки 404.
def page_not_found(request, exception):
    # Переменная exception содержит отладочную информацию;
    return render(request, 'core/404.html', status=404)


# Кастомизированная страница для ошибки 403.
def csrf_failure(request, reason=''):
    return render(request, 'core/403csrf.html', status=403)
