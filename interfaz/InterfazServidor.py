#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#
# generated by wxGlade 0.6.8 on Sat Aug  9 15:23:42 2014
#

import wx
import wx.calendar

# begin wxGlade: dependencies
import gettext
# end wxGlade
from ServicioPyro import *
# begin wxGlade: extracode
# end wxGlade


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
        #self.button_2 = wx.Button(self, wx.ID_ANY, _("Ver / Editar"))
        self.sizer_2_staticbox = wx.StaticBox(self, wx.ID_ANY, _("Menu"))
        self.calendar_ctrl_1 = wx.calendar.CalendarCtrl(self, wx.ID_ANY, style=wx.calendar.CAL_MONDAY_FIRST)
        self.button_3 = wx.Button(self, wx.ID_ANY, _("Crear"))
        #self.button_4 = wx.Button(self, wx.ID_ANY, _("Ver / Editar"))
        self.sizer_3_staticbox = wx.StaticBox(self, wx.ID_ANY, _("Ofertas"))
        self.calendar_ctrl_2 = wx.calendar.CalendarCtrl(self, wx.ID_ANY, style=wx.calendar.CAL_MONDAY_FIRST)
        self.list_ctrl_1 = wx.ListCtrl(self, wx.ID_ANY, style=wx.LC_REPORT | wx.SUNKEN_BORDER)
        self.list_ctrl_2 = wx.ListCtrl(self, wx.ID_ANY, style=wx.LC_REPORT | wx.SUNKEN_BORDER)

        self.list_ctrl_1.InsertColumn(0,"Nombre")
        self.list_ctrl_1.InsertColumn(1,"Precio")
        self.list_ctrl_1.InsertColumn(2,"Disponible")

        for data in servicio.Menus:
            # 0 will insert at the start of the list
            pos = self.list_ctrl_1.InsertStringItem(0,data['nombre'])
            # add values in the other columns on the same row
            self.list_ctrl_1.SetStringItem(pos,1,str(data['precio']))
            self.list_ctrl_1.SetStringItem(pos,2,str(data['disponible']))
        for data in servicio.Ofertas:
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
        #self.Bind(wx.EVT_BUTTON, self.ver_edit_menu, self.button_2)
        self.Bind(wx.EVT_BUTTON, self.crear_oferta, self.button_3)
        #self.Bind(wx.EVT_BUTTON, self.ver_edit_oferta, self.button_4)
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
        grid_sizer_5 = wx.GridSizer(1, 1, 0, 0) # cambiado
        grid_sizer_2 = wx.GridSizer(2, 1, 0, 0)
        self.sizer_2_staticbox.Lower()
        sizer_2 = wx.StaticBoxSizer(self.sizer_2_staticbox, wx.HORIZONTAL)
        grid_sizer_4 = wx.GridSizer(1, 1, 0, 0) # cambiado
        grid_sizer_4.Add(self.button_1, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL | wx.SHAPED, 0)
        #grid_sizer_4.Add(self.button_2, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL | wx.SHAPED, 0)
        sizer_2.Add(grid_sizer_4, 1, wx.EXPAND, 0)
        grid_sizer_2.Add(sizer_2, 1, wx.EXPAND | wx.SHAPED, 0)
        grid_sizer_2.Add(self.calendar_ctrl_1, 0, wx.ALL | wx.EXPAND | wx.ALIGN_CENTER_HORIZONTAL, 5)
        grid_sizer_1.Add(grid_sizer_2, 1, wx.EXPAND, 0)
        grid_sizer_5.Add(self.button_3, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL | wx.SHAPED, 0)
        #grid_sizer_5.Add(self.button_4, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL | wx.SHAPED, 0)
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

