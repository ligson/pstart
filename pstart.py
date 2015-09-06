# -*- coding: UTF-8 -*-
__author__ = 'Administrator'
import os
import index


def treePath(file):
    path = file.decode("UTF-8")
    print(path)
    if os.path.isfile(path):
        print(path)
        index.add_doc(path)

    else:
        for f in os.listdir(path):
            treePath(os.path.join(path, f))


if __name__ == '__main__':
    treePath("E:\workspace\pythonproj\pstart")
    index.commit()
