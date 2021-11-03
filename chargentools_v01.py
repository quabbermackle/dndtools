# -*- coding: utf-8 -*-
"""
Created on Sat Dec 26 10:01:09 2020

@author: theki

Character background generator using tables from the Explorer's Guide to
Wildemount
"""

import itertools as it
import random as rng
rng.seed()

'''
#%% Define tables as global dicts

bg = {} # background
bg[1] = 'Acolyte'
bg[2] = 'Acolyte (Luxonborn)'
bg[3] = 'Charlatan'
bg[4] = 'Criminal'
bg[5] = 'Criminal (Myriad operative)'
bg[6] = 'Entertainer'
bg[7] = 'Folk Hero'
bg[8] = 'Grinner'
bg[9] = 'Guild Artisan'
bg[10] = 'Hermit'
bg[11] = 'Noble'
bg[12] = 'Outlander'
bg[13] = 'Sage'
bg[14] = 'Sage (Cobalt Scholar)'
bg[15] = 'Sailor'
bg[16] = 'Sailor (Revelry pirate)'
bg[17] = 'Soldier'
bg[18] = 'Spy (Augen Trust)'
bg[19] = 'Urchin'
bg[20] = 'Volstrucker Agent'
'''

#%% Define tables and weights as lists

# Homelands
hl = ['Menagerie Coast',
      'Marrow Valley',
      'Zemni Fields',
      'Greying Wildlands',
      'Xhorhas',
      'Eiselcross']
hlw = [21, 40, 72, 77, 100, 105]

# Backgrounds
bg = ['Acolyte',
      'Acolyte (Luxonborn)',
      'Charlatan',
      'Criminal',
      'Criminal (Myriad operative)',
      'Entertainer',
      'Folk Hero',
      'Grinner',
      'Guild Artisan',
      'Hermit',
      'Noble',
      'Outlander',
      'Sage',
      'Sage (Cobalt Scholar)',
      'Sailor',
      'Sailor (Revelry pirate)',
      'Soldier',
      'Spy (Augen Trust)',
      'Urchin',
      'Volstrucker Agent']
bgw = list(range(1,21))

# Menagerie Coast Settlements
s_mc = [['Brokenbank',  'Town', 1520,  'Clovis Concord'],
        ['Darktow',     'Town', 1306,  'Revelry pirates'],
        ['Feolinn',     'City', 12700, 'Clovis Concord'],
        ['Gwardan',     'City', 18900, 'Clovis Concord'],
        ['Nicodranas',  'City', 31900, 'Clovis Concord'],
        ['Othe',        'City', 8320,  'Clovis Concord'],
        ['Palma Flora', 'Town', 1780,  'Clovis Concord'],
        ['Port Damali', 'City', 82110, 'Clovis Concord'],
        ['Port Zoon',   'City', 19120, 'Clovis Concord'],
        ['Tussoa',      'City', 15110, 'Clovis Concord']]
s_mcw = [1, 2, 9, 19, 36, 40, 41, 84, 93, 100]

# Menagerie Coast Settlement Populations
pop = {}
popw = {}
pop['Brokenbank'] = ['human', 'tabaxi', 'dwarf', 'other']
popw['Brokenbank'] = list(it.accumulate([74, 9, 6, 11]))
pop['Darktow'] = ['human', 'elf', 'dwarf', 'other']
popw['Darktow'] = list(it.accumulate([61, 12, 9, 18]))
pop['Feolinn'] = ['human', 'elf', 'gnome', 'other']
popw['Feolinn'] = list(it.accumulate([73, 10, 5, 12]))
pop['Gwardan'] = ['elf', 'human', 'gnome', 'other']
popw['Gwardan'] = list(it.accumulate([63, 16, 11, 10]))
pop['Nicodranas'] = ['human', 'halfling', 'dwarf', 'other']
popw['Nicodranas'] = list(it.accumulate([68, 13, 8, 10]))
pop['Othe'] = ['human', 'halfling', 'half-orc', 'other']
popw['Othe'] = list(it.accumulate([64, 16, 11, 9]))
pop['Palma Flora'] = ['human', 'halfling', 'dwarf', 'other']
popw['Palma Flora'] = list(it.accumulate([68, 13, 11, 8]))
pop['Port Damali'] = ['human', 'halfling', 'elf', 'other']
popw['Port Damali'] = list(it.accumulate([51, 16, 15, 18]))
pop['Port Zoon'] = ['human', 'halfling', 'other']
popw['Port Zoon'] = list(it.accumulate([80, 7, 13]))
pop['Tussoa'] = ['human', 'elf', 'halfling', 'other']
popw['Tussoa'] = list(it.accumulate([74, 10, 8, 8]))

