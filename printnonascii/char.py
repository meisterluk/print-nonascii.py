#!/usr/bin/env python3

class Character:
    def __init__(self, c):
        self.character = c
        self.unicode_point = None
        self.lineno = None
        self.colno = None
        self.category = None
        self.description = None
        self.line = None

    def asciionly(self):
        assert self.description or self.unicode_point

        if self.description is not None and self.unicode_point is not None:
            out = '{} {}'.format(self.unicode_point, self.description)
        elif self.description:
            out = '{}'.format(self.description)
        elif self.unicode_point is not None:
            out = '{}'.format(self.unicode_point)

        if self.category is not None:
            out += ' of category {}'.format(self.category)
        if self.lineno is not None:
            out += ' at line {}'.format(self.lineno)
        elif self.colno is not None:
            out += ' at column {}'.format(self.colno)

        return out

    def __str__(self):
        out = ''

        if self.line is not None and self.colno is not None:
            out += '{: <3d}: {}'.format(self.lineno, self.line)
            out += '   : {}⬏\n\n'.format('─' * self.colno)

        out += "{} ".format(self.character)

        if self.unicode_point:
            out += '{} '.format(self.unicode_point)

        if self.lineno is not None and self.colno is not None:
            out += '(line {}, col {})'.format(self.lineno, self.colno)
        elif self.lineno is not None:
            out += '(line {})'.format(self.lineno)
        elif self.colno is not None:
            out += '(col {})'.format(self.colno)

        out += "\n"

        if self.category:
            out += "  category: {}\n".format(self.category)
            out += "  name: {}\n".format(self.description)

        out += "\n"
        return out
