#!/usr/bin/python3
# -*- coding: utf-8 -*-

from PyQt5.QtCore import Qt

from PyQt5.QtWidgets import QTreeView
from PyQt5.QtWidgets import QScrollArea
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QToolBar

from PyQt5.QtGui import QIcon
from PyQt5.QtGui import QStandardItemModel


class CodeInspector(QWidget):

    def __init__(self, parent):
        QWidget.__init__(self, parent)

        self.parent = parent

        root_size = self.parent.size()
        w = root_size.width()
        #h = root_size.height()
        self.setMaximumWidth(250)

        hbox = QVBoxLayout(self)
        self.setLayout(hbox)

        scroll = QScrollArea(self)
        scroll.setAlignment(Qt.AlignLeft | Qt.AlignTop)
        scroll.setWidgetResizable(True)

        self.treeView = QTreeView(self)
        self.treeView.setAlternatingRowColors(True)
        model = self.createModel()
        self.treeView.setModel(model)

        toolbar = QToolBar(self)

        scroll.setWidget(self.treeView)
        hbox.addWidget(scroll)
        hbox.addWidget(toolbar)


        model.insertRow(0)
        model.setData(model.index(0, 0), 0)
        model.setData(model.index(0, 1), 'un icono')
        model.setData(model.index(0, 2), 'una definición')
        
    def createModel(self):
        model = QStandardItemModel(0, 3, self.treeView)
        model.setHeaderData(0, Qt.Horizontal, "id")
        model.setHeaderData(1, Qt.Horizontal, "icon")
        model.setHeaderData(2, Qt.Horizontal, "def")
        return model