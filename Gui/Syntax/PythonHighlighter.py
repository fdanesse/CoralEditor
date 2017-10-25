#!/usr/bin/python3
# -*- coding: utf-8 -*-

from PyQt5.QtGui import QSyntaxHighlighter

from Gui.Syntax.PySyntax import tri_single
from Gui.Syntax.PySyntax import tri_double
from Gui.Syntax.PySyntax import RULES


class PythonHighlighter(QSyntaxHighlighter):
    # http://doc.qt.io/qt-5/qsyntaxhighlighter.html
    # http://doc.qt.io/qt-5/qregexp.html

    def __init__(self, document):
        QSyntaxHighlighter.__init__(self, document)

    def highlightBlock(self, text):
        for expression, nth, form in RULES:
            index = expression.indexIn(text, 0)
            while index >= 0:
                index = expression.pos(nth)
                length = len(expression.cap(nth))
                # text[index:length]) == expression.cap(nth)
                self.setFormat(index, length, form)
                index = expression.indexIn(text, index + length)

        self.setCurrentBlockState(0)
        
        in_multiline = self.match_multiline(text, *tri_single)
        if not in_multiline:
            in_multiline = self.match_multiline(text, *tri_double)

    def match_multiline(self, text, delimiter, in_state, style):
        if self.previousBlockState() == in_state:
            start = 0
            add = 0
        else:
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

        if self.currentBlockState() == in_state:
            return True
        else:
            return False