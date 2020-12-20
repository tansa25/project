from PyQt5.QtCore import QCoreApplication

from scene import CompositeScene


class SearchScene(CompositeScene):
    def __init__(self, path):
        CompositeScene.__init__(self, path)

        self.App = QCoreApplication.instance()
        self.Config = self.App.Config
        self.companies = self.Config.get('companies')

        self.onclick(self.SearchBtn, self.search)

        # self.addSearchResult('AAPL APPLE INC')
        # self.addSearchResult('IBM INTERNATION BUSINESS MACHINE')

    def search(self):
        searchText = self.SearchInput.text()
        results = self.App.DataLoader.searchCompanyOrSymbol(searchText)

        self.cleanSearchResults()

        for result in results:
            self.addSearchResult(result['symbol'], result['description'])

    def addSearchResult(self, symbol, description):
        searchResult = self.initScene('SearchResult')
        searchResult.ResultLabel.setText(description)
        if symbol in self.companies:
            self.btnToTrashBtn(searchResult.ResultBtn, symbol, description)
        else:
            self.btnToPlusBtn(searchResult.ResultBtn, symbol, description)

        # searchResult.horizontalLayout.setAlignment(QtCore.Qt.AlignHCenter)

        self.SearchResults.addWidget(searchResult)

    def cleanSearchResults(self):
        for i in reversed(range(self.SearchResults.count())):
            self.SearchResults.itemAt(i).widget().setParent(None)

    def btnToTrashBtn(self, btn, symbol, description):
        self.setIcon(btn, 'assets/icons/trash.svg')
        self.onclick(btn, lambda: self.removeCompanyFromConfig(btn, symbol, description))

    def btnToPlusBtn(self, btn, symbol, description):
        self.setIcon(btn, 'assets/icons/plus.svg')
        self.onclick(btn, lambda: self.addCompanyToConfig(btn, symbol, description))

    def removeCompanyFromConfig(self, btn, symbol, description):
        del self.companies[symbol]
        self.Config.save()

        self.btnToPlusBtn(btn, symbol, description)

    def addCompanyToConfig(self, btn, symbol, description):
        self.companies[symbol] = description
        self.Config.save()

        self.btnToTrashBtn(btn, symbol, description)
