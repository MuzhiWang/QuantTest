from os import listdir
from os.path import isfile, join

def get_all_files(path: str):
    return [f for f in listdir(path) if isfile(join(path, f))]