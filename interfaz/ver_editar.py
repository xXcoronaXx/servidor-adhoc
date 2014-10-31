# -*- coding: UTF-8 -*-
#
# generated by wxGlade 0.6.8 on Sun Aug 10 21:46:08 2014
#

import wx
# begin wxGlade: dependencies
import wx.calendar
# end wxGlade
from crear_item import crear_item
# begin wxGlade: extracode
# end wxGlade

from MyFrame import *


class ver_editar(wx.MDIChildFrame):
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
        self.list_ctrl_3.InsertColumn(1,"Disponible")

        self.list_ctrl_5ab.InsertColumn(0,"Nombre")
        self.list_ctrl_5ab.InsertColumn(1,"Disponible")

        self.list_ctrl_5a.InsertColumn(0,"Nombre")
        self.list_ctrl_5a.InsertColumn(1,"Disponible")

        self.list_ctrl_5abc.InsertColumn(0,"Nombre")
        self.list_ctrl_5abc.InsertColumn(1,"Disponible")

        # for data in Items:
        #     # 0 will insert at the start of the list
        #     pos = self.list_ctrl_3.InsertStringItem(0,data['nombre'])
        #     # add values in the other columns on the same row
        #     self.list_ctrl_3.SetStringItem(pos,1,str(data['precio']))
        #     self.list_ctrl_3.SetStringItem(pos,2,str(data['disponible']))

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