import os
from clang.cindex import Index, TranslationUnit, CursorKind

class CrTags:
    "Class CrTags"

    def __init__(self):
        self.opts  = dict()
        self.args  = list()  # Arguments passed from the command line.
        self.ast   = dict()  # List containing nodes present in a source file.

    def __del__(self):
        self.ast.clear()
        
    def debug(self, message):
        if self.opts.verbose:
            print message

    def get_diag_info(self, diag):
        return { 'severity' : diag.severity,
                 'location' : diag.location,
                 'spelling' : diag.spelling,
                 'ranges' : diag.ranges,
                 'fixits' : diag.fixits }

    def get_cursor_id(self, cursor, cursor_list = []):
        if not self.opts.showIDs:
            return None
                
        if cursor is None:
            return None

        # FIXME: This is really slow. It would be nice if the index API exposed
        # something that let us hash cursors.
        for i,c in enumerate(cursor_list):
            if cursor == c:
                return i
        cursor_list.append(cursor)
        return len(cursor_list) - 1

    ###### Node's key reference:
    # 1.  location   : node's filename    
    # 2.  line       : location line number
    # 3.  column     : location column number
    # 4.  offset     : location offset
    # 5.  start_line : extent start line
    # 6.  start_col  : extent start column
    # 7.  end_line   : extent end line
    # 8.  end_col    : extent end column
    # 9.  kind_name  : node kind name
    # 10. type_name  : node type name
    # 11. spelling   : spelling
    # 12. display    : display
    # 13. is_def     : node is a definition?
    # 14. def        : USR of node's definition.
    # 15. is_static  : node is a static method?
    # 16. is_ref     : node is a reference?
    # 17. ref        : USR of node's that is referenced.
    # 18. usr        : USR of this node.
    ######
    def node_to_tuple(self, loc, node):
        definition = node.get_definition().get_usr() if node.get_definition() else None
        referenced = node.referenced.get_usr() if node.referenced else None
        return (loc,
                node.location.line,
                node.location.column,
                node.location.offset,
                node.extent.start.line,
                node.extent.start.column,
                node.extent.end.line,
                node.extent.end.column,
                node.kind.name,
                node.type.kind.name,
                node.spelling,
                node.displayname,
                node.is_definition(),
                definition,
                node.is_static_method(),
                node.kind.is_reference(),
                referenced,
                node.get_usr())

    def crangepath(self, loc):
        crpath = os.path.relpath(loc)
        if '..' in crpath:
            crpath = os.path.realpath(loc)
        return crpath

    def get_info(self, node, depth=0):
        if self.opts.maxDepth is not None and depth >= self.opts.maxDepth:
            children = None
        else:
            children = [self.get_info(c, depth+1)
                        for c in node.get_children()]

        loc = self.crangepath(str(node.location.file)) if node.location.file else None
        if loc is not None:
            if loc not in self.ast:
                self.ast[loc] = list()
            self.ast[loc].append(self.node_to_tuple(loc, node))
