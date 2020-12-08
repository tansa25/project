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

    @staticmethod
    def getRequestText(URL):
        return requests.get(URL).text


class InvestopediaDotComWebDataLoader(WebDataLoader):
    def __init__(self):
        super().__init__()
        self.searchURL = 'https://www.investopedia.com/markets/suggestions?q='
        self.companyURL = 'https://www.investopedia.com/markets/quote?tvwidgetsymbol='

    def searchCompanyOrSymbol(self, searchText):
        suggestions = []
        html = self.getRequestText(self.searchURL + searchText)
        # ... parsing process
        return suggestions

    def getCompany(self, symbol):
        company = Company()
        html = self.getRequestText(self.companyURL + symbol)
        # ... parsing process
        return company
