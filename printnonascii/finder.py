#!/usr/bin/env python3

import _io
import unicodedata

from .char import Character

UNICODE_CATEGORIES = {
    # Normative
    'Lu': 'Letter Uppercase',
    'Ll': 'Letter Lowercase',
    'Lt': 'Letter Titlecase',
    'Mn': 'Mark Non-Spacing',
    'Mc': 'Mark Spacing Combining',
    'Me': 'Mark Enclosing',
    'Nd': 'Number Decimal Digit',
    'Nl': 'Number Letter',
    'No': 'Number Other',
    'Zs': 'Separator Space',
    'Zl': 'Separator Line',
    'Zp': 'Separator Paragraph',
    'Cc': 'Other Control',
    'Cf': 'Other Format',
    'Cs': 'Other Surrogate',
    'Co': 'Other Private Use',
    'Cn': 'Other Not Assigned',

    # Informative
    'Lm': 'Letter Modifier',
    'Lo': 'Letter Other',
    'Pc': 'Punctuation Connector',
    'Pd': 'Punctuation Dash',
    'Ps': 'Punctuation Open',
    'Pe': 'Punctuation Close',
    'Pi': 'Punctuation Initial quote',
    'Pf': 'Punctuation Final quote',
    'Po': 'Punctuation Other',
    'Sm': 'Symbol Math',
    'Sc': 'Symbol Currency',
    'Sk': 'Symbol Modifier',
    'So': 'Symbol Other',

    # Bidirectional
    'L': 'Left-to-Right',
    'Lre': 'Left-to-Right Embedding',
    'Lro': 'Left-to-Right Override',
    'R': 'Right-to-Left',
    'Al': 'Right-to-Left Arabic',
    'Rle': 'Right-to-Left Embedding',
    'Rlo': 'Right-to-Left Override',
    'Pdf': 'Pop Directional Format',
    'En': 'European Number',
    'Es': 'European Number Separator',
    'Et': 'European Number Terminator',
    'An': 'Arabic Number',
    'Cs': 'Common Number Separator',
    'Nsm': 'Non-Spacing Mark',
    'Bn': 'Boundary Neutral',
    'B': 'Paragraph Separator',
    'S': 'Segment Separator',
    'Ws': 'Whitespace',
    'On': 'Other Neutrals'
}



def find(fd: _io.TextIOWrapper, *, filetype=('UNKNOWN',)) -> [Character]:
    """Read the text file from `fd` and return a generator for Character
    instances. If `filetype` is provided, it's value is returned by
    `printnonascii.guess`.
    """
    for lineno, line in enumerate(fd):
        for colno, char in enumerate(line):
            if ord(char) > 127:
                c = Character(char)

                c.lineno = lineno
                c.colno = colno
                c.description = unicodedata.name(char)
                c.category = UNICODE_CATEGORIES.get(unicodedata.category(char).title())
                c.unicode_point = 'U+' + hex(ord(char))[2:].upper()
                c.line = line

                yield c
