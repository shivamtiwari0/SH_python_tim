import fnmatch
import os


def find_file(start, ext):
    for path, directories, files in os.walk(start):
        for file in fnmatch.filter(files, ext):
            absolute_path = os.path.abspath(path)
            yield os.path.join(absolute_path, file)


root = "/Users/shivamtiwari/Downloads/"
var = find_file(root, "*.mp4")

for a in var:
    print(a)

