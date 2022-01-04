import os
import shutil

from update_pyc_head import UpdatePycHead


class ExtractObjectFile:
    def __init__(self):
        self.path = os.path.join(os.getcwd(), 'bucket')
        self.exe_name = None

    def get_exe_name(self):
        """get the EXE name
        """
        try:
            names = os.listdir(self.path)
            exe_name = []
            for i in names:
                if i.endswith('exe'):
                    exe_name.append(i.split('.exe')[0])
            return exe_name[0]
        except IndexError:
            print('Error:没有放入exe')

    def remove_file(self):
        """remove redundant file
        """
        file_path = os.path.join(self.path, f'{self.exe_name}.exe_extracted')
        for root, dirs, files in os.walk(file_path):
            for f in files:
                os.remove(os.path.join(root, f))

        shutil.rmtree(file_path)

        os.remove(os.path.join(self.path, 'struct'))
        os.remove(os.path.join(self.path, self.exe_name))
        return

    def get_target_file(self):
        """
        Run pyinstxtractor.py to get the .pyc file
        Get two target files
        """
        os.system(f'python ../packages/pyinstxtractor.py {self.exe_name}.exe')

        # move two target file to main path
        struct_path = os.path.join(self.path, f'{self.exe_name}.exe_extracted', 'struct')
        target_path = os.path.join(self.path, f'{self.exe_name}.exe_extracted', self.exe_name)
        shutil.move(struct_path, self.path)
        shutil.move(target_path, self.path)

    def decompiling(self):
        """
        decompiling
        """
        os.chdir(self.path)
        try:
            self.exe_name = self.get_exe_name()
            self.get_target_file()

            update_pyc_head = UpdatePycHead()
            update_pyc_head.restore_file(self.exe_name)

            os.system(f'uncompyle6  {self.exe_name}.pyc')
            os.system(f'uncompyle6  {self.exe_name}.pyc > {self.exe_name}.py')

            self.remove_file()
        except Exception as e:
            print(e)
