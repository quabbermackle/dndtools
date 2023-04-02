# -*- coding: utf-8 -*-
"""
Created on Sat Dec 26 10:01:09 2020

@author: Matthew Gunther

Character background generator using tables from the Explorer's Guide to
Wildemount
"""

import itertools as it
import random as rng
rng.seed()
import os
cwd = os.getcwd()

from treasuretools import *

# SETTLEMENTS BY REGION

# Settlement Sizes (5e DMG)
maxpop5e = {'Village':1000,
            'Town':   6000,
            'City':   25000}
poplist5e = list(maxpop5e.values())
maxpop3e = {'Camp':      20,
            'Thorp':     80,
            'Hamlet':    400,
            'Village':   900,
            'Small Town':2000,
            'Large Town':5000,
            'Small City':12000,
            'Large City':25000,
            'Metropolis':1000000}
poplist3e = list(maxpop3e.values())

# Homelands
hldict = {}
hldict['Aundair']  = 20
hldict['Breland']  = 40
hldict['Cyre']     = 60
hldict['Karrnath'] = 80
hldict['Thrane']   = 100
hl = list(hldict.keys())
hlw = list(hldict.values())
fivenations = ['Aundair', 'Breland', 'Cyre', 'Karrnath', 'Thrane']

# Backgrounds
bg = ['Acolyte',
      'Charlatan',
      'Criminal',
      'Entertainer',
      'Folk Hero',
      'Guild Artisan',
      'Hermit',
      'Noble',
      'Outlander',
      'Sage',
      'Sailor',
      'Sailor (pirate)',
      'Soldier',
      'Spy',
      'Urchin']
bgw = list(range(1,len(bg)+1))

# Aundairian Settlements
totpop = {} # total population of nations
totpop['Aundair'] = 2000000 # 2 million
s_audict = {}
s_audict['Arcanix']        = {'w':1,  'size':'Village',    'pop':800,   'gov':'Queen Aurala ir\'Wynarn'}
s_audict['Areksul']        = {'w':2,  'size':'Village',    'pop':1,     'gov':'Queen Aurala ir\'Wynarn'}
s_audict['Askelios']       = {'w':3,  'size':'Village',    'pop':1,     'gov':'Queen Aurala ir\'Wynarn'}
s_audict['Bluevine']       = {'w':4,  'size':'Village',    'pop':1,     'gov':'Queen Aurala ir\'Wynarn'}
s_audict['Fairhaven']      = {'w':5,  'size':'Metropolis', 'pop':92500, 'gov':'Queen Aurala ir\'Wynarn'}
s_audict['Ghalt']          = {'w':6,  'size':'City',       'pop':1,     'gov':'Queen Aurala ir\'Wynarn'}
s_audict['Kerkulin']       = {'w':7,  'size':'Hamlet',     'pop':1,     'gov':'Queen Aurala ir\'Wynarn'}
s_audict['Larunor']        = {'w':8,  'size':'Village',    'pop':1,     'gov':'Queen Aurala ir\'Wynarn'}
s_audict['Lathleer']       = {'w':9,  'size':'Town',       'pop':1,     'gov':'Queen Aurala ir\'Wynarn'}
s_audict['Marketplace']    = {'w':10, 'size':'Village',    'pop':1,     'gov':'Queen Aurala ir\'Wynarn'}
s_audict['Otharaunt']      = {'w':11, 'size':'Fort',       'pop':1,     'gov':'Queen Aurala ir\'Wynarn'}
s_audict['Passage']        = {'w':12, 'size':'City',       'pop':1,     'gov':'Queen Aurala ir\'Wynarn'}
s_audict['Rhenshia']       = {'w':13, 'size':'Hamlet',     'pop':1,     'gov':'Queen Aurala ir\'Wynarn'}
s_audict['Stormhome']      = {'w':14, 'size':'City',       'pop':1,     'gov':'Queen Aurala ir\'Wynarn'}
s_audict['Tanar']          = {'w':15, 'size':'Hamlet',     'pop':1,     'gov':'Queen Aurala ir\'Wynarn'}
s_audict['Tower Valiant']  = {'w':16, 'size':'Fort',       'pop':1,     'gov':'Queen Aurala ir\'Wynarn'}
s_audict['Tower Vigilant'] = {'w':17, 'size':'Fort',       'pop':1,     'gov':'Queen Aurala ir\'Wynarn'}
s_audict['Vanguard Keep']  = {'w':18, 'size':'Fort',       'pop':1,     'gov':'Queen Aurala ir\'Wynarn'}
s_audict['Windshire']      = {'w':19, 'size':'Village',    'pop':1,     'gov':'Queen Aurala ir\'Wynarn'}
s_audict['Wrogar Keep']    = {'w':20, 'size':'Fort',       'pop':1,     'gov':'Queen Aurala ir\'Wynarn'}
s_audict['Wyr']            = {'w':21, 'size':'Village',    'pop':1,     'gov':'Queen Aurala ir\'Wynarn'}
s_au = list()
s_auw = list()
for x in s_audict:
    s_au += [[x, s_audict[x]['size'], s_audict[x]['pop'], s_audict[x]['gov']]]
    s_auw += [s_audict[x]['w']]

# Aundairian Settlement Populations
pop = {}
popw = {}
pop['Fairhaven']  = ['human', 'half-elf', 'gnome', 'elf', 'changeling', 'other']
popw['Fairhaven'] = list(it.accumulate([65, 15, 9, 7, 2, 2]))
for i in s_audict.keys():
    if i != 'Fairhaven':
        pop[i] = pop['Fairhaven']
        popw[i] = popw['Fairhaven']

# Brelish Settlements
totpop['Breland'] = 3700000 # 3.7 million
s_brdict = {}
s_brdict['Argonth']         = {'w':1,  'size':'Fort',       'pop':1,     'gov':'King Boranel ir\'Wynarn'}
s_brdict['Ardev']           = {'w':2,  'size':'Small Town', 'pop':1600,  'gov':'King Boranel ir\'Wynarn'}
s_brdict['Black Pit']       = {'w':3,  'size':'Village',    'pop':1,     'gov':'King Boranel ir\'Wynarn'}
s_brdict['Brey Crossing']   = {'w':4,  'size':'Fort',       'pop':1,     'gov':'King Boranel ir\'Wynarn'}
s_brdict['Castle Arakhain'] = {'w':5,  'size':'Fort',       'pop':1,     'gov':'King Boranel ir\'Wynarn'}
s_brdict['Cragwar']         = {'w':6,  'size':'Large Town', 'pop':3600,  'gov':'King Boranel ir\'Wynarn'}
s_brdict['Drum Keep']       = {'w':7,  'size':'Fort',       'pop':1,     'gov':'King Boranel ir\'Wynarn'}
s_brdict['First Tower']     = {'w':8,  'size':'Village',    'pop':1,     'gov':'King Boranel ir\'Wynarn'}
s_brdict['Flint Keep']      = {'w':9,  'size':'Fort',       'pop':1,     'gov':'King Boranel ir\'Wynarn'}
s_brdict['Fort Tansend']    = {'w':10, 'size':'Fort',       'pop':1,     'gov':'King Boranel ir\'Wynarn'}
s_brdict['Galethspyre']     = {'w':11, 'size':'Large Town', 'pop':3900,  'gov':'King Boranel ir\'Wynarn'}
s_brdict['Hatheril']        = {'w':12, 'size':'Village',    'pop':1,     'gov':'King Boranel ir\'Wynarn'}
s_brdict['Katal Hazath']    = {'w':13, 'size':'Small Town', 'pop':950,   'gov':'Katal Hazath'} # in the mountains just to the Breland side of the Droaam/Breland border
s_brdict['Kennrun']         = {'w':14, 'size':'Fort',       'pop':1,     'gov':'King Boranel ir\'Wynarn'}
s_brdict['Lurching Tower']  = {'w':15, 'size':'Fort',       'pop':1,     'gov':'King Boranel ir\'Wynarn'}
s_brdict['Mistmarsh']       = {'w':16, 'size':'Hamlet',     'pop':240,   'gov':'King Boranel ir\'Wynarn'}
s_brdict['Moonwatch']       = {'w':17, 'size':'Town',       'pop':1,     'gov':'King Boranel ir\'Wynarn'}
s_brdict['New Cyre']        = {'w':18, 'size':'Large Town', 'pop':4200,  'gov':'Prince Oargev ir\'Wynarn'}
s_brdict['Nowhere']         = {'w':19, 'size':'Hamlet',     'pop':1,     'gov':'King Boranel ir\'Wynarn'}
s_brdict['Orcbone']         = {'w':20, 'size':'Fort',       'pop':450,   'gov':'King Boranel ir\'Wynarn'}
s_brdict['Ringbriar']       = {'w':21, 'size':'Village',    'pop':1,     'gov':'King Boranel ir\'Wynarn'}
s_brdict['Shadowlock Keep'] = {'w':22, 'size':'Fort',       'pop':1,     'gov':'King Boranel ir\'Wynarn'}
s_brdict['Sharn']           = {'w':23, 'size':'Metropolis', 'pop':1,     'gov':'King Boranel ir\'Wynarn'}
s_brdict['Shavalant']       = {'w':24, 'size':'Village',    'pop':820,   'gov':'King Boranel ir\'Wynarn'}
s_brdict['Shining Valley']  = {'w':25, 'size':'Thorp',      'pop':52,    'gov':'the Haunting Song'}
s_brdict['Silent Keep']     = {'w':26, 'size':'Fort',       'pop':100,   'gov':'King Boranel ir\'Wynarn'}
s_brdict['Starilaskur']     = {'w':27, 'size':'Town',       'pop':1,     'gov':'King Boranel ir\'Wynarn'}
s_brdict['Sterngate']       = {'w':28, 'size':'Fort',       'pop':800,   'gov':'King Boranel ir\'Wynarn'}
s_brdict['Sword Keep']      = {'w':29, 'size':'Fort',       'pop':1,     'gov':'King Boranel ir\'Wynarn'}
s_brdict['Torch Keep']      = {'w':30, 'size':'Fort',       'pop':80,    'gov':'King Boranel ir\'Wynarn'}
s_brdict['Vathirond']       = {'w':31, 'size':'Town',       'pop':1,     'gov':'King Boranel ir\'Wynarn'}
s_brdict['Woodhelm']        = {'w':32, 'size':'Village',    'pop':1,     'gov':'King Boranel ir\'Wynarn'}
s_brdict['Wroat']           = {'w':33, 'size':'Metropolis', 'pop':80870, 'gov':'King Boranel ir\'Wynarn'}
s_brdict['Xandrar']         = {'w':34, 'size':'Small City', 'pop':12800, 'gov':'King Boranel ir\'Wynarn'}
s_brdict['Zilspar']         = {'w':35, 'size':'Village',    'pop':1,     'gov':'King Boranel ir\'Wynarn'}
s_br = list()
s_brw = list()
for x in s_brdict:
    s_br += [[x, s_brdict[x]['size'], s_brdict[x]['pop'], s_brdict[x]['gov']]]
    s_brw += [s_brdict[x]['w']]

