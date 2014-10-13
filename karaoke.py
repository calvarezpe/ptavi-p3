#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

from xml.sax import make_parser
from xml.sax.handler import ContentHandler
import smallsmilhandler
import sys
import os

lista = sys.argv

try:
    fich = open(lista[1])
except IndexError:
    print "Usage: python karaoke.py file.smil."

parser = make_parser()
sHandler = smallsmilhandler.SmallSMILHandler()
parser.setContentHandler(sHandler)
parser.parse(fich)

list_tags = sHandler.get_tags()
list_recurso = []

for diccionarios in list_tags:
    frase = ""
    for clave in diccionarios.keys():
        if clave == "src":
            recurso = diccionarios[clave]
            os.system("wget -q " + recurso)
            list_recurso = recurso.split("/")
            recurso = list_recurso[-1]
            diccionarios[clave] = recurso
        if clave != "name" and diccionarios[clave] != "":
            frase = frase + clave + "=" + diccionarios[clave] + "\t"
    print diccionarios['name'], "\t", frase
