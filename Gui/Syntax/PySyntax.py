#!/usr/bin/python3
# -*- coding: utf-8 -*-

from PyQt5.QtGui import QColor
from PyQt5.QtGui import QTextCharFormat
from PyQt5.QtGui import QFont
from PyQt5.QtCore import QRegExp


def __formatear(color, estilo=""):
    qcolor = QColor()
    qcolor.setNamedColor(color)
    formato = QTextCharFormat()
    formato.setForeground(qcolor)
    if "bold" in estilo:
        formato.setFontWeight(QFont.Bold)
    if "italic" in estilo:
        formato.setFontItalic(True)
    return formato


ESTILOS = {
    "keyword": __formatear("blue"),
    "operator": __formatear("red"),
    "brace": __formatear("darkGray"),
    "defclass": __formatear("black", "bold"),
    "string": __formatear("magenta"),
    "string2": __formatear("darkMagenta"),
    "comment": __formatear("darkGreen", "italic"),
    "self": __formatear("black", "italic"),
    "numbers": __formatear("brown"),
}

keywords = [
    "and", "assert", "break", "class", "continue", "def",
    "del", "if", "elif", "else", "exec", "finally",
    "for", "from", "global", "import", "in",
    "is", "lambda", "not", "or", "pass", "print",
    "raise", "return", "try", "except", "while", "yield",
    "None", "True", "False",
    ]

operadores = [
    "=",
    "==", "!=", "<", "<=", ">", ">=",
    "\+", "-", "\*", "/", "//", "\%", "\*\*",
    "\+=", "-=", "\*=", "/=", "\%=",
    "\^", "\|", "\&", "\~", ">>", "<<",
    ]

parentesis = ["\{", "\}", "\(", "\)", "\[", "\]"]

tri_single = (QRegExp("'''"), 1, ESTILOS['string2'])
tri_double = (QRegExp('"""'), 2, ESTILOS['string2'])

rules = []
rules.extend([(r"\b%s\b" % w, 0, ESTILOS["keyword"]) for w in keywords])
rules.extend([(r"%s" % o, 0, ESTILOS["operator"]) for o in operadores])
rules.extend([(r"%s" % b, 0, ESTILOS["brace"]) for b in parentesis])

rules.extend([(r"\bself\b", 0, ESTILOS["self"]),
    (r'"[^"\\]*(\\.[^"\\]*)*', 0, ESTILOS["string"]),
    (r"\bdef\b\s*(\w+)", 1, ESTILOS["defclass"]),
    (r"\bclass\b\s*(\w+)", 1, ESTILOS["defclass"]),
    (r"#[^\n]*", 0, ESTILOS["comment"]),
    (r"\b[+-]?[0-9]+[lL]?\b", 0, ESTILOS["numbers"]),
    (r"\b[+-]?0[xX][0-9A-Fa-f]+[lL]?\b", 0, ESTILOS["numbers"]),
    (r"\b[+-]?[0-9]+(?:\.[0-9]+)?(?:[eE][+-]?[0-9]+)?\b", 0, ESTILOS["numbers"])])

rules = [(QRegExp(pat), index, fmt) for (pat, index, fmt) in rules]