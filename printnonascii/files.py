#!/usr/bin/env python3

import os.path


BINARY = {'.a', '.bin', '.exe', '.so'}
SOURCECODE = {'.c', '.cpp', '.go', '.h', '.hpp', '.hs', '.java', '.p', '.pl', '.py', '.sc'}


def guess(filepath: str) -> str:
    """Guess a filetype using its filepath.
    The return value is non-standardized, but can be
    understand by :func:`printnonascii.find`.
    """
    _, ext = os.path.splitext(filepath)
    if ext in BINARY:
        return ('BINARY',)
    elif ext in SOURCECODE:
        return ('SOURCE',)
    else:
        return ('UNKNOWN',)
