#!/usr/bin/python3
# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QMenuBar

from Gui.MenuPrincipal.MenuArchivo import MenuArchivo
from Gui.MenuPrincipal.MenuEdicion import MenuEdicion
from Gui.MenuPrincipal.MenuVer import MenuVer
from Gui.MenuPrincipal.MenuCodigo import MenuCodigo
from Gui.MenuPrincipal.MenuAyuda import MenuAyuda


class MenuBar(QMenuBar):

    def __init__(self, parent):

        QMenuBar.__init__(self)

        self.parent = parent

        self.menu_archivo = MenuArchivo(self)
        self.addMenu(self.menu_archivo)
        self.menu_edicion = MenuEdicion(self)
        self.menu_edicion.setEnabled(False)
        self.addMenu(self.menu_edicion)
        self.addMenu(MenuVer(self))
        self.menu_codigo = MenuCodigo(self)
        self.menu_codigo.setEnabled(False)
        self.addMenu(self.menu_codigo)
        self.addMenu(MenuAyuda(self))