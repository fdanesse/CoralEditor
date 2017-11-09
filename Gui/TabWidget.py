#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os

from PyQt5.QtCore import Qt

from PyQt5.QtWidgets import QTabWidget
from PyQt5.QtWidgets import QScrollArea

from PyQt5.QtGui import QIcon

from Gui.TextEdit import TextEdit


class TabWidget(QTabWidget):
    # https://github.com/Programmica/pyqt5-tutorial/blob/master/tabwidget.rst
    # https://doc.qt.io/qt-5/qtabwidget.html

    def __init__(self, parent):
        super(TabWidget, self).__init__(parent)

        self.parent = parent

        self.tabBarAutoHide()
        self.setTabsClosable(True)
        self.setMovable(True)
        self.setTabShape(1)

        self.tabCloseRequested.connect(self.__tab_close)
        self.currentChanged.connect(self.__tab_changed)
        
    def __tab_close(self, index):
        widget = self.widget(index)
        self.removeTab(index)
        del(widget)
        #FIXME: Verificar archivo guardado

    def __tab_changed(self, index):
        """
        Actualizar toolbar y menu principales.
        index == -1 si no hay tab en tabwidget.
        """
        if index > -1:
            tab = self.widget(index).widget()
            status = tab.getStatus()
            self.parent.parent.toolbar.setStatus(status)
            self.parent.parent.menubar.setStatus(status)
        #FIXME: Asegurar siempre al menos un archivo abierto?
        tabs = bool(self.count())
        self.parent.parent.menubar.setFilesTabs(tabs)
        self.parent.parent.toolbar.setFilesTabs(tabs)

    def new_file(self, path=""):
        label = "Sin Nombre"
        if os.path.exists(path):
            label = os.path.basename(path)
        #FIXME: Si el archivo ya esta abierto solo cambiar a su tab
        scrollarea = QScrollArea(self)
        scrollarea.setAlignment(Qt.AlignLeft | Qt.AlignTop)
        scrollarea.setWidgetResizable(True)
        textEdit = TextEdit(scrollarea, path=path)
        scrollarea.setWidget(textEdit)
        # FIXME: conectar señales de textEdit para actualizar toolbar y menu
        self.addTab(scrollarea, QIcon(
            'Iconos/coraleditor.png'), label)
        self.setCurrentIndex(self.count()-1)
        
        #self.setTabToolTip(0, "Descripción corta")
        #self.setWhatsThis("Descripción Larga")

    def selectedAll(self):
        self.currentWidget().widget().selectAll()