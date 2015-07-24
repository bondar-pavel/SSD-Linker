import os
import win32file
import shutil


class Linker(object):
    """Move data between drives and create symlinks

    Just untested pseudo code for now to describe concept.
    """

    def __init__(self, ssd='C:\\', hdd='D:\\', linker_dir='_linker_'):
        self._ssd = ssd
        self._hdd = hdd
        self._linker_dir = linker_dir
        ssd_sys_dir = self._ssd + self._linker_dir
        if not os.path.isdir(ssd_sys_dir):
            os.makedirs(ssd_sys_dir)

    def move_to_ssd(self, source):
        s_dir = '\\34324'
        ssd_dir = self._ssd + self._linker_dir + s_dir
        self.move_data(source, ssd_dir)

    def move_data(self, source, destination):
        """Moves data from source to destination and creates symlink"""
        print "Moving from %s" % source
        print "to %s" % destination
        shutil.copytree(source, destination)
        shutil.rmtree(source)
        self.create_link(destination, source)

    def move_data_back(self, source, destination):
        """Moves data back from destination to original source
        
        Moves data in two steps. At fist copy data back to original drive.
        After that remove symlink and move data back to source.
        Since now data on the same drive it should work as fast as rename.
        """
        tmp_source = self._hdd + self._linker_dir
        self.copy_file(destination, tmp_source)
        self.delete_symlink(source)
        move(tmp_source, source)

    def copy_file(self, source, destination):
        win32file.CopyFile(source, destination, 1)

    def create_link(self, source, link_name):
        os_symlink = getattr(os, "symlink", None)
        if callable(os_symlink):
            os_symlink(source, link_name)
        else:
            import ctypes
            csl = ctypes.windll.kernel32.CreateSymbolicLinkW
            csl.argtypes = (ctypes.c_wchar_p, ctypes.c_wchar_p, ctypes.c_uint32)
            csl.restype = ctypes.c_ubyte
            flags = 1 if os.path.isdir(source) else 0
            if csl(link_name, source, flags) == 0:
                raise ctypes.WinError()

    def delete_symlink(self, symlink):
        win32file.DeleteFile(symlink)
