#!/usr/bin/env python3

import sys
import argparse

from . import files
from . import finder


def run(filepath, encoding='utf-8', *, linemode=False, exitmode=False,
        unicodepoints=False, asciionly=False):
    filetype = files.guess(filepath)
    tmpl = "{: >3d}  {: >3d}  {}  {}"

    with open(filepath, 'r', encoding=encoding) as fd:
        for char in finder.find(fd, filetype=filetype):
            if exitmode:
                return 1
            elif linemode:
                character = char.unicode_point if unicodepoints else char.character
                print(tmpl.format(char.lineno, char.colno, character, char.description))
            elif asciionly:
                print(char.asciionly())
            else:
                print(str(char))

    return 0


def main():
    parser = argparse.ArgumentParser(description='Print all non-ascii characters in this file')
    parser.add_argument('file', help='the file to read from')
    parser.add_argument('-a', '--ascii-only', dest='asciionly', action='store_true',
        help='only write ASCII to stdout')
    parser.add_argument('-c', '--exit-code', dest='exitcode', action='store_true',
        help='do not print anything, non-zero exit code indicates existence of nonascii character')
    parser.add_argument('-e', '--encoding', help='encoding of the file (default: utf-8)')
    parser.add_argument('-l', '--list', action='store_true',
        help='print character line-by-line instead of human-readable')
    parser.add_argument('-u', '--unicode-point', dest='unipoint', action='store_true',
        help='print Unicode point instead of character itself')

    args = parser.parse_args()
    if args.list and args.exitcode:
        print("Cannot use --list and --exit-code together")
        sys.exit(1)

    if args.exitcode and args.unipoint:
        print("Cannot use --unicode-point and --exit-code together")
        sys.exit(1)

    sys.exit(run(args.file, args.encoding, linemode=args.list,
        exitmode=args.exitcode, unicodepoints=args.unipoint,
        asciionly=args.asciionly))


if __name__ == "__main__":
    main()
