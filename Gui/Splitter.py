#!/usr/bin/python3
# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QSplitter
from PyQt5.QtWidgets import QTreeView

from Gui.TabWidget import TabWidget


class Splitter(QSplitter):

    def __init__(self, parent):
        QSplitter.__init__(self, parent)

        self.parent = parent

        treeview = QTreeView(self)
        self.tabwidget = TabWidget(self)
        self.addWidget(treeview)
        self.addWidget(self.tabwidget)

        treeview = QTreeView(self)
        self.addWidget(treeview)