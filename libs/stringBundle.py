#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
if items were added in files in the resources/strings folder,
then execute "pyrcc5 resources.qrc -o resources.py" in the root directory
and execute "pyrcc5 ../resources.qrc -o resources.py" in the libs directory
"""
import re
import os
import sys
import locale

from PyQt5.QtCore import *

from libs.ustr import ustr


class StringBundle:

    __create_key = object()

    def __init__(self, create_key, locale_str):
        assert(create_key == StringBundle.__create_key), "StringBundle must be created using StringBundle.getBundle"
        self.id_to_message = {}
        self.__load_bundle(self.__create_path(locale_str))

    @classmethod
    def get_bundle(cls, locale_str=None):
        if locale_str is None:
            locale_str = 'en-US'
            # try:
            #     locale_str = locale.getlocale()[0] if locale.getlocale() and len(
            #         locale.getlocale()) > 0 else os.getenv('LANG')
            # except:
            #     print('Invalid locale')
                # locale_str = 'en-US'

        return StringBundle(cls.__create_key, locale_str)

    def get_string(self, string_id):
        assert(string_id in self.id_to_message), "Missing string id : " + string_id + '\n'+ os.path.join(self.base_path, f'string-en-US.properties')
        return self.id_to_message[string_id]

    def __create_path(self, locale_str):
        try:
            # PyInstaller creates a temp folder and stores path in _MEIPASS
            self.base_path = os.path.join(sys._MEIPASS, 'resources', 'strings')
        except Exception:
            self.base_path = os.path.normpath(os.path.join('resources', 'strings'))
        return os.path.join(self.base_path, f'string-{locale_str}.properties') if locale_str is not None else os.path.join(self.base_path, f'string-en-US.properties')


    def __load_bundle(self, path):
        PROP_SEPERATOR = '='
        f = QFile(path)
        if f.exists():
            if f.open(QIODevice.ReadOnly | QFile.Text):
                text = QTextStream(f)
                text.setCodec("UTF-8")

            while not text.atEnd():
                line = ustr(text.readLine())
                key_value = line.split(PROP_SEPERATOR)
                key = key_value[0].strip()
                value = PROP_SEPERATOR.join(key_value[1:]).strip().strip('"')
                self.id_to_message[key] = value

            f.close()
