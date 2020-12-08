from scene import CompositeScene
from PyQt5 import QtWidgets, QtCore


class SearchScene(CompositeScene):
    def __init__(self, path):
        CompositeScene.__init__(self, path)

        # self.changeButtonColor(self.SearchBtn, [255, 255, 255, 255])

        self.addSearchResult('AAPL APPLE INC')
        self.addSearchResult('IBM INTERNATION BUSINESS MACHINE')

        self.SearchResults.addSpacerItem(QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding))

    def addSearchResult(self, text):
        searchResult = self.initScene('SearchResult')
        searchResult.ResultLabel.setText(text)
        # searchResult.horizontalLayout.setAlignment(QtCore.Qt.AlignHCenter)
        self.SearchResults.addWidget(searchResult)
