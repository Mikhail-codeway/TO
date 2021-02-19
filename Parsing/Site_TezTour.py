# подгружаю необходимые библиотеки
import requests
from bs4 import BeautifulSoup



# создаю класс для парсинга данных с сайта
class TezTour:
    #TODO: сущность туроператора TezTour

    # задаю атрибуты класса
    def __init__(self):
        self.site = 'https://www.tez-tour.com/'
        self.data = self.parse_site()

    # функция осуществляющая непосредственный парсинг данных с сайта
    def parse_site(self):
        site = 'https://www.tez-tour.com/'
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:45.0) Gecko/20100101 Firefox/45.0' }

        response = requests.get(site, headers=headers)
        soup = BeautifulSoup(response.text, features='lxml')
        trs = soup.findChildren("table")

        # создаю саму базу данных по типу словаря где ключ название туроператора, а курс значение ключа
        db_teztour = {}
        i = 0
        for tr in trs[2]:
            i += 1
            if i == 4:
                tds = tr.findAll("td")
                name = 'TezTour'
                usd = tds[1].text
                eur = tds[2].text
                db_teztour[name] = [usd[:-3], eur[:-3]]

        return db_teztour

    def get_data(self):
        return self.data