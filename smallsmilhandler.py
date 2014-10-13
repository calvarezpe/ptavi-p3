#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

from xml.sax import make_parser
from xml.sax.handler import ContentHandler


class SmallSMILHandler(ContentHandler):

    def __init__(self):
        self.root_layout = ['width', 'height', 'background-color']
        self.region = ['id', 'top', 'bottom', 'left', 'right']
        self.img = ['src', 'region', 'begin', 'dur']
        self.audio = ['src', 'begin', 'dur']
        self.textstream = ['src', 'region']
        self.tags = []

    def startElement(self, name, attrs):
        if name == 'root-layout':
            dicc = {"name": "root-layaout"}
            for atributo in self.root_layout:
                dicc[atributo] = attrs.get(atributo, "")
            self.tags.append(dicc)
        elif name == 'region':
            dicc = {"name": "region"}
            for atributo in self.region:
                dicc[atributo] = attrs.get(atributo, "")
            self.tags.append(dicc)
        elif name == 'img':
            dicc = {"name": "img"}
            for atributo in self.img:
                dicc[atributo] = attrs.get(atributo, "")
            self.tags.append(dicc)
        elif name == 'audio':
            dicc = {"name": "audio"}
            for atributo in self.audio:
                dicc[atributo] = attrs.get(atributo, "")
            self.tags.append(dicc)
        elif name == 'textstream':
            dicc = {"name": "textstream"}
            for atributo in self.textstream:
                dicc[atributo] = attrs.get(atributo, "")
            self.tags.append(dicc)

    def get_tags(self):
        return self.tags
