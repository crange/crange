"""
Unit tests for crange module
"""
import sys
from os.path import dirname, abspath, join
sys.path.append(join(dirname(abspath(__file__)), '..'))

from unittest import TestCase, main
from mock import Mock
from operator import eq
from crange import *

class SourceFile(TestCase):

    def setUp(self):
        self.root  = join( dirname(abspath(__file__)), 'testdata')
        self.sf    = sourcefile.SourceFile()
        self.files = ['tests/testdata/file1.c', 'tests/testdata/header1.h', 'tests/testdata/file2.cpp']

    def test_locate_source_files_generator(self):
        source_files = self.sf.locate(self.root)
        self.assertEquals(type(source_files).__name__, 'generator')

    def test_locate_source_files(self):
        source_files = list(self.sf.locate(self.root))
        self.assertEquals(sorted(source_files), sorted(self.files))


class Tag(TestCase):

    def setUp(self):
        pass

    def test_find(self):
        pass    

class TagDB(TestCase):

    def setUp(self):
        pass

    def test_init(self):
        pass
        
    def test_create_index(self):
        pass

    def test_persist(self):
        pass
        
class Options(TestCase):

    def setUp(self):
        pass

    def test_crange_parser(self):
        pass
        
    def test_crtags_parser(self):
        pass

class Crange(TestCase):

    def setUp(self):
        pass

    def test_process(self):
        pass

class CrTags(TestCase):

    def setUp(self):
        pass

    def test_crtags(self):
        pass    

    def test_crangepath(self):
        pass

    def test_get_diag_info(self):
        pass


if __name__ == "__main__":
    main()
