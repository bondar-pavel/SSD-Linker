import sys
from PyQt4 import QtGui, uic
from PyQt4.QtCore import *
from PyQt4.QtGui import *

import tree as hdd_tree

data = [
    ("Alice", [
        ("Keys", []),
        ("Purse", [
            ("Cellphone", [])
            ])
        ]),
    ("Bob", [
        ("Wallet", [
            ("Credit card", []),
            ("Money", [])
            ])
        ])
    ]

class MyWindow(QtGui.QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        uic.loadUi('main.ui', self)
        self.show()

def addItems(parent, elements):
     for text, children in elements:
        item = QStandardItem(text)
        parent.appendRow(item)
        if children:
            addItems(item, children)

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    window = MyWindow()

    model = QStandardItemModel()
    tree = hdd_tree.list_dirs()
    print tree
    addItems(model, tree)
    window.treeView.setModel(model)
    sys.exit(app.exec_())
