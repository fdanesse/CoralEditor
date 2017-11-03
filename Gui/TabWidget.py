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

        self.tabBarAutoHide()
        self.setTabsClosable(True)
        self.setMovable(True)
        self.setTabShape(1)

        self.tabCloseRequested.connect(self.close_click)
        self.currentChanged.connect(self.tab_change)
        
    def close_click(self, index):
        widget = self.widget(index)
        self.removeTab(index)
        del(widget)
        #FIXME: Verificar archivo guardado
        #FIXME: Asegurar siempre al menos un archivo abierto?

    def tab_change(self, index):
        #FIXME: Se recogeran datos para actualizar toolbar y menu
        tab = self.widget(index).widget()
        status = tab.getStatus()

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
        self.addTab(scrollarea, QIcon('Iconos/coraleditor.png'), label)
        self.setCurrentIndex(self.count()-1)
        #self.setTabToolTip(0, "Descripción corta")
        #self.setWhatsThis("Descripción Larga")