# Brelish Settlement Populations
pop['Wroat']          = ['human', 'gnome', 'half-elf', 'elf', 'dwarf', 'halfling', 'changeling', 'warforged', 'goblin', 'hobgoblin', 'bugbear', 'other']
pop['Shining Valley'] = ['harpy']
pop['Katal Hazath']   = ['gith (githyanki)', 'human', 'other']
popw['Wroat']          = list(it.accumulate([30, 20, 15, 10, 8, 5, 4, 2, .67, .67, .67, 4]))
popw['Shining Valley'] = list(it.accumulate([100]))
popw['Katal Hazath']   = list(it.accumulate([92, 5, 3]))
for i in s_brdict.keys():
    if i not in ['Wroat', 'Shining Valley']:
        pop[i] = pop['Wroat']
        popw[i] = popw['Wroat']
        
# Cyran Settlements (pre-Mourning)
refugeecities = ['New Cyre', 'Sharn', 'Dragonroost', 'Zolanberg']
totpop['Cyre'] = 1500000 # 1.5 million
s_cydict = {}
s_cydict['Barren Keep']         = {'w':1,   'size':'Fort',       'pop':1,   'gov':'Queen Dannel ir\'Wynarn'}
s_cydict['Broken Tower']        = {'w':2,   'size':'Fort',       'pop':1,   'gov':'Queen Dannel ir\'Wynarn'}
s_cydict['Dollen on the River'] = {'w':3,   'size':'Village',    'pop':1,   'gov':'Queen Dannel ir\'Wynarn'}
s_cydict['Eston']               = {'w':4,   'size':'Small City', 'pop':1,   'gov':'Queen Dannel ir\'Wynarn'}
s_cydict['Fort Bright']         = {'w':5,   'size':'Fort',       'pop':1,   'gov':'Queen Dannel ir\'Wynarn'}
s_cydict['Greenland']           = {'w':6,   'size':'Village',    'pop':1,   'gov':'Queen Dannel ir\'Wynarn'}
s_cydict['Jarp']                = {'w':7,   'size':'Village',    'pop':1,   'gov':'Queen Dannel ir\'Wynarn'}
s_cydict['Kalazart']            = {'w':8,   'size':'Town',       'pop':1,   'gov':'Queen Dannel ir\'Wynarn'}
s_cydict['Lorn']                = {'w':9,   'size':'Village',    'pop':1,   'gov':'Queen Dannel ir\'Wynarn'}
s_cydict['Making']              = {'w':10,  'size':'Town',       'pop':1,   'gov':'Queen Dannel ir\'Wynarn'}
s_cydict['Metrol']              = {'w':11,  'size':'Town',       'pop':1,   'gov':'Queen Dannel ir\'Wynarn'}
s_cydict['Seaside']             = {'w':12,  'size':'Large City', 'pop':1,   'gov':'Queen Dannel ir\'Wynarn'}
s_cydict['Shaelas Tiraleth']    = {'w':13,  'size':'City',       'pop':1,   'gov':'Shan Tira'}
s_cydict['Swoz']                = {'w':14,  'size':'Town',       'pop':1,   'gov':'Queen Dannel ir\'Wynarn'}
s_cydict['Tronish']             = {'w':15,  'size':'Town',       'pop':1,   'gov':'Queen Dannel ir\'Wynarn'}
s_cydict['Whitehearth']         = {'w':16,  'size':'Town',       'pop':1,   'gov':'Queen Dannel ir\'Wynarn'}
s_cy = list()
s_cyw = list()
for x in s_cydict:
    s_cy += [[x, s_cydict[x]['size'], s_cydict[x]['pop'], s_cydict[x]['gov']]]
    s_cyw += [s_cydict[x]['w']]

# Cyran Settlement Populations
pop['Shaelas Tiraleth']  = ['eladrin']
pop['end']               = ['human', 'dwarf',    'elf',      'other']
popw['Shaelas Tiraleth'] = list(it.accumulate([100]))
popw['end']              = list(it.accumulate([54, 28, 14, 4]))

# Karrnathi Settlements
totpop['Karrnath'] = 2500000 # 2.5 million
s_kadict = {}
s_kadict['Atur']          = {'w':1,  'size':'City',       'pop':12600, 'gov':'King Kaius ir\'Wynarn III'}
s_kadict['Bastion']       = {'w':2,  'size':'Fort',       'pop':1,     'gov':'King Kaius ir\'Wynarn III'}
s_kadict['Brek']          = {'w':3,  'size':'Hamlet',     'pop':1,     'gov':'King Kaius ir\'Wynarn III'}
s_kadict['Brom']          = {'w':4,  'size':'Hamlet',     'pop':1,     'gov':'King Kaius ir\'Wynarn III'}
s_kadict['Cannith 12']    = {'w':5,  'size':'Fort',       'pop':1,     'gov':'King Kaius ir\'Wynarn III'}
s_kadict['Fort Bones']    = {'w':6,  'size':'Fort',       'pop':400,   'gov':'King Kaius ir\'Wynarn III'}
s_kadict['Fort Deepdark'] = {'w':7,  'size':'Fort',       'pop':1,     'gov':'King Kaius ir\'Wynarn III'}
s_kadict['Fort Zombie']   = {'w':8,  'size':'Fort',       'pop':1,     'gov':'King Kaius ir\'Wynarn III'}
s_kadict['Ice']           = {'w':9,  'size':'Hamlet',     'pop':1,     'gov':'King Kaius ir\'Wynarn III'}
s_kadict['Irontown']      = {'w':10, 'size':'Town',       'pop':1,     'gov':'King Kaius ir\'Wynarn III'}
s_kadict['Jern']          = {'w':11, 'size':'Hamlet',     'pop':1,     'gov':'King Kaius ir\'Wynarn III'}
s_kadict['Karnel']        = {'w':12, 'size':'Hamlet',     'pop':1,     'gov':'King Kaius ir\'Wynarn III'}
s_kadict['Karrlakton']    = {'w':13, 'size':'City',       'pop':1,     'gov':'King Kaius ir\'Wynarn III'}
s_kadict['Korth']         = {'w':14, 'size':'Metropolis', 'pop':85500, 'gov':'King Kaius ir\'Wynarn III'}
s_kadict['Lakeside']      = {'w':15, 'size':'Town',       'pop':1,     'gov':'King Kaius ir\'Wynarn III'}
s_kadict['Lhaz']          = {'w':16, 'size':'Hamlet',     'pop':1,     'gov':'King Kaius ir\'Wynarn III'}
s_kadict['Loom Keep']     = {'w':17, 'size':'Fort',       'pop':1,     'gov':'King Kaius ir\'Wynarn III'}
s_kadict['Loran Rath']    = {'w':18, 'size':'Fort',       'pop':1,     'gov':'King Kaius ir\'Wynarn III'}
s_kadict['Rekkenmark']    = {'w':19, 'size':'City',       'pop':1,     'gov':'King Kaius ir\'Wynarn III'}
s_kadict['Taer Syraen']   = {'w':20, 'size':'Large Town', 'pop':3500,  'gov':'the Prince of Frost'}
s_kadict['Tanar Rath']    = {'w':21, 'size':'Fort',       'pop':1,     'gov':'King Kaius ir\'Wynarn III'}
s_kadict['Teryk']         = {'w':22, 'size':'Town',       'pop':1,     'gov':'King Kaius ir\'Wynarn III'}
s_kadict['Thronehold']    = {'w':23, 'size':'City',       'pop':1,     'gov':'Thronehold'}
s_kadict['Trag']          = {'w':24, 'size':'Hamlet',     'pop':1,     'gov':'King Kaius ir\'Wynarn III'}
s_kadict['Senne']         = {'w':25, 'size':'Hamlet',     'pop':1,     'gov':'King Kaius ir\'Wynarn III'}
s_kadict['Vedykar']       = {'w':26, 'size':'City',       'pop':1,     'gov':'King Kaius ir\'Wynarn III'}
s_kadict['Vom']           = {'w':27, 'size':'Village',    'pop':1,     'gov':'King Kaius ir\'Wynarn III'}
s_kadict['Vulyar']        = {'w':28, 'size':'Town',       'pop':1,     'gov':'King Kaius ir\'Wynarn III'}
s_kadict['Vurgenslye']    = {'w':29, 'size':'Village',    'pop':1,     'gov':'King Kaius ir\'Wynarn III'}
s_ka = list()
s_kaw = list()
for x in s_kadict:
    s_ka += [[x, s_kadict[x]['size'], s_kadict[x]['pop'], s_kadict[x]['gov']]]
    s_kaw += [s_kadict[x]['w']]

# Karrnathi Settlement Populations
pop['Taer Syraen']  = ['eladrin']
pop['Korth']        = ['human', 'dwarf', 'halfling', 'half-elf', 'elf', 'other']
popw['Taer Syraen'] = list(it.accumulate([100]))
popw['Korth']         = list(it.accumulate([60, 19, 6, 4, 4, 7]))
for i in s_kadict.keys():
    if i not in ['Taer Syraen', 'Korth']:
        pop[i] = pop['Korth']
        popw[i] = popw['Korth']

