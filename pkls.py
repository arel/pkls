#! /usr/bin/env python

import sys
import pprint
import argparse
import importlib
import cPickle


parser = argparse.ArgumentParser(description="List contents of a pickle file")
parser.add_argument('files', metavar='FILE', type=unicode, nargs='+',
                   help='Pickle files to list.')


def make_stub(module_name, class_name):
    """
    Return a dummy class, given a module name and class name.
    Its representation is the (pretty-printed) pickled state of the object.

    :param str module_name:
        The module name to display this class as.

    :param str class_name:
        The class name to display this class as.

    :returns:
        A "stub" class with the given names.
    """

    class StubObject(object):

        def __init__(self, *args, **kwargs):
            self.state = None

        def __repr__(self):

            cls_str = "%s.%s" % (module_name, class_name)

            if getattr(self, 'state', None):
                pp = pprint.PrettyPrinter(indent=4)
                contents = pp.pformat(self.state)
                newline = "\n" if "\n" in contents else ""
                cls_str += " : %s%s" % (newline, contents)

            return cls_str

        def __setstate__(self, state):
            StubObject.__init__(self)
            self.state = state

    # rename stub class
    StubObject.__name__ = class_name

    return StubObject


def safe_load(fileobject):
    """
    Unpickles an object, stubbing objects not in the python path.

    :param file fileobject:
        An open file to load.

    :returns:
        The unpickled object in the file.
    """

    def _find_global(module_name, class_name):

        try:
            module = importlib.import_module(module_name)
            return getattr(module, class_name)
        except:
            print >> sys.stderr, "stubbing %s.%s" % (module_name, class_name)
            return make_stub(module_name, class_name)

    unpickler = cPickle.Unpickler(fileobject)
    unpickler.find_global = _find_global

    return unpickler.load()


def main(args):
    
    pp = pprint.PrettyPrinter(indent=4)
    for fn in args.files:
        with open(fn) as f:
            obj = safe_load(f)

            print fn
            print pp.pformat(obj)
            print


if __name__ == '__main__':
    args = parser.parse_args()
    sys.exit(main(args))
