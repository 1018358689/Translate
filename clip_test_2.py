#!/usr/bin/env python
# -*- coding:utf-8 -*-
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QApplication

app = QApplication([])
clipboard = app.clipboard()
def on_clipboard_change():
    data = clipboard.mimeData()
    if data.hasFormat('text/uri-list'):
        for path in data.urls():
            print(path)
    if data.hasText():
        print(data.text())

clipboard.dataChanged.connect(on_clipboard_change)
app.exec_()