#!/usr/bin/python3
# -*- coding: utf-8 -*-

from PyQt5.QtCore import QRegExp

from PyQt5.QtGui import QSyntaxHighlighter

from Gui.Syntax.PySyntax import tri_single
from Gui.Syntax.PySyntax import tri_double
from Gui.Syntax.PySyntax import SYNTAX
from Gui.Syntax.PySyntax import COLOR_SCHEME
from Gui.Syntax.PySyntax import estilizar
from Gui.Syntax.PySyntax import STYLES


class PythonHighlighter(QSyntaxHighlighter):
    # http://doc.qt.io/qt-5/qsyntaxhighlighter.html
    # https://github.com/hugoruscitti/pilas/blob/e33bfd80a9c9faec432dbd3de1d82066b8704303/pilasengine/interprete/editorbase/highlighter.py

    def __init__(self, document, scheme=None):
        QSyntaxHighlighter.__init__(self, document)
        
        self.multi_start = None
        self.rules = []

        self.apply_highlight(scheme)

    def apply_highlight(self, scheme=None):
        if scheme:
            estilizar(scheme)

        rules = []
        rules.extend([(r'\b%s\b' % w, 0, STYLES['keyword']) for w in SYNTAX.get('keywords', [])])
        rules.extend([(r'%s' % o, 0, STYLES['operator']) for o in SYNTAX.get('operators', [])])

        for pr in SYNTAX['properObject']:
            expr = '\\b' + pr + '\\b'
            rules.append((expr, 0, STYLES['properObject']))
            #FIXME: self los parametros en funciones deben ser igual

        definition = SYNTAX.get('definition', [])
        for de in definition:
            expr = '\\b' + de + '\\b\\s*(\\w+)'
            rules.append((expr, 1, STYLES['definition']))
            #FIXME: def, class, super ¿Por qué 1?

        # Numeric literals # r fuerza a que las secuencias de escape no sean interpretadas
        rules.extend([
            (r'\b[+-]?[0-9]+[lL]?\b', 0, STYLES['numbers']),
            (r'\b[+-]?0[xX][0-9A-Fa-f]+[lL]?\b', 0, STYLES['numbers']),
            (r'\b[+-]?[0-9]+(?:\.[0-9]+)?(?:[eE][+-]?[0-9]+)?\b', 0,
            STYLES['numbers']),
        ])

        # FIXME: No existe esta key
        #regex = SYNTAX.get('regex', [])
        #for reg in regex:
        #    expr = reg[0]
        #    color = COLOR_SCHEME['extras']
        #    style = ''
        #    if len(reg) > 1:
        #        color = COLOR_SCHEME[reg[1]]
        #    if len(reg) > 2:
        #        style = reg[2]
        #    rules.append((expr, 0, format(color, style)))

        for co in SYNTAX['comment']:
            expr = co + '[^\\n]*'
            rules.append((expr, 0, STYLES['comment']))

        for sc in SYNTAX['string']:
            expr = r'"[^"\\]*(\\.[^"\\]*)*"' if sc == '"' \
                else r"'[^'\\]*(\\.[^'\\]*)*'"
            rules.append((expr, 0, STYLES['string']))
        
        #FIXME: no existe esta key
        #multi = SYNTAX.get('multiline_comment', [])
        #if multi:
        #    self.multi_start = (QRegExp(multi['open']), STYLES['comment'])
        #    self.multi_end = (QRegExp(multi['close']), STYLES['comment'])
        #else:
        #    self.multi_start = None

        # Build a QRegExp for each pattern
        self.rules = [(QRegExp(pat), index, fmt)
            for (pat, index, fmt) in rules]

        self.rehighlight()

    def highlightBlock(self, text):
        """Cada vez que cambia el texto en el editor, se ejecuta esta función."""        
        for expression, nth, form in self.rules:
            index = expression.indexIn(text, 0)
            while index >= 0:
                index = expression.pos(nth)
                length = len(expression.cap(nth))
                self.setFormat(index, length, form)
                index = expression.indexIn(text, index + length)

        self.setCurrentBlockState(0)
        # FIXME: dado que no existe la key multiline_comment
        # self.multi_start siempre es None 
        #if not self.multi_start:
        #    # Do multi-line strings
        #    in_multiline = self.match_multiline(text, *tri_single)
        #    if not in_multiline:
        #        in_multiline = self.match_multiline(text, *tri_double)
        #else:
        #    # Do multi-line comment
        #    self.comment_multiline(text, self.multi_end[0], *self.multi_start)
        
        in_multiline = self.match_multiline(text, *tri_single)
        if not in_multiline:
            in_multiline = self.match_multiline(text, *tri_double)
        
        #Spaces
        #FIXME: totalmente innecesario e inservible
        '''
        expression = QRegExp('\s+')
        index = expression.indexIn(text, 0)
        while index >= 0:
            index = expression.pos(0)
            length = len(expression.cap(0))
            self.setFormat(index, length, STYLES['spaces'])
            index = expression.indexIn(text, index + length)
        '''

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

    # FIXME: dado que no existe la key multiline_comment
    # self.multi_start siempre es None y por lo tanto esta funcion nunca es llamada
    '''
    def comment_multiline(self, text, delimiter_end, delimiter_start, style):
        startIndex = 0
        if self.previousBlockState() != 1:
            startIndex = delimiter_start.indexIn(text)
        while startIndex >= 0:
            endIndex = delimiter_end.indexIn(text, startIndex)
            commentLength = 0
            if endIndex == -1:
                self.setCurrentBlockState(1)
                commentLength = text.length() - startIndex
            else:
                commentLength = endIndex - startIndex + delimiter_end.matchedLength()
            self.setFormat(startIndex, commentLength, style)
            startIndex = delimiter_start.indexIn(text, startIndex + commentLength)
    '''