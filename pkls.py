#! /usr/bin/env python

import sys
import pprint
import argparse
import cPickle as pickle 


parser = argparse.ArgumentParser(description="List contents of a pickle file")
parser.add_argument('files', metavar='FILE', type=unicode, nargs='+',
                   help='Pickle files to list.')


def main(args):
    pp = pprint.PrettyPrinter(indent=4)
    for fn in args.files:
        with open(fn) as f:
            obj = pickle.load(f)

            print fn
            print pp.pformat(obj)
            print


if __name__ == '__main__':
    args = parser.parse_args()
    sys.exit(main(args))