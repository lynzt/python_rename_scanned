import sys
from file_utils import *

scanned_dir = '~/Pictures/scanned'

def get_dir_files(url):

    r = requests.get(url)
    return r.text



def main():
    files = get_dir_files()

if __name__ == '__main__':
    sys.exit(main()
