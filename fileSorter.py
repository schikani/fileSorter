#!/usr/bin/env python3

import os
import shutil
from sys import argv
import json


class FileSorter:

    def __init__(self):
        self.initialize()

    def initialize(self):
        for arg in argv[1:]:
            if arg == ".":
                arg = str(os.getcwd())
            if arg[-1] == "/":
                arg = arg[:-1]
            self.fileSorter(arg)

    @staticmethod
    def jsonRead():
        database = open("database.json", "r")
        j_read = json.load(database)
        database.close()
        return j_read

    @staticmethod
    def jsonWrite(_list, folder_name):
        _list.append(folder_name)
        _dictionary = {"Other": _list}
        with open("Other.json", "w") as write:
            json.dump(_dictionary, write)

    def folderName(self, name):
        found = False
        folder_name = name
        key_list = list(self.jsonRead()["type"].keys())

        for t in key_list:
            val_list = list(self.jsonRead()["type"][t])
            if folder_name in val_list:
                index = key_list.index(t)
                folder_name = key_list[index]
                found = True
                break

        _list = list()

        if not found:
            try:
                with open("Other.json", "r") as _read:
                    _r = json.load(_read)
                    for item in _r["Other"]:
                        _list.append(item)

                self.jsonWrite(_list, folder_name)

            except FileNotFoundError:
                self.jsonWrite(_list, folder_name)

            except json.decoder.JSONDecodeError:
                self.jsonWrite(_list, folder_name)

            folder_name = "Other"

        return folder_name

    def fileSorter(self, folder):
        if os.path.exists(folder):
            sorted_folder = folder + "_sorted"
            os.mkdir(sorted_folder)
            for root, dir_, files in os.walk(folder):
                for f in files:

                    i = f.rfind(".") + 1

                    if i == 0:
                        folder_name = f.lower()

                    else:
                        folder_name = f[i:].lower()

                    try:
                        folder_name = self.folderName(folder_name)
                        os.mkdir(os.path.join(sorted_folder, folder_name))
                        shutil.move(os.path.join(root, f), os.path.join(sorted_folder, folder_name))

                    except FileExistsError:
                        shutil.move(os.path.join(root, f), os.path.join(sorted_folder, folder_name))

            shutil.rmtree(folder)
            os.rename(sorted_folder, folder)
            print(f"'{folder}' is sorted!")

        else:
            print(f"'{folder}' does not exist!")


if __name__ == "__main__":
    FileSorter()