# Marrow Valley Settlements
s_mv = [['Alfield',             'Town',             3410,  'Dwendalian Empire'],
        ['Ashguard Garrison',   'Military outpost', 5720,  'Kryn Dynasty'],
        ['Berleben',            'Town',             3230,  'Dwendalian Empire'],
        ['Bladegarden',         'City',             9910,  'Dwendalian Empire'],
        ['Deastok',             'City',             10090, 'Dwendalian Empire'],
        ['Felderwin',           'City',             8180,  'Dwendalian Empire'],
        ['Grimgolir',           'City',             19090, 'Dwendalian Empire'],
        ['Hupperdook',          'City',             12090, 'Dwendalian Empire'],
        ['Kamordah',            'City',             7440,  'Dwendalian Empire'],
        ['Talonstadt',          'Town',             1810,  'Dwendalian Empire'],
        ['Trostenwald',         'City',             8900,  'Dwendalian Empire'],
        ['Vol\'antim',          'Town',             3890,  'Vol\'antim'],
        ['Zadash',              'City',             89210, 'Dwendalian Empire']]
s_mvw = [2, 5, 7, 12, 18, 22, 32, 40, 44, 45, 50, 52, 100]

# Marrow Valley Settlement Populations
pop['Alfield'] = ['human', 'halfling', 'gnome', 'other']
popw['Alfield'] = list(it.accumulate([61, 22, 11, 6]))
pop['Ashguard Garrison'] = ['drow', 'other']
popw['Ashguard Garrison'] = list(it.accumulate([74, 26]))
pop['Berleben'] = ['human', 'halfling', 'gnome', 'other']
popw['Berleben'] = list(it.accumulate([63, 17, 12, 8]))
pop['Bladegarden'] = ['half-orc', 'orc', 'human', 'other']
popw['Bladegarden'] = list(it.accumulate([32, 21, 25, 22]))
pop['Deastok'] = ['human', 'dwarf', 'halfling', 'other']
popw['Deastok'] = list(it.accumulate([60, 26, 10, 4]))
pop['Felderwin'] = ['halfling', 'human', 'dragonborn', 'other']
popw['Felderwin'] = list(it.accumulate([58, 21, 6, 15]))
pop['Grimgolir'] = ['dwarf', 'human', 'halfling', 'other']
popw['Grimgolir'] = list(it.accumulate([81, 8, 6, 5]))
pop['Hupperdook'] = ['gnome', 'dwarf', 'human', 'other']
popw['Hupperdook'] = list(it.accumulate([76, 10, 8, 6]))
pop['Kamordah'] = ['human', 'halfling', 'dwarf', 'other']
popw['Kamordah'] = list(it.accumulate([58, 23, 13, 6]))
pop['Talonstadt'] = ['dragonborn', 'human', 'halfling', 'other']
popw['Talonstadt'] = list(it.accumulate([82, 11, 4, 3]))
pop['Trostenwald'] = ['human', 'halfling', 'half-elf', 'other']
popw['Trostenwald'] = list(it.accumulate([66, 13, 8, 13]))
pop['Vol\'antim'] = ['aarakocra', 'other']
popw['Vol\'antim'] = list(it.accumulate([96, 4]))
pop['Zadash'] = ['human', 'halfling', 'dwarf', 'other']
popw['Zadash'] = list(it.accumulate([70, 11, 9, 10]))

# Zemni Fields Settlements
s_zf = [['Blumenthal',          'Town',             3850,   'Dwendalian Empire'],
        ['Bysaes Tyl',          'City',             19090,  'Dwendalian Empire'],
        ['Druvenlode',          'City',             12110,  'Dwendalian Empire'],
        ['Icehaven',            'Town',             5090,   'Dwendalian Empire'],
        ['Nogvurot',            'City',             15270,  'Dwendalian Empire'],
        ['Odessloe',            'City',             6970,   'Dwendalian Empire'],
        ['Pride\'s Call',       'City',             16090,  'Dwendalian Empire'],
        ['Rexxentrum',          'City',             205200, 'Dwendalian Empire'],
        ['Rockguard Garrison',  'Military outpost', 6800,   'Dwendalian Empire'],
        ['Velvin Thicket',      'Nomadic diaspora', 850,    'Velvins'],
        ['Yrrosa',              'Town',             3220,   'Dwendalian Empire']]
s_zfw = [1, 7, 11, 13, 18, 20, 26, 96, 98, 99, 100]

