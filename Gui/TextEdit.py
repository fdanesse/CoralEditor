#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os

#from PyQt5.QtCore import Qt

from PyQt5.QtWidgets import QPlainTextEdit

from PyQt5.QtGui import QPalette
from PyQt5.QtGui import QColor
#from PyQt5.QtGui import QFont
#from PyQt5.QtGui import QTextCursor

from Gui.Syntax.PythonHighlighter import PythonHighlighter


class TextEdit(QPlainTextEdit):
    # https://doc.qt.io/qt-5/qplaintextedit.html
    # https://github.com/hugoruscitti/pilas/blob/e33bfd80a9c9faec432dbd3de1d82066b8704303/pilasengine/interprete/editorbase/editor_base.py
    # http://www.binpress.com/tutorial/developing-a-pyqt-text-editor-part-2/145
    # http://ftp.ics.uci.edu/pub/centos0/ics-custom-build/BUILD/PyQt-x11-gpl-4.7.2/doc/html/qtextedit.html
    # http://nullege.com/codes/show/src@p@y@pyqt5-HEAD@examples@tools@customcompleter@customcompleter.py/92/PyQt5.QtWidgets.QTextEdit.textCursor
    # http://nullege.com/codes/show/src@p@y@pyqt5-HEAD@examples@richtext@textedit@textedit.py/87/PyQt5.QtWidgets.QTextEdit.setFocus

    def __init__(self, parent, path=""):
        #super().__init__()
        super(TextEdit, self).__init__(parent)

        self.path = path
        # FIXME: que tabulación siempre sean 4 espacios

        #FIXME: Usaremos qss
        pal = QPalette()
        bgc = QColor(39, 40, 34)
        pal.setColor(QPalette.Base, bgc)
        textc = QColor(255, 255, 255)
        pal.setColor(QPalette.Text, textc)
        self.setPalette(pal)

        self.setLineWrapMode(QPlainTextEdit.NoWrap)
        #FIXME: Funciona en QTextEdit
        #self.setCurrentFont(QFont("Monospace", 8))
        #self.setFontPointSize(8)
        #self.setTextBackgroundColor(QColor(0, 255, 255))
        #self.setTextColor(QColor(0, 255, 255))
        #self.setFontWeight(QFont.Normal)

        #self.setTabStopWidth(4)
        #self.setFocus()
        #cursor = self.textCursor()
        #cursor.movePosition(QTextCursor.End)
        #self.setDocumentTitle("Coso")

        if os.path.exists(self.path):
            file = open(self.path, 'r')
            with file:
                data = file.read()
                #FIXME: Corregir codigo al abrir ?
                self.setPlainText(data)
        else:
            #self.setText("#!/usr/bin/python3\n# -*- coding: utf-8 -*-\n\n")
            self.setPlainText("#!/usr/bin/python3\n# -*- coding: utf-8 -*-\n\n")

        self.syntaxHighlighter = PythonHighlighter(self.document())

        #self.selectAll()