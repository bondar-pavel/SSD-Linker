import os
import sys
from PyQt4 import QtCore, QtGui, uic
from PyQt4.QtCore import pyqtSlot, SIGNAL, SLOT

import tree as hdd_tree


class MyWindow(QtGui.QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        uic.loadUi('main.ui', self)
        self.show()

    def index_to_path_array(self, index):
        dirs = []
        while (index.data().toString()):
            dirs.insert(0, str(index.data().toString()))
            index = index.parent()
        return dirs

    def isSsd(self, path):
        return len(path) > 10

    @pyqtSlot(QtCore.QPoint)
    def contextMenuRequested(self, point):
        menu         = QtGui.QMenu()
        index = self.treeView.indexAt(point)
        print index
        print dir(index)
        dirs = self.index_to_path_array(index)
        path = os.path.join(*dirs)
        print path
        if self.isSsd(path):
            action = menu.addAction("Move to SSD")
            self.connect(action, SIGNAL("triggered()"),
                         lambda: self._move_to_ssd(path))
        else:
            action = menu.addAction("Move to HDD")
            self.connect(action, SIGNAL("triggered()"),
                         lambda: self._move_to_hdd(path))
        property = menu.addAction("Property")
        self.connect(property, SIGNAL("triggered()"),
                     self,SLOT("_property()"))
        menu.exec_(self.mapToGlobal(point))

    @pyqtSlot()
    def _move_to_ssd(self, path):
        print "Moving to SSD: %s" % path
        self.show()

    @pyqtSlot()
    def _move_to_hdd(self, path):
        print "Moving to HDD: %s" % path
        self.show()

    @pyqtSlot()
    def _property(self):
        print "Checking properties"


def addItems(parent, elements):
     for text, children in elements:
        item = QtGui.QStandardItem(text)
        parent.appendRow(item)
        if children:
            addItems(item, children)


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    window = MyWindow()

    #tree = hdd_tree.list_dirs(3)
    #print tree

    model = QtGui.QDirModel()
    #addItems(model, tree)
    window.setWindowTitle('SSD Linker')
    window.treeView.setModel(model)
    window.treeView.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
    window.connect(window.treeView, SIGNAL("customContextMenuRequested(QPoint)"),
                   window, SLOT("contextMenuRequested(QPoint)"))
    window.show()
    sys.exit(app.exec_())
