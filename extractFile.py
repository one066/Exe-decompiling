import os
import shutil
from textProcessing import text_processing

class extract_object_file:

    def __init__(self):
        self.path = os.getcwd()

    def get_exe_name(self):
        '''
        Get the EXE name
        '''
        try:
            names = os.listdir(self.path)
            name = []
            for i in names:
                if i.endswith('exe'):
                    name.append(i)
            return name[0]
        except IndexError:
            print('Error:没有放入exe')


    def run_pyinstxtractor(self, name):
        '''
        Run pyinstxtractor.py to get the .pyc file
        Get two target files
        '''
        os.system(f'python pyinstxtractor.py {name}')

        new_path = self.path + '\\' + name + '_extracted'

        shutil.move(new_path + '\\' + 'struct',self.path)
        shutil.move(new_path + '\\' + name.split('.')[0], self.path)

        for root, dirs, files in os.walk(new_path):
            for f in files:
                os.remove(os.path.join(root, f))

        shutil.rmtree(new_path)

    def uncompyle_pyc(self):
        '''
        Compile the .pyc file with uncompyle
        '''

        name = self.get_exe_name()
        self.run_pyinstxtractor(name)
        text_processing().restore_file(name.split(".")[0])
        os.system(f'uncompyle6  {name.split(".")[0] + ".pyc"}')
        os.system(f'uncompyle6  {name.split(".")[0] + ".pyc"} > {name.split(".")[0] + ".py"}')

        os.remove(self.path + '\\' + 'struct')
        os.remove(self.path + '\\' + f'{name.split(".")[0]}')

if __name__ == '__main__':
    extract_object_file().uncompyle_pyc()
