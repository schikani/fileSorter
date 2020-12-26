import os
import shutil
from sys import argv


def fileSorter(folder):
    sorted_folder = folder + "_sorted"
    os.mkdir(sorted_folder)
    mkdir_ = set()

    for root, dir_, files in os.walk(folder):
        for f in files:
            try:
                mkdir_.add(f.split(".")[1])
            except IndexError:
                mkdir_.add(f)

    for m in mkdir_:
        os.mkdir(os.path.join(sorted_folder, m))

    for root, dir_, files in os.walk(folder):
        for f in files:
            try:
                shutil.move(os.path.join(root, f), os.path.join(sorted_folder, f.split(".")[1]))
            except IndexError:
                shutil.move(os.path.join(root, f), os.path.join(sorted_folder, f))

    shutil.rmtree(folder)
    os.rename(sorted_folder, folder)
    print("Done!")


if __name__ == "__main__":
    argv_ = argv[1]
    if argv_[-1] == "/":
        argv_ = argv_[:-1]
    fileSorter(argv_)
