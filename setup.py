#!/usr/bin/env python
# -*- coding:utf-8 -*-
from cx_Freeze import setup, Executable

setup(
    name = 'clip_translate',
    version = '0.1',
    description = 'Translate through the clipboard',
    executables = [Executable('Clip_Translate.py')]
)