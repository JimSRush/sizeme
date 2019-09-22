import urllib.request, urllib.parse, urllib.error
from PIL import ImageFile
import re
import csv
import os, sys, getopt


def getsizes(uri):
    # get file size *and* image size (None if not known)
    file = urllib.request.urlopen(uri)
    size = file.headers.get("content-length")
    if size:
        size = int(size)
    p = ImageFile.Parser()
    while 1:
        data = file.read(1024)
        if not data:
            break
        p.feed(data)
        if p.image:
            return (
                "Image file size: " + str(size),
                "Image dimensions: " + str(p.image.size),
                "Filename: " + uri,
            )
            break
    file.close()
    return size, None

def main(argv):
    baseURL = ""
    fileName = ""
    paths = []
    try:
        opts, args = getopt.getopt(argv, "hb:f:", ["baseURL=", "fileName="])

    except getopt.GetoptError:
        print("test.py -b <baseURL> -F <outputfile>")
        sys.exit(2)
    for opt, arg in opts:
        if opt == "-h":
            print("test.py -b <baseURL> -f <fileName>")
            sys.exit()
        elif opt in ("-b", "--baseURL"):
            baseURL = arg
        elif opt in ("-f", "--fileName"):
            fileName = arg
    f = open(fileName, "r")

    for x in f:
        paths.append(baseURL + x.rstrip())

    for uri in paths:
        print(getsizes(uri))

if __name__ == "__main__":
    main(sys.argv[1:])
