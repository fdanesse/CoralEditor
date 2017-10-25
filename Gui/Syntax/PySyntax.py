#!/usr/bin/python3
# -*- coding: utf-8 -*-

from PyQt5.QtGui import QColor
from PyQt5.QtGui import QTextCharFormat
from PyQt5.QtGui import QFont
from PyQt5.QtCore import QRegExp

#FIXME: faltan reglas para funciones, por ejemplo range()


def __format(color, style=''):
    _color = QColor()
    _color.setNamedColor(color)
    _format = QTextCharFormat()
    _format.setForeground(_color)
    if 'bold' in style:
        _format.setFontWeight(QFont.Bold)
    if 'italic' in style:
        _format.setFontItalic(True)
    return _format


COLOR_SCHEME = {
    "keyword": "#c9264c",
    "operator": "#c9264c",
    "definition": "#a4de2d",
    "definition2": "cyan",
    "string": "#d8d170",
    "string2": "#ff9dc6",
    "comment": "gray",
    "properObject": "orange",
    "numbers": "brown",
    }

STYLES = {
    'keyword': __format(COLOR_SCHEME['keyword']),
    'operator': __format(COLOR_SCHEME['operator']),
    'definition': __format(COLOR_SCHEME['definition']),
    'definition2': __format(COLOR_SCHEME['definition2']),
    'string': __format(COLOR_SCHEME['string']),
    'string2': __format(COLOR_SCHEME['string2']),
    'comment': __format(COLOR_SCHEME['comment']),
    'properObject': __format(COLOR_SCHEME['properObject']),
    'numbers': __format(COLOR_SCHEME['numbers']),
    }

SYNTAX = {
    'comment': ['#'],
    'definition': ['def', 'class', 'super'],
    'definition2': ['def', 'class', 'super'],
    'string': ["'", '"'],
    'properObject': ['self'],
    'operators': ['=', '==', '!=', '<', '<=', '>', '>=', '\\+', '-', '\\*',
        '/', '//', '\\%', '\\*\\*', '\\+=', '-=', '\\*=', '/=', '\\%=', '\\^',
        '\\|', '\\&', '\\~', '>>', '<<'],
    'keywords': ['and', 'assert', 'break', 'continue',
        'del', 'elif', 'else', 'except', 'exec', 'finally', 'for', 'from',
        'global', 'if', 'import', 'in', 'is', 'lambda', 'not', 'or', 'pass',
        'print', 'raise', 'return', 'try', 'while', 'yield',
        'None', 'True', 'False']
    }

tri_single = (QRegExp("'''"), 1, STYLES['string2'])
tri_double = (QRegExp('"""'), 2, STYLES['string2'])

RULES = []
RULES.extend([(r'\b%s\b' % w, 0, STYLES['keyword']) for w in SYNTAX.get('keywords', [])])
RULES.extend([(r'%s' % w, 0, STYLES['operator']) for w in SYNTAX.get('operators', [])])
RULES.extend([(r'\b%s\b' % w, 0, STYLES['properObject']) for w in SYNTAX.get('properObject', [])])
#Nombres de clases o función
RULES.extend([(r'\b%s\b\s*(\w+)' % w, 1, STYLES['definition']) for w in SYNTAX.get('definition', [])])
RULES.extend([(r'\b%s\b\s' % w, 0, STYLES['definition2']) for w in SYNTAX.get('definition2', [])])

# Numeric literals # r fuerza a que las secuencias de escape no sean interpretadas
RULES.extend([
    (r'\b[+-]?[0-9]+[lL]?\b', 0, STYLES['numbers']),
    (r'\b[+-]?0[xX][0-9A-Fa-f]+[lL]?\b', 0, STYLES['numbers']),
    (r'\b[+-]?[0-9]+(?:\.[0-9]+)?(?:[eE][+-]?[0-9]+)?\b', 0,
    STYLES['numbers']),
])

for co in SYNTAX['comment']:
    expr = co + '[^\\n]*'
    RULES.append((expr, 0, STYLES['comment']))

for sc in SYNTAX['string']:
    expr = r'"[^"\\]*(\\.[^"\\]*)*"' if sc == '"' \
        else r"'[^'\\]*(\\.[^'\\]*)*'"
    RULES.append((expr, 0, STYLES['string']))

RULES = [(QRegExp(pat), index, fmt) for (pat, index, fmt) in RULES]