# Thranish Settlements
totpop['Thrane'] = 2300000 # 2.3 million
s_thdict = {}
s_thdict['Aelyndar']           = {'w':1,  'size':'Village',    'pop':1,      'gov':'the Church of the Silver Flame'}
s_thdict['Angwar Keep']        = {'w':2,  'size':'Fort',       'pop':80,     'gov':'the Church of the Silver Flame'}
s_thdict['Arolangard']         = {'w':3,  'size':'Fort',       'pop':1,      'gov':'the Church of the Silver Flame'}
s_thdict['Aruldusk']           = {'w':4,  'size':'Small City', 'pop':10800,  'gov':'the Church of the Silver Flame'}
s_thdict['Arythawn Keep']      = {'w':5,  'size':'Fort',       'pop':100,    'gov':'the Church of the Silver Flame'}
s_thdict['Athandra']           = {'w':6,  'size':'Town',       'pop':1,      'gov':'the Church of the Silver Flame'}
s_thdict['Auxylgard']          = {'w':7,  'size':'Fort',       'pop':200,    'gov':'the Church of the Silver Flame'}
s_thdict['Avaroth']            = {'w':8,  'size':'Town',       'pop':1,      'gov':'the Church of the Silver Flame'}
s_thdict['Castle Rhonewatch']  = {'w':9,  'size':'Fort',       'pop':1,      'gov':'the Church of the Silver Flame'}
s_thdict['Danthaven']          = {'w':10, 'size':'Town',       'pop':1,      'gov':'the Church of the Silver Flame'}
s_thdict['Daskaran']           = {'w':11, 'size':'Large Town', 'pop':4500,   'gov':'the Church of the Silver Flame'}
s_thdict['Flamekeep']          = {'w':12, 'size':'Metropolis', 'pop':150000, 'gov':'the Church of the Silver Flame'}
s_thdict['Fort Light']         = {'w':13, 'size':'Fort',       'pop':120,    'gov':'the Church of the Silver Flame'}
s_thdict['Harrowgard']         = {'w':14, 'size':'Fort',       'pop':1,      'gov':'the Church of the Silver Flame'}
s_thdict['Lessyk']             = {'w':15, 'size':'Village',    'pop':1,      'gov':'the Church of the Silver Flame'}
s_thdict['Morningcrest']       = {'w':16, 'size':'Fort',       'pop':300,    'gov':'the Church of the Silver Flame'}
s_thdict['Nathyrr']            = {'w':17, 'size':'Village',    'pop':1,      'gov':'the Church of the Silver Flame'}
s_thdict['Olath']              = {'w':18, 'size':'Town',       'pop':1,      'gov':'the Church of the Silver Flame'}
s_thdict['Rellekor']           = {'w':19, 'size':'Village',    'pop':1,      'gov':'the Church of the Silver Flame'}
s_thdict['Sentinel Keep']      = {'w':20, 'size':'Fort',       'pop':1,      'gov':'the Church of the Silver Flame'}
s_thdict['Shadukar']           = {'w':21, 'size':'City',       'pop':0,      'gov':'the Church of the Silver Flame'}
s_thdict['Sharavacion']        = {'w':22, 'size':'Town',       'pop':1,      'gov':'the Church of the Silver Flame'}
s_thdict['Sigilstar']          = {'w':23, 'size':'Small City', 'pop':12000,  'gov':'the Church of the Silver Flame'}
s_thdict['Silvercliff Castle'] = {'w':24, 'size':'Fort',       'pop':50,     'gov':'the Church of the Silver Flame'}
s_thdict['Siyar']              = {'w':25, 'size':'Village',    'pop':1,      'gov':'the Church of the Silver Flame'}
s_thdict['Tellyn']             = {'w':26, 'size':'Town',       'pop':1,      'gov':'the Church of the Silver Flame'}
s_thdict['Thaliost']           = {'w':27, 'size':'Large City', 'pop':24500,  'gov':'the Church of the Silver Flame'}
s_thdict['Tower Perilous']     = {'w':28, 'size':'Fort',       'pop':1,      'gov':'the Church of the Silver Flame'}
s_thdict['Traelyn']            = {'w':28, 'size':'Town',       'pop':1,      'gov':'the Church of the Silver Flame'}
s_thdict['Valiron']            = {'w':30, 'size':'Village',    'pop':1,      'gov':'the Church of the Silver Flame'}
# s_thw = list(it.accumulate([1, 25, 25, 10, 25]))
s_th = list()
s_thw = list()
for x in s_thdict:
    s_th += [[x, s_thdict[x]['size'], s_thdict[x]['pop'], s_thdict[x]['gov']]]
    s_thw += [s_thdict[x]['w']]

# Thranish Settlement Populations
pop['Flamekeep']  = ['human', 'dwarf', 'halfling', 'half-elf', 'elf', 'other']
pop['end']                = ['drow',  'orc',      'gnoll', 'other']
popw['Flamekeep'] = list(it.accumulate([70, 9, 6, 4, 4, 7]))
popw['end']               = list(it.accumulate([51, 23, 14, 12]))
for i in s_thdict.keys():
    if i not in ['Flamekeep']:
        pop[i] = pop['Flamekeep']
        popw[i] = popw['Flamekeep']
        
# Eldeen Reaches Settlements
s_eldict = {}
s_eldict['Alvirad']         = {'w':1,  'size':'Village', 'pop':1,    'gov':'the Great Druid Oalian'}
s_eldict['Cree']            = {'w':2,  'size':'Town',    'pop':1,    'gov':'the Great Druid Oalian'}
s_eldict['Delethorn']       = {'w':3,  'size':'Town',    'pop':1,    'gov':'the Great Druid Oalian'}
s_eldict['Erlaskar']        = {'w':4,  'size':'Town',    'pop':1,    'gov':'the Great Druid Oalian'}
s_eldict['Greenblade']      = {'w':5,  'size':'Village', 'pop':1,    'gov':'the Great Druid Oalian'}
s_eldict['Greenheart']      = {'w':6,  'size':'City',    'pop':1,    'gov':'the Great Druid Oalian'}
s_eldict['Havenglen']       = {'w':7,  'size':'Village', 'pop':1,    'gov':'the Great Druid Oalian'}
s_eldict['Merylsward']      = {'w':8,  'size':'Town',    'pop':1,    'gov':'the Great Druid Oalian'}
s_eldict['Mossmantle']      = {'w':9,  'size':'Village', 'pop':1,    'gov':'the Great Druid Oalian'}
s_eldict['Niern']           = {'w':10, 'size':'Village', 'pop':1,    'gov':'the Great Druid Oalian'}
s_eldict['Owl\'s Perch']    = {'w':11, 'size':'Village', 'pop':1,    'gov':'the Great Druid Oalian'}
s_eldict['Redleaf']         = {'w':12, 'size':'Village', 'pop':1,    'gov':'the Great Druid Oalian'}
s_eldict['Riverweep']       = {'w':13, 'size':'Village', 'pop':1,    'gov':'the Great Druid Oalian'}
s_eldict['Shae Loralyndar'] = {'w':14, 'size':'Town',    'pop':4500, 'gov':'Lord Eversun'}
s_eldict['Sylbaran']        = {'w':15, 'size':'Town',    'pop':1,    'gov':'the Great Druid Oalian'}
s_eldict['Varna']           = {'w':16, 'size':'Town',    'pop':1,    'gov':'the Great Druid Oalian'}
s_eldict['Wolf\'s Paw']     = {'w':17, 'size':'Village', 'pop':1,    'gov':'the Great Druid Oalian'}
s_el = list()
s_elw = list()
for x in s_eldict:
    s_el += [[x, s_eldict[x]['size'], s_eldict[x]['pop'], s_eldict[x]['gov']]]
    s_elw += [s_eldict[x]['w']]

# Eldeen Reaches Settlement Populations
pop['Shae Loralyndar']  = ['eladrin']
pop['end']              = ['drow',  'orc',      'gnoll', 'other']
popw['Shae Loralyndar'] = list(it.accumulate([100]))
popw['end']             = list(it.accumulate([51, 23, 14, 12]))

# Shadow Marches Settlements
s_shdict = {}
s_shdict['Arashuul']       = {'w':1,  'size':'Village', 'pop':1,    'gov':'the Shadow Marches'}
s_shdict['Dhavin\'s Post'] = {'w':2,  'size':'Village', 'pop':1,    'gov':'the Shadow Marches'}
s_shdict['Glumtown']       = {'w':3,  'size':'Village', 'pop':1,    'gov':'the Shadow Marches'}
s_shdict['Goldmire']       = {'w':4,  'size':'Village', 'pop':1,    'gov':'the Shadow Marches'}
s_shdict['Patrahk\'n']     = {'w':5,  'size':'Town',    'pop':1,    'gov':'the Shadow Marches'}
s_shdict['Urthhold']       = {'w':6,  'size':'Town',    'pop':1,    'gov':'the Shadow Marches'}
s_shdict['Valshar\'ak']    = {'w':7,  'size':'Town',    'pop':1,    'gov':'the Shadow Marches'}
s_shdict['Yrlag']          = {'w':8,  'size':'Town',    'pop':1,    'gov':'the Shadow Marches'}
s_shdict['Zarash\'ak']     = {'w':9,  'size':'City',    'pop':1,    'gov':'the Shadow Marches'}
s_sh = list()
s_shw = list()
for x in s_shdict:
    s_sh += [[x, s_shdict[x]['size'], s_shdict[x]['pop'], s_shdict[x]['gov']]]
    s_shw += [s_shdict[x]['w']]

# Shadow Marches Settlement Populations
pop['Zarash\'ak']  = ['eladrin']
pop['end']              = ['drow',  'orc',      'gnoll', 'other']
popw['Zarash\'ak'] = list(it.accumulate([100]))
popw['end']             = list(it.accumulate([51, 23, 14, 12]))

# Droaam Settlements
s_drdict = {}
s_drdict['Cazhaak Draal']        = {'w':1,  'size':'Town',    'pop':1,    'gov':'the Daughters of Sora Kell'}
s_drdict['Graywall']             = {'w':2,  'size':'Town',    'pop':1,    'gov':'the Daughters of Sora Kell'}
s_drdict['Graywall Outpost']     = {'w':3,  'size':'Fort',    'pop':1,    'gov':'the Daughters of Sora Kell'}
s_drdict['Grimstone Keep']       = {'w':4,  'size':'Fort',    'pop':1,    'gov':'the Daughters of Sora Kell'}
s_drdict['Mordain\'s Hall']      = {'w':5,  'size':'Fort',    'pop':1,    'gov':'Mordain the Fleshweaver'}
s_drdict['Shaarat Kol']          = {'w':6,  'size':'Fort',    'pop':1,    'gov':'the Daughters of Sora Kell'}
s_drdict['Stonejaw Keep']        = {'w':7,  'size':'Fort',    'pop':1,    'gov':'the Daughters of Sora Kell'}
s_drdict['The Great Crag']       = {'w':8,  'size':'City',    'pop':1,    'gov':'the Daughters of Sora Kell'}
s_drdict['The Venemous Demesne'] = {'w':9,  'size':'Town',    'pop':1,    'gov':'the Daughters of Sora Kell'}
s_drdict['Thrakelorn']           = {'w':10, 'size':'Village', 'pop':1,    'gov':'the Daughters of Sora Kell'}
s_drdict['Turakbar\'s Fist']     = {'w':11, 'size':'Fort',    'pop':1,    'gov':'the Daughters of Sora Kell'}
s_drdict['Tzaryan Keep']         = {'w':12, 'size':'Fort',    'pop':1,    'gov':'the Daughters of Sora Kell'}
s_drdict['Vralkek']              = {'w':13, 'size':'Town',    'pop':1,    'gov':'the Daughters of Sora Kell'}
s_drdict['Znir']                 = {'w':14, 'size':'Town',    'pop':1,    'gov':'the Daughters of Sora Kell'}
s_dr = list()
s_drw = list()
for x in s_drdict:
    s_dr += [[x, s_drdict[x]['size'], s_drdict[x]['pop'], s_drdict[x]['gov']]]
    s_drw += [s_drdict[x]['w']]

# Droaam Settlement Populations
pop['Cazhaak Draal']   = ['medusa']
pop['The Great Crag']  = ['goblin']
popw['Cazhaak Draal']  = list(it.accumulate([100]))
popw['The Great Crag'] = list(it.accumulate([100]))

# Zilargo Settlements
    
# Darguun Settlements
    
# Talenta Plains Settlements
    
# Valenar Settlements
    
# Mror Holds Settlements
    
# Q'barra Settlements
    
# Lhazaar Principalities Settlements
    
# Demon Wastes Settlements
s_dedict = {}
s_dedict['Ashtakala']      = {'w':1,  'size':'City',    'pop':1, 'gov':'the Council of Ashtakala'}
s_dedict['Blood Crescent'] = {'w':2,  'size':'Village', 'pop':1, 'gov':'Blood Crescent'}
s_dedict['Festering Holt'] = {'w':3,  'size':'Village', 'pop':1, 'gov':'Festering Holt'}
s_dedict['Ghaash Dar']     = {'w':4,  'size':'Town',    'pop':1, 'gov':'the Ghaash\'kala'}
s_dedict['Maruk Dar']      = {'w':5,  'size':'Town',    'pop':1, 'gov':'the Ghaash\'kala'}
s_dedict['Rotting Blade']  = {'w':6,  'size':'Village', 'pop':1, 'gov':'Rotting Blade'}
s_de = list()
s_dew = list()
for x in s_dedict:
    s_de += [[x, s_dedict[x]['size'], s_dedict[x]['pop'], s_dedict[x]['gov']]]
    s_dew += [s_dedict[x]['w']]

