#!/usr/bin/env python

import os
from crange import *

if __name__ == '__main__':
    parser = crange_parser()
    opts, args = parser.parse_args()
    
    if opts.tagListKinds == False and opts.tagListTypes == False and len(args) == 0:
        parser.error('Invalid arguments. Try --help for more information.')

    if not os.path.isfile(opts.database):
        parser.error("%s is not a file" % opts.database)
    else:
        c = Crange()
        c.process(opts, args)
