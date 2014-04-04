from optparse import OptionParser

DEFAULT_OUTPUT_FILE = "tags.db"

def crange_parser():
    parser = OptionParser("usage: %prog [options] identifier")
    parser.add_option("-d", "--database",  dest="database", metavar="DATABASE", type="string", default=DEFAULT_OUTPUT_FILE, help="Search for identifiers in database FILE")
    parser.add_option("-b", "--show-body", dest="showBody", default=False, action="store_true", help="Show complete body for the identifier")
    parser.add_option("",   "--list-kinds",dest="tagListKinds", default=False, action="store_true", help="List all identifier kinds present in tag database")
    parser.add_option("-k", "--kind",      dest="tagKind", metavar="KIND", type="string", help="Show identifiers of kind")
    parser.add_option("",   "--list-types",dest="tagListTypes", default=False, action="store_true", help="List all identifier types present in tag database")
    parser.add_option("-t", "--type",      dest="tagType", metavar="TYPE", type="string", help="Show identifiers of type")
    parser.add_option("-r", "--refs",      dest="tagRefs", default=False, action="store_true", help="Show identifier references")
    parser.add_option("-v", "--verbose",   dest="verbose", default=False, action="store_true", help="Enable verbose mode")
    parser.disable_interspersed_args()
    return parser

def crtags_parser():
    parser = OptionParser("usage: %prog [options] {directory} [clang-args*]")
    parser.add_option("-a", "--auto-include", dest="autoInclude" ,default=False, action="store_true", help="Automatically detect and add include paths (-Isrc/include)")
    parser.add_option("-i", "--show-ids", dest="showIDs", default=False, action="store_true", help="Don't compute cursor IDs (very slow)")
    parser.add_option("-m", "--max-depth", dest="maxDepth", metavar="N", type="int", default=None, help="Limit cursor expansion to depth N")
    parser.add_option("-d", "--database", dest="outputFile", metavar="FILE", type="string", default=DEFAULT_OUTPUT_FILE, help="Create tags in database FILE")
    parser.add_option("-j", "--jobs", dest="jobs", metavar="JOBS", type="int", default=1, help="Specifies the number of jobs to run simultaneously")
    parser.add_option("-v", "--verbose", dest="verbose", default=False, action="store_true", help="Enable verbose mode")
    parser.disable_interspersed_args()
    return parser

