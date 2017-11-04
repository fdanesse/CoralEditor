#!/usr/bin/python3
# -*- coding: utf-8 -*-

from PyQt5.QtCore import pyqtSignal
from PyQt5.QtCore import QObject
from PyQt5.QtCore import Qt

from PyQt5.QtWidgets import QMenu
from PyQt5.QtWidgets import QAction
#from PyQt5.QtWidgets import qApp

from PyQt5.QtGui import QIcon


class Communicate(QObject):
    new_file = pyqtSignal()
    open_file = pyqtSignal()
    save_file = pyqtSignal()
    save_file_as = pyqtSignal()


class MenuArchivo(QMenu):

    def __init__(self, parent):
        QMenu.__init__(self, "&Archivo", parent)

        self.sig = Communicate()
        #self.parent = parent

        self.new = QAction(QIcon(
            'Iconos/document-new.png'), 'Nuevo', self)
        self.new.setShortcut('Ctrl+N')
        self.new.triggered.connect(self.sig.new_file.emit)
        self.addAction(self.new)

        self.open = QAction(QIcon(
            'Iconos/document-open.png'), 'Abrir...', self)
        self.open.setShortcut('Ctrl+O')
        self.open.triggered.connect(self.sig.open_file.emit)
        self.addAction(self.open)

        self.addSeparator()

        self.save = QAction(QIcon(
            'Iconos/document-save.png'), 'Guardar', self)
        self.save.setShortcut('Ctrl+S')
        self.save.triggered.connect(self.sig.save_file.emit)
        self.save.setEnabled(False)
        self.addAction(self.save)

        self.saveas = QAction(QIcon(
            'Iconos/document-save-as.png'), 'Guardar Como...', self)
        self.saveas.triggered.connect(self.sig.save_file_as.emit)
        self.saveas.setEnabled(False)
        self.addAction(self.saveas)

        '''
        item = QAction('Salir', self)  #QAction(QIcon(
            'Iconos/coraleditor.png'), '&Exit', self)
        item.triggered.connect(qApp.quit)
        item.setShortcut('Ctrl+X')
        item.setStatusTip('Salir de la Aplicación')
        self.addAction(item)

        item = QAction('View statusbar', self, checkable=True)
        item.setStatusTip('View statusbar')
        item.setChecked(True)
        item.triggered.connect(self.toggleMenu)
        self.addAction(item)
        '''

    def setFilesTabs(self, tabs):
        if not tabs:
            self.save.setEnabled(tabs)
        self.saveas.setEnabled(tabs)

    def setStatus(self, modified):
        self.save.setEnabled(modified)

    def toggleMenu(self, state):
        '''
        if state:
            self.statusBar().show()
        else:
            self.statusBar().hide()
        '''
        pass