
import os
import re
import shutil


def get_global_filepaths(root_dir):
    ls = os.listdir(root_dir)
    paths = [os.path.join(root_dir, c) for c in ls]
    lses = [[path] if os.path.isfile(path) else get_global_filepaths(path)
            for path in paths]
    filepaths = sum(lses, [])
    return filepaths


def get_global_dir_paths(root_dir):
    ls = os.listdir(root_dir)
    paths = [os.path.join(root_dir, c) for c in ls]
    lses = [[path, *get_global_dir_paths(path)]
            for path in paths if os.path.isdir(path)]
    dir_paths = sum(lses, [])
    return dir_paths


def clear_current_dir(blacklist):
    for black in blacklist:
        print("[%s]" % black)
        parser = re.compile('(.*?[\\\\/]'+black+')([\\\\/].*|$)')
        paths = get_global_filepaths('.')+get_global_dir_paths('.')
        paths = [parser.search(v).group(1) for v in paths if parser.search(v)]
        paths = sorted(set(paths))
        for path in paths:
            if os.path.isdir(path):
                shutil.rmtree(path)
            else:
                os.remove(path)
            print(path)
