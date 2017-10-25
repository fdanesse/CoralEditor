#!/usr/bin/python3
# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui

from PyQt5.QtGui import QSyntaxHighlighter


class PythonHighlighter2(QSyntaxHighlighter):
    # http://doc.qt.io/qt-5/qsyntaxhighlighter.html
    # http://doc.qt.io/qt-5/qregexp.html
    # https://wiki.python.org/moin/PyQt/Python%20syntax%20highlighting

    def __init__(self, document):
        QSyntaxHighlighter.__init__(self, document)
 
        self.highlightingRules = []

        keywordFormat = QtGui.QTextCharFormat()
        keywordFormat.setForeground(QtCore.Qt.darkRed)
        keywordFormat.setFontWeight(QtGui.QFont.Bold)
 
        keywords = ['class', 'def', 'for', 'in', 'try', 'except',
                    'and', 'del', 'is', 'raise', 'assert', 'elif',
                    'global', 'lambda', 'return', 'break', 'else',
                    'not', 'try', 'from', 'if', 'or', 'while',
                    'continue', 'exec', 'import', 'pass', 'yield',
                    'finally', 'print', 'eval']
 
        keywordPatterns = map(lambda x: "\\b"+x+"\\b", keywords)
 
        self.highlightingRules = [(QtCore.QRegExp(pattern), keywordFormat) for pattern in keywordPatterns]
 
        singleLineCommentFormat = QtGui.QTextCharFormat()
        singleLineCommentFormat.setForeground(QtCore.Qt.gray)
        self.highlightingRules.append((QtCore.QRegExp("#[^\n]*"), singleLineCommentFormat))
 
        quotationFormat = QtGui.QTextCharFormat()
        quotationFormat.setForeground(QtCore.Qt.red)
        self.highlightingRules.append((QtCore.QRegExp("\".*\""), quotationFormat))
        self.highlightingRules.append((QtCore.QRegExp("\'.*\'"), quotationFormat))
 
        functionFormat = QtGui.QTextCharFormat()
        #functionFormat.setFontWeight(QtGui.QFont.Bold)
        functionFormat.setForeground(QtCore.Qt.blue)
        self.highlightingRules.append((QtCore.QRegExp("\\b[A-Za-z0-9_]+(?=\\()"),
                functionFormat))
 
        classFormat = QtGui.QTextCharFormat()
        classFormat.setForeground(QtCore.Qt.magenta)
        classFormat.setFontWeight(QtGui.QFont.Bold)
        self.highlightingRules.append((QtCore.QRegExp("\\bMT[A-Za-z]+\\b"),classFormat))
  
        self.commentStartExpression = QtCore.QRegExp("\"\"\"")
        self.commentEndExpression = QtCore.QRegExp("\"\"\"")
        self.multiLineCommentFormat = QtGui.QTextCharFormat()
        self.multiLineCommentFormat.setForeground(QtCore.Qt.darkGreen)
 
    def highlightBlock(self, text):
        for pattern, format in self.highlightingRules:
            expression = QtCore.QRegExp(pattern)
            index = expression.indexIn(text)
            while index >= 0:
                length = expression.matchedLength()
                self.setFormat(index, length, format)
                index = expression.indexIn(text, index + length)
 
        self.setCurrentBlockState(0)
 
        startIndex = 0
        if self.previousBlockState() != 1:
            startIndex = self.commentStartExpression.indexIn(text)
 
        while startIndex >= 0:
            endIndex = self.commentEndExpression.indexIn(text, startIndex)
 
            if endIndex == -1:
                self.setCurrentBlockState(1)
                commentLength = len(text) - startIndex
            else:
                commentLength = endIndex - startIndex + self.commentEndExpression.matchedLength()
 
            self.setFormat(startIndex, commentLength,
                    self.multiLineCommentFormat)
            startIndex = self.commentStartExpression.indexIn(text,
                    startIndex + commentLength)