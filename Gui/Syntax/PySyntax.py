#!/usr/bin/python3
# -*- coding: utf-8 -*-

from PyQt5.QtGui import QColor
from PyQt5.QtGui import QTextCharFormat
from PyQt5.QtGui import QFont
from PyQt5.QtCore import QRegExp

SYNTAX = {}
#BRACES = ['\\(', '\\)', '\\{', '\\}', '\\[', '\\]']

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
    #"brace": "#858585",
    "definition": "#55a92d",
    "string": "#d8d170",
    "string2": "darkGreen",
    "comment": "gray",
    "properObject": "orange",
    "numbers": "brown",
    #"spaces": "#BFBFBF",
    #"extras": "orange",
    #"editor-background": "white",
    #"editor-selection-color": "white",
    #"editor-selection-background": "#437DCD",
    #"editor-text": "black",
    #"current-line": "darkCyan",
    #"selected-word": "yellow",
    #"brace-background": "#5BC85B",
    #"brace-foreground": "red"
    }


STYLES = {
    'keyword': __format(COLOR_SCHEME['keyword']),
    'operator': __format(COLOR_SCHEME['operator']),
    #'brace': __format(COLOR_SCHEME['brace']),
    'definition': __format(COLOR_SCHEME['definition']),
    'string': __format(COLOR_SCHEME['string']),
    'string2': __format(COLOR_SCHEME['string2']),
    'comment': __format(COLOR_SCHEME['comment']),
    'properObject': __format(COLOR_SCHEME['properObject']),
    'numbers': __format(COLOR_SCHEME['numbers']),
    #'spaces': __format(COLOR_SCHEME['spaces']),
    #'extras': __format(COLOR_SCHEME['extras'])
    }

SYNTAX = {
    'comment': ['#'],
    'definition': ['def', 'class', 'super'],
    'string': ["'", '"'],
    #'extension': ['py'],
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

def estilizar(scheme):
    """Aplica un esquema de colores determinado"""
    STYLES['keyword'] = __format(scheme.get('keyword', COLOR_SCHEME['keyword']))
    STYLES['operator'] = __format(scheme.get('operator', COLOR_SCHEME['operator']))
    #STYLES['brace'] = __format(scheme.get('brace', COLOR_SCHEME['brace']))
    STYLES['definition'] = __format(scheme.get('definition', COLOR_SCHEME['definition']))
    STYLES['string'] = __format(scheme.get('string', COLOR_SCHEME['string']))
    STYLES['string2'] = __format(scheme.get('string2', COLOR_SCHEME['string2']))
    STYLES['comment'] = __format(scheme.get('comment', COLOR_SCHEME['comment']))
    STYLES['properObject'] = __format(scheme.get('properObject', COLOR_SCHEME['properObject']))
    STYLES['numbers'] = __format(scheme.get('numbers', COLOR_SCHEME['numbers']))
    #STYLES['spaces'] = __format(scheme.get('spaces', COLOR_SCHEME['spaces']))
    #STYLES['extras'] = __format(scheme.get('extras', COLOR_SCHEME['extras']))