# Zemni Fields Settlement Populations
pop['Blumenthal'] = ['human', 'dwarf', 'elf', 'other']
popw['Blumenthal'] = list(it.accumulate([71, 12, 11, 6]))
pop['Bysaes Tyl'] = ['elf', 'human', 'other']
popw['Bysaes Tyl'] = list(it.accumulate([83, 7, 10]))
pop['Druvenlode'] = ['human', 'dwarf', 'elf', 'other']
popw['Druvenlode'] = list(it.accumulate([70, 14, 9, 7]))
pop['Icehaven'] = ['human', 'elf', 'dwarf', 'other']
popw['Ivehaven'] = list(it.accumulate([71, 12, 10, 7]))
pop['Nogvurot'] = ['human', 'dwarf', 'elf', 'other']
popw['Nogvurot'] = list(it.accumulate([70, 17, 8, 5]))
pop['Odessloe'] = ['human', 'elf', 'dwarf', 'other']
popw['Odessloe'] = list(it.accumulate([73, 12, 8, 7]))
pop['Pride\'s Call'] = ['dwarf', 'human', 'halfling', 'other']
popw['Pride\'s Call'] = list(it.accumulate([81, 8, 6, 5]))
pop['Rexxentrum'] = ['human', 'dwarf', 'halfling', 'other']
popw['Rexxentrum'] = list(it.accumulate([81, 8, 6, 5]))
pop['Rockguard Garrison'] = ['human', 'halfling', 'dwarf', 'other']
popw['Rockguard Garrison'] = list(it.accumulate([71, 12, 12, 5]))
pop['Velvin Thicket'] = ['gnome', 'other']
popw['Velvin Thicket'] = list(it.accumulate([98, 2]))
pop['Yrrosa'] = ['human', 'dwarf', 'elf', 'other']
popw['Yrrosa'] = list(it.accumulate([54, 28, 14, 4]))

# Greying Wildlands Settlements
s_gw = [['Boroftkrah',          'Town',    3060,  'Boroftkrah'],
        ['Palebank Village',    'Village', 690,   'Uthodurn'],
        ['Shadycreek Run',      'City',    14770, 'Tribes of Shadycreek Run'],
        ['Uthodurn',            'City',    26240, 'Uthodurn']]
s_gww = [3, 6, 30, 100]

# Greying Wildlands Settlement Populations
pop['Boroftkrah'] = ['orc', 'half-orc', 'other']
popw['Boroftkrah'] = list(it.accumulate([70, 17, 13]))
pop['Palebank Village'] = ['dwarf', 'elf', 'gnome', 'other']
popw['Palebank Village'] = list(it.accumulate([61, 32, 3, 4]))
pop['Shadycreek Run'] = ['human', 'elf', 'dwarf', 'other']
popw['Shadycreek Run'] = list(it.accumulate([56, 15, 14, 15]))
pop['Uthodurn'] = ['dwarf', 'elf', 'gnome', 'other']
popw['Uthodurn'] = list(it.accumulate([56, 36, 4, 4]))

# Eiselcross Settlements
s_ec = [['Allowak\'s Sanctuary', 'Village', 532, 'Allowak\'s Sanctuary'],
        ['Balenpost',            'Outpost', 205, 'Cerberus Assembly'],
        ['Syrinlya',             'Outpost', 182, 'Uthodurn'],
        ['Tomb of the Worm',     'Village', 345, 'Cult of Quajath'],
        ['Vurmas',               'Outpost', 193, 'Kryn Dynasty']]
s_ecw = [1, 2, 3, 4, 5]

# Eiselcross Settlement Populations
pop['Allowak\'s Sanctuary'] = ['yeti']
popw['Allowak\'s Sanctuary'] = list(it.accumulate([100]))
pop['Balenpost'] = ['human', 'halfling', 'gnome', 'dragonborn', 'other']
popw['Balenpost'] = list(it.accumulate([69, 11, 7, 7, 6]))
pop['Syrinlya'] = ['dwarf', 'elf', 'other']
popw['Syrinlya'] = list(it.accumulate([72, 24, 4]))
pop['Tomb of the Worm'] = ['human', 'halfling']
popw['Tomb of the Worm'] = list(it.accumulate([83, 17]))
pop['Vurmas'] = ['drow', 'orc', 'gnoll', 'other']
popw['Vurmas'] = list(it.accumulate([51, 23, 14, 12]))

# Eastern Wynandir Settlements
s_ew = [['Asarius',                 'City',             48025,  'Kryn Dynasty'],
        ['Bazzoxan',                'Town',             2610,   'Kryn Dynasty'],
        ['Charis',                  'Village',          950,    'Charis'],
        ['Igrathad',                'Seven villages',   6750,   'Kryn Dynasty'],
        ['Jigow',                   'City',             13210,  'Kryn Dynasty'],
        ['New Haxon',               'Military Outpost', 1250,   'Cerberus Assembly'],
        ['Rosohna (Ghor Dranas)',   'City',             113190, 'Kryn Dynasty'],
        ['Rotthold',                'City',             8800,   'Rotthold'],
        ['Urzin',                   'Town',             5930,   'Kryn Dynasty'],
        ['Xarzith Kitril',          'City',             9110,   'Xarzith Kitril']]
