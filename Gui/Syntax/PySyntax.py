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
    'string': __format(COLOR_SCHEME['string']),
    'string2': __format(COLOR_SCHEME['string2']),
    'comment': __format(COLOR_SCHEME['comment']),
    'properObject': __format(COLOR_SCHEME['properObject']),
    'numbers': __format(COLOR_SCHEME['numbers']),
    }

SYNTAX = {
    'comment': ['#'],
    'definition': ['def', 'class', 'super'],
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

definition = SYNTAX.get('definition', [])
for de in definition:
    expr = '\\b' + de + '\\b\\s*(\\w+)'
    RULES.append((expr, 0, STYLES['definition']))
    #FIXME: def, class, super ¿Por qué 1?

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
