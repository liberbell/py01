import os
from os import path
import shutil

def main():
    if path.exists('textfile.txt'):
        src = path.realpath('textfile.txt')

        dst = src + '.bak'

        # shutil.copy(src, dst)
        # shutil.copystat(src, dst)

        os.rename('textfile.txt', 'newfile.txt')


if __name__ == '__main__':
    main()