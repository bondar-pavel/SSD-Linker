import sys
from PyQt4 import QtGui, uic
from PyQt4.QtCore import *
from PyQt4.QtGui import *

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

import os
def buildTree(dir, deep=1):
    if not os.path.isdir(dir) or not os.access(dir, os.R_OK) or deep < 0:
        return []
    return [(name, buildTree(os.path.join(dir, name), deep - 1))
            for name in os.listdir(dir)]

def get_drives():
    import win32api
    drives = win32api.GetLogicalDriveStrings()
    drives = drives.split('\000')[:-1]
    print drives
    return drives

def list_dirs(deep=1):
    if sys.platform == "win32":
        drives = get_drives()
        return [(name, buildTree(name, deep - 1))
                for name in drives]
    else:
        return buildTree('/', deep)

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    window = MyWindow()

    model = QStandardItemModel()
    tree = list_dirs()
    print tree
    addItems(model, tree)
    window.treeView.setModel(model)
    sys.exit(app.exec_())
