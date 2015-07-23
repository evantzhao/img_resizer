#!/usr/bin/env python3
from __future__ import print_function
from PIL import Image
import os

def main():
    path = "bleh"
    cycle(path)

# Cycles through every single folder in the path, converting each file to an excel file.
def cycle(source):
    home = os.path.expanduser('~')
    folder_path = home + "/Desktop/" + source + "/"

    for x in range(0, len(seek(folder_path))):
        try:
            ratio = 9/16
            im=Image.open("%s%s" % (folder_path, seek(folder_path)[x]))
            convert(im, ("%s%s" % (folder_path, seek(folder_path)[x])))
        except:
            pass

# Finds all files within a folder. Argument takes a directory path.
def seek(path):
    files = os.listdir(path)
    return files

def convert(picture, path):
    size = picture.size
    ta = (size[1] + size[0]) / 25
    x = int(16 * ta)
    y = int(9 * ta)
    out = picture.resize((x,y))
    nsize = out.size
    print(nsize[1] / nsize[0])
    out.save(path, "JPEG")


# Runs the main, after establishing that this is not a library.
if __name__ == "__main__":
    main()
