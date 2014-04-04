import os
import fnmatch

class SourceFile:
    def __init__(self):
        self.extensions = ['*.c', '*.h', '*.C', '*.H',
                           '*.c++', '*.cc', '*.cp', '*.cpp', '*.cxx',
                           '*.h++', '*.hh', '*.hp', '*.hpp', '*.hxx']

    def locate(self, root):
        '''Locate all C/C++ files matching extensions attribute.
        '''
        for path, dirs, files in os.walk(os.path.relpath(root)):
            for extension in self.extensions:
                for filename in fnmatch.filter(files, extension):
                    yield os.path.join(os.path.relpath(path), filename)
