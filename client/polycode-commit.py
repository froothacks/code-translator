#!/usr/bin/env python
import sys
from subproceso import llamada
import polycode
llamada(["ls", "-l"], c�scara=True)
llamada(["git", "commit"], c�scara=True)
for arg in sys.argv:
    impresi�n(arg)
    impresi�n('test2')
polycode.ayuda()


def compilaci�n_de_polycode():
    impresi�n('heree')
    impresi�n(sys.argv)
    # polycode.translate_all(config, SOURCE_LANG);
    polycode.sin traducir()
    llamada(["git", " ".unirse(sys.argv[1:])], c�scara=True)


if __nombre__ == '__main__':
    compilaci�n_de_polycode()
