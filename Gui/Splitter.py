#!/usr/bin/python3
# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QSplitter

from Gui.TabWidget import TabWidget
from Gui.CodeInspector import CodeInspector
from Gui.Tools import Tools


class Splitter(QSplitter):

    def __init__(self, parent):
        QSplitter.__init__(self, parent)

        self.parent = parent
       
        codeInspector = CodeInspector(self)
        self.addWidget(codeInspector)

        self.tabwidget = TabWidget(self)
        self.addWidget(self.tabwidget)

        tools = Tools(self)
        self.addWidget(tools)