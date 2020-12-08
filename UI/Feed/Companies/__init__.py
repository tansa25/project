from scene import CompositeScene
from PyQt5 import QtWidgets
from PyQt5.QtGui import QColor, QPalette


class CompaniesScene(CompositeScene):
    def __init__(self, path):
        CompositeScene.__init__(self, path)

        self.companies = {}

        self.addCompany('Apple')
        self.addCompany('Google')
        self.addCompany('IBM')

        self.makeBtnActive('Apple')

        self.Companies.addSpacerItem(QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding))

    def getCompany(self, name):
        return self.companies[name]

    def makeBtnActive(self, name):
        # TODO Make it via cheatsheet
        btn = self.getCompany('Apple').NameBtn
        p = btn.palette()
        p.setColor(QPalette.Button, QColor('#c7417b'))
        btn.setPalette(p)

    def addCompany(self, name):
        """ TODO Add possibility to use long names for companies
        company = self.initScene('Company')
        longtext = 'Novusssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssss'
        label = QtWidgets.QLabel(longtext, company.NameBtn)
        label.setWordWrap(True)
        company.NameBtn = QtWidgets.QHBoxLayout(company.NameBtn)
        company.NameBtn.addWidget(label)
        self.Companies.addWidget(company)
        """
        company = self.initScene('Company')
        company.NameBtn.setText(name)
        self.Companies.addWidget(company)

        self.companies[name] = company

        """ TODO Add spacer after all companies
        self.Companies.addSpacerItem(QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding))
        """
