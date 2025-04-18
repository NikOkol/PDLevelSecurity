from django.shortcuts import render
from django.http import HttpResponse
from .models import PD_TYPES, LEVEL_TABLE, REASON_DICT
from .security_measures import SECURITY_MEASURES  # ДОБАВЛЕНО

def get_id(strings_array):
    if not strings_array:
        return None
    min_num = float('inf')
    min_string = ""
    for s in strings_array:
        try:
            num = int(s[0])
            if num < min_num:
                min_num = num
                min_string = s
        except (IndexError, ValueError):
            continue
    return min_string

def form_view(request):
    if request.method == "POST":
        cert1 = request.POST.get("cert-os")
        cert2 = request.POST.get("cert-app")
        network = request.POST.get("network")
        number = request.POST.get("number")  # 'lt' или 'gt'

        selected_options = [item for item in PD_TYPES if request.POST.get(f"option_{item}")]

        if not all([cert1, cert2, network, number]):
            return HttpResponse("Ошибка: Все поля должны быть заполнены!", status=400)

        threat_type = 3
        if network == "network":
            threat_type = 3
        if cert2 != "certified":
            threat_type = 2
        if cert1 != "certified":
            threat_type = 1

        subjects_type = "gt" if number == "gt" else "lt"

        level_ids = []
        for option in selected_options:
            level_ids.append(LEVEL_TABLE[option][threat_type][subjects_type])

        max_level = get_id(level_ids)
        level_digit = int(max_level[0])  # Извлекаем цифру из уровня, например из \"2г\" → 2

        # Формируем меры по разделам
        measures_by_section = {}
        for section, items in SECURITY_MEASURES.items():
            filtered = [i for i in items if level_digit in i["levels"]]
            if filtered:
                measures_by_section[section] = filtered

        return render(request, "levelSecurity/result.html", {
            "max_level": max_level,
            "reason": REASON_DICT.get(max_level, "Ошибка: уровень не найден."),
            "measures_by_section": measures_by_section
        })

    return render(request, "levelSecurity/home.html", {"PD_TYPES": PD_TYPES})