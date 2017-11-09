#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os

from PyQt5.QtCore import Qt
from PyQt5.QtCore import QEvent

from PyQt5.QtWidgets import QPlainTextEdit
from PyQt5.QtWidgets import QApplication

from PyQt5.QtGui import QPalette
from PyQt5.QtGui import QColor
from PyQt5.QtGui import QFont
from PyQt5.QtGui import QFontMetrics
from PyQt5.QtGui import QTextCharFormat
from PyQt5.QtGui import QKeyEvent
#from PyQt5.QtGui import QTextCursor

#from Gui.Syntax.PythonHighlighter import PythonHighlighter


class TextEdit(QPlainTextEdit):
    # https://doc.qt.io/qt-5/qplaintextedit.html
    # https://github.com/hugoruscitti/pilas/blob/e33bfd80a9c9faec432dbd3de1d82066b8704303/pilasengine/interprete/editorbase/editor_base.py
    # http://www.binpress.com/tutorial/developing-a-pyqt-text-editor-part-2/145
    # http://ftp.ics.uci.edu/pub/centos0/ics-custom-build/BUILD/PyQt-x11-gpl-4.7.2/doc/html/qtextedit.html
    # http://nullege.com/codes/show/src@p@y@pyqt5-HEAD@examples@tools@customcompleter@customcompleter.py/92/PyQt5.QtWidgets.QTextEdit.textCursor
    # http://nullege.com/codes/show/src@p@y@pyqt5-HEAD@examples@richtext@textedit@textedit.py/87/PyQt5.QtWidgets.QTextEdit.setFocus
    # Ejemplos:
    #   https://stackoverflow.com/questions/31610351/qplaintextedit-thinks-its-modified-if-it-has-an-empty-text
    #   https://john.nachtimwald.com/2009/08/19/better-qplaintextedit-with-line-numbers/
    #   https://github.com/Werkov/PyQt4/blob/master/examples/demos/textedit/textedit.py
    
    def __init__(self, parent, path=""):
        #super().__init__()
        super(TextEdit, self).__init__(parent)

        self.parent = parent
        self.path = path
        
        font = QFont("Monospace", 8)  #QFont()
        #font.setFamily("Monospace")
        font.setStyleHint(QFont.Monospace)
        font.setStyle(QFont.StyleNormal)
        font.setStyleStrategy(QFont.PreferDefault)
        font.setWeight(QFont.ExtraLight)
        font.setCapitalization(QFont.MixedCase)
        font.setHintingPreference(QFont.PreferDefaultHinting)
        font.setLetterSpacing(QFont.PercentageSpacing, 100.0)
        font.setStretch(QFont.AnyStretch)

        font.setBold(False)
        font.setFixedPitch(True)
        font.setItalic(False)
        font.setKerning(True)
        font.setOverline(False)  # sobrelinea
        #font.setPixelSize(8) #font.setPointSize(8) font.setPointSizeF(8)
        font.setStrikeOut(False)  # tachado
        #font.setStyleName()
        font.setUnderline(False)
        #font.setWordSpacing(1)
        print(font.toString())

        charFormat = QTextCharFormat()
        charFormat.setFont(font)

        #self.setTabStopWidth(4)
        self.setCursorWidth(5)
        self.setCurrentCharFormat(charFormat)
        #print(self.document().defaultTextOption())

        #FIXME: Usaremos qss
        pal = QPalette()
        bgc = QColor(39, 40, 34)
        pal.setColor(QPalette.Base, bgc)
        textc = QColor(255, 255, 255)
        pal.setColor(QPalette.Text, textc)
        self.setPalette(pal)

        self.setLineWrapMode(QPlainTextEdit.NoWrap)

        #self.setTextBackgroundColor(QColor(0, 255, 255))
        #self.setTextColor(QColor(0, 255, 255))
        #self.setFontWeight(QFont.Normal)

        #cursor = self.textCursor()
        #cursor.movePosition(QTextCursor.End)
        #self.setDocumentTitle("Coso")

        #self.syntaxHighlighter = PythonHighlighter(self.document())

        # Señales
        #self.blockCountChanged.connect(self.__newBlock)
        #self.cursorPositionChanged.connect()
        #self.selectionChanged.connect(self.__changedSelection)
        #self.textChanged.connect(self.__changedText)
        #self.updateRequest.connect((const QRect &rect, int dy)
        #self.modificationChanged.connect(self.__chanedModification)

        #self.copyAvailable.connect(self.__copyAvailable)
        #self.undoAvailable.connect(self.__undoAvailable)
        #self.redoAvailable.connect(self.__redoAvailable)

        if os.path.exists(self.path):
            file = open(self.path, 'r')
            data = file.read()
            texto = self.__limpiar_codigo(data)
            self.setPlainText(texto)
            self.document().setModified(data != texto)
            if data != texto:
                print("El texto fue corregido al abrir el archivo.")
        else:
            self.setPlainText("#!/usr/bin/python3\n# -*- coding: utf-8 -*-\n\n")
            self.document().setModified(True)

        self.setFocus()

    def getStatus(self):
        """
        Si se modifica el texto, se puede guardar.
        """
        return{
            "modified": self.document().isModified(),
        }

    #def __chanedModification(self, changed):
    #    pass
    #    #print("Document changed:", changed)

    #def __changedSelection(self):
    #    cursor = self.textCursor()
    #    selected = cursor.selectionEnd()-cursor.selectionStart()
    #    self.canSelectAll = selected < len(self.toPlainText())
        
    #def __copyAvailable(self, available):
    #    self.canCopy = available

    #def __undoAvailable(self, available):
    #    pass
    #    #print("Undo:", available)

    #def __redoAvailable(self, available):
    #    pass
    #    #print("Redo:", available)

    def keyPressEvent(self, event):
        # https://doc.qt.io/qt-5/qt.html#Key-enum
        if event.key() == Qt.Key_Tab:
            event.ignore()
            event.accept = True
            for x in range(0, 4):
                newevent = QKeyEvent(QEvent.KeyPress, Qt.Key_Space,
                    Qt.NoModifier, text=" ", autorep=False, count=1)
                QApplication.postEvent(self, newevent)
        else:
            super(TextEdit, self).keyPressEvent(event)
            event.accept = True
        self.setFocus()

    '''
    def __newBlock(self, newBlockCount):
        #print(newBlockCount)

    def __changedText(self):
        text = self.document().toPlainText()
        text = self.__limpiar_codigo(text)
        #self.setPlainText(text)
        print(text, self.document().size())
    '''
        
    def __limpiar_codigo(self, texto):
        limpio = ""
        for line in texto.splitlines():
            text_line = "%s\n" % (line.rstrip())
            ret = text_line.replace("\t", "    ")
            for l in ret:
                limpio = "%s%s" % (limpio, l)
        return limpio