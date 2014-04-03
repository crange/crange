
#: Version info (major, minor, maintenance, status)
VERSION = (0, 0, 1)
STATUS = ''
__version__ = ('%d.%d.%d' % VERSION[0:3]) + STATUS

import sys as _sys

if _sys.version_info[0:2] < (2, 4):
    raise RuntimeError('Python 2.4.x or higher is required!')