# Demon Wastes Settlement Populations
pop['Ashtakala']  = ['rakshasa']
pop['end']              = ['drow',  'orc',      'gnoll', 'other']
popw['Ashtakala'] = list(it.accumulate([100]))
popw['end']             = list(it.accumulate([51, 23, 14, 12]))

# Riedran Settlements
    
# Tashan Plains Settlements
    
# Adar Settlements
    
# Syrkarn Settlements
    
# Xen'drik Settlements
    
# Aerenal Settlements

# COLLATE SETTLEMENT DATA

# Dict of all settlements
all_s = {}
homelands = [s_audict, # Aundair
             s_brdict, # Breland
             s_cydict, # Cyre
             s_kadict, # Karrnath
             s_thdict, # Thrane
             s_eldict, # Eldeen Reaches
             s_shdict, # Shadow Marches
             s_dedict, # Demon Wastes
             s_drdict, # Droaam
             ]
for x in homelands:
    all_s.update(x)
    
# Dict of all settlements, by region
reg_s = {}
reg_s['Aundair']        = s_audict
reg_s['Breland']        = s_brdict
reg_s['Cyre']           = s_cydict
reg_s['Karrnath']       = s_kadict
reg_s['Thrane']         = s_thdict
reg_s['Eldeen Reaches'] = s_eldict
reg_s['Shadow Marches'] = s_shdict
reg_s['Demon Wastes']   = s_dedict

# Dict of settlement weights, by region
reg_sw = {}
reg_sw['Aundair']        = s_auw
reg_sw['Breland']        = s_brw
reg_sw['Cyre']           = s_cyw
reg_sw['Karrnath']       = s_kaw
reg_sw['Thrane']         = s_thw
reg_sw['Eldeen Reaches'] = s_elw
reg_sw['Shadow Marches'] = s_shw
reg_sw['Demon Wastes']   = s_dew

# HEROIC CHRONICLE TABLES

# List of all possible character races
races = ['aarakocra',
         'aasimar',
         'aasimar (Court)',
         'aasimar (fallen)',
         'aasimar (Fernian)',
         'aasimar (Mabaran)',
         'aasimar (protector)',
         'aasimar (scourge)',
         'aasimar (Seeker)',
         'bugbear',
         'bugbear (Dhakaani Guul\'dar)',
         'bullywug',
         'centaur',
         'changeling',
         'dhampir',
         'dragonborn',
         'dwarf',
         'dwarf (duergar)',
         'dwarf (hill)',
         'dwarf (Mark of Warding)',
         'dwarf (mountain)',
         'dwarf (ruinbound)',
         'elf',
         'elf (Aereni)',
         'elf (eladrin)',
         'elf (drow)',
         'elf (high)',
         'elf (Mark of Shadow)',
         'elf (pallid)',
         'elf (sea)',
         'elf (shadar-kai)',
         'elf (wood)',
         'firbolg',
         'genasi',
         'genasi (air)',
         'genasi (earth)',
         'genasi (fire)',
         'genasi (water)',
         'gith',
         'gith (githyanki)',
         'gith (githzerai)',
         'gnoll',
         'gnome',
         'gnome (svirfneblin)',
         'gnome (forest)',
         'gnome (Mark of Scribing)',
         'gnome (rock)',
         'goblin',
         'goblin (Dhakaani Golin\'dar)',
         'goliath',
         'grimlock',
         'grung',
         'half-elf',
         'half-elf (Mark of Detection)',
         'half-elf (Mark of Storm)',
         'half-orc',
         'half-orc (Mark of Finding)',
         'halfling',
         'halfling (ghostwise)',
         'halfling (lightfoot)',
         'halfling (lotusden)',
         'halfling (Mark of Healing)',
         'halfling (Mark of Hospitality)',
         'halfling (stout)'
         'harpy',
         'hexblood',
         'hobgoblin',
         'hobgoblin (Dhaakaani Ghaal\'dar)',
         'human',
         'human (Mark of Finding)',
         'human (Mark of Handling)',
         'human (Mark of Making)',
         'human (Mark of Passage)',
         'human (Mark of Sentinel)',
         'kalashtar',
         'kenku',
         'kobold',
         'kuo-toa',
         'leonin',
         'lizardfolk',
         'loxodon',
         'medusa',
         'merfolk',
         'minotaur',
         'ogre',
         'orc',
         'reborn',
         'satyr',
         'shifter',
         'shifter (beasthide)',
         'shifter (longtooth)',
         'shifter (swiftstride)',
         'shifter (wildhunt)',
         'simic hybrid',
         'tabaxi',
         'tiefling',
         'tortle',
         'triton',
         'troll',
         'vedalken',
         'verdan',
         'warforged',
         'yuan-ti pureblood',
         'yuan-ti shulassakar']

# Family Size
fs = {'parents':['3 or more', '2', '1', '0'],
      'siblings':['2d4+2','2d4','1d4','0d0']}
fs_w = {'Village':[10, 50, 89, 100],
        'City':[5, 50, 89, 100]}

# Family Relationships [text, ally, rival]
fr = [[('You thought you killed this family member, whether by accident or '
       'otherwise. You never expected to see them again - but now they\'re '
       'out for your blood.'), False, True],
      [('You insulted this family member so gravely that they left your life '
        'forever. If they ever return, it will be to settle the score.'),
        False, True],
      [('You have always been better than this family member at a particular '
        'activity. They grew jealous and abandoned you, so that they could '
        'return and best you one day.'), False, True],
      [('You uncovered a secret about this family member, whether a tiny '
        'embarrassment or a life-changing scandal. They now seek to unveil '
        'your darkest secret.'), False, True],
      [('You and this family member have a friendly rivalry, and are '
        'constantly trying to best each other in an activity, craft, or '
        'other pursuit. You visit occasionally to test each other\'s skills.'),
        False, True],
      [('This family member owes you a debt, and they don\'t like it. '
        'They\'ll help you out when you need it, but only to clear the '
        'slate.'), True, False],
      [('This family member loves you, but you were never that close. '
        'They\'ll do anything to help you - as long as they won\'t be at '
        'risk of injury or death.'), True, False],
      [('This family member caused you to have a horrible accident when you '
        'were a child. They still feel incredible guilt, which they would do '
        'anything to assuage.'), True, False],
      [('This family member left long ago for reasons you don\'t understand '
        'or won\'t talk about. Before they left, they promised you that they '
        'would return in your hour of greatest need.'), True, False],
      [('This family member has always loved you with all their heart, and '
        'would do anything for you.'), True, False]]

# Ally relationships
ar = [[('This ally is a loyal pet. Choose 1 beast of CR 1/8 or lower as your '
        'pet.'), False],
      [('This person once lost a bet to you and is still trying to scrounge '
        'up the cash to pay you back. They\'ve decided you\'d both be better '
        'off if they put you in their debt instead.'), True],
      [('This person was once a beggar to whom you gave a large sum of money. '
        'They have transformed their life thanks to you, and now want to '
        'repay your generosity.'), True],
      [('You were this person\'s favorite drinking buddy, and their home is '
        'always open to you and your friends.'), True],
      [('This person was once your mentor, but you left before you could '
        'complete your training. You are welcome to return and finish what '
        'you started, but only when you are ready.'), True],
      [('You bonded with this person over a traumatic event such as a battle '
        'or an armed robbery. If you ever tell them that you are in danger, '
        'they will try to aid you.'), True],
      [('You and this person share a terrible secret, and you have sworn to '
        'never receal it to anyone. They will help you keep this secret if it '
        'is ever in danger of being revealed'), True],
      [('This person fell in love with you. If you reciprocated, they always '
        'stand at your side. If you didn\'t, they took it well, and still '
        'consider you their closest friend.'), True],
      [('You and this person were affected by a powerful magic, and now you '
        'both share a telepathic connection that functions while you are '
        'within 1 mile of each other.'), True],
      [('This person owes you their life. Even if they can\'t follow you '
        'everywhere you go, they will do anything they can to protect you.'),
        True]]

# Rival relationships
rr = [('This person believes that you murdered their sibling. Regardless of '
       'your guilt or innocence, they are out for your blood.'),
      ('You bested this person in combat, but they believe you cheated to '
       'defeat them. They long to prove that they are the superior warrior.'),
      ('You broke a promise to this person, and it caused them to suffer '
       'greatly. Now they conspire to make someone else break a valuable '
       'promise to you.'),
      ('You once loved this person, but broke their heart. They are now '
       'obsessed with making you feel the same pain they felt.'),
      ('This person was ordered to arrest you, and doggedly hunts you '
       'wherever you go.'),
      ('This person thinks that you were replaced by a doppelganger or '
       'possessed by a spirit or monster. They are now trying to defeat you, '
       'so as to find or free the original you.'),
      ('You fled from your home under mysterious circumstances. This person '
       'is obsessed with finding out the truth of what caused you to leave.'),
      ('You and this person tried to harness power beyond your control, and '
       'it left them disfigured and in constant pain. Having since mastered '
       'the power that nearly destroyed them, they now seek to turn it upon '
       'you.'),
      ('You helped this person out once when they were down on their luck, '
       'and now they go to you whenever they need help.'),
      ('This person wants to be your friend, but their help has always made '
       'your life harder.')]

# Ally/Rival Identities
ids = ['Commoner',
       'Acolyte',
       'Bandit',
       'Bandit Captain',
       'Berserker',
       'Cultist',
       'Cult Fanatic',
       'Druid',
       'Gladiator',
       'Guard',
       'Knight',
       'Priest',
       'Scout',
       'Spy',
       'Tribal Warrior',
       'Veteran',
       'Mage',
       'Noble',
       'Assassin',
       'Blood Hunter',
       'Werebear',
       'Weretiger',
       'Wereboar',
       'Wererat',
       'Werewolf',
       'Archmage',
       'Adult Gold Dragon',
       'Adult Red Dragon']
ids_w = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80,
         84, 88, 92, 94, 95, 96, 96.666, 97.333, 98, 99, 99.5, 100]
fateids = ['Cult Fanatic',
           'Gladiator',
           'Mage',
           'Noble',
           'Assassin',
           'Blood Hunter',
           'Werebear',
           'Weretiger',
           'Wereboar',
           'Wererat',
           'Werewolf',
           'Archmage',
           'Adult Gold Dragon',
           'Adult Red Dragon']
def choose_id(): return rng.choices(ids, cum_weights=ids_w)[0]

