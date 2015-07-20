import os
import sys

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