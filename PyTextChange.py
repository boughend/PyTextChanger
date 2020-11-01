import os
import glob
import shutil


class PyTextChange:
    py_dir = './py_file'.replace('/', os.sep)
    txt_dir = './txt_file'.replace('/', os.sep)
    ext_txt = 'txt'

    def __init__(self):
        pass

    def change_py_to_text(self, ext=ext_txt):
        py_list = glob.glob(self.py_dir + "/*")

        if not py_list:
           return self.exception_no_file()

        for py_file in py_list:
            py_name = os.path.basename(py_file)
            print py_name
            base_name, old_ext = os.path.splitext(py_name)
            txt_name = base_name + '.' + ext
            txt_path = os.path.join(self.txt_dir, txt_name)
            py_path = os.path.join(self.py_dir, py_name)
            print 'copy of [' + py_name + '] to [' + txt_name + ']'
            shutil.copyfile(py_path, txt_path)
        return 0

    def exception_no_file(self):
        print '[ERROR] python file is not exists of :' + self.py_dir
        return -1


if __name__ == '__main__':
    a = PyTextChange()
    a.change_py_to_text()