# Fateful Moments [text, rollfor:[id, item, madness, lycan, disease]]
fm = [[('Your parents were murdered in front of you. Roll on the Ally and '
        'Rival Identities table to determine the type of creature that killed '
        'them. You have proficiency in the Stealth and Survival Skills.'),
        ['id']],
      [('You met a dark elf dying in the wilderness. Around their neck was a '
        'silver talisman containing a cameo of their child and the name '
        '"Il\'viranya." It is an amulet of proof against detection and '
        'location.'),
        []],
      [('A mysterious stanger gave you a gift that saved your life while you '
        'were lost in the wilderness. Roll on the Ally and Rival Identities '
        'table to determine the identity of the stranger. Then roll on Magic '
        'Item Table B in the Dungeon Master\'s Guide to determine the item. '
        'If you roll a consumable item from the table, roll again.'),
        ['id', 'itemB']],
      [('You were caught in a terrible storm but miraculously survived. Now '
        'your dreams contain visions sent by a mysterious god or demigod. You '
        'have proficiency in the Arcana or Religion skill (your choice).'),
        []],
      [('A famous warrior trained you with what has become your signature '
        'weapon. You have proficiency with a martial weapon of your choice, '
        'and you own one such weapon. It has special features as detailed in '
        'chapter 7 of the Dungeon Master\'s Guide. You also have the Martial '
        'Adept feat from the Player\'s Handbook.'),
        []],
      [('You were the sole survivor when a horde of rampaging monsters raided '
        'your village or your neighborhood. You have proficiency in the '
        'Stealth skill or proficiency with martial weapons (your choice).'),
        []],
      [('A famous mage saw potential in you and tutored you in the arcane '
        'arts. You have a spellbook and the Magic Initiate feat from the '
        'Player\'s Handbook.'),
        []],
      [('While on a long journey, you were picked up by a traveling circus, '
        'spending a year with them before returning to your home. You have '
        'proficiency in the Acrobatics or Performance skill (your choice) and '
        'proficiency with the disguise kit.'),
        []],
      [('You were transformed into a bear by mysterious magic, and lived for a '
        'year as an animal before you were saved by a druid. Magic still '
        'lingers within you, though, and you can cast speak with animals at '
        'will.'),
        []],
      [('You were press-ganged into military service, and were left shaken by '
        'what you saw on the battlefield. You have proficiency with medium '
        'armor, shields, and martial weapons. You also have a random form of '
        'indefinite madness, determined by rolling on the Indefinite Madness '
        'table in chapter 8 of the Dungeon Master\'s Guide.'),
        ['indefmadness']],
      [('You were kidnapped by bandits while traveling between towns. While '
        'captured, you met an old thief who helped you escape. You have '
        'proficiency with thieves\' tools and proficiency in the Stealth '
        'skill.'),
        []],
      [('You were visited by a demon lord in a dream. You awakened knowing the '
        'find familiar spell and are now able to cast it as a ritual, but your '
        'familiar always takes the form of a quasit. You also have a random '
        'form of indefinite madness, determined by rolling on the Indefinite '
        'Madness table in chapter 8 of the Dungeon Master\'s Guide.'),
        ['madness']],
      [('While exploring a remote forest, you were attacked by lycanthropes '
        'but escaped before being killed. You are cursed with wereboar, '
        'wererat, or werewolf lycanthropy.'),
        ['lycancurse']],
      [('While lost in a remote forest or jungle, you were saved by a '
        'werebear or weretiger. The lycanthrope believed you were destined '
        'for greatness and granted you the gift of lycanthropy with your '
        'consent.'),
        ['lycangift']],
      [('You saved a pseudodragon from being eaten by a giant spider in a '
        'dark forest. The pseudodragon now loyally follows you wherever you '
        'go, even if you\'d rather it stay hidden. It is controlled by the DM '
        'but obeys your commands if treated well.'),
        []],
      [('You nearly died from a virulent disease (cackle fever, sewer plague, '
        'or sight rot; see chapter 8 of the Dungeon Master\'s Guide). Your '
        'life was saved by an agent of the Library of Korranberg, who could '
        'not cure the disease, but who gave you a periapt of health that '
        'suppresses it.'),
        ['disease']],
      [('You were accused of a crime and were exiled or imprisoned, '
        'regardless of whether or not you were guilty. Having spent time '
        'among criminals, you have proficiency in the Intimidation skill and '
        'you know thieves\' cant.'),
        []],
      [('You saved a riderless horse wearing full tack and harness from '
        'wolves. You own a riding horse and a saddle, and you have '
        'proficiency in the Animal Handling skill.'),
        []],
      [('While reading through a mysterious tome once owned by your parent, '
        'you found a treasure map that points toward a place in Khorvaire '
        'of the DM\'s choice.'),
        []],
      [('You received a letter revealing that you were the secret child of a '
        'wealthy noble family living in Wroat within Breland. They enclosed '
        '100 gp to ensure your safe passage to the capital, and a signet ring '
        'bearing your true family\'s seal.'),
        []]]
indefmadness = []
lycancurse = ['wereboar', 'wererat', 'werewolf']
lycangift = ['werebear', 'weretiger']
disease = ['cackle fever', 'sewer plague', 'sight rot']

# Favorite Foods table
favfoods = {'Menagerie Coast':['Paella - a working-class dish made with rice, white beans, and seafood',
                               'Plantain cups - a sweet and savory dish of fried plantains stuffed with meat and rice',
                               'Gazpacho - a cold soup served on hot days, made from pounded vegetables and fruit',
                               'Honeyflame bread - a fried dessert soaked in honey and coated in Marquesian spices',
                               'Fusaka fish - seafood cutlets smothered in Marquesian fusaka spice and fried in oil',
                               'Snakelocks noodles - sea anemone tendrils coated in honey batter and delicately fried',
                               'Queen\'s water - a soft drink made from syrup, honey, guava, and tamarind',
                               'Blacksand coffee - a tiny shot of coffee, brewed atop red-hot sand, Marquet-style',
                               'Silvertooth - a potent and sweet brandy distilled from the starchy palm lily root',
                               'Rum - a piratical specialty'],
            'Marrow Valley':['Dumplings - a steamed potato bread that can be served with any meal',
                             'Sauerbraten - a Zemnian peasant dish of pickled horse meat served with cabbage',
                             'Brawn (also known as head cheese) - a meat jelly made from boiled calf\'s head',
                             'Schweinshaxe - a Zemnian peasant dish of long-marinated roasted pork knuckle',
                             'Dampfnudel - a regal steamed roll served in sweet custard or with savory potatoes',
                             'Spanferkel - an expensive dish of suckling pig, roasted and served at royal parties',
                             'Imperial pickled plums',
                             'Trost - a sweet, dark ale brewed in Trostenwald',
                             'Radler - a sweet, expensive drink made from imported lemonade mixed with beer'],
            'Greying Wildlands':['Imperial pickled plums, smuggled from the Dwendalian Empire by Myriad agents',
                                 'Charred venison and roasted potatoes, prepared with local game and local tubers',
                                 'Raw venison still dripping with blood',
                                 'Elf-mash - a creamy dish made from overripe cloudberries',
                                 'Dwarven rootbake - a hearty casserole of roots and tubers wrapped in seaweed',
                                 'Jam porridge - made from Xhorhasian rice and topped with salmonberry jam',
                                 'Blazing tea - a beverage blended from fermented fireroot and mouth-scalding spices',
                                 'Sbiten - a drink made from honey and spices, best enjoyed hot on snowy days'],
            'Xhorhas':['Rzukaal - a dish made from sauteed rice noodles, hearty mushrooms, and giant spider legs',
                       'Yuyandl - grilled yuyo (a zucchini-like vegetable that grows in Rosohna\'s sunless gardens) spiced and served with rice',
                       'Mastodon kor\'rundl - grilled mastodon served with sunless kor\'run (a squash-like vegetable that grows in Rosohna\'s sunless gardens) and rice',
                       'Kinespaji spaaldl - soup made from mushrooms or vegetables and the boiled spit of a horizonback turtle',
                       'Umarindaly - a dessert akin to rice pudding, topped with spiced gooseberry jam',
                       'Keltaly - heavy cream mixed with pulverized black currants and frozen into a fluffy, sweet, creamy dessert',
                       'Erzfaalyu - a potent spirit made from fermented rice',
                       'Yunfaalyu - a fragrant plum liquor served at frigid temperatures and garnished with carrots',
                       'Fiery plum spirits',
                       'Earthy mushroom beer']}
favfoods['Zemni Fields'] = favfoods['Marrow Valley'] # both are Western Wynandir

