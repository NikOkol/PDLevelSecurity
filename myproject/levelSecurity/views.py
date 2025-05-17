from django.shortcuts import render
from django.http import HttpResponse
from .models import PD_TYPES, LEVEL_TABLE, REASON_DICT
from .security_measures import SECURITY_MEASURES
from .gis_measures import GIS_MEASURES, CLASS_TABLE
from django.shortcuts import redirect
def custom_404_view(request, exception):
    return redirect('/')

def home_view(request):
    return render(request, 'levelSecurity/home.html')

def gis_form_view(request):
    if request.method == "POST":
        level = int(request.POST.get("signif"))
        scale = request.POST.get("scale")
        protect_class = CLASS_TABLE[level][scale]

        measures_by_section = {}
        for section, items in SECURITY_MEASURES.items():
            filtered = [i for i in items if protect_class in i["levels"]]
            if filtered:
                measures_by_section[section] = filtered

        return render(request, "levelSecurity/result.html", {
            "max_level": protect_class,
            "analys_type": "класса",
            "measures_by_section": measures_by_section
        })
    return render(request, 'levelSecurity/gis_page.html')

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

def pd_form_view(request):
    if request.method == "POST":
        cert1 = request.POST.get("cert-os")
        cert2 = request.POST.get("cert-app")
        network = request.POST.get("network")
        number = request.POST.get("number")  # 'lt' или 'gt'
        checkbox_value = request.POST.get('employee') == 'on'
        is_employee = ""
        if checkbox_value:
            is_employee = "empl"
        else:
            is_employee = "notempl"

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
            level_ids.append(LEVEL_TABLE[option][threat_type][subjects_type][is_employee])

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
            "analys_type": "уровня",
            "measures_by_section": measures_by_section
        })

    return render(request, "levelSecurity/pd_page.html", {"PD_TYPES": PD_TYPES})