s_eww = [20, 21, 22, 30, 36, 37, 89, 93, 96, 100]

# Eastern Wynandir Settlement Populations
pop['Asarius'] = ['goblin', 'hobgoblin', 'bugbear', 'gnoll', 'drow', 'other']
popw['Asarius'] = list(it.accumulate([13.7, 13.6, 13.7, 32, 10, 17]))
pop['Bazzoxan'] = ['drow', 'goblin', 'hobgoblin', 'bugbear', 'other']
popw['Bazzoxan'] = list(it.accumulate([81, 2.7, 2.6, 2.7, 11]))
pop['Charis'] = ['dragonborn', 'halfling', 'other']
popw['Charis'] = list(it.accumulate([53, 41, 6]))
pop['Jigow'] = ['goblin', 'hobgoblin', 'bugbear', 'orc', 'other']
popw['Jigow'] = list(it.accumulate([18.7, 18.6, 18.7, 31, 13]))
pop['Igrathad'] = ['goblin', 'hobgoblin', 'bugbear', 'orc', 'human', 'other']
popw['Igrathad'] = list(it.accumulate([13.7, 13.6, 13.7, 19, 15, 25]))
pop['New Haxon'] = ['human', 'dragonborn', 'other']
popw['New Haxon'] = list(it.accumulate([70, 20, 10]))
pop['Rosohna (Ghor Dranas)'] = ['drow', 'goblin', 'duergar', 'other']
popw['Rosohna (Ghor Dranas)'] = list(it.accumulate([66, 9, 7, 18]))
pop['Rotthold'] = ['human', 'drow', 'goblin', 'tiefling', 'hollow one', 'other']
popw['Rotthold'] = list(it.accumulate([30, 15, 15, 15, 5, 20]))
pop['Urzin'] = ['goblin', 'hobgoblin', 'bugbear', 'gnoll', 'orc', 'other']
popw['Urzin'] = list(it.accumulate([20.7, 20.6, 20.7, 21, 10, 7]))
pop['Xarzith Kitril'] = ['dragonborn', 'other']
popw['Xarzith Kitril'] = list(it.accumulate([93, 7]))

# Dict of all settlements
all_s = {}
all_s['Menagerie Coast'] = [s_mc, s_mcw]
all_s['Marrow Valley'] = [s_mv, s_mvw]
all_s['Zemni Fields'] = [s_zf, s_zfw]
all_s['Greying Wildlands'] = [s_gw, s_gww]
all_s['Eiselcross'] = [s_ec, s_ecw]
all_s['Xhorhas'] = [s_ew, s_eww]

# List of all possible character races
races = ['aarakocra',
         'aasimar',
         'bugbear',
         'centaur',
         'changeling',
         'draonborn',
         'dwarf',
         'elf',
         'firbolg',
         'genasi',
         'gith',
         'gnome',
         'goblin',
         'goliath',
         'grung',
         'half-elf',
         'half-orc',
         'halfling',
         'hobgoblin',
         'human',
         'kalashtar',
         'kenku',
         'kobold',
         'leonin',
         'lizardfolk',
         'loxodon',
         'minotaur',
         'orc',
         'satyr',
         'shifter',
         'simic hybrid',
         'tabaxi',
         'tiefling',
         'tortle',
         'triton',
         'vedalken',
         'verdan',
         'warforged',
         'yuan-ti pureblood']

#%% Define helper functions

def choose_region():
    region = rng.choices(hl, cum_weights=hlw)[0]
    return region

def choose_settlement(region=choose_region()):
    if region == 'Menagerie Coast':
        settlement = rng.choices(s_mc, cum_weights=s_mcw)[0]
    elif region == 'Marrow Valley':
        settlement = rng.choices(s_mv, cum_weights=s_mvw)[0]
    elif region == 'Zemni Fields':
        settlement = rng.choices(s_zf, cum_weights=s_zfw)[0]
    elif region == 'Greying Wildlands':
        settlement = rng.choices(s_gw, cum_weights=s_gww)[0]
    elif region == 'Xhorhas':
        settlement = rng.choices(s_ew, cum_weights=s_eww)[0]
    elif region == 'Eiselcross':
        settlement = rng.choices(s_ec, cum_weights=s_ecw)[0]
    return settlement

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

#%% Define character object class

