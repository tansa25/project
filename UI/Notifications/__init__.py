from datetime import datetime
from scene import CompositeScene
from PyQt5 import QtWidgets


class NotificationsScene(CompositeScene):
    def __init__(self, path):
        CompositeScene.__init__(self, path)
        self.total = 0

        self.addNotification('Apple now cost 5$ more!!!')
        self.addNotification('IBM price dropped to 300$')

        self.Notifications.addSpacerItem(QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding))

    def addNotification(self, text, date=None):
        if date is None:
            date = str(datetime.now().strftime("%d.%m %H:%M:%S"))

        notification = self.initScene('Notification')
        notification.DataLabel.setText(date)
        notification.TextLabel.setText(text)
        self.Notifications.addWidget(notification)

        self.updateTotal(+1)

    def updateTotal(self, numberToAdd=0):
        if numberToAdd:
            self.total += numberToAdd
        self.NumberLabel.setText(str(self.total))
