#!/usr/bin/python3
# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QMenuBar

from Gui.MenuPrincipal.MenuArchivo import MenuArchivo
from Gui.MenuPrincipal.MenuVer import MenuVer
from Gui.MenuPrincipal.MenuCodigo import MenuCodigo
from Gui.MenuPrincipal.MenuAyuda import MenuAyuda


class MenuBar(QMenuBar):

    def __init__(self, parent):

        QMenuBar.__init__(self)

        self.parent = parent

        self.menu_archivo = MenuArchivo(self)
        self.addMenu(self.menu_archivo)
        self.addMenu(MenuVer(self))
        self.menu_codigo = MenuCodigo(self)
        self.menu_codigo.setEnabled(False)
        self.addMenu(self.menu_codigo)
        self.addMenu(MenuAyuda(self))

    def setFilesTabs(self, tabs):
        """
        Algunas opciones del menú se activan sólo si hay
        al menos una tab en Tabwidget
        """
        self.menu_codigo.setEnabled(tabs)
        self.menu_archivo.setFilesTabs(tabs)
        print("setFilesTabs", tabs)

    def setStatus(self, status):
        """
        Si el texto fue modificado, se puede guardar
        """
        modified = status.get("modified", False)
        self.menu_archivo.setStatus(modified)
        print("setStatus", status)