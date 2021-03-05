# подгружаю необходимые библиотеки
import requests
from bs4 import BeautifulSoup


# создаю класс для парсинга данных с сайта
class TezTours:
    # задаю атрибуты класса
    def __init__(self):
        self.site = 'https://www.tez-tour.com/'
        self.data = self.parse_site()

    # функция осуществляющая непосредственный парсинг данных с сайта
    def parse_site(self):
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:45.0) Gecko/20100101 Firefox/45.0' }

        response = requests.get(self.site, headers=headers)
        soup = BeautifulSoup(response.text, features='lxml')
        trs = soup.findChildren("table")

        # создаю саму базу данных по типу словаря где ключ название туроператора, а курс значение ключа
        db_teztours = {}
        i = 0
        for tr in trs[2]:
            i += 1
            if i == 4:
                tds = tr.findAll("td")

                name = 'TezTours'

                usd = tds[1].text
                eur = tds[2].text
                db_teztours[name] = [usd[:-4], eur[:-4]]
        #print(db_teztours)
        return db_teztours


if __name__ == '__main__':
    pars = TezTours()