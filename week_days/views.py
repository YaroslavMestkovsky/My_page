from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

# Create your views here.
week = {'monday': 'Понедельник день тяжелый',
        'thusday': 'Вторник тоже напряженный',
        'wednesday': 'Долго длится как всегда, день с названием среда',
        'thursday': 'И в четверг все как обычно, ни секунды жизни личной',
        'friday': 'Будем в пятницу опять о субботе все мечтать',
        'saturday': 'Забивай на все, зажигай в субботу, забивай на все, не надо на работу.',
        'sunday': 'Воскресенье день похмелья'}


def index(request):
    days = list(week)
    li_elements = ''
    for day_week in days:
        redirect_path = reverse('day_name', args=[day_week])
        li_elements += f' <a href="{redirect_path}"> <li>{day_week}</li> </a>'
    response = f'''
    <ul>
        {li_elements}
    </ul>
    '''
    return HttpResponse(response)


def get_info_about_day(request, day: str):
    return render(request, 'week_days/greeting.html')


def get_info_about_day_by_number(request, day: int):
    days = list(week)
    if day > 7 or day == 0:
        return HttpResponseNotFound(f'В неделе всего 7 дней, указан неверный номер дня - {day}')
    name_day = days[day - 1]
    week_days_redirect = reverse('day_name', args=[name_day])
    return HttpResponseRedirect(week_days_redirect)
