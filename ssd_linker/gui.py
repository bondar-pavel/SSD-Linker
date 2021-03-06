import os
import sys
from PyQt4 import QtCore, QtGui, uic
from PyQt4.QtCore import pyqtSlot, SIGNAL, SLOT

import linker


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

    def get_os_specific_dirs(self, raw_dirs):
        if sys.platform == "win32" and raw_dirs:
            raw_dirs.insert(1, '\\')
        return raw_dirs

    def isSsd(self, path):
        return len(path) > 10

    @pyqtSlot(QtCore.QPoint)
    def contextMenuRequested(self, point):
        menu         = QtGui.QMenu()
        index = self.treeView.indexAt(point)
        print index
        print dir(index)
        model = self.treeView.model()
        info = model.fileInfo(index)
        print dir(info)
        print "Info %s" % info.filePath()
        print "Info %s" % info.canonicalFilePath()
        print "Dir %s" % info.dir()
        raw_dirs = self.index_to_path_array(index)
        dirs = self.get_os_specific_dirs(raw_dirs)
        path = os.path.join(*dirs) if dirs else ''
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
        my_linker = linker.Linker()
        my_linker.move_to_ssd(path)

    @pyqtSlot()
    def _move_to_hdd(self, path):
        print "Moving to HDD: %s" % path
        my_linker = linker.Linker()
        my_linker.move_to_ssd(path)

    @pyqtSlot()
    def _property(self):
        print "Checking properties"


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    window = MyWindow()

    model = QtGui.QDirModel()
    window.setWindowTitle('SSD Linker')
    window.treeView.setModel(model)
    window.treeView.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
    window.connect(window.treeView, SIGNAL("customContextMenuRequested(QPoint)"),
                   window, SLOT("contextMenuRequested(QPoint)"))
    window.show()
    sys.exit(app.exec_())
