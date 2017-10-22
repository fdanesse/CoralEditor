#!/usr/bin/python3
# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QMenu
from PyQt5.QtWidgets import QAction

from PyQt5.QtGui import QIcon


class MenuAyuda(QMenu):

    def __init__(self, parent):
        QMenu.__init__(self, "A&yuda", parent)
