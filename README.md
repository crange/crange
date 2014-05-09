Crange
======

Synopsis
--------
    crtags [options] {directory} [clang-args*]

    crange [options] identifier

Description
-----------
Crange is a tool to index and cross-reference C/C++ source code. It
can be used to generate tags database that can help with:

* Identifier definitions
* Identifier declaraions
* References
* Expressions
* Operators
* Symbols
* Source range

The source metadata collected by Crange can help with building tools
to provide cross-referencing, syntax highlighting, code folding and
deep source code search.


Command line options
--------------------

*crtags*

| Option                  | Description                                               |
| ----------------------- |:---------------------------------------------------------:|
|-a, --auto-include       | Automatically detect and add include paths (-Isrc/include)|
|-i, --show-ids           | Don't compute cursor IDs (very slow)                      |
|-m N, --max-depth=N      | Limit cursor expansion to depth N                         |
|-d FILE, --database=FILE | Create tags in database FILE                              |
|-j JOBS, --jobs=JOBS     | Specifies the number of jobs to run simultaneously        |
|-v, --verbose            | Enable verbose mode                                       |

*crange*

| Option                          | Description                                       |
| ------------------------------- |:-------------------------------------------------:|
|-d DATABASE, --database=DATABASE | Search for identifiers in database FILE           |
|-b, --show-body                  | Show complete body for the identifier             |
|--list-kinds                     | List all identifier kinds present in tag database |
|-k KIND, --kind=KIND             | Show identifiers of kind                          |
|--list-types                     | List all identifier types present in tag database |
|-t TYPE, --type=TYPE             | Show identifiers of type                          |
|-r, --refs                       | Show identifier references                        |
|-v, --verbose                    | Enable verbose mode                               |

Example usage
-------------
**Generating tags database for Linux 3.13.5**

    $ cd linux-3.13.5
    $ crtags -v -j 32 .
    Parsing fs/xfs/xfs_bmap_btree.c (count: 1)
    Indexing fs/xfs/xfs_bmap_btree.c (nodes: 379, qsize: 0)
    ...
    Parsing sound/soc/codecs/ak4641.h (count: 34348)
    Generating indexes
    $  

This would create a new file named tags.db containing all the
identified tags.

**Searching tags**

Search all declarations for identifier named tty_open

    $ crange device_create
    Location                  Line  Kind           Type           Spelling       Display                                                                           USR
    ----------------------  ------  -------------  -------------  -------------  --------------------------------------------------------------------------------  ------------------
    include/linux/device.h     942  FUNCTION_DECL  FUNCTIONPROTO  device_create  device_create(struct class *, struct device *, dev_t, void *, const char *, ...)  c:@F@device_create
    drivers/base/core.c       1754  FUNCTION_DECL  FUNCTIONPROTO  device_create  device_create(struct class *, struct device *, dev_t, void *, const char *, ...)  c:@F@device_create
    $ 

Search all references for identifier named tty_open

    $ crange -r device_create
    Location                     Line  Kind           Type             Spelling  Display        USR
    -------------------------  ------  -------------  -------------  ----------  -------------  ------------------
    drivers/dca/dca-sysfs.c        41  DECL_REF_EXPR  FUNCTIONPROTO              device_create  c:@F@device_create
    drivers/dca/dca-sysfs.c        41  CALL_EXPR      POINTER                    device_create  c:@F@device_create
    drivers/dca/dca-sysfs.c        70  DECL_REF_EXPR  FUNCTIONPROTO              device_create  c:@F@device_create
    drivers/dca/dca-sysfs.c        70  CALL_EXPR      POINTER                    device_create  c:@F@device_create
    drivers/scsi/pmcraid.c       5397  DECL_REF_EXPR  FUNCTIONPROTO              device_create  c:@F@device_create
    drivers/scsi/pmcraid.c       5397  CALL_EXPR      POINTER                    device_create  c:@F@device_create
    drivers/scsi/osst.c          5791  DECL_REF_EXPR  FUNCTIONPROTO              device_create  c:@F@device_create
    ...

Performance
-----------

Running crtags on Linux kernel v3.13.5 sources (containing 45K files,
size 614MB) took a little less than 7 hours (415m10.974s) on 32 CPU
Xeon server with 16GB of memory and 32 jobs. The generated tags.db
file was 22GB in size and contained 60,461,329 unique identifiers.

Installaion
-----------

    $ sudo python setup.py install
or
    $ sudo pip install crange


Also see
--------

* http://clang.llvm.org/get_started.html
* https://github.com/trolldbois/python-clang/tree/master/tests/cindex
* https://docs.python.org/2/library/multiprocessing.html
* http://clang.llvm.org/doxygen/group__CINDEX.html