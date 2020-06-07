import os
import sys

class Folder:
    def __init__(self, path):
        if not os.path.exists(path):
            raise ValueError('Path specified in class argument does not exist')
        if not os.path.isdir(path):
            raise ValueError('Path is not a directory')
        self.path = path
        self._children = []


class File:
    def __init__(self, path):
        if not os.path.exists(path):
            raise ValueError('Path specified in class argument does not exist')
        if not os.path.isfile(path):
            raise ValueError('Path is not a file')
        self.path = path
        self.name = os.path.split(path)[-1]
    
    def __str__(self):
        return f'File: {self.name}'

    def get_extension(self):
        return self.name.split('.')[-1]

    def get_content(self):
        with open(self.path, 'r') as file:
            content = file.readlines()
        return content
    

test = File('hello/man/woman/test.txt')
def list_files(startpath):
    for root, dirs, files in os.walk(startpath):
        level = root.replace(startpath, '').count(os.sep)
        indent = ' ' * 4 * (level)
        print('{}{}/'.format(indent, os.path.basename(root)))
        subindent = ' ' * 4 * (level + 1)
        for f in files:
            print('{}{}'.format(subindent, f))

list_files('.')