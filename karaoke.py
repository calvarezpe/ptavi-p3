#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

from xml.sax import make_parser
from xml.sax.handler import ContentHandler
import smallsmilhandler
import sys
import os


class KaraokeLocal(smallsmilhandler.SmallSMILHandler):

    def __init__(self, fich):
        parser = make_parser()
        sHandler = smallsmilhandler.SmallSMILHandler()
        parser.setContentHandler(sHandler)
        parser.parse(fich)
        self.list_tags = sHandler.get_tags()

    def __str__(self):
        todo = ""
        for diccionarios in self.list_tags:
            frase = ""
            for clave in diccionarios.keys():
                if clave != "name" and diccionarios[clave] != "":
                    frase = frase + clave + "=" + diccionarios[clave] + "\t"
            todo = todo + diccionarios['name'] + "\t" + frase + "\n"
        return todo

    def do_local(self):
        list_recurso = []
        for diccionarios in self.list_tags:
            for clave in diccionarios.keys():
                if clave == "src":
                    recurso = diccionarios[clave]
                    os.system("wget -q " + recurso)
                    list_recurso = recurso.split("/")
                    recurso = list_recurso[-1]
                    diccionarios[clave] = recurso

if __name__ == "__main__":
    try:
        fich = open(sys.argv[1])
    except IndexError:
        print "Usage: python karaoke.py file.smil."

    KL = KaraokeLocal(fich)
    print KL
    KL.do_local()
    print KL
