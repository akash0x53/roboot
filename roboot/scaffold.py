# vim: et ts=4 sw=4

import os

__all__ = ["create_project"]

def create_dir(paths):
    """ create dir at `path` """
    if isinstance(paths, basestring):
        paths = [paths]

    for path in paths:
        try:
            os.mkdir(path)
        except IOError, e:
            print(e)
        except OSError, oe:
            print(oe)

def create_project(project_name):
    """ create dir for `project_name` """
    cur = os.curdir
    high_level = [os.path.join(cur, project_name, _dir) for _dir in
                     ["env", "res", "lib", "tests", "docs", "scripts"]
                     ]

    create_dir(project_name)
    create_dir(high_level)

