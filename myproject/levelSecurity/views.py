from django.shortcuts import render

from django.shortcuts import render
from django.http import HttpResponse
from .models import PD_TYPES, LEVEL_TABLE, REASON_DICT


def get_id(strings_array):

    # Переменная для хранения наибольшего числа и соответствующей строки
    min_num = float('inf')  # Начинаем с очень большого числа
    min_string = ""

    # Проходим по всем строкам
    for s in strings_array:
        # Извлекаем первый символ и преобразуем его в число
        num = int(s[0])

        # Обновляем наименьшее число и строку, если найдено меньшее число
        if num < min_num:
            min_num = num
            min_string = s

    return min_string

def form_view(request):
    if request.method == "POST":
        cert1 = request.POST.get("cert-os")
        cert2 = request.POST.get("cert-app")
        network = request.POST.get("network")
        number = request.POST.get("number")

        selected_options = [item for item in PD_TYPES if request.POST.get(f"option_{item}")]

        # Проверка на пустые значения
        if not all([cert1, cert2, network, number]):
            return HttpResponse("Ошибка: Все поля должны быть заполнены!", status=400)

        threat_type = 0
        subjects_type = ""

        if network == "network":
            threat_type = 1
        if cert2 != "certified":
            threat_type = 2
        if cert1 != "certified":
            threat_type = 3

        if int(number) > 100000:
            subjects_type = "gt"
        else:
            subjects_type = "lt"

        level_ids = []

        for option in selected_options:
            level_ids.append(LEVEL_TABLE[option][threat_type][subjects_type])

        max_level = get_id(level_ids)

        print(max_level)  # Вывод в консоль

        return HttpResponse(f"{max_level}: {REASON_DICT[max_level]}")

    return render(request, "levelSecurity/home.html", {"PD_TYPES": PD_TYPES})

