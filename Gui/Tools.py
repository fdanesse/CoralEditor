#!/usr/bin/python3
# -*- coding: utf-8 -*-

from PyQt5.QtCore import Qt

from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QScrollArea
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QToolBar


class Tools(QWidget):

    def __init__(self, parent):
        QWidget.__init__(self, parent)

        self.parent = parent

        root_size = self.parent.size()
        w = root_size.width()
        #h = root_size.height()
        self.setMaximumWidth(450)

        hbox = QVBoxLayout(self)
        self.setLayout(hbox)

        scroll = QScrollArea(self)
        scroll.setAlignment(Qt.AlignLeft | Qt.AlignTop)
        scroll.setWidgetResizable(True)

        toolbar = QToolBar(self)

        #scroll.setWidget(self.treeView)
        hbox.addWidget(toolbar)
        hbox.addWidget(scroll)