# Names
n = {'Aundair':{'masc':['Ari', 'Bokk', 'Breyten', 'Daen', 'Dover', 'Erben',
                        'Fluin', 'Gavrin', 'Hagro', 'Herschem', 'Huys',
                        'Jurian', 'Kamiel', 'Killian', 'Kleris', 'Reng',
                        'Retief', 'Riaan', 'Saal', 'Sarelo', 'Sithov', 'Tak',
                        'Tyman', 'Urik'],
                'femm':['Aafki', 'Agate', 'Baltia', 'Batrax', 'Beleth',
                        'Chantal', 'Fientia', 'Flerentia', 'Gwen', 'Hjeltia',
                        'Juliona', 'Levini', 'Margana', 'Marloes', 'Sanne',
                        'Sien', 'Tanneken', 'Vilina'],
                'last':['Aarland', 'Acker', 'Adriansen', 'Alyea', 'Arendt',
                        'Bacher', 'Banekert', 'Bartell', 'Bateau', 'Crudaker',
                        'Caldamus', 'Corleis', 'Dekker', 'Ennes', 'Gerlach',
                        'Haldron', 'Hugrin', 'Jurians', 'Karch', 'Kendig',
                        'Maartel', 'Mantanye', 'Merchiot', 'Nagel', 'Ostren',
                        'Petilom', 'Redeker', 'Rhuli', 'Romhaar', 'Serontain',
                        'Shreve', 'Sykes', 'Taumen', 'Thiel', 'Toriun',
                        'Tullier', 'Valleau', 'Veseur', 'Yanger', 'Zenden']},
     'Breland':{'masc':['Alain', 'Beren', 'Cord', 'Curlot', 'Destir', 'Duran',
                        'Erix', 'Jovi', 'Kaine', 'Kuven', 'Laren', 'Lis',
                        'Maal', 'Minyu', 'Nelt', 'Norn', 'Oarsen', 'Pater',
                        'Pol', 'Rand', 'Reesir', 'Saal', 'Stend', 'Tars',
                        'Teesen', 'Uthar', 'Verden', 'Vorj', 'Werem',
                        'Wrogarr', 'Yelfis'],
                'femm':['Aanna', 'Alike', 'Beaf', 'Channa', 'Dabren', 'Delru',
                        'Elazti', 'Fromm', 'Gersi', 'Glenas', 'Habra',
                        'Heeson', 'Isti', 'Itlani', 'Jojerra', 'Ket', 'Khaal',
                        'Lorsanna', 'Margu', 'Maril', 'Monesti', 'Narcy',
                        'Nebra', 'Penti', 'Riki', 'Soranda', 'Tabin', 'Tolri',
                        'Wroaan', 'Wroenna'],
                'last':['Aggan', 'Bakker', 'Colworn', 'Devir', 'Ebinor',
                        'Faldren', 'Graccen', 'Helmworth', 'Jonz', 'Kemble',
                        'Lanner', 'Lonn', 'Makker', 'Morrus', 'Nelview',
                        'Perryn', 'Riston', 'Roole', 'Smyth', 'Snarik',
                        'Thorn', 'Toppe', 'Wrighten']},
     'Cyre':{'masc':[],
             'femm':[],
             'last':[]},
     'Karrnath':{'masc':['Adalstan', 'Alarich', 'Arend', 'Berend', 'Brenius',
                         'Detlev', 'Drago', 'Evetius', 'Falko', 'Fraedus',
                         'Garrick', 'Geroldt', 'Gertan', 'Gustavus', 'Halden',
                         'Leonus', 'Leodegar', 'Maenrad', 'Rochus', 'Rolund',
                         'Sigor', 'Theoban', 'Vedim', 'Vorik', 'Wultram'],
                 'femm':['Adalgisa', 'Alinda', 'Asta', 'Bauin', 'Clotrila',
                         'Demuth', 'Ebba', 'Ermena', 'Forsindh', 'Gisaul',
                         'Harika', 'Haedrun', 'Karola', 'Lorelea', 'Mauriana',
                         'Menelda', 'Oydelis', 'Renilda', 'Syardis', 'Syele',
                         'Theda', 'Valpaea', 'Vaunn'],
                 'last':['Altaner', 'Argland', 'Balich', 'Barthus', 'Brand',
                         'Cerfas', 'Denka', 'Dorn', 'Erdei', 'Eschus',
                         'Furnau', 'Gaebler', 'Gergus', 'Grogloth',
                         'Hellekanus', 'Hintram', 'Jaranus', 'Karlach',
                         'Kessler', 'Kraal', 'Lassinus', 'Losho', 'Maerer',
                         'Ochem', 'Rangoth', 'Roerith', 'Sattler', 'Senglin',
                         'Taggert', 'Thul', 'Trothut', 'Vanalan', 'Vedenin',
                         'Zecklin']},
     'Thrane':{'masc':['Alestair', 'Arrun', 'Andri', 'Calemi', 'Coref',
                       'Demodir', 'Drego', 'Drosin', 'Egen', 'Javi', 'Jeffin',
                       'Kaith', 'Lukar', 'Mizar', 'Ossul', 'Pentar', 'Rave',
                       'Sercyl', 'Sudro', 'Suthar', 'Syro', 'Taran', 'Tokorin',
                       'Urdan', 'Valtar', 'Vencyl', 'Verodin', 'Zoder'],
               'femm':['Avaliah', 'Beref', 'Chantalyn', 'Draci', 'Ghanji',
                       'Hariel', 'Heken', 'Imperi', 'Irulan', 'Jahanah',
                       'Kahlia', 'Lycia', 'Maradal', 'Margil', 'Melindri',
                       'Morgana', 'Narvala', 'Norah', 'Nyllestra', 'Sede',
                       'Suspiria', 'Taris', 'Thradi', 'Varikah'],
               'last':['Aeyliros', 'Askarda', 'Atrelioth', 'Corliostor',
                       'Corus', 'Desekane', 'Drosin', 'Entarro', 'Eskeliendro',
                       'Ghastor', 'Hetrion', 'Imaradi', 'Irvallo',
                       'Karavastar', 'Krayci', 'Lerendazi', 'Marktaros',
                       'Neskus', 'Ovion', 'Ravadanci', 'Sarhain', 'Talandro',
                       'Tarravan', 'Teskelyndros', 'Vanatar', 'Vasiraghi']},
    'Changeling':{'any':['Aunn', 'Bin', 'Cas', 'Dox', 'Fie', 'Hars', 'Jin',
                         'Lam', 'Max', 'Nix', 'Ot', 'Paik', 'Ruz', 'Sim',
                         'Toox', 'Vil', 'Yug']},
    'Goblinoid':{'masc':['Aruget', 'Chetiin', 'Daavn', 'Dabrak', 'Dagii',
                         'Drevduul', 'Duulan', 'Fenic', 'Gudruun', 'Haluun',
                         'Haruuc', 'Jhazaal', 'Kallaad', 'Krakuul', 'Krootad',
                         'Mazaan', 'Munta', 'Nasaar', 'Rakari', 'Reksiit',
                         'Tariic', 'Taruuzh', 'Thuun', 'Vanii', 'Vanon', 'Wuudaraj'],
                 'femm':['Aaspar', 'Aguuz', 'Belaluur', 'Denaal', 'Draraar',
                         'Duusha', 'Ekhaas', 'Eluun', 'Graal', 'Gaduul',
                         'Hashak', 'Jheluum', 'Kelaal', 'Mulaan', 'Nasree',
                         'Raleen', 'Razu', 'Rekseen', 'Shedroor', 'Tajin',
                         'Tuneer', 'Valii', 'Wuun']},
    'Kalashtar':{'quori':['Ashana', 'Ashtai', 'Ishara', 'Hareth', 'Khad',
                          'Kosh', 'Melk', 'Nari', 'Tana', 'Tari', 'Tash',
                          'Ulad', 'Vakri', 'Vash'],
                 'all':['Coratash', 'Dalavash', 'Dolishara', 'Halakosh',
                        'Khoratari', 'Koratana', 'Lanhareth', 'Molavakri',
                        'Nevitash', 'Sorashana', 'Torashtai', 'Valakhad', 'Vishara']},
    'Shifter':{'all':['Badger', 'Bear', 'Cat', 'Fang', 'Grace', 'Grim',
                      'Moon', 'Rain', 'Red', 'Scar', 'Stripe', 'Swift',
                      'Talon', 'Wolf']},
    'Warforged':{'all':['Anchor', 'Banner', 'Bastion', 'Blade', 'Blue', 'Bow',
                        'Cart', 'Church', 'Crystal', 'Dagger', 'Dent', 'Five',
                        'Glaive', 'Hammer', 'Iron', 'Lucky', 'Mace', 'Oak', 'Onyx',
                        'Pants', 'Pierce', 'Red', 'Rod', 'Rusty', 'Scout', 'Seven',
                        'Shield', 'Smash', 'Smith', 'Spike', 'Temple', 'Vault', 'Wall']},
    'Githyanki':{'femm':["Aaryl", "B'noor", "Fenelzi'ir", "Jen'lig", "Pah'zel",
                         "Quorstyl", "Sirruth", "Vaira", "Yessune", "Zar'ryth"],
                 'masc':["Elirdain", "Gaath", "Ja'adoc", "Kar'i'nas", "Lykus",
                         "Quith", "Ris'a'an", "Tropos", "Viran", 'Xamados']},
    'Githzerai':{'femm':['Adaka', 'Adeya', 'Ella', 'Ezhelya', 'Immilzin',
                         'Izera', 'Janara', 'Loraya', 'Uweya', 'Vithka'],
                 'masc':['Dak', 'Duurth', 'Ferzth', 'Greth', 'Hurm',
                         'Kalla', 'Muurg', 'Nurm', 'Shrakk', 'Xorm']},
    'Lizardfolk':{'all':['Achuak (green)', 'Aryte (war)', 'Baeshra (animal)', 'Darastrix (dragon)',
                         'Garurt (axe)', 'Jhank (hammer)', 'Kepesk (storm)', 'Kethend (gem)',
                         'Korth (danger)', 'Kosj (small)', 'Kothar (demon)', 'Litrix (armor)',
                         'Mirik (song)', 'Throden (many)', 'Thurkear (night)', 'Usk (iron)',
                         'Valignat (burn)', 'Vargach (battle)', 'Vutha (black)', 'Vyth (steel)']},
    'Dragonborn':{'clan':['Akambherylliax', 'Argenthrixus', 'Baharoosh', 'Beryntolthropal', 'Bhenkumbyrznaax',
                          'Caavylteradyn', 'Chumbyxirinnish', 'Clethtinthiallor', 'Daardendrian', 'Delmirev',
                          'Dhyrktelonix', 'Ebynichtomonis', 'Esstyrlynn', 'Fharngnarthnost', 'Ghaallixirn',
                          'Grrrmmballhyst', 'Gygazzylyshrift', 'Hashphronyxadyn', 'Hshhsstoroth', 'Imbixtellrhyst',
                          'Jerynomonis', 'Jharthraxyn', 'Kerrhylon', 'Kimbatuul', 'Lhamboldennish', 'Linxakasendalor',
                          'Mohradyllion', 'Mystan', 'Nemmonis', 'Norixius', 'Ophinshtalajiir', 'Orexijandilin',
                          'Pfaphnyrennish', 'Phrahdrandon', 'Pyraxtallinost', 'Qyxpahrgh', 'Raghthroknaar',
                          'Shestendeliath', 'Skaarzborroosh', 'Sumnarghthrysh', 'Tiammanthyllish', 'Turnuroth',
                          'Umbyrphrael', 'Vangdondalor', 'Verthisathurgiesh', 'Wivvyrholdalphiax', 'Wystongjiir',
                          'Xephyrbahnor', 'Yarjerit', 'Zzzxaaxthroth'],
                  'femm':['Akra', 'Aasathra', 'Antrara', 'Arava', 'Biri', 'Blendaeth',
                          'Burana', 'Chassath', 'Daar', 'Dentratha', 'Doudra', 'Driindar',
                          'Eggren', 'Farideh', 'Findex', 'Furrele', 'Gesrethe', 'Gilkass',
                          'Harann', 'Havilar', 'Hethress', 'Hillanot', 'Jaxi', 'Jezean',
                          'Jheri', 'Kadana', 'Kava', 'Korinn', 'Megren', 'Miijira', 'Mishann',
                          'Nala', 'Nuthra', 'Perra', 'Pogranix', 'Pyxrin', 'Quespa', 'Raiann',
                          'Rezena', 'Ruloth', 'Saphara', 'Savaran', 'Sora', 'Surina', 'Synthrin',
                          'Tatyan', 'Thava', 'Uadjit', 'Vezera', 'Zykroff'],
                  'masc':['Adrex', 'Arjhan', 'Azzakh', 'Balasar', 'Baradad', 'Bharash', 'Bidreked',
                          'Dadalan', 'Dazzazn', 'Direcris', 'Donaar', 'Fax', 'Gargax', 'Ghesh',
                          'Gorbundus', 'Greethen', 'Heskan', 'Hirrathak', 'Ildrex', 'Kaladan',
                          'Kerkad', 'Kiirith', 'Kriv', 'Maagog', 'Medrash', 'Mehen', 'Mozikth',
                          'Mreksh', 'Mugrunden', 'Nadarr', 'Nithther', 'Norkruuth', 'Nykkan',
                          'Pandjed', 'Patrin', 'Pijjirik', 'Quarethon', 'Rathkran', 'Rhogar',
                          'Rivaan', 'Sethrekar', 'Shamash', 'Shedinn', 'Srorthen', 'Tarhun',
                          'Torinn', 'Trynnicus', 'Valorean', 'Vrondiss', 'Zedaar']},
    'Gnoll':{'all':['Dagnyr', 'Dhyrn', 'Ghyrryn', 'Gnasc', 'Gnoryc', 'Gnyrn', 'Hyrn', 'Lhoryn',
                    'Lhyr', 'Lhyrl', 'Mognyr', 'Myrl', 'Sorgnyn', 'Thyrn', 'Toryc', 'Yrgnyn', 'Yrych']}
    } # end names
