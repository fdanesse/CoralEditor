#!/usr/bin/python3
# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QMenu
from PyQt5.QtWidgets import QAction
from PyQt5.QtWidgets import QFontDialog

from PyQt5.QtGui import QIcon


class MenuCodigo(QMenu):

    def __init__(self, parent):
        QMenu.__init__(self, "&Código", parent)

        item = QAction('Aumentar Texto', self)
        item.setShortcut('Ctrl++')
        self.addAction(item)

        item = QAction('Disminuir Texto', self)
        item.setShortcut('Ctrl+-')
        self.addAction(item)

        item = QAction('Formato Texto...', self)
        item.setShortcut('Ctrl+T')
        item.triggered.connect(self.showDialog)
        self.addAction(item)

        self.addSeparator()

        item = QAction('Aumentar Tabulación', self)
        #item.setShortcut('Ctrl+X')
        self.addAction(item)

        item = QAction('Disminuir Tabulación', self)
        #item.setShortcut('Ctrl+V')
        self.addAction(item)

        self.addSeparator()

        item = QAction('Buscar Texto...', self)
        item.setShortcut('Ctrl+B')
        self.addAction(item)

        item = QAction('Remplazar Texto...', self)
        #item.setShortcut('Ctrl+B')
        self.addAction(item)

        self.addSeparator()

        item = QAction('Chequear Sintaxis...', self)
        #item.setShortcut('Ctrl+B')
        self.addAction(item)

    def showDialog(self):
        font, ok = QFontDialog.getFont()
        if ok:
            #self.lbl.setFont(font)
            print(font)