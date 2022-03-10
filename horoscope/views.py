from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string

# Create your views here.

signs = {'aries': 'Овен - первый знак зодиака, планета Марс (с 21 марта по 20 апреля)',
         'taurus': 'Телец - второй знак зодиака, планета Венера (с 21 апреля по 21 мая)',
         'gemini': 'Близнецы - третий знак зодиака, планета Меркурий (с 22 мая по 21 июня).',
         'cancer': 'Рак - четвёртый знак зодиака, Луна (с 22 июня по 22 июля).',
         'leo': 'Лев - пятый знак зодиака, солнце (с 23 июля по 21 августа).',
         'virgo': 'Дева - шестой знак зодиака, планета Меркурий (с 22 августа по 23 сентября).',
         'libra': 'Весы - седьмой знак зодиака, планета Венера (с 24 сентября по 23 октября).',
         'scorpio': 'Скорпион - восьмой знак зодиака, планета Марс (с 24 октября по 22 ноября).',
         'sagittarius': 'Стрелец - девятый знак зодиака, планета Юпитер (с 23 ноября по 22 декабря).',
         'capricorn': 'Козерог - десятый знак зодиака, планета Сатурн (с 23 декабря по 20 января).',
         'aquarius': 'Водолей - одиннадцатый знак зодиака, планеты Уран и Сатурн (с 21 января по 19 февраля).',
         'pisces': 'Рыбы - двенадцатый знак зодиака, планеты Юпитер (с 20 февраля по 20 марта).',
}
types = {
    'fire': ['aries', 'leo', 'sagittarius'],
    'earth': ['taurus', 'virgo', 'capricorn'],
    'air': ['gemini', 'libra', 'aquarius'],
    'water': ['cancer', 'scorpio', 'pisces'], }

months = {
    1: 'Январь',
    2: 'Февраль',
    3: 'Март',
    4: 'Апрель',
    5: 'Май',
    6: 'Июнь',
    7: 'Июль',
    8: 'Август',
    9: 'Сентябрь',
    10: 'Октябрь',
    11: 'Ноябрь',
    12: 'Декабрь',
}

sign_guess_by_month = {
    'Март-Апрель': 'Овен',
    'Апрель-Май': 'Телец',
    'Май-Июнь': 'Близнецы',
    'Июнь-Июль': 'Рак',
    'Июль-Август': 'Лев',
    'Август-Сентябрь': 'Дева',
    'Сентябрь-Октябрь': 'Весы',
    'Октябрь-Ноябрь': 'Скорпион',
    'Ноябрь-Декабрь': 'Стрелец',
    'Декабрь-Январь': 'Козерог',
    'Январь-Февраль': 'Водолей',
    'Февраль-Март': 'Рыбы',
}


def get_yyyy_converters(request, number):
    return HttpResponse(f'Вы передали число из 4х цифр - {number}')


def get_float_converters(request, number):
    return HttpResponse(f'Вы передали вещественное число - {number}')


def get_date_converters(request, number):
    return HttpResponse(f'Вы передали дату - {number}')


def index(request):
    zodiacs = list(signs)
    context = {
        'zodiacs': zodiacs
    }
    return render(request, 'horoscope/index.html', context=context)


def get_guinness_world_records(request):
    context = {
        'power_man': 'Narve Laeret',
        'bar_name': 'Bob’s BBQ & Grill',
        'count_needle': 1790,
    }
    return render(request, 'horoscope/guinnessworldrecords.html', context=context)


def get_kiany_info(request):
    data = {
        'year_born': '10',
        'city_born': 'Vologda',
        'movie_name': 'Brat 2',
    }
    return render(request, 'horoscope/kiany.html', context=data)


def get_info_about_zodiac_sign(request, sign_zodiac: str):
    description = signs.get(sign_zodiac)
    data = {
        'description': description,
        'sign': sign_zodiac,
        'zodiacs': signs,
    }
    return render(request, 'horoscope/info_zodiac.html', context=data)


def get_info_about_zodiac_sign_by_number(request, sign_zodiac: int):
    zodiacs = list(signs)
    if sign_zodiac > len(list(signs)) or sign_zodiac == 0:
        return HttpResponseNotFound(f'Неправильный порядковый номер знака зодиака - {sign_zodiac}')
    name_zodiac = zodiacs[sign_zodiac - 1]
    redirect_url = reverse('horoscope_name', args=[name_zodiac])
    return HttpResponseRedirect(redirect_url)


def show_types(request):
    li_elements = ''
    for element in types:
        redirect_path = reverse('type_name', args=(element,))
        li_elements += f'<li> <a href="{redirect_path}"> {element.title()} </a> </li>'
    response = f'''
        <ul>
            {li_elements}
        </ul>
        '''
    return HttpResponse(response)


def show_element_signs(request, element):
    li_elements = ''
    for sign in types[element]:
        redirect_path = reverse('horoscope_name', args=(sign,))
        li_elements += f'<li> <a href="{redirect_path}"> {sign.title()} <a> </li>'
    response = f'''
        <ul>
            {li_elements}
        </ul>
        '''
    return HttpResponse(response)


def day_month(request, month: int, day: int):
    response = 'Неверно указана дата'
    if 0 < month < 13 and 0 < day < 32:
        guess = []
        for mont in sign_guess_by_month:
            if months[month] in mont:
                guess.append(sign_guess_by_month[mont])
        response = f'Месяц - {months[month]}, день - {day}. Это может быть или {" или ".join(guess)}'
    return HttpResponse(f'<h2>{response}</h2>')
