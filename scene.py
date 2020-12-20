from PyQt5 import uic, QtGui
from PyQt5.QtWidgets import QWidget, QGraphicsColorizeEffect
import os
import importlib


class Scene(QWidget):
    def __init__(self, scenePath):
        QWidget.__init__(self)

        self.path = scenePath
        self.name = None

        uic.loadUi(scenePath, self)

    @staticmethod
    def onclick(btnObject, func):
        try:
            btnObject.clicked.disconnect()
        except Exception:
            pass

        btnObject.clicked.connect(func)

    @staticmethod
    def setIcon(btnObject, iconPath):
        btnObject.setIcon(QtGui.QIcon(iconPath))

    @staticmethod
    def changeButtonColor(btnObject, color):
        effect = QGraphicsColorizeEffect()
        effect.setColor(QtGui.QColor(*color))
        btnObject.setGraphicsEffect(effect)


class Placeholder():
    def __init__(self, name, object_, initScene):
        self.name = name
        self.object = object_
        self.scene = None
        self.changeScene(initScene)

    def clear(self):
        for i in reversed(range(self.object.count())):
            self.object.itemAt(i).widget().setParent(None)

    def changeScene(self, scene):
        self.clear()
        self.object.addWidget(scene)
        self.scene = scene


class ScenePattern():
    def __init__(self, name, path, class_):
        self.name = name
        self.path = path
        self.class_ = class_

    def init(self):
        sceneInstance = self.class_(self.path)
        sceneInstance.name = self.name

        return sceneInstance


class CompositeScene(Scene):
    def __init__(self, scenePath):
        Scene.__init__(self, scenePath + '/__init__.ui')

        self._placeholders = []
        self._scenePatterns = []
        self.loadScenePatterns()

    def addScenePattern(self, scenePath, composite=False):
        importPath = scenePath.replace('/', '.')
        if not composite:
            importPath = importPath[:-3]

        sceneName = importPath[importPath.rfind('.') + 1:]
        className = sceneName + 'Scene'

        sceneModule = importlib.import_module(importPath)
        sceneClass = getattr(sceneModule, className)

        scenePattern = ScenePattern(sceneName, scenePath, sceneClass)

        if self.getScenePatternByName(sceneName):
            raise Exception('Scene name conflict: {sceneName}')

        self._scenePatterns.append(scenePattern)
        return scenePattern

    def initScene(self, sceneName):
        return self.getScenePatternByName(sceneName).init()

    def removeScenePatternByPath(self, scenePath):  # TODO
        pass

    def getScenePatternByPath(self, scenePath):
        if not scenePath.endswith('.ui'):  # If folder
            scenePath += '/__init__.ui'

        for scenePattern in self._scenePatterns:
            if scenePattern.path == scenePath:
                return scenePattern
        return None

    def getScenePatternByName(self, sceneName):
        for scenePattern in self._scenePatterns:
            if scenePattern.name == sceneName:
                return scenePattern
        return None

    def loadScenePatterns(self):
        sceneDir = self.path[:self.path.rfind('/')]
        dirContent = os.listdir(sceneDir)
        for object_ in dirContent:
            objectPath = f'{sceneDir}/{object_}'
            if os.path.isdir(objectPath) and object_ != '__pycache__':
                self.addScenePattern(objectPath, True)
            elif object_.endswith('.py') and object_ != '__init__.py':
                self.addScenePattern(objectPath[:-3] + '.ui')

    def addPlaceholder(self, placeholder):
        self._placeholders.append(placeholder)

    def removePlaceholder(self, name):  # TODO
        pass

    def getPlaceholder(self, name):
        for placeholder in self._placeholders:
            if placeholder.name == name:
                return placeholder
        return None

    def changePlaceholdersScene(self, placeholderName, scene):
        placeholder = self.getPlaceholder(placeholderName)
        placeholder.changeScene(scene)


class LeafScene(Scene):
    def __init__(self, scenePath):
        Scene.__init__(self, scenePath)
