from bs4 import BeautifulSoup
import requests as req
import re

# Стартовая ссылка на страницу википедии с животными
link = 'https://ru.wikipedia.org/wiki/%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D1%8F:%D0%96%D0%B8%D0%B2%D0%BE%D1%82%D0%BD%D1%8B%D0%B5_%D0%BF%D0%BE_%D0%B0%D0%BB%D1%84%D0%B0%D0%B2%D0%B8%D1%82%D1%83'

# Переменная заголовка для отправки запроса
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}

# Объявление переменной словаря, которая будет заполняться
#   Ключ - буква русского алфавита
#   Значение - список названий животных
animals_by_letter = {}
is_russian_letter = True


def get_soup(link):
    '''
    Функция принимает ссылку на страницу, создаёт запрос.
    Возвращает содержимое страницы в виде экземпляра класса BS4.
    '''

    getting_request = req.get(link, headers=headers)
    soup = BeautifulSoup(getting_request.text, 'html.parser')

    return soup


def get_link(soup):
    '''
    Функция принимает экземпляр класса BS4, осуществляет в нём поиск тэга <a> с текстом
    'Следующая страница' для получения части ссылки.
    Возвращает полную ссылку страницы Википедии или False, если поиск не удался.
    '''

    main_page_link = 'https://ru.wikipedia.org/'
    next_page = soup.find('a', text='Следующая страница')

    if next_page:
        return main_page_link + next_page['href']
    else:
        return False


def fill_animals(soup):
    '''
    Функция принимает экземпляр класса BS4, осуществляет в нём поиск тэгов <div>,
    содержащих класс 'mw-category-group', заполняет словарь данными.
    Возвращает True, если найдены группы животных русскоязычного алфавита,
    False в ином случае.
    '''

    # Итерируемый объект с буквенными группами названия животных
    divs_by_letter = soup.findAll('div', class_='mw-category-group')

    # Тэгов может быть несколько на одной странице
    for div in divs_by_letter:

        # Используем только животных с названием из русскоязычного алфавита
        is_russ_letter = bool(re.search(r'[а-яА-Я]', div.h3.text))

        if is_russ_letter:
            animals = div.findAll('li')

            # Заполнение словаря 'animals_by_letter' данными
            if div.h3.text in animals_by_letter:
                animals_by_letter[div.h3.text].extend([i.text for i in animals])
            else:
                animals_by_letter[div.h3.text] = [i.text for i in animals]

        return is_russ_letter


# Основной цикл вызова функций
# Заканчивается в случае, если не найдена ссылка на следующую страницу или
# найдена группа животных, начинающихся с буквы не из русского алфавита
while link and is_russian_letter:
    soup = get_soup(link)

    link = get_link(soup)

    is_russian_letter = fill_animals(soup)

# Вывод словаря
for key, value in animals_by_letter.items():
    print(f'{key}: {len(value)}')







