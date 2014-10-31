# -*- coding: UTF-8 -*-
#
# generated by wxGlade 0.6.8 on Sun Aug 10 21:46:08 2014
#

import wx
# begin wxGlade: dependencies
import wx.calendar
# end wxGlade
from ver_editar import ver_editar
from crear_oferta import crear_oferta
# begin wxGlade: extracode
# end wxGlade

from Servidor import *

KEY='the_same_string_for_server_and_client'
print 'Conectando ...'
Pyro4.config.HMAC_KEY=KEY
servicio = Pyro4.Proxy('PYRONAME:servidor1.configura')
print 'Conectado al servicio !'
#variables globales
Menus = []
Ofertas = []
Items = []
#fin de variables  globales

servicio.online()
Menus = serpent.loads(servicio.getMenus())
Ofertas = serpent.loads(servicio.getOfertas())
Items = serpent.loads(servicio.getItems())


class MyFrame(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: MyFrame.__init__
        kwds["style"] = wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        
        # Menu Bar
        self.main_menubar = wx.MenuBar()
        self.Inicio = wx.Menu()
        self.main_menubar.Append(self.Inicio, _("Inicio"))
        self.Online = wx.Menu()
        self.main_menubar.Append(self.Online, _("Online"))
        self.Salir = wx.Menu()
        self.main_menubar.Append(self.Salir, _("Salir"))
        self.SetMenuBar(self.main_menubar)
        # Menu Bar end
        self.button_1 = wx.Button(self, wx.ID_ANY, _("Crear"))
        self.button_2 = wx.Button(self, wx.ID_ANY, _("Ver / Editar"))
        self.sizer_2_staticbox = wx.StaticBox(self, wx.ID_ANY, _("Menu"))
        self.calendar_ctrl_1 = wx.calendar.CalendarCtrl(self, wx.ID_ANY, style=wx.calendar.CAL_MONDAY_FIRST)
        self.button_3 = wx.Button(self, wx.ID_ANY, _("Crear"))
        self.button_4 = wx.Button(self, wx.ID_ANY, _("Ver / Editar"))
        self.sizer_3_staticbox = wx.StaticBox(self, wx.ID_ANY, _("Ofertas"))
        self.calendar_ctrl_2 = wx.calendar.CalendarCtrl(self, wx.ID_ANY, style=wx.calendar.CAL_MONDAY_FIRST)
        self.list_ctrl_1 = wx.ListCtrl(self, wx.ID_ANY, style=wx.LC_REPORT | wx.SUNKEN_BORDER)
        self.list_ctrl_2 = wx.ListCtrl(self, wx.ID_ANY, style=wx.LC_REPORT | wx.SUNKEN_BORDER)

        self.list_ctrl_1.InsertColumn(0,"Nombre")
        self.list_ctrl_1.InsertColumn(1,"Precio")
        self.list_ctrl_1.InsertColumn(2,"Disponible")

        for data in Menus:
            # 0 will insert at the start of the list
            pos = self.list_ctrl_1.InsertStringItem(0,data['nombre'])
            # add values in the other columns on the same row
            self.list_ctrl_1.SetStringItem(pos,1,str(data['precio']))
            self.list_ctrl_1.SetStringItem(pos,2,str(data['disponible']))
        for data in Ofertas:
            # 0 will insert at the start of the list
            pos = self.list_ctrl_2.InsertStringItem(0,data['nombre'])
            # add values in the other columns on the same row
            self.list_ctrl_2.SetStringItem(pos,1,str(data['precio']))
            self.list_ctrl_2.SetStringItem(pos,2,str(data['disponible']))

        self.list_ctrl_2.InsertColumn(0,"Nombre")
        self.list_ctrl_2.InsertColumn(1,"Precio")
        self.list_ctrl_2.InsertColumn(2,"Disponible")
        
        self.__set_properties()
        self.__do_layout()

        self.Bind(wx.EVT_BUTTON, self.crear_menu, self.button_1)
        self.Bind(wx.EVT_BUTTON, self.ver_edit_menu, self.button_2)
        self.Bind(wx.EVT_BUTTON, self.crear_oferta, self.button_3)
        self.Bind(wx.EVT_BUTTON, self.ver_edit_oferta, self.button_4)
        self.Bind(wx.EVT_LIST_ITEM_SELECTED, self.menu_selected, self.list_ctrl_1)
        self.Bind(wx.EVT_LIST_ITEM_SELECTED, self.oferta_selected, self.list_ctrl_2)
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: MyFrame.__set_properties
        self.SetTitle(_("Servidor"))
        self.SetSize((697, 657))
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: MyFrame.__do_layout
        sizer_1 = wx.BoxSizer(wx.VERTICAL)
        grid_sizer_1 = wx.GridSizer(2, 2, 0, 0)
        grid_sizer_3 = wx.GridSizer(2, 1, 0, 0)
        self.sizer_3_staticbox.Lower()
        sizer_3 = wx.StaticBoxSizer(self.sizer_3_staticbox, wx.HORIZONTAL)
        grid_sizer_5 = wx.GridSizer(1, 2, 0, 0)
        grid_sizer_2 = wx.GridSizer(2, 1, 0, 0)
        self.sizer_2_staticbox.Lower()
        sizer_2 = wx.StaticBoxSizer(self.sizer_2_staticbox, wx.HORIZONTAL)
        grid_sizer_4 = wx.GridSizer(1, 2, 0, 0)
        grid_sizer_4.Add(self.button_1, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL | wx.SHAPED, 0)
        grid_sizer_4.Add(self.button_2, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL | wx.SHAPED, 0)
        sizer_2.Add(grid_sizer_4, 1, wx.EXPAND, 0)
        grid_sizer_2.Add(sizer_2, 1, wx.EXPAND | wx.SHAPED, 0)
        grid_sizer_2.Add(self.calendar_ctrl_1, 0, wx.ALL | wx.EXPAND | wx.ALIGN_CENTER_HORIZONTAL, 5)
        grid_sizer_1.Add(grid_sizer_2, 1, wx.EXPAND, 0)
        grid_sizer_5.Add(self.button_3, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL | wx.SHAPED, 0)
        grid_sizer_5.Add(self.button_4, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL | wx.SHAPED, 0)
        sizer_3.Add(grid_sizer_5, 1, wx.EXPAND, 0)
        grid_sizer_3.Add(sizer_3, 1, wx.EXPAND | wx.SHAPED, 0)
        grid_sizer_3.Add(self.calendar_ctrl_2, 0, wx.ALL | wx.EXPAND | wx.ALIGN_CENTER_HORIZONTAL, 5)
        grid_sizer_1.Add(grid_sizer_3, 1, wx.EXPAND, 0)
        grid_sizer_1.Add(self.list_ctrl_1, 1, wx.EXPAND, 0)
        grid_sizer_1.Add(self.list_ctrl_2, 1, wx.EXPAND, 0)
        sizer_1.Add(grid_sizer_1, 1, wx.EXPAND, 0)
        self.SetSizer(sizer_1)
        self.Layout()
        # end wxGlade


    def crear_menu(self, event):  # wxGlade: MyFrame.<event_handler>
        print "Event handler 'crear_menu'"
        crearMenu = ver_editar(self)
        crearMenu.Show()


    def ver_edit_menu(self, event):  # wxGlade: MyFrame.<event_handler>
        print "Event handler 'ver_edit_menu'"
        editarMenu = ver_editar(self)
        editarMenu.Show()

    def crear_oferta(self, event):  # wxGlade: MyFrame.<event_handler>
        print "Event handler 'crear_oferta'"
        crearOferta = crear_oferta(self)
        crearOferta.Show()

    def ver_edit_oferta(self, event):  # wxGlade: MyFrame.<event_handler>
        print "Event handler 'ver_edit_oferta'"
        verOferta = crear_oferta(self)
        verOferta.Show()

    def menu_selected(self, event):  # wxGlade: MyFrame.<event_handler>
        print "Event handler 'menu_selected' not implemented!"
        event.Skip()

    def oferta_selected(self, event):  # wxGlade: MyFrame.<event_handler>
        print "Event handler 'oferta_selected' not implemented!"
        event.Skip()

# end of class MyFrame