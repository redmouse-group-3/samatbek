import os
import time


def print_properties(file_dir_path):
    print("path: %s" % file_dir_path)
    if os.path.isdir(file_dir_path):
        print("type: directory")
    else:
        extension = os.path.splitext(file_dir_path)[1]
        print("type: file")
        print("extension: %s" % extension)
    print("size: %s bytes" % os.stat(file_dir_path).st_size)
    print("last modified: %s" % time.ctime(os.path.getmtime(file_dir_path)))
    print("created: %s" % time.ctime(os.path.getctime(file_dir_path)))

path = raw_input('Enter path: ')
file_dir_name = raw_input('Enter directory or file name: ')
file_dir_path = os.path.join(path, file_dir_name)

if os.path.exists(file_dir_path):
    print_properties(file_dir_path)
else:
    print("directory or file doesn't exist")
