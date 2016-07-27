#!/usr/bin/env python

import random
import numpy as np
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

from PyQt5.QtCore import (QLineF, QPointF, QRectF, Qt, QTimer)
from PyQt5.QtGui import (QBrush, QColor, QPainter)
from PyQt5.QtWidgets import (QApplication, QGraphicsView, QGraphicsScene, QGraphicsItem,
                             QGridLayout, QVBoxLayout, QHBoxLayout, QSizePolicy,
                             QLabel, QLineEdit, QPushButton, QMainWindow, QWidget)

# FigureCanvas inherits QWidget
class Canvas(FigureCanvas):
    def __init__(self, parent=None, width=4, height=3, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        self.axes2 = fig.add_subplot(111)

        super(Canvas, self).__init__(fig)
        self.setParent(parent)

        FigureCanvas.setSizePolicy(self,
                                   QSizePolicy.Expanding,
                                   QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)

        timer = QTimer(self)
        timer.timeout.connect(self.update_figure)
        timer.start(500)

        self.x  = tbx
        self.y  = tby

        self.setWindowTitle(sys.argv[1])

    def update_figure(self):
        self.axes.clear()
        self.axes.plot(self.x, self.y, 'bo')
        if hasattr(self, 'x2'):
            self.axes2.plot(self.x2, self.y2, 'ro')
        self.draw()

class MainWindow(QMainWindow):

    def __init__(self, parent=None):

        super(MainWindow, self).__init__(parent)
        self.form_widget = FormWidget(self) 
        self.setCentralWidget(self.form_widget)

class FormWidget(QWidget):

    def __init__(self, parent):        
        super(FormWidget, self).__init__(parent)
        self.layout = QVBoxLayout(self)

        self.canvas = Canvas()
        self.layout.addWidget(self.canvas)

        self.blm_btn = QPushButton("Black Lives Matter")
        self.blm_btn.clicked.connect(self.blmGraph)
        self.layout.addWidget(self.blm_btn)

        self.maga_btn = QPushButton("Make America Great Again")
        self.maga_btn.clicked.connect(self.magaGraph)
        self.layout.addWidget(self.maga_btn)

        self.setLayout(self.layout)

        self.blmon = True
        self.magaon = False

    def blmGraph(self):
        if self.blmon:
            self.blmon = False
            self.canvas.x = []
            self.canvas.y = []
        else:
            self.blmon = True
            self.canvas.x = tbx
            self.canvas.y = tby

    def magaGraph(self):
        if self.magaon:
            self.magaon = False
            self.canvas.x2 = []
            self.canvas.y2 = []
        else:
            self.magaon = True
            self.canvas.x2 = tbx2
            self.canvas.y2 = tby2

if __name__ == '__main__':
    import sys
    f = open(str(sys.argv[1]) + "_results")
    tb = [eval(x) for x in f.read().split("\n")]
    tbx = [x[0] for x in tb]
    tby = [x[1] for x in tb]
    f = open(str(sys.argv[2]) + "_results")
    tb = [eval(x) for x in f.read().split("\n")]
    tbx2 = [x[0] for x in tb]
    tby2 = [x[1] for x in tb]
    app = QApplication(sys.argv)
    mainWindow = MainWindow()

    mainWindow.show()
    sys.exit(app.exec_())