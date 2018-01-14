import os
import re
import sys
from file_utils import file_utils

def get_dir_files(path):
    ctime = lambda f: os.stat(os.path.join(path, f)).st_ctime
    files = list(sorted(file_utils.get_files_in_directory_skip_hidden(path), key=ctime)) # files listed in created order

    regex = re.compile(r'Scan(\s\d+)?')
    return list(filter(regex.match, files)) # don't rename files already renamed


def rename_files(files, starting_nbr, tmp_dir):
    for filename in files:
        print ('renaming {}'.format(filename))
        file_utils.move_file(tmp_dir + filename, tmp_dir + 'scan_' + str(starting_nbr) + '.jpeg')
        starting_nbr += 1

def main():
    starting_nbr = 100761 # this could be figured out... meh
    tmp_dir = '/tmp/'

    files = get_dir_files(tmp_dir)
    rename_files(files, starting_nbr, tmp_dir)

if __name__ == '__main__':
    main()

# docker run -it --rm -v "$PWD":/usr/src/app -v "/Users/lynzt/Pictures/scanned":/tmp py/rename python3 ./rename_pics.py
