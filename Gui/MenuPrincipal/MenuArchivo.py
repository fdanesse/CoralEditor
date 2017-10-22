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
        self.parent = parent

        #QAction('Nuevo', self)
        item = QAction(QIcon('Iconos/document-new.png'), 'Nuevo', self)
        item.setShortcut('Ctrl+N')
        item.triggered.connect(self.sig.new_file.emit)
        self.addAction(item)

        item = QAction(QIcon('Iconos/document-open.png'), 'Abrir...', self)
        item.setShortcut('Ctrl+O')
        item.triggered.connect(self.sig.open_file.emit)
        self.addAction(item)

        self.addSeparator()

        item = QAction(QIcon('Iconos/document-save.png'), 'Guardar', self)
        item.setShortcut('Ctrl+S')
        item.triggered.connect(self.sig.save_file.emit)
        self.addAction(item)

        item = QAction(QIcon('Iconos/document-save-as.png'), 'Guardar Como...', self)
        item.triggered.connect(self.sig.save_file_as.emit)
        self.addAction(item)

        '''
        item = QAction('Salir', self)  #QAction(QIcon('Iconos/coraleditor.png'), '&Exit', self)
        #item.triggered.connect(qApp.quit)
        item.setShortcut('Ctrl+X')
        item.setStatusTip('Salir de la Aplicación')
        self.addAction(item)

        item = QAction('View statusbar', self, checkable=True)
        item.setStatusTip('View statusbar')
        item.setChecked(True)
        item.triggered.connect(self.toggleMenu)
        self.addAction(item)
        '''

    def toggleMenu(self, state):
        '''
        if state:
            self.statusBar().show()
        else:
            self.statusBar().hide()
        '''
        pass