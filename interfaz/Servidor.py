#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#
# generated by wxGlade 0.6.8 on Sun Aug 10 21:46:08 2014
#

# This is an automatically generated file.
# Manual changes will be overwritten without warning!

import wx
import gettext
from MyFrame import *

import Pyro4

import time
from datetime import date
#from Models import *


import base64
import serpent
import os
import time



class InterfazServidor(wx.App):
    def OnInit(self):
        wx.InitAllImageHandlers()
        main = MyFrame(None, wx.ID_ANY, "")
        self.SetTopWindow(main)
        main.Show()
        return 1

# end of class InterfazServidor



if __name__ == "__main__":
    gettext.install("Servidor") # replace with the appropriate catalog name
    

    try:
        Servidor = InterfazServidor(0)
        Servidor.MainLoop()
        #Servidor.start()
    except Exception, e:
        print 'No se encontro el servidor'