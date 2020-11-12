import sys, requests, traceback
from PyQt5 import QtCore, QtGui, QtWidgets
from window import Ui_MainWindow, Ui_Form_Home, Ui_Form_Notifications, Ui_Form_Search, Ui_Form_Settings
from abc import ABC, abstractmethod

# Custom Exceptions
class DataLoaderRequestFailure(Exception):
  def __init__(self, e):
    super().__init__('\'{}\''.format(e))

class NoSceneError(Exception):
  def __init__(self, sceneName):
    super().__init__('There is no scene with such a name as \'{}\''.format(sceneName))
# ...

class Company:
  def __init__(self, price=None, valueChange=None, percentageChange=None, history=None):
    self.price = price
    self.valueChange = valueChange
    self.percentageChange = percentageChange
    self.history = history

  @property
  def price(self): return self.price
  @price.setter
  def price(self, value): self.price = value

  @property
  def valueChange(self): return self.valueChange
  @valueChange.setter
  def valueChange(self, value): self.valueChange = value

  @property
  def percentageChange(self): return self.percentageChange
  @percentageChange.setter
  def percentageChange(self, value): self.percentageChange = value

  @property
  def history(self): return self.history
  @history.setter
  def history(self, value): self.history = value

# INTERFACES
class IConfig(ABC):
  @abstractmethod
  def load(self): pass

  @abstractmethod
  def save(self): pass

  @abstractmethod
  def update(self, key, value): pass

  @abstractmethod
  def reset(self): pass

class IDataLoader(ABC):
  @abstractmethod
  def searchCompanyOrSymbol(self, searchText): pass

  @abstractmethod
  def getCompany(self, id): pass

# ABSTRACT CLASS
class WebDataLoader(IDataLoader):
  def __init__(self):
    self.searchURL = None
    self.companyURL = None

  @property
  def searchURL(self): return self.searchURL
  @searchURL.setter
  def searchURL(self, value): self.searchURL = value

  @property
  def companyURL(self): return self.companyURL
  @companyURL.setter
  def companyURL(self, value): self.companyURL = value

  @staticmethod
  def getRequestText(URL):
    r = requests.get(URL)
    r.raise_for_status()
    return r.text

# ABSTRACT CLASS REALIZATION
class InvestopediaDotComWebDataLoader(WebDataLoader):
  def __init__(self):
    super().__init__()
    self.searchURL = 'https://www.investopedia.com/markets/suggestions?q='
    self.companyURL = 'https://www.investopedia.com/markets/quote?tvwidgetsymbol='

  def searchCompanyOrSymbol(self, searchText):
    suggestions = []
    try:
      html = self.getRequestText(self.searchURL + searchText)
    except requests.exceptions.HTTPError as e: # Exception 3
      raise DataLoaderRequestFailure(e) from e # Custom Exception that will be catched later by that one who call this function
    else:
      #... parsing process
      return suggestions

  def getCompany(self, symbol):
    company = Company()
    try:
      html = self.getRequestText(self.companyURL + searchText)
    except requests.exceptions.HTTPError as e: # Exception 4
      raise DataLoaderRequestFailure(e) from e  # Custom Exception that will be catched later by that one who call this function
    else:
      #... parsing process
      return company

# WINDOW
class Window (QtWidgets.QMainWindow, Ui_MainWindow):
  def __init__ (self):
    super().__init__()

    self.scenes = {

      'home': self.generateSceneFromForm(Ui_Form_Home),
      'notifications': self.generateSceneFromForm(Ui_Form_Notifications),
      'search': self.generateSceneFromForm(Ui_Form_Search),
      'settings': self.generateSceneFromForm(Ui_Form_Settings)

    }

    self.initialScene = 'home'
    self.currentScene = None

    self.setupUi(self)
    self.connectButtons()

    self.changeSceneTo(self.initialScene)

  @staticmethod
  def generateSceneFromForm( Form ):
    class Scene(QtWidgets.QWidget, Form):
      def __init__(self):
        super().__init__()
        self.setupUi(self)

    return Scene()

  def connectButtons(self):
    self.Home.clicked.connect(lambda: self.changeSceneTo( 'home' ))
    self.Notifications.clicked.connect(lambda: self.changeSceneTo( 'notificationss' )) # CHANGE AFTER SHOWING CODE TO notifications
    self.Search.clicked.connect(lambda: self.changeSceneTo( 'search' ))
    self.Settings.clicked.connect(lambda: self.changeSceneTo( 'settings' ))
    self.Exit.clicked.connect(lambda: sys.exit())
    
  def clearScene( self ):
    for i in reversed(range(self.MainMenuLayout.count())): 
      self.MainMenuLayout.itemAt(i).widget().setParent(None)

  def changeSceneTo( self, sceneName ):
    self.clearScene()
    try:
      self.MainMenuLayout.addWidget(self.scenes[sceneName])
    except KeyError as e: # Exception 2
      raise NoSceneError(sceneName) from e # Custom Exception without further catching it
    else:
      self.currentScene = sceneName

# MAIN
def main():
  try:
    app = QtWidgets.QApplication([])
    win = Window()
    win.show()
    sys.exit(app.exec())

  except Exception: # Exception 1
    f = open("log.txt", "w")
    f.write (traceback.format_exc())
    f.close()

    sys.exit()    

if __name__ == '__main__':
  main()