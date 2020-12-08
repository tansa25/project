from PyQt5 import QtWidgets
from scene import CompositeScene, Placeholder


class UIScene(QtWidgets.QMainWindow, CompositeScene):
    def __init__(self, path):
        CompositeScene.__init__(self, path)

        self.addPlaceholder(Placeholder('inner-content', self.InnerContent, self.initScene('Feed')))
        # self.colorButtons([self.FeedBtn, self.NotificationsBtn, self.SearchBtn, self.SettingsBtn], (255, 255, 255, 255))
        self.connectButtons()

    def colorButtons(self, buttons, color):
        for button in buttons:
            self.changeButtonColor(button, color)

    def connectButtons(self):
        self.onclick(self.FeedBtn, lambda: self.changePlaceholdersScene('inner-content', self.initScene('Feed')))
        self.onclick(self.NotificationsBtn, lambda: self.changePlaceholdersScene('inner-content', self.initScene('Notifications')))
        self.onclick(self.SearchBtn, lambda: self.changePlaceholdersScene('inner-content', self.initScene('Search')))
        self.onclick(self.SettingsBtn, lambda: self.changePlaceholdersScene('inner-content', self.initScene('Settings')))