firstnames = {'Dragonborn':{'m':['Heldeofol', 'Numesh',   'Keskur',  'Jhunvar',    'Talasseth',
                                 'Grethnich', 'Radonaar', 'Vorkil',  'Shudrech',   'Darangreth',
                                 'Kutreen',   'Rendurss', 'Phanath', 'Chulmeth',   'Thrunev',
                                 'Perethul',  'Krenzul',  'Gharaxx', 'Zuvan',      'Lorthnul'],
                            'f':['Sokra',     'Zirnee',   'Hareena', 'Aorinza',    'Levea',
                                 'Arvena',    'Derra',    'Tylora',  'Quorthessa', 'Suthini',
                                 'Hishvedi',  'Meruva',   'Letheen', 'Sorenlesh',  'Narenn',
                                 'Wuressi',   'Trenela',  'Edethei', 'Opnatra',    'Surian']},
              'Dwarf':{'m':['Therin',   'Konitir',   'Gunthraz',  'Fughanor',  'Hithdren',
                            'Okino',    'Badrik',    'Kordrek',   'Rebern',    'Granthrim',
                            'Thorelin', 'Karrackis', 'Donvel',    'Thromfir',  'Dereben',
                            'Vavek',    'Mabergor',  'Skirilath', 'Duthtrock', 'Zorlgrum'],
                       'f':['Orthinia', 'Wynnthri',  'Diesina',   'Gorthriss', 'Listra',
                            'Ladreyn',  'Tristryd',  'Thrayka',   'Pinzla',    'Deldith',
                            'Norian',   'Yarthrea',  'Arthena',   'Torera',    'Helini',
                            'Selthenn', 'Runefiss',  'Geselen',   'Doa',       'Niln']},
              'Eladrin':{'m':['Dijulian',  'Larthon',    'Thayeren',   'Arizlakuza', 'Saravis',
                              'Lelethir',  'Gavilindan', 'Immilen',    'Laineth',    'Pramilar',
                              'Qualias',   'Revunalor',  'Dinartisar', 'Berkian',    'Moyanzir',
                              'Rayazan',   'Alazar',     'Leovorian',  'Farlieth',   'Relathar'],
                         'f':['Leannia',   'Kaylleigh',  'Bethidela',  'Leria',      'Quinala',
                              'Thistrani', 'Anisvilan',  'Kaeryn',     'Thelenisa',  'Saliar',
                              'Vainara',   'Aleath',     'Lethyri',    'Telonia',    'Shenwrynn',
                              'Andoriel',  'Levethien',  'Sivarea',    'Arvaneria',  'Quendili']},
              'Elf':{'m':['Raven',     'Deltor',  'Nunel',    'Marrdrin',   'Nelor',
                          'Olorion',   'Venolen', 'Nerepar',  'Lenevelon',  'Vasaren',
                          'Netherin',  'Relean',  'Talon',    'Tinaris',    'Hiranel',
                          'Warric',    'Burenus', 'Kinsalor', 'Guthrin',    'Hilsadar'],
                     'f':['Treloreen', 'Lafar',   'Chiarus',  'Aila',       'Annun',
                          'Leairi',    'Lotus',   'Thia',     'Kalathiana', 'Pasarin',
                          'Julna',     'Raniq',   'Vashara',  'Eridiun',    'Oseri',
                          'Lorinea',   'Rosen',   'Feralia',  'Foxy',       'Yulia']},
              'Halfling':{'m':['Narshi',  'Huffy',    'Chuvy',   'Rukker',  'Terrin',
                               'Frenny',  'Nemmer',   'Mazal',   'Yander',  'Worric',
                               'Tunner',  'Nerrim',   'Banadil', 'Pedin',   'Sleer',
                               'Windel',  'Solstrun', 'Zulm',    'Junan',   'Laffer'],
                          'f':['Jilly',   'Lillic',   'Deia',    'Nashana', 'Adenna',
                               'Chussy',  'Kebrina',  'Tavara',  'Yanelia', 'Luz',
                               'Kinithi', 'Allena',   'Queryn',  'Suneel',  'Kwenlo',
                               'Dellen',  'Palulae',  'Veruni',  'Suleris', 'Peffy']},
              'Human':{'m':['Valec',    'Lenherrow', 'Kriz',    'Mirly',    'Jor',
                            'Jonlin',   'Aleb',      'Mirul',   'Bren',     'Elthid',
                            'Witglen',  'Bessir',    'Grefdon', 'Brenthor', 'Martegan',
                            'Drunthen', 'Pronluc',   'Manny',   'Urik',     'Delin'],
                       'f':['Aliana',   'Kisani',    'Shaya',   'Petrivi',  'Eltez',
                            'Juva',     'Nana',      'Myri',    'Sass',     'Miko',
                            'Elicia',   'Stucy',     'Gwin',    'Shilly',   'Peneresil',
                            'Mirn',     'Mulonny',   'Elly',    'Drea',     'Farila']},
              'Tiefling':{'m':['Xul',       'Delatos',   'Kamados',     'Querinax',  'Menos',
                               'Horthos',   'Sluethis',  'Emokess',     'Terath',    'Sarakka',
                               'Dinusin',   'Siadiss',   'Moskiz',      'Anmen',     'Taluss',
                               'Kutrech',   'Ruleph',    'Edelandross', 'Malich',    'Xanros'],
                          'f':['Thrainee',  'Delzidiae', 'Zoa',         'Derecia',   'Lyseliss',
                               'Tizerea',   'Morianna',  'Terinna',     'Phoebitia', 'Taktra',
                               'Skraya',    'Ravertia',  'Vacheri',     'Peluna',    'Doomensel',
                               'Wallistra', 'Iruvedi',   'Hedonastrae', 'Lamita',    'Therseeli']}}
lastnames = {'Dragonborn':['Firedrinker', 'Kulzabesh',   'Ironmelter',  'Frenthaviss', 'Seshlaron',
                           'Thuresh',     'Cinderheart', 'Nazthuron',   'Ulzariss',    'Frostsworn',
                           'Akralech',    'Delberon',    'Stormcradle', 'Rethreleck',  'Tethnuvesh',
                           'Venomfang',   'Jorlsenviss', 'Ossnelech',   'Lithnaron',   'Bekrashess'],
             'Dwarf':['Grimbeard', 'Darkstone',  'Boozeblood', 'Orestrike',   'Gemseeker',
                      'Anvilsoul', 'Rockchewer', 'Orethane',   'Silvercask',  'Minequaff',
                      'Runechip',  'Firebrow',   'Irongut',    'Bloodbeard',  'Stoneshield',
                      'Alefoot',   'Hammersong', 'Forgeheart', 'Boulderhelm', 'Hillcrusher'],
             'Eladrin':['Kantiluthian', 'Talespinner', 'Ruquelar',  'Incantius',  'Feysong',
                        'Valinora',     'Ethereala',   'Tresquiar', 'Keldrannor', 'Lendalir',
                        'Mythalandis',  'Duirsarian',  'Corellis',  'Starweaver', 'Silmanthor',
                        'Grathal',      'Astralania',  'Velshara',  'Winterfire', 'Songstar'],
             'Elf':['Darkshadow',  'Rivermist', 'Stormbird',  'Duskwhisper', 'Swiftarrow',
                    'Glittermoon', 'Cloudborn', 'Wolfcaller', 'Hawksong',    'Spiritwind',
                    'Dawnbreaker', 'Goldwood',  'Shimmersun', 'Starfall',    'Brookspeaker',
                    'Moongleam',   'Redleaves', 'Farshot',    'Glimmerdawn', 'Willowsinger'],
             'Halfling':['Fastfingers', 'Smallpockets', 'Quickfeet',    'Treejumper',  'Mousebane',
                         'Longfoot',    'Pondhopper',   'Silvertongue', 'Coinslapper', 'Keenears',
                         'Spryblade',   'Hastyhands',   'Gemnose',      'Goldslinger', 'Fateskipper',
                         'Nimbletoes',  'Shotluck',     'Huddlebrush',  'Burrowborn',  'Hedgethane'],
             'Human':['Blackwinter', 'Heathington', 'Nubingor', 'Ortegena',   'Nightharrow',
                      'Runthrop',    'Beldock',     'Algoy',    'Grash',      'Nararis',
                      'Welnib',      'Grij',        'Hilden',   'Grethkin',   'McRufrick',
                      'Tebril',      'Kalmin',      'Renfold',  'Kenisville', 'McAndrik'],
             'Tiefling':['Lathian',   'Whiptail',  'Gloomgrin', 'Felstrike',  'Zezbulane',
                         'Jeferloch', 'Dozmordin', 'Querelech', 'Darkfire',   'Relzdexun',
                         'Grasht',    'Pulediz',   'Armansuss', 'Blackflame', 'Wrevilicus',
                         'Kerevon',   'Ophenzul',  'Tethenbri', 'Chemmidon',  'Sinfury']}

# Noble Title Hierarchy (5e DMG)
# key = title, value = rank
titlerank = {'Empress':     1,
             'Emperor':     1,
             'Queen':       2,
             'King':        2,
             'Duchess':     3,
             'Duke':        3,
             'Princess':    4,
             'Prince':      4,
             'Marquise':    5,
             'Marquess':    5,
             'Countess':    6,
             'Count':       6,
             'Earl':        6,
             'Viscountess': 7,
             'Viscount':    7,
             'Baroness':    8,
             'Baron':       8,
             'Baronet':     9,
             'Knight':      10}

# Daelkyr Modifications (ERLW)
daelkyrmod = ['The creature is fused with another creature or object',
              'The creature has additional eyes, or its existing eyes are replaced with the eyes of a different creature',
              'The creature produces eerie music instead of speech',
              'The creature\'s skin has an unusual texture or color',
              'The creature\'s hair is replaced by spines or tentacles',
              'The creature\'s flesh is transparent',
              'The creature has extra limbs',
              'The creature is bioluminescent',
              'The creature has an additional head',
              'The creature sheds its skin every 60 days']

# 5e DMG - Creating NPCs
# One sentence to sum up each of the following:
# - Occupation and history
# - Appearance
# - Abilities
# - Talent
# - Mannerism
# - Interactions with others
# - Useful knowledge
# - Ideal
# - Bond
# - Flaw or secret

# Occupation and history
# - maybe gen a random background?

# Appearance
appearance = ['Distinctive jewelry: earrings, necklace, circlet, bracelets',
              'Piercings',
              'Flamboyant or outlandish clothes',
              'Formal, clean clothes',
              'Ragged, dirty clothes',
              'Pronounced scar',
              'Missing teeth',
              'Missing fingers',
              'Unusual eye color',
              'Two different eye colors',
              'Tattoos',
              'Birthmark',
              'Unusual skin color',
              'Bald',
              'Braided beard or hair',
              'Unusual hair color',
              'Nervous eye twitch',
              'Distinctive nose',
              'Distinctive crooked posture',
              'Distinctive rigid posture',
              'Exceptionally beautiful',
              'Exceptionally ugly']

