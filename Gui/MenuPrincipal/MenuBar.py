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

    def setFilesTabs(self, tabs):
        self.menu_edicion.setEnabled(tabs)
        self.menu_codigo.setEnabled(tabs)
        self.menu_archivo.setFilesTabs(tabs)

    def setStatus(self, status):
        paste = status.get("paste", True)
        undo = status.get("undo", True)
        redo = status.get("redo", True)
        modified = status.get("modified", True)
        #FIXME: Implementar canCopy()

        self.menu_archivo.setStatus(modified)
        self.menu_edicion.setStatus(paste, undo, redo)
        # FIXME: en menu_edicion seleccionar se activa si hay archivo con texto y sin seleccionar