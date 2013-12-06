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

    class StubObject(object):

        def __init__(self, *args, **kwargs):
            self.args = args
            self.kwargs = kwargs

        def __repr__(self):
            cls_str = "%s.%s" % (module_name, class_name)

            if hasattr(self, 'args'):
                arg_str = ", ".join(self.args)
                cls_str += " (%s)" % arg_str

            if hasattr(self, 'kwargs'):
                kwarg_str = ", ".join("%s=%s" % (k,v) for k,v in self.kwargs.iteritems())
                cls_str += " (%s)" % kwarg_str

            return cls_str

    # rename stub class
    StubObject.__name__ = class_name

    return StubObject


def safe_load(fileobject):

    def _find_global(module_name, class_name):

        try:
            module = importlib.import_module(module_name)
            return getattr(module, class_name)
        except:
            print >> sys.stderr, "stubbing", module_name, class_name
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
