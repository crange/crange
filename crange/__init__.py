import sys

#: Version info (major, minor, maintenance, status)
VERSION = (0, 1, 1)
STATUS = ''
__version__ = ('%d.%d.%d' % VERSION[0:3]) + STATUS

if sys.version_info[0:2] < (2, 6):
    raise RuntimeError('Python 2.6.x or higher is required!')

from .crange import Crange
from .crtags import CrTags
from .sourcefile import SourceFile
from .tag import Tag
from .tagdb import TagDB
from .options import *
