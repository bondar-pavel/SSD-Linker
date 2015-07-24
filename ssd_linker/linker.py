import win32
import shutil


class Linker(object):
    """Move data between drives and create symlinks

    Just untested pseudo code for now to describe concept.
    """

    def __init__(ssd='C:\\', hdd='D:\\', linker_dir='_linker_'):
        self._ssd = ssd
        self._hdd = hdd
        self._linker_dir = linker_dir

    def move_data(self, source, destination):
        """Moves data from source to destination and creates symlink"""
        self.copy_file(source, destination)
        shutil.rmtree(source)
        self.create_link(destination, source)

    def move_data_back(self, source, destination):
        """Moves data back from destination to original source
        
        Moves data in two steps. At fist copy data back to original drive.
        After that remove symlink and move data back to source.
        Since now data on the same drive it should work as fast as rename.
        """
        tmp_source = source + self.ADDITION
        self.copy_file(destination, tmp_source)
        self.delete_symlink(source)
        move(tmp_source, source)

    def copy_file(self, source, desitnation):
        win32file.CopyFile(source, desitnation, 1)

    def create_link(self, data, symlink):
        win32file.CreateSymbolicLink(data, symlink, 1)

    def delete_symlink(self, symlink):
        win32file.DeleteFile(symlink)
