from django.shortcuts import render
from django.http import HttpResponse
from .models import PD_TYPES, LEVEL_TABLE, REASON_DICT
from .security_measures import SECURITY_MEASURES
from .gis_measures import CLASS_TABLE
from django.shortcuts import redirect

def custom_404_view(request, exception):
    return redirect('/')

def home_view(request): # представление для домашней страницы
    return render(request, 'levelSecurity/home.html')

def gis_form_view(request): # Представление для страницы ГИС
    if request.method == "POST": # если POST-запрос, то считается класс защищенности и меры
        # из запроса вносим параметры в переменные
        level = int(request.POST.get("signif")) # уровень значимости
        scale = request.POST.get("scale") # масштаб
        protect_class = CLASS_TABLE[level][scale] # из таблицы берем класс защищенности по заданным параметрам

        measures_by_section = {}
        # Посекционно выбираем меры для найденного класса
        for section, items in SECURITY_MEASURES.items():
            filtered = [i for i in items if protect_class in i["levels"]]
            if filtered:
                measures_by_section[section] = filtered

        # рендерим страницу результата со следующими параметрами:
        return render(request, "levelSecurity/result.html", {
            "max_level": protect_class, # определенный класс защищенности
            "analys_type": "класса", # уровня/класса (для ПД или для ГИС)
            "measures_by_section": measures_by_section # меры посекционно
        })
    return render(request, 'levelSecurity/gis_page.html') # если запрос не POST, рендерим страницу выбора параметров ГИС


def get_id(strings_array): # Функция для выбора наивысшего уровня защищенности
    # На вход поступает массив причин, например, "2а", "1б"
    # Из них выбирается с наименьшим числом и возвращается (пример - "1б")
    if not strings_array:
        return None
    min_num = float('inf')
    min_string = ""
    for s in strings_array: # для каждой строки массива
        try:
            num = int(s[0]) # извлекается число
            if num < min_num: # проверяется, меньше ли оно всех предыдущих
                min_num = num # если меньше, то заносится в переменную наименьшего числа
                min_string = s
        except (IndexError, ValueError):
            continue
    return min_string

def pd_form_view(request): # представление страницы с ПД
    if request.method == "POST": # если отправляется POST-запрос, запускается расчет уровня защищенности

        # извлечение переменных из запроса:
        cert1 = request.POST.get("cert-os") # 'certified' или 'not'
        cert2 = request.POST.get("cert-app") # 'certified' или 'not'
        network = request.POST.get("network") # 'network' или 'local'
        number = request.POST.get("number")  # 'lt' (< 100k) или 'gt' (> 100k)
        checkbox_value = request.POST.get('employee') == 'on' # чекбокс с сотрудниками
        is_employee = ""
        if checkbox_value: # проверка, отмечен ли чекбокс с сотрудниками
            is_employee = "empl" # если отмечено, заносим в переменную empl
        else:
            is_employee = "notempl" # иначе notempl

        # Выбранные типы ПД
        selected_options = [item for item in PD_TYPES if request.POST.get(f"option_{item}")]

        # Проверка на наличие всех обязательных параметров
        if not all([cert1, cert2, network, number, selected_options]):
            return HttpResponse("Ошибка: Все поля должны быть заполнены!", status=400)

        # Определение типа угрозы
        threat_type = min( # берется минимум, т.к. 1й тип - самый серьезный
            3,
            2 if cert2 != "certified" else 3, # если отсутствует серт. прикладного ПО, то есть угрозы типа 2
            1 if cert1 != "certified" else 3 # если отсутствует серт. ОС, то есть угрозы типа 1
        )


        level_ids = []
        # Т.к. можно выбрать несколько типов ПД, вносим в массив все подходящие уровни защищенности
        for option in selected_options: # для каждого выбранного типа ПД
            level_ids.append(LEVEL_TABLE[option][threat_type][number][is_employee]) # из таблицы LEVEL_TABLE по критериям находим уровень

        # Из всех подходящих уровней находим наивысший
        max_level = get_id(level_ids)
        level_digit = int(max_level[0])  # Извлекаем цифру из уровня, например из "2г" → 2

        # Формируем меры по разделам
        measures_by_section = {}
        for section, items in SECURITY_MEASURES.items(): # Уровни из таблицы SECURITY_MEASURES для каждого раздела
            filtered = [i for i in items if level_digit in i["levels"]] # Фильтруем по нужному уровню защищенности
            if filtered:
                measures_by_section[section] = filtered # Заносим нужные меры в переменную посекционно

        return render(request, "levelSecurity/result.html", { # Рендерим страницу результата со следующими параметрами:
            "max_level": max_level, # наивысший уровень защищенности
            "reason": REASON_DICT.get(max_level, "Ошибка: уровень не найден."), # текст причины выбора уровня (выбирается по словарю)
            "analys_type": "уровня", # уровня/класса (для ПД или для ГИС)
            "measures_by_section": measures_by_section # меры для выбранного уровня
        })

    return render(request, "levelSecurity/pd_page.html", {"PD_TYPES": PD_TYPES}) # без POST-запроса рендерим страницу выбора параметров
