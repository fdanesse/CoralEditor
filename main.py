#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os
import sys
#import commands FIXME: commands no funciona en python 3

from PyQt5 import QtCore

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow #QMdiArea #QWidget
#from PyQt5.QtWidgets import QAction
#from PyQt5.QtWidgets import QMenu
#from PyQt5.QtWidgets import qApp
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import QFileDialog

from PyQt5.QtGui import QIcon

from Gui.MenuPrincipal.MenuBar import MenuBar
from Gui.ToolbarPrincipal import Toolbar
from Gui.Splitter import Splitter

# Guia Rápida pyqt: http://www.w3ii.com/es/pyqt/pyqt_quick_guide.html


class Coral(QMainWindow):  #Coral(QWidget):  #A widget with no parent is called a window

    def __init__(self):
        super().__init__()

        #self.setObjectName("MainWindow") ??
        self.setStyleSheet(open("Gui/Style.qss", "r").read())
        #self.setAutoFillBackground(True) ??

        self.setWindowTitle('Coral Editor')
        self.setWindowIcon(QIcon('Iconos/coraleditor.png'))

        self.menubar = MenuBar(self)
        self.setMenuBar(self.menubar)
        self.toolbar = Toolbar(self)
        self.addToolBar(QtCore.Qt.LeftToolBarArea, self.toolbar)
        self.splitter = Splitter(self)
        self.setCentralWidget(self.splitter)
        self.statusBar().showMessage('Ready')

        self.showMaximized()  #self.setWindowState(QtCore.Qt.WindowMaximized)

        #area = QMdiArea()  # para aplicaciones con subventanas

        self.menubar.menu_archivo.sig.new_file.connect(
            self.splitter.tabwidget.new_file)
        self.menubar.menu_archivo.sig.open_file.connect(
            self.showDialog_open_file)
        
        self.menubar.menu_edicion.sig.select_all.connect(
            self.splitter.tabwidget.selectedAll)

        self.toolbar.sig.new_file.connect(self.new_file)
        self.toolbar.sig.open_file.connect(self.showDialog_open_file)

        print("Coral process:", os.getpid())

    def closeEvent(self, event):
        #FIXME: Verificar archivos sin guardar
        reply = QMessageBox.question(self, 'Message',
            "Salir de la Aplicación?", QMessageBox.Yes |
            QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def showDialog_open_file(self):
        dialog = QFileDialog(self)
        dialog.setViewMode(QFileDialog.Detail)
        dialog.setAcceptMode(QFileDialog.AcceptOpen)
        dialog.setOption(QFileDialog.DontUseNativeDialog, True)
        dialog.setOption(QFileDialog.DontResolveSymlinks, True)
        #FIXME: Mejorar sistema o completar formatos
        ret = dialog.getOpenFileNames(self, 'Abrir Archivo',
            os.environ["HOME"], "Texto (*.txt *.py *.json *.html \
            *.js *.css *.qss *.vala *.svg *.xml)")
            #;;Text files (*.txt);;XML files (*.xml)")
        for path in ret[0]:
            if os.path.exists(path):
                path = os.path.realpath(path)
                #FIXME: commands no funciona en python 3
                self.splitter.tabwidget.new_file(path)
                '''
                datos = commands.getoutput('file -ik \"%s\"' % (path))
                if "text" in datos or "x-python" in datos or \
                    "x-empty" in datos or "svg+xml" in datos or \
                    "application/xml" in datos:
                    self.new_file(path)
                else:
                    print("No se pudo abrir:", path, datos)
                '''
            else:
                print("No se pudo abrir:", path)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Coral()
    sys.exit(app.exec_())