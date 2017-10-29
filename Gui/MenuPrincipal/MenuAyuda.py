#!/usr/bin/python3
# -*- coding: utf-8 -*-

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMenu
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QHBoxLayout
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QAction
#from PyQt5.QtGui import QIcon


class MenuAyuda(QMenu):

    def __init__(self, parent):
        QMenu.__init__(self, "A&yuda", parent)

        self.parent = parent

        curso = QMenu("Curso Inicial", self)
        item = QAction('Directorios y Archivos', self)
        item.triggered.connect(self.__open_help)
        curso.addAction(item)
        item = QAction('Permisos de Archivos y Directorios', self)
        item.triggered.connect(self.__open_help)
        curso.addAction(item)
        self.addMenu(curso)

        curso = QMenu("Programar en python", self)
        item = QAction('Escribir un programa', self)
        item.triggered.connect(self.__open_help)
        curso.addAction(item)
        item = QAction('Tipos de Datos', self)
        item.triggered.connect(self.__open_help)
        curso.addAction(item)
        self.addMenu(curso)

        self._help = None

    def __open_help(self):
        if not self._help:
            self._help = WindowAyuda(self.parent)
            self._help.show()
        else:
            self._help.show()


class WindowAyuda(QWidget):

    def __init__(self, parent):
        QWidget.__init__(self, parent)

        root_size = parent.size()
        w = root_size.width()
        h = root_size.height()

        # http://doc.qt.io/qt-5/qt.html#WindowType-enum
        self.setWindowFlags(Qt.Tool)  #Qt.Window | Qt.WindowStaysOnTopHint
        #self.activateWindow()
        self.setGeometry(w-(w/3),0,w/3,h)
        #self.resize(300, 300)
        #self.setCentralWidget()
        self.setWindowTitle("Ayuda")