class ver_editar(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: ver_editar.__init__
        kwds["style"] = wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.calendar_ctrl_3 = wx.calendar.CalendarCtrl(self, wx.ID_ANY, style=wx.calendar.CAL_MONDAY_FIRST)
        self.text_ctrl_3 = wx.TextCtrl(self, wx.ID_ANY, "")
        self.sizer_34_staticbox = wx.StaticBox(self, wx.ID_ANY, _("Nombre"))
        self.text_ctrl_1 = wx.TextCtrl(self, wx.ID_ANY, "")
        self.sizer_12_staticbox = wx.StaticBox(self, wx.ID_ANY, _("Duracion"))
        self.text_ctrl_2 = wx.TextCtrl(self, wx.ID_ANY, "")
        self.sizer_13_staticbox = wx.StaticBox(self, wx.ID_ANY, _("Precio"))
        self.checkbox_1 = wx.CheckBox(self, wx.ID_ANY, "")
        self.sizer_14_staticbox = wx.StaticBox(self, wx.ID_ANY, _("Activo"))
        self.Guardar = wx.Button(self, wx.ID_ANY, _("Guardar"))
        self.button_14 = wx.Button(self, wx.ID_ANY, _("img"))
        self.list_ctrl_5a = wx.ListCtrl(self, wx.ID_ANY, style=wx.LC_REPORT | wx.SUNKEN_BORDER)
        self.sizer_15_staticbox = wx.StaticBox(self, wx.ID_ANY, _("Primeros"))
        self.list_ctrl_5ab = wx.ListCtrl(self, wx.ID_ANY, style=wx.LC_REPORT | wx.SUNKEN_BORDER)
        self.sizer_16_staticbox = wx.StaticBox(self, wx.ID_ANY, _("Segundos"))
        self.list_ctrl_5abc = wx.ListCtrl(self, wx.ID_ANY, style=wx.LC_REPORT | wx.SUNKEN_BORDER)
        self.sizer_17_staticbox = wx.StaticBox(self, wx.ID_ANY, _("Postres"))
        self.button_5 = wx.Button(self, wx.ID_ANY, _("<<"))
        self.button_7 = wx.Button(self, wx.ID_ANY, _(">>"))
        self.button_6 = wx.Button(self, wx.ID_ANY, _("Crear item"))
        self.button_8 = wx.Button(self, wx.ID_ANY, _("<<"))
        self.button_9 = wx.Button(self, wx.ID_ANY, _(">>"))
        self.button_10 = wx.Button(self, wx.ID_ANY, _("<<"))
        self.button_11 = wx.Button(self, wx.ID_ANY, _(">>"))
        self.list_ctrl_3 = wx.ListCtrl(self, wx.ID_ANY, style=wx.LC_REPORT | wx.SUNKEN_BORDER)

        self.list_ctrl_3.InsertColumn(0,"Nombre")
        self.list_ctrl_3.InsertColumn(1,"Precio")
        self.list_ctrl_3.InsertColumn(2,"Disponible")

        self.list_ctrl_5ab.InsertColumn(0,"Nombre")
        self.list_ctrl_5ab.InsertColumn(1,"Precio")
        self.list_ctrl_5ab.InsertColumn(2,"Disponible")

        self.list_ctrl_5a.InsertColumn(0,"Nombre")
        self.list_ctrl_5a.InsertColumn(1,"Precio")
        self.list_ctrl_5a.InsertColumn(2,"Disponible")

        self.list_ctrl_5abc.InsertColumn(0,"Nombre")
        self.list_ctrl_5abc.InsertColumn(1,"Precio")
        self.list_ctrl_5abc.InsertColumn(2,"Disponible")

        for data in servicio.Items:
            # 0 will insert at the start of the list
            pos = self.list_ctrl_3.InsertStringItem(0,data['_data']['nombre'])
            # add values in the other columns on the same row
            self.list_ctrl_3.SetStringItem(pos,1,str(data['_data']['precio']))
            self.list_ctrl_3.SetStringItem(pos,2,str(data['_data']['disponible']))

        self.__set_properties()
        self.__do_layout()

        self.Bind(wx.calendar.EVT_CALENDAR, self.calendario, self.calendar_ctrl_3)
        self.Bind(wx.EVT_TEXT, self.solo_num, self.text_ctrl_1)
        self.Bind(wx.EVT_TEXT, self.solo_num, self.text_ctrl_2)
        self.Bind(wx.EVT_CHECKBOX, self.activo, self.checkbox_1)
        self.Bind(wx.EVT_BUTTON, self.save_menu, self.Guardar)
        self.Bind(wx.EVT_BUTTON, self.load_img, self.button_14)
        self.Bind(wx.EVT_LISTBOX_DCLICK, self.primero_selec, self.list_ctrl_5a)
        self.Bind(wx.EVT_LISTBOX_DCLICK, self.segundo_selec, self.list_ctrl_5ab)
        self.Bind(wx.EVT_LISTBOX_DCLICK, self.postre_selec, self.list_ctrl_5abc)
        self.Bind(wx.EVT_BUTTON, self.add_prim, self.button_5)
        self.Bind(wx.EVT_BUTTON, self.left_prim, self.button_7)
        self.Bind(wx.EVT_BUTTON, self.crear_item, self.button_6)
        self.Bind(wx.EVT_BUTTON, self.add_seg, self.button_8)
        self.Bind(wx.EVT_BUTTON, self.left_seg, self.button_9)
        self.Bind(wx.EVT_BUTTON, self.add_postre, self.button_10)
        self.Bind(wx.EVT_BUTTON, self.left_postre, self.button_11)
        self.Bind(wx.EVT_LIST_ITEM_SELECTED, self.item_selec, self.list_ctrl_3)

        self.crearItem = None
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: ver_editar.__set_properties
        self.SetTitle(_("frame_1"))
        self.SetSize((650, 531))
        self.checkbox_1.SetValue(1)
        self.list_ctrl_3.SetMinSize((164, 500))
        self.calendar_ctrl_3.SetMinSize((215, 140))
        # primeros segundos y postre
        self.list_ctrl_5a.SetMinSize((164, 140))
        self.list_ctrl_5ab.SetMinSize((164, 140))
        self.list_ctrl_5abc.SetMinSize((164, 140))
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: ver_editar.__do_layout
        sizer_4 = wx.BoxSizer(wx.VERTICAL)
        sizer_5 = wx.BoxSizer(wx.HORIZONTAL)
        grid_sizer_6 = wx.FlexGridSizer(1, 2, 0, 0)
        sizer_7 = wx.BoxSizer(wx.VERTICAL)
        sizer_10 = wx.BoxSizer(wx.VERTICAL)
        sizer_11 = wx.BoxSizer(wx.VERTICAL)
        sizer_8 = wx.BoxSizer(wx.VERTICAL)
        sizer_9 = wx.BoxSizer(wx.VERTICAL)
        sizer_6 = wx.BoxSizer(wx.VERTICAL)
        self.sizer_17_staticbox.Lower()
        sizer_17 = wx.StaticBoxSizer(self.sizer_17_staticbox, wx.HORIZONTAL)
        self.sizer_16_staticbox.Lower()
        sizer_16 = wx.StaticBoxSizer(self.sizer_16_staticbox, wx.HORIZONTAL)
        self.sizer_15_staticbox.Lower()
        sizer_15 = wx.StaticBoxSizer(self.sizer_15_staticbox, wx.HORIZONTAL)
        grid_sizer_7 = wx.FlexGridSizer(7, 1, 0, 0)
        self.sizer_14_staticbox.Lower()
        sizer_14 = wx.StaticBoxSizer(self.sizer_14_staticbox, wx.HORIZONTAL)
        self.sizer_13_staticbox.Lower()
        sizer_13 = wx.StaticBoxSizer(self.sizer_13_staticbox, wx.HORIZONTAL)
        self.sizer_12_staticbox.Lower()
        sizer_12 = wx.StaticBoxSizer(self.sizer_12_staticbox, wx.HORIZONTAL)
        self.sizer_34_staticbox.Lower()
        sizer_34 = wx.StaticBoxSizer(self.sizer_34_staticbox, wx.HORIZONTAL)
        grid_sizer_7.Add(self.calendar_ctrl_3, 0, 0, 0)
        sizer_34.Add(self.text_ctrl_3, 0, 0, 0)
        grid_sizer_7.Add(sizer_34, 1, wx.EXPAND, 0)
        sizer_12.Add(self.text_ctrl_1, 0, 0, 0)
        grid_sizer_7.Add(sizer_12, 1, wx.EXPAND, 0)
        sizer_13.Add(self.text_ctrl_2, 0, 0, 0)
        grid_sizer_7.Add(sizer_13, 1, wx.EXPAND, 0)
        sizer_14.Add(self.checkbox_1, 0, 0, 0)
        grid_sizer_7.Add(sizer_14, 1, wx.EXPAND, 0)
        grid_sizer_7.Add(self.Guardar, 0, wx.ALIGN_CENTER_HORIZONTAL, 0)
        grid_sizer_7.Add(self.button_14, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL, 0)
        sizer_5.Add(grid_sizer_7, 1, wx.EXPAND, 0)
        sizer_15.Add(self.list_ctrl_5a, 1, wx.EXPAND, 0)
        sizer_6.Add(sizer_15, 1, wx.EXPAND | wx.ALIGN_RIGHT , 0)
        sizer_16.Add(self.list_ctrl_5ab, 1, wx.EXPAND , 0)
        sizer_6.Add(sizer_16, 1, wx.EXPAND | wx.ALIGN_RIGHT, 0)
        sizer_17.Add(self.list_ctrl_5abc, 1, wx.EXPAND, 0)
        sizer_6.Add(sizer_17, 1, wx.EXPAND | wx.ALIGN_RIGHT, 0)
        sizer_5.Add(sizer_6, 1, wx.EXPAND, 0)
        sizer_7.Add(self.button_5, 0, 0, 0)
        sizer_7.Add(self.button_7, 0, 0, 0)
        sizer_7.Add(self.button_6, 0, 0, 0)
        sizer_7.Add((85, 150), 0, 0, 0)
        sizer_9.Add(self.button_8, 0, 0, 0)
        sizer_9.Add(self.button_9, 0, 0, 0)
        sizer_8.Add(sizer_9, 1, wx.EXPAND, 0)
        sizer_8.Add((86, 120), 0, 0, 0)
        sizer_7.Add(sizer_8, 1, wx.EXPAND, 0)
        sizer_11.Add(self.button_10, 0, 0, 0)
        sizer_11.Add(self.button_11, 0, 0, 0)
        sizer_10.Add(sizer_11, 1, wx.EXPAND, 0)
        sizer_7.Add(sizer_10, 1, wx.EXPAND, 0)
        grid_sizer_6.Add(sizer_7, 1, wx.EXPAND, 0)
        grid_sizer_6.Add(self.list_ctrl_3, 1, 0, 0)
        sizer_5.Add(grid_sizer_6, 1, wx.EXPAND, 0)
        sizer_4.Add(sizer_5, 1, wx.EXPAND, 0)
        self.SetSizer(sizer_4)
        self.Layout()
        # end wxGlade

    def calendario(self, event):  # wxGlade: ver_editar.<event_handler>
        print "Event handler 'calendario' not implemented!"
        event.Skip()

    def solo_num(self, event):  # wxGlade: ver_editar.<event_handler>
        print "Event handler 'solo_num' not implemented!"
        event.Skip()

    def activo(self, event):  # wxGlade: ver_editar.<event_handler>
        print "Event handler 'activo' not implemented!"
        event.Skip()

    def save_menu(self, event):  # wxGlade: ver_editar.<event_handler>
        print "Event handler 'save_menu' not implemented!"
        event.Skip()

    def load_img(self, event):  # wxGlade: ver_editar.<event_handler>
        print "Event handler 'load_img' not implemented!"
        event.Skip()

    def primero_selec(self, event):  # wxGlade: ver_editar.<event_handler>
        print "Event handler 'primero_selec' not implemented!"
        event.Skip()

    def segundo_selec(self, event):  # wxGlade: ver_editar.<event_handler>
        print "Event handler 'segundo_selec' not implemented!"
        event.Skip()

    def postre_selec(self, event):  # wxGlade: ver_editar.<event_handler>
        print "Event handler 'postre_selec' not implemented!"
        event.Skip()

    def add_prim(self, event):  # wxGlade: ver_editar.<event_handler>
        print "Event handler 'add_prim' not implemented!"
        event.Skip()

    def left_prim(self, event):  # wxGlade: ver_editar.<event_handler>
        print "Event handler 'left_prim' not implemented!"
        event.Skip()

    def crear_item(self, event):  # wxGlade: ver_editar.<event_handler>
        print "Event handler 'crear_item'"
        crearItem = crear_item(self)
        crearItem.Show()
        self.Hide()
        crearItem.Bind(wx.EVT_CLOSE, self.on_close_crear_item)
        self.crearItem = crearItem
        event.Skip()

    def on_close_crear_item(self, event):
        self.list_ctrl_3.DeleteAllItems() # limpiamos la lista
        servicio.updateItems()            # actualizamos los items del servidor
        for data in servicio.Items:       # y actualizamos la lista
            pos = self.list_ctrl_3.InsertStringItem(0,data['_data']['nombre'])
            self.list_ctrl_3.SetStringItem(pos,1,str(data['_data']['precio']))
            self.list_ctrl_3.SetStringItem(pos,2,str(data['_data']['disponible']))
        closed_window = event.EventObject
        if closed_window == self.crearItem:
            self.crearItem = None
            self.Show()
        elif closed_window == self:
            print 'Carry out your code for when Main window closes'
        event.Skip()

    def add_seg(self, event):  # wxGlade: ver_editar.<event_handler>
        print "Event handler 'add_seg' not implemented!"
        event.Skip()

    def left_seg(self, event):  # wxGlade: ver_editar.<event_handler>
        print "Event handler 'left_seg' not implemented!"
        event.Skip()

    def add_postre(self, event):  # wxGlade: ver_editar.<event_handler>
        print "Event handler 'add_postre' not implemented!"
        event.Skip()

    def left_postre(self, event):  # wxGlade: ver_editar.<event_handler>
        print "Event handler 'left_postre' not implemented!"
        event.Skip()

    def item_selec(self, event):  # wxGlade: ver_editar.<event_handler>
        print "Event handler 'item_selec' not implemented!"
        event.Skip()

# end of class ver_editar

class crear_item(wx.Frame):
    #variables para guardar la imagen codificada en base64
    img = 0

    def __init__(self, *args, **kwds):
        # begin wxGlade: crear_item.__init__
        kwds["style"] = wx.CLOSE_BOX
        wx.Frame.__init__(self, *args, **kwds)
        self.text_ctrl_8 = wx.TextCtrl(self, wx.ID_ANY, "")
        self.sizer_32_staticbox = wx.StaticBox(self, wx.ID_ANY, _("Nombre"))
        self.text_ctrl_9 = wx.TextCtrl(self, wx.ID_ANY, "")
        self.sizer_33_staticbox = wx.StaticBox(self, wx.ID_ANY, _("Precio"))
        #self.combo_box_1 = wx.ComboBox(self, wx.ID_ANY, choices=[_("Primero"), _("Segundo"), _("Postre")], style=wx.CB_DROPDOWN)
        self.sizer_20_staticbox = wx.StaticBox(self, wx.ID_ANY, _("Descripcion"))
        self.text_ctrl_4 = wx.TextCtrl(self, wx.ID_ANY, "", style=wx.TE_MULTILINE)
        #self.sizer_21_staticbox = wx.StaticBox(self, wx.ID_ANY, _(""))
        self.button_13 = wx.Button(self, wx.ID_ANY, _("img"))
        self.sizer_22_staticbox = wx.StaticBox(self, wx.ID_ANY, _("Imagen"))
        self.checkbox_2 = wx.CheckBox(self, wx.ID_ANY, "")
        self.sizer_23_staticbox = wx.StaticBox(self, wx.ID_ANY, _("Disponible"))
        self.button_12 = wx.Button(self, wx.ID_ANY, _("Crear"))

        self.__set_properties()
        self.__do_layout()

        self.Bind(wx.EVT_TEXT, self.solo_num, self.text_ctrl_9)
        self.Bind(wx.EVT_BUTTON, self.load_img_item, self.button_13)
        self.Bind(wx.EVT_CHECKBOX, self.item_disp, self.checkbox_2)
        self.Bind(wx.EVT_BUTTON, self.crear_item_go, self.button_12)
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: crear_item.__set_properties
        self.SetTitle(_("Item"))
        #self.combo_box_1.SetSelection(0)
        self.text_ctrl_4.SetMinSize((200, 100))
        self.checkbox_2.SetValue(1)
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: crear_item.__do_layout
        sizer_18 = wx.BoxSizer(wx.VERTICAL)
        grid_sizer_8 = wx.GridSizer(2, 2, 0, 0)
        self.sizer_23_staticbox.Lower()
        sizer_23 = wx.StaticBoxSizer(self.sizer_23_staticbox, wx.HORIZONTAL)
        self.sizer_22_staticbox.Lower()
        sizer_22 = wx.StaticBoxSizer(self.sizer_22_staticbox, wx.HORIZONTAL)
        #self.sizer_21_staticbox.Lower()
        #sizer_21 = wx.StaticBoxSizer(self.sizer_21_staticbox, wx.HORIZONTAL)
        self.sizer_20_staticbox.Lower()
        sizer_20 = wx.StaticBoxSizer(self.sizer_20_staticbox, wx.HORIZONTAL)
        
        sizer_19 = wx.BoxSizer(wx.VERTICAL)
        sizer_sal = wx.BoxSizer(wx.VERTICAL)
        self.sizer_33_staticbox.Lower()
        sizer_33 = wx.StaticBoxSizer(self.sizer_33_staticbox, wx.HORIZONTAL)
        self.sizer_32_staticbox.Lower()
        sizer_32 = wx.StaticBoxSizer(self.sizer_32_staticbox, wx.HORIZONTAL)
        sizer_32.Add(self.text_ctrl_8, 0, wx.EXPAND, 0)
        
        sizer_19.Add(sizer_32, 1, wx.EXPAND, 0)
        sizer_33.Add(self.text_ctrl_9, 0, wx.EXPAND, 0)
        sizer_19.Add(sizer_33, 1, wx.EXPAND, 0)
        grid_sizer_8.Add(sizer_19, 1, wx.EXPAND, 0)
        #sizer_21.Add(self.combo_box_1, 0, 0, 0)
        grid_sizer_8.Add(sizer_20, 1, wx.EXPAND, 0)
        sizer_20.Add(self.text_ctrl_4, 0, wx.EXPAND, 0)
        #grid_sizer_8.Add(sizer_21, 1, wx.EXPAND, 0)
        sizer_22.Add(self.button_13, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL, 0)
        grid_sizer_8.Add(sizer_22, 1, wx.EXPAND, 0)
        sizer_23.Add(self.checkbox_2, 0, 0, 0)
        sizer_sal.Add(sizer_23,0, wx.EXPAND, 0)
        sizer_sal.Add(self.button_12,0,wx.EXPAND,0)
        grid_sizer_8.Add(sizer_sal, 1, wx.EXPAND, 0)
        #grid_sizer_8.Add(self.button_12, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL | wx.SHAPED, 0)
        sizer_18.Add(grid_sizer_8, 1, wx.EXPAND, 0)
        self.SetSizer(sizer_18)
        sizer_18.Fit(self)
        self.Layout()
        # end wxGlade

    def solo_num(self, event):  # wxGlade: crear_item.<event_handler>
        print "solo_num"
        raw_value = self.text_ctrl_9.GetValue().strip()
        # numeric check
        if all(x in '0123456789.' for x in raw_value):
            pass
        else:
            self.text_ctrl_9.ChangeValue('')
        event.Skip()

    def load_img_item(self, event):  # wxGlade: crear_item.<event_handler>
        print "load_img_item"
        img = self.img
        openFileDialog = wx.FileDialog(self, "Selecionar imagen del artículo", "", "", "pictures (*.jpeg,*.jpg,*.png)|*.jpeg;*.jpg;*.png", wx.FD_OPEN | wx.FD_FILE_MUST_EXIST)

        if openFileDialog.ShowModal() == wx.ID_CANCEL:
            return     # the user changed idea...

        print openFileDialog.GetPath()
        # pasar a base64 y guardar en variable
        with open(openFileDialog.GetPath(), "rb") as imageFile:
            img = base64.b64encode(imageFile.read())
        if img!=self.img:
            msgbox = wx.MessageBox('!Imágen guardada!', 'Información', wx.ICON_INFORMATION | wx.STAY_ON_TOP)
            self.img = img
        else:
            msgbox = wx.MessageBox('¡La imágen no se guardo, o elegiste la misma que ya estaba guardada!', 'Alerta', wx.ICON_EXCLAMATION | wx.STAY_ON_TOP)
        event.Skip()

    def item_disp(self, event):  # wxGlade: crear_item.<event_handler>
        print "Event handler 'item_disp' not implemented!"
        event.Skip()

    def crear_item_go(self, event):  # wxGlade: crear_item.<event_handler>
        print "crear_item_go"
        if len(self.text_ctrl_9.GetValue()) and len(self.text_ctrl_8.GetValue()) and len(self.text_ctrl_4.GetValue()):
            if servicio.createItem(self.checkbox_2.GetValue(), self.text_ctrl_9.GetValue(), self.text_ctrl_8.GetValue(), self.text_ctrl_4.GetValue(), self.img, 0, 0, 0, 0):
                print 'item creado'
                msgbox = wx.MessageBox('!Item creado!', 'Información', wx.ICON_INFORMATION | wx.STAY_ON_TOP)
            else:
                print 'no se creo!'
                msgbox = wx.MessageBox('¡El item no se pudo crear!', 'Alerta', wx.ICON_EXCLAMATION | wx.STAY_ON_TOP)
            self.Close(True)
        else:
            msgbox = wx.MessageBox('¡Rellena los campos!', 'Alerta', wx.ICON_EXCLAMATION | wx.STAY_ON_TOP)
        event.Skip()

# end of class crear_item

class crear_oferta(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: crear_oferta.__init__
        kwds["style"] = wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.calendar_ctrl_4 = wx.calendar.CalendarCtrl(self, wx.ID_ANY, style=wx.calendar.CAL_MONDAY_FIRST)
        self.text_ctrl_10 = wx.TextCtrl(self, wx.ID_ANY, "")
        self.sizer_35_staticbox = wx.StaticBox(self, wx.ID_ANY, _("Nombre"))
        self.text_ctrl_5 = wx.TextCtrl(self, wx.ID_ANY, "")
        self.sizer_26_staticbox = wx.StaticBox(self, wx.ID_ANY, _("Duracion"))
        self.text_ctrl_6 = wx.TextCtrl(self, wx.ID_ANY, "")
        self.sizer_27_staticbox = wx.StaticBox(self, wx.ID_ANY, _("Precio"))
        self.checkbox_3 = wx.CheckBox(self, wx.ID_ANY, "")
        self.sizer_28_staticbox = wx.StaticBox(self, wx.ID_ANY, _("Activo"))
        self.button_15 = wx.Button(self, wx.ID_ANY, _("img"))
        self.button_16 = wx.Button(self, wx.ID_ANY, _("Guardar"))
        self.list_ctrl_5 = wx.ListCtrl(self, wx.ID_ANY, style=wx.LC_REPORT | wx.SUNKEN_BORDER)
        self.sizer_29_staticbox = wx.StaticBox(self, wx.ID_ANY, _("Items"))
        self.button_17 = wx.Button(self, wx.ID_ANY, _("<<"))
        self.button_18 = wx.Button(self, wx.ID_ANY, _(">>"))
        self.list_ctrl_4 = wx.ListCtrl(self, wx.ID_ANY, style=wx.LC_REPORT | wx.SUNKEN_BORDER)

        self.list_ctrl_4.InsertColumn(0,"Nombre")
        self.list_ctrl_4.InsertColumn(1,"Precio")
        self.list_ctrl_4.InsertColumn(2,"Disponible")

        self.list_ctrl_5.InsertColumn(0,"Nombre")
        self.list_ctrl_5.InsertColumn(1,"Precio")
        self.list_ctrl_5.InsertColumn(2,"Disponible")

        for data in servicio.Items:
            # 0 will insert at the start of the list
            pos = self.list_ctrl_4.InsertStringItem(0,data['_data']['nombre'])
            # add values in the other columns on the same row
            self.list_ctrl_4.SetStringItem(pos,1,str(data['_data']['precio']))
            self.list_ctrl_4.SetStringItem(pos,2,str(data['_data']['disponible']))

        self.__set_properties()
        self.__do_layout()

        self.Bind(wx.EVT_TEXT, self.solo_num, self.text_ctrl_5)
        self.Bind(wx.EVT_TEXT, self.solo_num, self.text_ctrl_6)
        self.Bind(wx.EVT_CHECKBOX, self.activo, self.checkbox_3)
        self.Bind(wx.EVT_BUTTON, self.load_img_oferta, self.button_15)
        self.Bind(wx.EVT_BUTTON, self.guardar_oferta, self.button_16)
        self.Bind(wx.EVT_LIST_ITEM_SELECTED, self.item_selec2, self.list_ctrl_5)
        self.Bind(wx.EVT_BUTTON, self.pasar_izq, self.button_17)
        self.Bind(wx.EVT_BUTTON, self.pasar_der, self.button_18)
        self.Bind(wx.EVT_LIST_ITEM_SELECTED, self.item_select, self.list_ctrl_4)
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: crear_oferta.__set_properties
        self.SetTitle(_("frame_2"))
        self.SetSize((648, 529))
        self.checkbox_3.SetValue(1)
        self.list_ctrl_5.SetMinSize((160, 469))
        self.list_ctrl_4.SetMinSize((164, 500))
        self.calendar_ctrl_4.SetMinSize((215, 140))
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: crear_oferta.__do_layout
        sizer_24 = wx.BoxSizer(wx.VERTICAL)
        sizer_25 = wx.BoxSizer(wx.HORIZONTAL)
        grid_sizer_10 = wx.FlexGridSizer(1, 2, 0, 0)
        sizer_30 = wx.BoxSizer(wx.VERTICAL)
        sizer_31 = wx.BoxSizer(wx.VERTICAL)
        self.sizer_29_staticbox.Lower()
        sizer_29 = wx.StaticBoxSizer(self.sizer_29_staticbox, wx.HORIZONTAL)
        grid_sizer_9 = wx.FlexGridSizer(7, 1, 0, 0)
        self.sizer_28_staticbox.Lower()
        sizer_28 = wx.StaticBoxSizer(self.sizer_28_staticbox, wx.HORIZONTAL)
        self.sizer_27_staticbox.Lower()
        sizer_27 = wx.StaticBoxSizer(self.sizer_27_staticbox, wx.HORIZONTAL)
        self.sizer_26_staticbox.Lower()
        sizer_26 = wx.StaticBoxSizer(self.sizer_26_staticbox, wx.HORIZONTAL)
        self.sizer_35_staticbox.Lower()
        sizer_35 = wx.StaticBoxSizer(self.sizer_35_staticbox, wx.HORIZONTAL)
        grid_sizer_9.Add(self.calendar_ctrl_4, 0, 0, 0)
        sizer_35.Add(self.text_ctrl_10, 0, 0, 0)
        grid_sizer_9.Add(sizer_35, 1, wx.EXPAND, 0)
        sizer_26.Add(self.text_ctrl_5, 0, 0, 0)
        grid_sizer_9.Add(sizer_26, 1, wx.EXPAND, 0)
        sizer_27.Add(self.text_ctrl_6, 0, 0, 0)
        grid_sizer_9.Add(sizer_27, 1, wx.EXPAND, 0)
        sizer_28.Add(self.checkbox_3, 0, 0, 0)
        grid_sizer_9.Add(sizer_28, 1, wx.EXPAND, 0)
        grid_sizer_9.Add(self.button_15, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL, 0)
        grid_sizer_9.Add(self.button_16, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL, 0)
        sizer_25.Add(grid_sizer_9, 1, wx.EXPAND, 0)
        sizer_29.Add(self.list_ctrl_5, 1, wx.EXPAND, 0)
        sizer_25.Add(sizer_29, 1, wx.EXPAND, 0)
        sizer_30.Add((80, 200), 0, 0, 0)
        sizer_31.Add(self.button_17, 0, 0, 0)
        sizer_31.Add(self.button_18, 0, 0, 0)
        sizer_30.Add(sizer_31, 1, wx.EXPAND, 0)
        grid_sizer_10.Add(sizer_30, 1, wx.EXPAND, 0)
        grid_sizer_10.Add(self.list_ctrl_4, 1, wx.EXPAND, 0)
        sizer_25.Add(grid_sizer_10, 1, wx.EXPAND, 0)
        sizer_24.Add(sizer_25, 1, wx.EXPAND, 0)
        self.SetSizer(sizer_24)
        self.Layout()
        # end wxGlade

    def solo_num(self, event):  # wxGlade: crear_oferta.<event_handler>
        print "Event handler 'solo_num' not implemented!"
        event.Skip()

    def activo(self, event):  # wxGlade: crear_oferta.<event_handler>
        print "Event handler 'activo' not implemented!"
        event.Skip()

    def load_img_oferta(self, event):  # wxGlade: crear_oferta.<event_handler>
        print "Event handler 'load_img_oferta' not implemented!"
        event.Skip()

    def guardar_oferta(self, event):  # wxGlade: crear_oferta.<event_handler>
        print "Event handler 'guardar_oferta' not implemented!"
        event.Skip()

    def item_selec2(self, event):  # wxGlade: crear_oferta.<event_handler>
        print "Event handler 'item_selec2' not implemented!"
        event.Skip()

    def pasar_izq(self, event):  # wxGlade: crear_oferta.<event_handler>
        print "Event handler 'pasar_izq' not implemented!"
        event.Skip()

    def pasar_der(self, event):  # wxGlade: crear_oferta.<event_handler>
        print "Event handler 'pasar_der' not implemented!"
        event.Skip()

    def item_select(self, event):  # wxGlade: crear_oferta.<event_handler>
        print "Event handler 'item_select' not implemented!"
        event.Skip()

# end of class crear_oferta

class InterfazServidor(wx.App):
    def OnInit(self):
        wx.InitAllImageHandlers()
        main = MyFrame(None, wx.ID_ANY, "")
        self.SetTopWindow(main)
        main.Show()
        return 1

# end of class InterfazServidor

if __name__ == "__main__":
    servicio = ServicioPyro()
    servicio.isOnline()

    gettext.install("Servidor") # replace with the appropriate catalog name

    Servidor = InterfazServidor(0)
    Servidor.MainLoop()