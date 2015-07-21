import os
import sys


def buildTree(dir, deep=1):
    ok_for_read = (deep > 0 and os.path.isdir(dir)
                   and os.access(dir, os.R_OK))
    if not ok_for_read:
        return []

    # From my findings it isimpossible to check if directory is accessible 
    # prior to reading it.
    # os.access does not cover all permission issues.
    try:
        dirs = os.listdir(dir)
    except WindowsError:
        return []

    return [(name, buildTree(os.path.join(dir, name), deep - 1))
            for name in dirs]

def get_drives():
    import win32api
    drives = win32api.GetLogicalDriveStrings()
    drives = drives.split('\000')[:-1]
    return drives

def list_dirs(deep=1):
    if sys.platform == "win32":
        drives = get_drives()
        return [(name, buildTree(name, deep - 1))
                for name in drives]
    else:
        return buildTree('/', deep)
