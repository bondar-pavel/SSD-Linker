import sys
from PyQt4 import QtCore, QtGui, uic

import tree as hdd_tree


class MyWindow(QtGui.QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        uic.loadUi('main.ui', self)
        self.show()

def addItems(parent, elements):
     for text, children in elements:
        item = QtGui.QStandardItem(text)
        parent.appendRow(item)
        if children:
            addItems(item, children)

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    window = MyWindow()

    model = QtGui.QStandardItemModel()
    tree = hdd_tree.list_dirs(3)
    print tree
    addItems(model, tree)
    window.treeView.setModel(model)
    sys.exit(app.exec_())
