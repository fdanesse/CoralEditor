#!/usr/bin/python3
# -*- coding: utf-8 -*-

from PyQt5.QtCore import pyqtSignal
from PyQt5.QtCore import QObject
from PyQt5.QtCore import Qt

from PyQt5.QtWidgets import QToolBar
from PyQt5.QtWidgets import QAction
#from PyQt5.QtWidgets import qApp

from PyQt5.QtGui import QIcon


class Communicate(QObject):
    new_file = pyqtSignal()
    open_file = pyqtSignal()
    save_file = pyqtSignal()
    save_file_as = pyqtSignal()
    #myclick = pyqtSignal()


class Toolbar(QToolBar):
    #https://www.tutorialspoint.com/pyqt/pyqt_qtoolbar_widget.htm
    #https://github.com/Programmica/pyqt5-tutorial/blob/master/toolbar.rst

    def __init__(self, parent):
        #QToolBar.__init__(self, "")
        super(Toolbar, self).__init__(parent)

        self.sig = Communicate()
        self.parent = parent
    
        #self.setStyleSheet("background-color: yellow; color: white;")

        self.setOrientation(Qt.Vertical)
        self.setMovable(True)
        self.setFloatable(False)

        item = QAction(QIcon('Iconos/document-new.png'),
            'Crear Archivo', self)
        item.triggered.connect(self.sig.new_file.emit)
        #item.triggered.connect(qApp.quit)
        self.addAction(item)
        
        item = QAction(QIcon('Iconos/document-open.png'),
            'Abrir Archivo...', self)
        item.triggered.connect(self.sig.open_file.emit)
        self.addAction(item)

        self.addSeparator()

        item = QAction(QIcon('Iconos/document-save.png'),
            'Guardar Archivo', self)
        item.triggered.connect(self.sig.save_file.emit)
        self.addAction(item)

        item = QAction(QIcon('Iconos/document-save-as.png'),
            'Guardar Como...', self)
        item.triggered.connect(self.sig.save_file_as.emit)
        self.addAction(item)

        self.addSeparator()

        item = QAction(QIcon('Iconos/media-playback-start.png'),
            'Ejecutar Archivo', self)
        item.setEnabled(False)
        self.addAction(item)

        item = QAction(QIcon('Iconos/media-playback-stop.png'),
            'Detener Ejecución', self)
        item.setEnabled(False)
        self.addAction(item)

        self.addSeparator()

        item = QAction(QIcon('Iconos/edit-undo.png'),
            'Deshacer', self)
        item.setEnabled(False)
        self.addAction(item)

        item = QAction(QIcon('Iconos/edit-redo.png'),
            'Rehacer', self)
        item.setEnabled(False)
        self.addAction(item)

        self.addSeparator()

        item = QAction(QIcon('Iconos/edit-select-all.png'),
            'Seleccionar Todo', self)
        item.setEnabled(False)
        self.addAction(item)

        self.addSeparator()

        item = QAction(QIcon('Iconos/buscar.png'),
            'Buscar...', self)
        item.setEnabled(False)
        self.addAction(item)