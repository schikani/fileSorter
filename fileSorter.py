#!/usr/bin/env python3

import os
import shutil
from sys import argv


def folderName(name):
    i = name.rfind(".") + 1
    if i == 0:
        folder_name = name
    else:
        folder_name = name[i:]

    return folder_name


def fileSorter(folder):
    sorted_folder = folder + "_sorted"
    os.mkdir(sorted_folder)

    for root, dir_, files in os.walk(folder):
        for f in files:
            try:
                os.mkdir(os.path.join(sorted_folder, folderName(f)))
                shutil.move(os.path.join(root, f), os.path.join(sorted_folder, folderName(f)))
            except FileExistsError:
                shutil.move(os.path.join(root, f), os.path.join(sorted_folder, folderName(f)))

    shutil.rmtree(folder)
    os.rename(sorted_folder, folder)


if __name__ == "__main__":
    for arg in argv[1:]:
        if arg == ".":
            cwd = os.getcwd()
            arg = cwd
        if arg[-1] == "/":
            arg = arg[:-1]
        fileSorter(arg)
        print(f"'{arg}' is sorted!")
