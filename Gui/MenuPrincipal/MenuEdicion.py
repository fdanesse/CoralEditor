#!/usr/bin/python3
# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QMenu
from PyQt5.QtWidgets import QAction

from PyQt5.QtGui import QIcon


class MenuEdicion(QMenu):

    def __init__(self, parent):
        QMenu.__init__(self, "&Edición", parent)

        item = QAction(QIcon('Iconos/edit-undo.png'), 'Deshacer', self)
        item.setShortcut('Ctrl+Z')
        self.addAction(item)

        item = QAction(QIcon('Iconos/edit-redo.png'), 'Rehacer', self)
        item.setShortcut('Ctrl+R')
        self.addAction(item)

        self.addSeparator()

        item = QAction('Copiar', self)
        item.setShortcut('Ctrl+C')
        self.addAction(item)

        item = QAction('Cortar', self)
        item.setShortcut('Ctrl+X')
        self.addAction(item)

        item = QAction('Pegar', self)
        item.setShortcut('Ctrl+V')
        self.addAction(item)

        self.addSeparator()
        
        item = QAction(QIcon('Iconos/edit-select-all.png'), 'Seleccionar Todo', self)
        item.setShortcut('Ctrl+A')
        self.addAction(item)
