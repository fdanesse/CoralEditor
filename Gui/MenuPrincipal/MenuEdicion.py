#!/usr/bin/python3
# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QMenu
from PyQt5.QtWidgets import QAction

from PyQt5.QtGui import QIcon


class MenuEdicion(QMenu):

    def __init__(self, parent):
        QMenu.__init__(self, "&Edición", parent)

        self.undo = QAction(QIcon(
            'Iconos/edit-undo.png'), 'Deshacer', self)
        self.undo.setShortcut('Ctrl+Z')
        self.undo.setEnabled(False)
        self.addAction(self.undo)

        self.redo = QAction(QIcon(
            'Iconos/edit-redo.png'), 'Rehacer', self)
        self.redo.setShortcut('Ctrl+R')
        self.redo.setEnabled(False)
        self.addAction(self.redo)

        self.addSeparator()

        self.copiar = QAction('Copiar', self)
        self.copiar.setShortcut('Ctrl+C')
        self.copiar.setEnabled(False)
        self.addAction(self.copiar)

        self.cortar = QAction('Cortar', self)
        self.cortar.setShortcut('Ctrl+X')
        self.cortar.setEnabled(False)
        self.addAction(self.cortar)

        self.pegar = QAction('Pegar', self)
        self.pegar.setShortcut('Ctrl+V')
        self.pegar.setEnabled(False)
        self.addAction(self.pegar)

        self.addSeparator()
        
        self.seleccionar = QAction(QIcon(
            'Iconos/edit-select-all.png'),
            'Seleccionar Todo', self)
        self.seleccionar.setShortcut('Ctrl+A')
        self.seleccionar.setEnabled(False)
        self.addAction(self.seleccionar)

    def setStatus(self, paste, undo, redo, copy, selectAll):
        self.pegar.setEnabled(paste)  #FIXME: desactivado si textwidget no tiene el cursor activo
        self.undo.setEnabled(undo)
        self.redo.setEnabled(redo)
        self.copiar.setEnabled(copy)
        self.cortar.setEnabled(copy)
        self.seleccionar.setEnabled(selectAll)
