from PyQt5.QtGui import QColor, QPalette
from PyQt5.QtCore import QCoreApplication

from scene import CompositeScene


class CompaniesScene(CompositeScene):
    def __init__(self, path):
        CompositeScene.__init__(self, path)

        self.companiesWidgets = {}

        self.App = QCoreApplication.instance()
        self.Config = self.App.Config
        self.companies = self.Config.get('companies')

    def update(self):
        self.removeAllCompaniesWidgets()
        self.addCompaniesWidgets()

        if self.App.FeedCurrentCompanySymbol:
            self.makeBtnActive(self.App.FeedCurrentCompanySymbol)

    def getCompany(self, symbol):
        return self.companiesWidgets[symbol]

    def makeBtnActive(self, symbol):
        self.removeAllCompaniesWidgets()
        self.addCompaniesWidgets()

        btn = self.getCompany(symbol).NameBtn
        btn.setStyleSheet('QPushButton { background-color: #ff0b76; }')

    def addCompanyWidget(self, name, symbol):
        """ TODO Add possibility to use long names for companies
        company = self.initScene('Company')
        longtext = 'Novusssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssss'
        label = QtWidgets.QLabel(longtext, company.NameBtn)
        label.setWordWrap(True)
        company.NameBtn = QtWidgets.QHBoxLayout(company.NameBtn)
        company.NameBtn.addWidget(label)
        self.Companies.addWidget(company)
        """
        nameMaxLength = 15
        name = name if len(name) <= nameMaxLength else name[:nameMaxLength - 1] + '...'

        company = self.initScene('Company')

        company.NameBtn.setText(name)
        self.onclick(company.NameBtn, lambda: self.setCurrentActiveCompany(symbol))

        self.onclick(company.DeleteBtn, lambda: self.removeCompanyFromConfig(symbol))

        self.Companies.addWidget(company)
        self.companiesWidgets[symbol] = company

    def addCompaniesWidgets(self):
        for symbol in self.companies.keys():
            self.addCompanyWidget(self.companies[symbol], symbol)

    def removeAllCompaniesWidgets(self):
        for i in reversed(range(self.Companies.count())):
            self.Companies.itemAt(i).widget().setParent(None)
        self.companiesWidgets = {}

    def setCurrentActiveCompany(self, symbol):
        self.App.FeedSetCurrentCompanySymbol(symbol)

        if symbol:
            self.makeBtnActive(symbol)

    def removeCompanyFromConfig(self, symbol):
        del self.companies[symbol]
        self.Config.save()

        if symbol == self.App.FeedCurrentCompanySymbol:
            self.setCurrentActiveCompany(None)
        else:
            self.update()
