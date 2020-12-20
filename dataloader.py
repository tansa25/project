from abc import ABC, abstractmethod
import requests

from data import Company


class IDataLoader(ABC):
    @abstractmethod
    def searchCompanyOrSymbol(self, searchText):
        pass

    @abstractmethod
    def getCompany(self, id):
        pass


class WebDataLoader(IDataLoader):
    def __init__(self):
        self.searchURL = None
        self.companyURL = None

    @property
    def searchURL(self):
        return self._searchURL

    @searchURL.setter
    def searchURL(self, value):
        self._searchURL = value

    @property
    def companyURL(self):
        return self._companyURL

    @companyURL.setter
    def companyURL(self, value):
        self._companyURL = value


class InvestopediaDotComWebDataLoader(WebDataLoader):
    def __init__(self):
        super().__init__()
        self.searchURL = 'https://www.investopedia.com/markets/suggestions?q='
        self.companyURL = 'https://www.investopedia.com/markets/quote?tvwidgetsymbol='

    def searchCompanyOrSymbol(self, searchText):
        return requests.get(self.searchURL + searchText).json()

    def getCompany(self, symbol):
        data = {'symbol': symbol}

        data['graphicURL'] = f'https://s.tradingview.com/investopedia/widgetembed/?frameElementId=tradingview_97eec&symbol={symbol}&interval=D&saveimage=0&toolbarbg=f1f3f6&studies=%5B%5D&theme=Light&style=3&timezone=Etc%2FUTC&studies_overrides=%7B%7D&overrides=%7B%7D&enabled_features=%5B%5D&disabled_features=%5B%5D&locale=en&utm_source=www.investopedia.com&utm_medium=widget&utm_campaign=chart&utm_term={symbol}'
        data['headerURL'] = f'https://s.tradingview.com/embed-widget/symbol-info/investopedia/?locale=en&symbol={symbol}'
        data['companyProfileURL'] = f'https://s.tradingview.com/embed-widget/symbol-profile/investopedia/?locale=en&symbol={symbol}'

        return Company(**data)


if __name__ == '__main__':
    DL = InvestopediaDotComWebDataLoader()

    suggestions = DL.searchCompanyOrSymbol('APPLE')
    print(suggestions)
    print(DL.getCompany(suggestions[0]['symbol']))