# Abilities
# pick one high and one low
high = {'Strength':    ['powerful', 'brawny', 'strong as an ox'],
        'Dexterity':   ['lithe', 'agile', 'graceful'],
        'Constitution':['hardy', 'hale', 'healthy'],
        'Intelligence':['studious', 'learned', 'inquisitive'],
        'Wisdom':      ['perceptive', 'spiritual', 'insightful'],
        'Charisma':    ['persuasive', 'forceful', 'born leader']}
low = {'Strength':    ['feeble', 'scrawny'],
       'Dexterity':   ['clumsy', 'fumbling'],
       'Constitution':['sickly', 'pale'],
       'Intelligence':['dim-witted', 'slow'],
       'Wisdom':      ['oblivious', 'absentminded'],
       'Charisma':    ['dull', 'boring']}

# Talent
talent = ['Plays a musical instrument',
          'Speaks several languages fluently',
          'Unbelievably lucky',
          'Perfect memory',
          'Great with animals',
          'Great with children',
          'Great at solving puzzles',
          'Great at one game',
          'Great at impersonations',
          'Draws beautifully',
          'Paints beautifully',
          'Sings beautifully',
          'Drinks everyone under the table',
          'Expert carpenter',
          'Expert cook',
          'Expert dart thrower and rock skipper',
          'Expert juggler',
          'Skilled actor and master of disguise',
          'Skilled dancer',
          'Knows thieves\' cant']

# Mannerism
mannerism = ['Prone to singing, whistling, or humming quietly',
             'Speaks in rhyme or some other peculiar way',
             'Particularly low or high voice',
             'Slurs words, lisps, or stutters',
             'Enunciates overly clearly',
             'Speaks loudly',
             'Whispers',
             'Uses flowery speech or long words',
             'Frequently uses the wrong word',
             'Uses colorful oaths and exclamations',
             'Makes constant jokes or puns',
             'Prone to predictions of doom',
             'Fidgets',
             'Squints',
             'Stares into the distance',
             'Chews something',
             'Paces',
             'Taps fingers',
             'Bites fingernails',
             'Twirls hair or tugs beard']

# Interactions with others
interactions = ['Argumentative',
                'Arrogant',
                'Blustering',
                'Rude',
                'Curious',
                'Friendly',
                'Honest',
                'Hot tempered',
                'Irritable',
                'Ponderous',
                'Quiet',
                'Suspicious']

# Useful knowledge
# anything from the best inn in town to a clue needed to solve a murder

# Ideals
ideals = {'Good':['Beauty',
                  'Charity',
                  'Greater good',
                  'Life',
                  'Respect',
                  'Self-sacrifice'],
          'Evil':['Domination',
                  'Greed',
                  'Might',
                  'Pain',
                  'Retribution',
                  'Slaughter'],
          'Lawful':['Community',
                    'Fairness',
                    'Honor',
                    'Logic',
                    'Responsibility',
                    'Tradition'],
          'Chaotic':['Change',
                     'Creativity',
                     'Freedom',
                     'Independence',
                     'No limits',
                     'Whimsy'],
          'Neutral':['Balance',
                     'Knowledge',
                     'Live and let live',
                     'Moderation',
                     'Neutrality',
                     'People'],
          'Other':['Aspiration',
                   'Discovery',
                   'Glory',
                   'Nation',
                   'Redemption',
                   'Self-knowledge']
          }
          
# Bond
# can also use backgrounds from the Player's Handbook to pick bonds
npcbonds = ['Dedicated to fulfilling a personal life goal',
            'Protective of close family members',
            'Protective of colleagues or compatriots',
            'Loyal to a benefactor, patron, or employer',
            'Captivated by a romantic interest',
            'Drawn to a special place',
            'Protective of a sentimental keepsake',
            'Protective of a valuable possession',
            'Out for revenge',
            'Roll twice']

# Flaw or secret
# again, can also use PHB backgrounds
npcflaworsecret = ['Forbidden love',
                   'Susceptibility to romance',
                   'Enjoys decadent pleasures',
                   'Arrogance',
                   'Envies another creature\'s possessions or station',
                   'Overpowering greed',
                   'Prone to rage',
                   'Has a powerful enemy',
                   'Specific phobia',
                   'Shameful or scandalous history',
                   'Secret crime or misdeed',
                   'Possession of forbidden lore',
                   'Foolhardy bravery']

# NPC alignment
alignment = ['LG','NG','CG','LN','N','CN','LE','NE','CE']
alignmentw = [2,4,6,9,11,12,15,18,20]

# NPC class
npcclass = ['Barbarian',
            'Bard',
            'Cleric',
            'Druid',
            'Fighter',
            'Monk',
            'Paladin',
            'Ranger',
            'Rogue',
            'Sorceror',
            'Warlock',
            'Wizard',
            'Artificer']
npcclassw = [1,2,4,5,7,8,9,10,13,14,15,17,20]

# Define helper functions

def choose_region():
    region = rng.choices(list(hldict), cum_weights=hlw)[0]
    return region

def choose_settlement(region='none', retreg=False):
    if region == 'none':
        region = choose_region()
    settlement = rng.choices(list(reg_s[region]), cum_weights=reg_sw[region])[0]
    if retreg: return settlement, region
    else: return settlement

def choose_race(settlement='none', presetrace='none'):
    if settlement != 'none':
        if presetrace != 'other':
            race = rng.choices(pop[settlement], cum_weights=popw[settlement])[0]
        else:
            race = presetrace
        if (race == 'other') or (presetrace == 'other'):
            tempraces = list(races)
            for x in pop[settlement]:
                for y in tempraces:
                    if x == y:
                        tempraces.remove(y)
            race = rng.choice(tempraces)
    else:
        race = rng.choice(races)
    return race

def choose_family(hometownsize='Village'):
    if hometownsize != 'City': hometownsize = 'Village'
    parents = rng.choices(fs['parents'], cum_weights=fs_w[hometownsize])[0]
    numsiblings = rng.choices(fs['siblings'], cum_weights=fs_w[hometownsize])[0]
    siblings = roll(numsiblings)
    return parents, siblings

def choose_famrel(nrel=1):
    famrel = []
    for x in range(0, nrel):
        famrel += [rng.choice(fr)]
    return famrel

def choose_allyrel(): return rng.choice(ar)

def choose_rivalrel(): return rng.choice(rr)

def choose_fatemoments(nmoments=0):
    fatemoments = []
    for x in range(0, nmoments):
        fatemoments += [rng.choice(fm)]
    return fatemoments

# Define character object class

class Character:
    def __init__(self, **preset ):
        
        # Set Hometown
        if 'settlement' in preset:
            self.settlement = preset['settlement']
            for x in reg_s:
                if self.settlement in reg_s[x]:
                    self.homeland = x
        elif 'homeland' in preset:
            self.homeland = preset['homeland']
            self.settlement = choose_settlement(region=self.homeland)
        else:
            self.settlement, self.homeland = choose_settlement(retreg=True)
        self.hometownsize = all_s[self.settlement]['size']
        self.hometownpop  = all_s[self.settlement]['pop']
        self.government   = all_s[self.settlement]['gov']

        # Set Background
        if 'background' in preset:
            self.background = preset['background']
        else:
            self.background = rng.choices(bg, cum_weights=bgw)[0]
        
        # Determine Ally
        if 'ally' in preset: self.ally = preset('ally')
        else: self.ally = rng.choice([True, False])
            
        # Determine Rival
        if 'rival' in preset: self.rival = preset('rival')
        else: self.rival = rng.choice([True, False])
        
        # Determine whether character has resettled from land of birth
        if 'resettled' in preset:
            self.resettled = preset['resettled']
        else:
            self.resettled = rng.choices([False, True], cum_weights=[75, 100])[0]
        
        # Choose birthplace if different from hometown
        if self.resettled:
            if 'birthsettlement' in preset:
                self.birthsettlement = preset['birthsettlement']
                for x in reg_s:
                    if self.birthsettlement in reg_s[x]:
                        self.birthland = x
            elif 'birthland' in preset:
                self.birthland = preset['birthland']
                self.birthsettlement = choose_settlement(region=self.birthland)
            else:
                self.birthsettlement, self.birthland = choose_settlement(retreg=True)
            self.birthtownsize   = all_s[self.birthsettlement]['size']
            self.birthtownpop    = all_s[self.birthsettlement]['pop']
            self.birthgovernment = all_s[self.birthsettlement]['gov']
        else:
            # character grew up in land of birth
            self.birthland       = self.homeland
            self.birthsettlement = self.settlement
            self.birthtownsize   = self.hometownsize
            self.birthtownpop    = self.hometownpop
            self.birthgovernment = self.government
    
        # Set Race
        if 'race' in preset:
            self.race = preset['race']
            if self.race == 'other':
                self.race = choose_race(settlement=self.birthsettlement,
                                        presetrace=self.race)
        else:
            self.race = choose_race(settlement=self.birthsettlement)
            
        # Set Family size
        self.parents, self.siblings = choose_family(self.hometownsize)
        if 'parents' in preset:
            self.parents = preset['parents']
        if 'siblings' in preset:
            self.siblings = preset['siblings']
            
        # Determine Family Relationships
        self.famrel = choose_famrel(nrel=roll('1d3'))
    
        # Set Acquired Ally/Rival Relationships, Identities, & Fateful Moments
        nfatemoments = 0
        if self.ally:
            self.allyrel = choose_allyrel()
            if self.allyrel[1]:
                self.allyid = choose_id()
                if self.allyid in fateids: nfatemoments += 1
        if self.rival:
            self.rivalrel = choose_rivalrel()
            self.rivalid = choose_id()
            if self.rivalid in fateids: nfatemoments += 1
        self.fatemoments = choose_fatemoments(nfatemoments)
    
    def narrate(self):
        text = 'I am '
        if self.race.startswith(('a','e','i','o','u')): text += 'an '
        else: text += 'a '
        text += self.race.capitalize() + ' ' + self.background
        text += ', who was born in the '
        if self.settlement == self.government: text += 'independent '
        text += self.birthtownsize.lower() + ' of ' + self.birthsettlement + ', '
        if self.birthland in fivenations:
            text += 'in the nation of '
        else:
            text += 'in '
        text += self.birthland
        if self.birthsettlement != self.settlement:
            text += ', and grew up in the '
            if self.settlement == self.government:
                text += 'independent '
            text += self.hometownsize.lower() + ' of ' + self.settlement + ', '
            if self.homeland in fivenations:
                text += 'in the nation of'
            else:
                text += 'in '
            text += self.homeland
        if self.settlement != self.government:
            text += ', under the rule of '
            text += self.government + '.'
        else:
            text += '.'
        print(text)
    
    def stats(self):
        print('Race:', self.race.capitalize())
        print('Background:', self.background)
        print('Birthplace:', self.birthsettlement, ',', self.birthland)
        if self.birthsettlement != self.settlement:
            print('Hometown:', self.settlement, ',', self.homeland)
        print('Citizenship:', self.government)
        print('Parents:', self.parents)
        print('Siblings:', self.siblings)
        print('Family Relationships:')
        for x in self.famrel:
            if x[1]: print('Ally:', x[0])
            elif x[2]: print('Rival:', x[0])
        print('Acquired Relationships:')
        
if __name__=='__main__':
  test = Character()
  test.narrate()
  test.stats()