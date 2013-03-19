'''
Created on Mar 19, 2013

@author: rittz
'''
import sys
from PySide.QtCore import *
from PySide.QtGui import *

class Simple_draw_window(QWidget):
    def __init__(self):
        QWidget.__init__(self, None)
        self.setWindowTitle("Simple Drawing")
        
    def paintEvent(self, e):
        p = QPainter()
        p.begin(self)
        
        p.drawPolygon([
            QPoint(70, 100) , QPoint(100, 110),
            QPoint(130,100) , QPoint(100, 150),])
        
        p.setPen(QColor(0, 0, 0))
        p.setBrush(QColor(0, 127, 0))
        p.drawPolygon([
            QPoint( 50, 50), QPoint(50, 100),
            QPoint( 100, 50), QPoint(100, 100),
        ])

def main():
    app = QApplication(sys.argv)

    w = Simple_draw_window()
    w.show()

    return app.exec_()

if __name__ == "__main__":
    sys.exit(main())
