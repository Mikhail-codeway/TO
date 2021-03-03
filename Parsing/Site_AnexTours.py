# подгружаю необходимые библиотеки
import requests
from bs4 import BeautifulSoup


# создаю класс для парсинга данных с сайта
class AnexTours:
    # задаю атрибуты класса
    def __init__(self):
        self.site = 'https://anextours.com/'
        self.data = self.parse_site()

    # функция осуществляющая непосредственный парсинг данных с сайта
    def parse_site(self):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:45.0) Gecko/20100101 Firefox/45.0'}

        response = requests.get(self.site, headers=headers)
        soup = BeautifulSoup(response.text, features='lxml')
        spans = soup.findChildren("span")

        # создаю саму базу данных по типу словаря где ключ название туроператора, а курс значение ключа
        db_anextours = {}

        usd = spans[2].text
        eur = spans[3].text

        name = 'AnexTours'
        db_anextours[name] = [usd[4:], eur[4:]]
        #print(db_anextours)
        return db_anextours


if __name__ == '__main__':
    pars = AnexTours()