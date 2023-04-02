# -*- coding: utf-8 -*-
"""
Created on Sun Oct 23 2022

@author: Matthew

This module is a GUI interface for generating treasure from various
random tables.

Imports the treasuretools.py module, where the actual calculations
are performed.
"""

from tkinter import * # classic widgets
from tkinter import ttk # themed widgets
import random as rng

import treasuretools as ttools # Eberron treasure module

rng.seed()
debug = True

# supported trinket options
trinketkeys_list = list(ttools.trinket.keys())
trinketkeys = list(trinketkeys_list)
trinketkeys.append("Random")
trinketkeys = tuple(trinketkeys) # combobox data validation has to be a tuple

# predefine function callbacks
def gen_trinket(*args):
    #try:
    #    if calvar_in.get() == calvar_out.get(): # no conversion required
    #        date_out = date_in
    #        datestr_out.set(date_out.disp())
    #        if debug: print('no conversion')
    #except ValueError:
    #    pass
    # Mundane Items
    trinket_type = trinktype_var_in.get()
    numtrink = 1
    trinktext = ''
    for _ in range(0, numtrink):
        if trinket_type in trinketkeys_list: # true if valid trinket table name
            trinktext += rng.choice(ttools.trinket[trinket_type]) + '\n'
        elif trinket_type.lower() in ['all', 'random']: # choose from all trinkets
            trinktext += rng.choice(ttools.alltrinkets) + '\n'
    if trinktext == '':
        trinktext += 'none\n'
    trink_var_out.set(trinktext)

# for debugging
def print_hierarchy(w, depth=0):
    print('  '*depth + w.winfo_class() + ' w=' + str(w.winfo_width()) + ' h=' + str(w.winfo_height()) + ' x=' + str(w.winfo_x()) + ' y=' + str(w.winfo_y()))
    for i in w.winfo_children():
        print_hierarchy(i, depth+1)

# set up containers for entire GUI        
root = Tk() # create the base Tk instance
root.title("Shardspace Treasure Generator") # window title
mainframe = ttk.Frame(root, padding = "12 12 12 12") # 12 pixel padding around edges
mainframe.grid(column=0, row=0, sticky='nsew') # put mainframe in 0,0 cell of root, attached to all four sides
root.columnconfigure(0, weight=1) # let col 0 (mainframe) resize horizontally
root.rowconfigure(0, weight=1) # let row 0 (mainframe) resize vertically
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

# set up frame for treasure gen
dateframe = ttk.Frame(mainframe)
dateframe.grid(column=0, row=0, sticky='nsew')
dateframe.columnconfigure(0, weight=1)
dateframe.rowconfigure(0, weight=1)
dateframe.columnconfigure(1, weight=1)
#dateframe.rowconfigure(1, weight=1)
dateframe.columnconfigure(2, weight=1)
#dateframe.rowconfigure(2, weight=1)
dateframe.columnconfigure(3, weight=1)
#dateframe.rowconfigure(3, weight=1)
dateframe.columnconfigure(4, weight=1)
#dateframe.rowconfigure(4, weight=1)

# static elements
desclabel = ttk.Label(dateframe, text='Generate trinkets of desired\n number and type:')
desclabel.grid(column=1, row=2, padx=5, pady=5, sticky='nsew')
outlabel = ttk.Label(dateframe, text='Output:')
outlabel.grid(column=1, row=3, padx=5, pady=5, sticky='nsew')

# trinket selection comboboxes
trinktype_var_in = StringVar()
trink_var_out = StringVar()
trinktype_in = ttk.Combobox(dateframe, textvariable=trinktype_var_in)
trinktype_in.grid(column=3, row=1, padx=5, pady=5, sticky='nsew')
trink_out = ttk.Label(dateframe, textvariable=trink_var_out)
trink_out.grid(column=5, row=1, padx=5, pady=5, sticky='nsew')
def function(entry):
    entry.selection_clear() # clear when value changes
trinktype_in.bind('<<ComboboxSelected>>', function(trinktype_in))
trinktype_in['values'] = trinketkeys
trinktype_in.state(["readonly"])
#cal_out.bind('<<ComboboxSelected>>', function(cal_out))
#cal_out['values'] = calendars
#cal_out.state(["readonly"])

# input selection frame
#select = ttk.Frame(dateframe)
#select.grid(column=2, row=1, padx=5, pady=5, sticky='nsew')

# datestring labels
#date_in = cal.GalifarDate()
#date_out = cal.GalifarDate()
#datestr_in = StringVar()
#datestr_out = StringVar()
#datelbl_in = ttk.Label(dateframe, textvariable=datestr_in)
#datelbl_out = ttk.Label(dateframe, textvariable=datestr_out)
#datelbl_in.grid(column=2, row=2, padx=5, pady=5, sticky='nsew')
#datelbl_out.grid(column=2, row=3, padx=5, pady=5, sticky='nsew')

# create a button to press to perform the calculation
calc = ttk.Button(dateframe, text="Generate Trinkets", command=gen_trinket)
calc.grid(column=4, row=3, sticky='nsew')

# misc functions
def reset_to_default():
    #date_in = cal.GalifarDate()
    #date_out = cal.GalifarDate()
    #datestr_in.set(date_in.disp())
    #datestr_out.set(date_out.disp())
    trinktype_var_in.set('Random')
    #calvar_out.set('Galifar')

# debug
if debug: print_hierarchy(root)

# start the GUI
reset_to_default()
root.mainloop()