class Character:
    def __init__(self, **preset ):
        if 'homeland' in preset:
            self.homeland = preset['homeland']
        else:
            self.homeland = choose_region()
        
        if 'background' in preset:
            self.background = preset['background']
        else:
            self.background = rng.choices(bg, cum_weights=bgw)[0]
        
        if 'ally' in preset:
            self.ally = preset('ally')
        else:
            if self.background == 'Acolyte':
                if self.homeland == 'Menagerie Coast':
                    self.ally = True
                elif (self.homeland == 'Marrow Valley') or (self.homeland == 'Zemni Fields'):
                    self.ally = rng.choice([True, False])[0]
                elif self.homeland == 'Greying Wildlands':
                    self.ally = False
                elif self.homeland == 'Xhorhas':
                    self.ally = True
                else:
                    self.ally = False
            elif self.background == 'Acolyte (Luxonborn)':
                if self.homeland == 'Menagerie Coast':
                    self.ally = False
                elif (self.homeland == 'Marrow Valley') or (self.homeland == 'Zemni Fields'):
                    self.ally = False
                elif self.homeland == 'Greying Wildlands':
                    self.ally = False
                elif self.homeland == 'Xhorhas':
                    self.ally = True
                else:
                    self.ally = False
            elif self.background == 'Charlatan':
                if self.homeland == 'Menagerie Coast':
                    self.ally = True
                elif (self.homeland == 'Marrow Valley') or (self.homeland == 'Zemni Fields'):
                    self.ally = False
                elif self.homeland == 'Greying Wildlands':
                    self.ally = True
                elif self.homeland == 'Xhorhas':
                    self.ally = False
                else:
                    self.ally = False
            elif self.background == 'Criminal':
                if self.homeland == 'Menagerie Coast':
                    self.ally = False
                elif (self.homeland == 'Marrow Valley') or (self.homeland == 'Zemni Fields'):
                    self.ally = False
                elif self.homeland == 'Greying Wildlands':
                    self.ally = True
                elif self.homeland == 'Xhorhas':
                    self.ally = False
                else:
                    self.ally = False
            elif self.background == 'Criminal (Myriad Operative)':
                if self.homeland == 'Menagerie Coast':
                    self.ally = False
                elif (self.homeland == 'Marrow Valley') or (self.homeland == 'Zemni Fields'):
                    self.ally = True
                elif self.homeland == 'Greying Wildlands':
                    self.ally = True
                elif self.homeland == 'Xhorhas':
                    self.ally = False
                else:
                    self.ally = False
            elif self.background == 'Entertainer':
                if self.homeland == 'Menagerie Coast':
                    self.ally = True
                elif (self.homeland == 'Marrow Valley') or (self.homeland == 'Zemni Fields'):
                    self.ally = True
                elif self.homeland == 'Greying Wildlands':
                    self.ally = False
                elif self.homeland == 'Xhorhas':
                    self.ally = True
                else:
                    self.ally = False
            elif self.background == 'Folk Hero':
                if self.homeland == 'Menagerie Coast':
                    self.ally = True
                elif (self.homeland == 'Marrow Valley') or (self.homeland == 'Zemni Fields'):
                    self.ally = False
                elif self.homeland == 'Greying Wildlands':
                    self.ally = False
                elif self.homeland == 'Xhorhas':
                    self.ally = True
                else:
                    self.ally = False
            elif self.background == 'Grinner':
                if self.homeland == 'Menagerie Coast':
                    self.ally = True
                elif (self.homeland == 'Marrow Valley') or (self.homeland == 'Zemni Fields'):
                    self.ally = False
                elif self.homeland == 'Greying Wildlands':
                    self.ally = False
                elif self.homeland == 'Xhorhas':
                    self.ally = False
                else:
                    self.ally = False
            elif self.background == 'Guild Artisan':
                if self.homeland == 'Menagerie Coast':
                    self.ally = False
                elif (self.homeland == 'Marrow Valley') or (self.homeland == 'Zemni Fields'):
                    self.ally = True
                elif self.homeland == 'Greying Wildlands':
                    self.ally = False
                elif self.homeland == 'Xhorhas':
                    self.ally = True
                else:
                    self.ally = False
            elif self.background == 'Hermit':
                if self.homeland == 'Menagerie Coast':
                    self.ally = False
                elif (self.homeland == 'Marrow Valley') or (self.homeland == 'Zemni Fields'):
                    self.ally = False
                elif self.homeland == 'Greying Wildlands':
                    self.ally = True
                elif self.homeland == 'Xhorhas':
                    self.ally = True
                else:
                    self.ally = False
            elif self.background == 'Noble':
                if self.homeland == 'Menagerie Coast':
                    self.ally = True
                elif (self.homeland == 'Marrow Valley') or (self.homeland == 'Zemni Fields'):
                    self.ally = True
                elif self.homeland == 'Greying Wildlands':
                    self.ally = False
                elif self.homeland == 'Xhorhas':
                    self.ally = True
                else:
                    self.ally = False
            elif self.background == 'Outlander':
                if self.homeland == 'Menagerie Coast':
                    self.ally = False
                elif (self.homeland == 'Marrow Valley') or (self.homeland == 'Zemni Fields'):
                    self.ally = False
                elif self.homeland == 'Greying Wildlands':
                    self.ally = True
                elif self.homeland == 'Xhorhas':
                    self.ally = False
                else:
                    self.ally = False
            elif self.background == 'Sage':
                if self.homeland == 'Menagerie Coast':
                    self.ally = False
                elif (self.homeland == 'Marrow Valley') or (self.homeland == 'Zemni Fields'):
                    self.ally = False
                elif self.homeland == 'Greying Wildlands':
                    self.ally = False
                elif self.homeland == 'Xhorhas':
                    self.ally = True
                else:
                    self.ally = False
            elif self.background == 'Sage (Cobalt Scholar)':
                if self.homeland == 'Menagerie Coast':
                    self.ally = True
                elif (self.homeland == 'Marrow Valley') or (self.homeland == 'Zemni Fields'):
                    self.ally = True
                elif self.homeland == 'Greying Wildlands':
                    self.ally = True
                elif self.homeland == 'Xhorhas':
                    self.ally = False
                else:
                    self.ally = False
            elif self.background == 'Sailor':
                if self.homeland == 'Menagerie Coast':
                    self.ally = True
                elif (self.homeland == 'Marrow Valley') or (self.homeland == 'Zemni Fields'):
                    self.ally = False
                elif self.homeland == 'Greying Wildlands':
                    self.ally = False
                elif self.homeland == 'Xhorhas':
                    self.ally = True
                else:
                    self.ally = False
            elif self.background == 'Sailor (Revelry pirate)':
                if self.homeland == 'Menagerie Coast':
                    self.ally = True
                elif (self.homeland == 'Marrow Valley') or (self.homeland == 'Zemni Fields'):
                    self.ally = False
                elif self.homeland == 'Greying Wildlands':
                    self.ally = True
                elif self.homeland == 'Xhorhas':
                    self.ally = False
                else:
                    self.ally = False
            elif self.background == 'Soldier':
                if self.homeland == 'Menagerie Coast':
                    self.ally = True
                elif (self.homeland == 'Marrow Valley') or (self.homeland == 'Zemni Fields'):
                    self.ally = True
                elif self.homeland == 'Greying Wildlands':
                    self.ally = False
                elif self.homeland == 'Xhorhas':
                    self.ally = True
                else:
                    self.ally = False
            elif self.background == 'Spy (Augen Trust)':
                if self.homeland == 'Menagerie Coast':
                    self.ally = False
                elif (self.homeland == 'Marrow Valley') or (self.homeland == 'Zemni Fields'):
                    self.ally = True
                elif self.homeland == 'Greying Wildlands':
                    self.ally = False
                elif self.homeland == 'Xhorhas':
                    self.ally = False
                else:
                    self.ally = False
            elif self.background == 'Urchin':
                if self.homeland == 'Menagerie Coast':
                    self.ally = True
                elif (self.homeland == 'Marrow Valley') or (self.homeland == 'Zemni Fields'):
                    self.ally = False
                elif self.homeland == 'Greying Wildlands':
                    self.ally = False
                elif self.homeland == 'Xhorhas':
                    self.ally = False
                else:
                    self.ally = False
            elif self.background == 'Volstrucker Agent':
                if self.homeland == 'Menagerie Coast':
                    self.ally = False
                elif (self.homeland == 'Marrow Valley') or (self.homeland == 'Zemni Fields'):
                    self.ally = True
                elif self.homeland == 'Greying Wildlands':
                    self.ally = False
                elif self.homeland == 'Xhorhas':
                    self.ally = False
                else:
                    self.ally = False
            else:
                self.ally = False
            
        if 'rival' in preset:
            self.rival = preset('rival')
        else:
            if self.background == 'Acolyte':
                if self.homeland == 'Menagerie Coast':
                    self.rival = False
                elif (self.homeland == 'Marrow Valley') or (self.homeland == 'Zemni Fields'):
                    self.rival = not self.ally
                elif self.homeland == 'Greying Wildlands':
                    self.rival = True
                elif self.homeland == 'Xhorhas':
                    self.rival = False
                else:
                    self.rival = False
            elif self.background == 'Acolyte (Luxonborn)':
                if self.homeland == 'Menagerie Coast':
                    self.rival = False
                elif (self.homeland == 'Marrow Valley') or (self.homeland == 'Zemni Fields'):
                    self.rival = True
                elif self.homeland == 'Greying Wildlands':
                    self.rival = False
                elif self.homeland == 'Xhorhas':
                    self.rival = False
                else:
                    self.rival = False
            elif self.background == 'Charlatan':
                if self.homeland == 'Menagerie Coast':
                    self.rival = False
                elif (self.homeland == 'Marrow Valley') or (self.homeland == 'Zemni Fields'):
                    self.rival = True
                elif self.homeland == 'Greying Wildlands':
                    self.rival = False
                elif self.homeland == 'Xhorhas':
                    self.rival = True
                else:
                    self.rival = False
            elif self.background == 'Criminal':
                if self.homeland == 'Menagerie Coast':
                    self.rival = True
                elif (self.homeland == 'Marrow Valley') or (self.homeland == 'Zemni Fields'):
                    self.rival = True
                elif self.homeland == 'Greying Wildlands':
                    self.rival = False
                elif self.homeland == 'Xhorhas':
                    self.rival = True
                else:
                    self.rival = False
            elif self.background == 'Criminal (Myriad Operative)':
                if self.homeland == 'Menagerie Coast':
                    self.rival = True
                elif (self.homeland == 'Marrow Valley') or (self.homeland == 'Zemni Fields'):
                    self.rival = False
                elif self.homeland == 'Greying Wildlands':
                    self.rival = True
                elif self.homeland == 'Xhorhas':
                    self.rival = False
                else:
                    self.rival = False
            elif self.background == 'Entertainer':
                if self.homeland == 'Menagerie Coast':
                    self.rival = False
                elif (self.homeland == 'Marrow Valley') or (self.homeland == 'Zemni Fields'):
                    self.rival = False
                elif self.homeland == 'Greying Wildlands':
                    self.rival = True
                elif self.homeland == 'Xhorhas':
                    self.rival = False
                else:
                    self.rival = False
            elif self.background == 'Folk Hero':
                if self.homeland == 'Menagerie Coast':
                    self.rival = False
                elif (self.homeland == 'Marrow Valley') or (self.homeland == 'Zemni Fields'):
                    self.rival = True
                elif self.homeland == 'Greying Wildlands':
                    self.rival = True
                elif self.homeland == 'Xhorhas':
                    self.rival = False
                else:
                    self.rival = False
            elif self.background == 'Grinner':
                if self.homeland == 'Menagerie Coast':
                    self.rival = False
                elif (self.homeland == 'Marrow Valley') or (self.homeland == 'Zemni Fields'):
                    self.rival = True
                elif self.homeland == 'Greying Wildlands':
                    self.rival = False
                elif self.homeland == 'Xhorhas':
                    self.rival = False
                else:
                    self.rival = False
            elif self.background == 'Guild Artisan':
                if self.homeland == 'Menagerie Coast':
                    self.rival = True
                elif (self.homeland == 'Marrow Valley') or (self.homeland == 'Zemni Fields'):
                    self.rival = False
                elif self.homeland == 'Greying Wildlands':
                    self.rival = False
                elif self.homeland == 'Xhorhas':
                    self.rival = False
                else:
                    self.rival = False
            elif self.background == 'Hermit':
                if self.homeland == 'Menagerie Coast':
                    self.rival = False
                elif (self.homeland == 'Marrow Valley') or (self.homeland == 'Zemni Fields'):
                    self.rival = True
                elif self.homeland == 'Greying Wildlands':
                    self.rival = False
                elif self.homeland == 'Xhorhas':
                    self.rival = False
                else:
                    self.rival = False
            elif self.background == 'Noble':
                if self.homeland == 'Menagerie Coast':
                    self.rival = False
                elif (self.homeland == 'Marrow Valley') or (self.homeland == 'Zemni Fields'):
                    self.rival = True
                elif self.homeland == 'Greying Wildlands':
                    self.rival = True
                elif self.homeland == 'Xhorhas':
                    self.rival = True
                else:
                    self.rival = False
            elif self.background == 'Outlander':
                if self.homeland == 'Menagerie Coast':
                    self.rival = False
                elif (self.homeland == 'Marrow Valley') or (self.homeland == 'Zemni Fields'):
                    self.rival = False
                elif self.homeland == 'Greying Wildlands':
                    self.rival = False
                elif self.homeland == 'Xhorhas':
                    self.rival = False
                else:
                    self.rival = False
            elif self.background == 'Sage':
                if self.homeland == 'Menagerie Coast':
                    self.rival = True
                elif (self.homeland == 'Marrow Valley') or (self.homeland == 'Zemni Fields'):
                    self.rival = True
                elif self.homeland == 'Greying Wildlands':
                    self.rival = False
                elif self.homeland == 'Xhorhas':
                    self.rival = True
                else:
                    self.rival = False
            elif self.background == 'Sage (Cobalt Scholar)':
                if self.homeland == 'Menagerie Coast':
                    self.rival = False
                elif (self.homeland == 'Marrow Valley') or (self.homeland == 'Zemni Fields'):
                    self.rival = True
                elif self.homeland == 'Greying Wildlands':
                    self.rival = False
                elif self.homeland == 'Xhorhas':
                    self.rival = True
                else:
                    self.rival = False
            elif self.background == 'Sailor':
                if self.homeland == 'Menagerie Coast':
                    self.rival = True
                elif (self.homeland == 'Marrow Valley') or (self.homeland == 'Zemni Fields'):
                    self.rival = False
                elif self.homeland == 'Greying Wildlands':
                    self.rival = True
                elif self.homeland == 'Xhorhas':
                    self.rival = False
                else:
                    self.rival = False
            elif self.background == 'Sailor (Revelry pirate)':
                if self.homeland == 'Menagerie Coast':
                    self.rival = True
                elif (self.homeland == 'Marrow Valley') or (self.homeland == 'Zemni Fields'):
                    self.rival = False
                elif self.homeland == 'Greying Wildlands':
                    self.rival = False
                elif self.homeland == 'Xhorhas':
                    self.rival = False
                else:
                    self.rival = False
            elif self.background == 'Soldier':
                if self.homeland == 'Menagerie Coast':
                    self.rival = False
                elif (self.homeland == 'Marrow Valley') or (self.homeland == 'Zemni Fields'):
                    self.rival = True
                elif self.homeland == 'Greying Wildlands':
                    self.rival = True
                elif self.homeland == 'Xhorhas':
                    self.rival = True
                else:
                    self.rival = False
            elif self.background == 'Spy (Augen Trust)':
                if self.homeland == 'Menagerie Coast':
                    self.rival = False
                elif (self.homeland == 'Marrow Valley') or (self.homeland == 'Zemni Fields'):
                    self.rival = False
                elif self.homeland == 'Greying Wildlands':
                    self.rival = False
                elif self.homeland == 'Xhorhas':
                    self.rival = True
                else:
                    self.rival = False
            elif self.background == 'Urchin':
                if self.homeland == 'Menagerie Coast':
                    self.rival = False
                elif (self.homeland == 'Marrow Valley') or (self.homeland == 'Zemni Fields'):
                    self.rival = True
                elif self.homeland == 'Greying Wildlands':
                    self.rival = True
                elif self.homeland == 'Xhorhas':
                    self.rival = True
                else:
                    self.rival = False
            elif self.background == 'Volstrucker Agent':
                if self.homeland == 'Menagerie Coast':
                    self.rival = False
                elif (self.homeland == 'Marrow Valley') or (self.homeland == 'Zemni Fields'):
                    self.rival = False
                elif self.homeland == 'Greying Wildlands':
                    self.rival = False
                elif self.homeland == 'Xhorhas':
                    self.rival = True
                else:
                    self.rival = False
            else:
                self.rival = False
            
        if 'settlement' in preset:
            for x in all_s[self.homeland][0][:][0]
            self.settlement = preset['settlement']
        else:
            self.settlement = choose_settlement(region=self.homeland)
            
        self.hometownname = self.settlement[0]
        self.hometownsize = self.settlement[1]
        self.hometownpop = self.settlement[2]
        self.government = self.settlement[3]
        
        if 'resettled' in preset:
            self.resettled = preset['resettled']
        else:
            self.resettled = rng.choices([False, True], cum_weights=[75, 100])[0]
        
        if self.resettled:
            # character has resettled from land of birth
            self.birthland = choose_region()
            if 'birthsettlement' in preset:
                self.birthsettlement = preset['birthsettlement']
            else:
                self.settlement = choose_settlement(region=self.birthland)
            self.birthtownname = self.birthsettlement[0]
            self.birthtownsize = self.birthsettlement[1]
            self.birthtownpop = self.birthsettlement[2]
            self.birthgovernment = self.birthsettlement[3]
        else:
            # character grew up in land of birth
            self.birthland = self.homeland
            self.birthgovernment = self.government
            self.birthsettlement = self.settlement
            self.birthtownname = self.hometownname
            self.birthtownsize = self.hometownsize
            self.birthtownpop = self.hometownpop
    
        if 'race' in preset:
            self.race = preset['race']
            if self.race == 'other':
                self.race = choose_race(settlement=self.birthtownname,
                                        presetrace=self.race)
        else:
            self.race = choose_race(settlement=self.birthtownname)
    
    def narrate(self):
        text = 'I am a '
        text += self.race + ' ' + self.background + ',\n'
        text += 'who was born in the '
        text += self.birthtownsize + ' of ' + self.birthtownname + ', '
        if self.birthland == 'Menagerie Coast':
            text += 'on the '
        elif self.birthland == 'Xhorhas':
            text += 'in '
        else:
            text += 'in the '
        text += self.birthland + ',\n'
        if self.birthtownname != self.hometownname:
            text += 'and grew up in '
            text += self.hometownname + ',\n'
            text += 'in the region of '
            text += self.homeland + ',\n'
        text += 'under the rule of the '
        text += self.government + '.'
        print(text)
    
        
        