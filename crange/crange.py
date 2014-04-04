from tabulate import tabulate
from .tag import Tag

class Crange:
    def __init__(self):
        pass

    def __del__(self):
        pass
                    
    def process(self, opts, args):
        tag = Tag(opts.database)
        res = ""
        
        if opts.tagListKinds:
            res = tabulate(tag.find_kinds(), headers=["Kinds"])
        elif opts.tagListTypes:
            res = tabulate(tag.find_types(), headers=["Types"])
        elif len(args) > 0:
            if opts.tagRefs:
                res = tabulate(tag.find_refs(args[0]), headers=tag.headers)
            else:
                res = tabulate(tag.find(args[0]), headers=tag.headers)
        print "Not found" if (not res or res.isspace()) else res
