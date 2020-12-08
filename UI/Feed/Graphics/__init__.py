from scene import CompositeScene
"""
from PyQt5.QtCore import QDateTime, Qt
from PyQt5.QtGui import QPainter
from PyQt5.QtWidgets import (QWidget, QHeaderView, QHBoxLayout, QTableView, QSizePolicy)
from PyQt5.QtChart import QtChart
"""

from PyQt5.QtChart import QChart, QLineSeries, QChartView, QValueAxis, QCategoryAxis
from PyQt5.QtGui import QPainter, QColor, QPen
from PyQt5.QtCore import Qt


class GraphicsScene(CompositeScene):
    def __init__(self, path):
        CompositeScene.__init__(self, path)
        self.createTestChart()

    def createTestChart(self):
        chart = QChart()
        chart.setBackgroundRoundness(0)

        series = QLineSeries()
        pen = QPen(QColor(0xf5487f))
        pen.setWidth(2)
        series.setPen(pen)

        import random
        for i in range(1, 365, random.randrange(6, 14)):
            series.append(i, random.randrange(5, 38))
        chart.addSeries(series)

        x = QCategoryAxis()
        m = 1
        x.append('Jan', m := m + 31)
        x.append('Feb', m := m + 28)
        x.append('Mar', m := m + 31)
        x.append('Apr', m := m + 30)
        x.append('May', m := m + 31)
        x.append('Jun', m := m + 30)
        x.append('Jul', m := m + 31)
        x.append('Aug', m := m + 31)
        x.append('Sep', m := m + 30)
        x.append('Oct', m := m + 31)
        x.append('Nov', m := m + 30)
        x.append('Dec', m := m + 31)
        if m != 365 and m != 366:
            print('Fuck')
        x.setRange(1, m)
        x.setTitleText("Month")
        chart.addAxis(x, Qt.AlignBottom)
        series.attachAxis(x)

        y = QValueAxis()
        y.setRange(0, 40)
        chart.addAxis(y, Qt.AlignLeft)
        series.attachAxis(y)

        # chart.setTitle("Apple")
        chart.legend().setVisible(False)

        chartView = QChartView(chart)
        chartView.setRenderHint(QPainter.Antialiasing)

        self.Chart.addWidget(chartView)
