from PyQt5.QtCore import QCoreApplication

from scene import CompositeScene, Placeholder


class FeedScene(CompositeScene):
    def __init__(self, path):
        CompositeScene.__init__(self, path)

        self.addPlaceholder(Placeholder('graphics', self.Graphics, self.initScene('Graphics')))
        self.addPlaceholder(Placeholder('companies', self.Companies, self.initScene('Companies')))

        self.App = QCoreApplication.instance()
        Config = self.App.Config
        companies = Config.get('companies')

        self.App.FeedSetCurrentCompanySymbol = lambda symbol: self.setCurrentCompanySymbol(symbol)

        if len(companies.keys()) != 0:
            self.setCurrentCompanySymbol(list(companies.keys())[0])
        else:
            self.setCurrentCompanySymbol(None)

    def setCurrentCompanySymbol(self, symbol):
        self.App.FeedCurrentCompanySymbol = symbol

        self.getPlaceholder('graphics').scene.update()
        self.getPlaceholder('companies').scene.update()
