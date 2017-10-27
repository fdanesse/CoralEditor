#!/usr/bin/python3
# -*- coding: utf-8 -*-

from PyQt5.QtGui import QSyntaxHighlighter

from Gui.Syntax.PySyntax import tri_single
from Gui.Syntax.PySyntax import tri_double
from Gui.Syntax.PySyntax import RULES
from PyQt5.QtCore import QRegExp

class PythonHighlighter(QSyntaxHighlighter):
    # http://doc.qt.io/qt-5/qsyntaxhighlighter.html
    # http://doc.qt.io/qt-5/qregexp.html
    # https://wiki.python.org/moin/PyQt/Python%20syntax%20highlighting
    # http://ninja-ide.github.io/ninja-ide/listings/ninja_ide/gui/editor/highlighter.py.html

    def __init__(self, document):
        QSyntaxHighlighter.__init__(self, document)

    def highlightBlock(self, text):
        for expression, nth, form in RULES:
            index = expression.indexIn(text, 0)
            while index >= 0:
                index = expression.pos(nth)
                length = len(expression.cap(nth))
                # text[index:length] == expression.cap(nth)
                self.setFormat(index, length, form)
                index = expression.indexIn(text, index + length)
        self.setCurrentBlockState(0)
        
        # Verificación de comentarios o strings multilinea
        for delimiter, in_state, style in [tri_single, tri_double]:
            start = 0
            add = 0

            if self.previousBlockState() != in_state:
                start = delimiter.indexIn(text)
                add = delimiter.matchedLength()

            while start >= 0:
                end = delimiter.indexIn(text, start + add)
                if end >= add:
                    length = end - start + add + delimiter.matchedLength()
                    self.setCurrentBlockState(0)
                else:
                    self.setCurrentBlockState(in_state)
                    length = len(text) - start + add

                self.setFormat(start, length, style)
                start = delimiter.indexIn(text, start + length)

        self.setCurrentBlockState(0)