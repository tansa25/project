from scene import CompositeScene

from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QCoreApplication, QUrl


class GraphicsScene(CompositeScene):
    def __init__(self, path):
        CompositeScene.__init__(self, path)

        self.App = QCoreApplication.instance()
        self.Config = self.App.Config

        self.HeaderView = QWebEngineView()
        self.Header.addWidget(self.HeaderView)

        self.ChartView = QWebEngineView()
        self.Chart.addWidget(self.ChartView)

        self.CompanyProfileView = QWebEngineView()
        self.CompanyProfileInfo.addWidget(self.CompanyProfileView)

    def update(self):
        symbol = self.App.FeedCurrentCompanySymbol
        if symbol:
            company = self.getCompanyData(symbol)

            self.ChartView.load(QUrl(company.graphicURL))
            self.ChartView.show()

            self.HeaderView.load(QUrl(company.headerURL))
            self.HeaderView.show()

            self.CompanyProfileView.load(QUrl(company.companyProfileURL))
            self.CompanyProfileView.show()

    def getCompanyData(self, symbol):
        return self.App.DataLoader.getCompany(symbol)
