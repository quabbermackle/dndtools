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

#%% Define tables and weights

# Homelands
hldict = {}
hldict['Menagerie Coast']   = 21
hldict['Marrow Valley']     = 40
hldict['Zemni Fields']      = 72
hldict['Greying Wildlands'] = 77
hldict['Xhorhas']           = 100
hldict['Eiselcross']        = 101
hl = list(hldict.keys())
hlw = list(hldict.values())

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
s_mcdict = {}
s_mcdict['Brokenbank']  = {'w':1,   'size':'Town', 'pop':1520,  'gov':'Clovis Concord'}
s_mcdict['Darktow']     = {'w':2,   'size':'Town', 'pop':1306,  'gov':'Revelry pirates'}
s_mcdict['Feolinn']     = {'w':9,   'size':'City', 'pop':12700, 'gov':'Clovis Concord'}
s_mcdict['Gwardan']     = {'w':19,  'size':'City', 'pop':18900, 'gov':'Clovis Concord'}
s_mcdict['Nicodranas']  = {'w':36,  'size':'City', 'pop':31900, 'gov':'Clovis Concord'}
s_mcdict['Othe']        = {'w':40,  'size':'City', 'pop':8320,  'gov':'Clovis Concord'}
s_mcdict['Palma Flora'] = {'w':41,  'size':'Town', 'pop':1780,  'gov':'Clovis Concord'}
s_mcdict['Port Damali'] = {'w':84,  'size':'City', 'pop':82110, 'gov':'Clovis Concord'}
s_mcdict['Port Zoon']   = {'w':93,  'size':'City', 'pop':19120, 'gov':'Clovis Concord'}
s_mcdict['Tussoa']      = {'w':100, 'size':'City', 'pop':15110, 'gov':'Clovis Concord'}
s_mc = list()
s_mcw = list()
for x in s_mcdict:
    s_mc += [[x, s_mcdict[x]['size'], s_mcdict[x]['pop'], s_mcdict[x]['gov']]]
    s_mcw += [s_mcdict[x]['w']]

# Menagerie Coast Settlement Populations
pop = {}
popw = {}
pop['Brokenbank']   = ['human', 'tabaxi',   'dwarf',    'other']
pop['Darktow']      = ['human', 'elf',      'dwarf',    'other']
pop['Feolinn']      = ['human', 'elf',      'gnome',    'other']
pop['Gwardan']      = ['elf',   'human',    'gnome',    'other']
pop['Nicodranas']   = ['human', 'halfling', 'dwarf',    'other']
pop['Othe']         = ['human', 'halfling', 'half-orc', 'other']
pop['Palma Flora']  = ['human', 'halfling', 'dwarf',    'other']
pop['Port Damali']  = ['human', 'halfling', 'elf',      'other']
pop['Port Zoon']    = ['human', 'halfling', 'other']
pop['Tussoa']       = ['human', 'elf',      'halfling', 'other']
popw['Brokenbank']  = list(it.accumulate([74, 9,  6,  11]))
popw['Darktow']     = list(it.accumulate([61, 12, 9,  18]))
popw['Feolinn']     = list(it.accumulate([73, 10, 5,  12]))
popw['Gwardan']     = list(it.accumulate([63, 16, 11, 10]))
popw['Nicodranas']  = list(it.accumulate([68, 13, 8,  10]))
popw['Othe']        = list(it.accumulate([64, 16, 11, 9]))
popw['Palma Flora'] = list(it.accumulate([68, 13, 11, 8]))
popw['Port Damali'] = list(it.accumulate([51, 16, 15, 18]))
popw['Port Zoon']   = list(it.accumulate([80, 7,  13]))
popw['Tussoa']      = list(it.accumulate([74, 10, 8,  8]))

# Marrow Valley Settlements
s_mvdict = {}
s_mvdict['Alfield']           = {'w':2,   'size':'Town',             'pop':3410,  'gov':'Dwendalian Empire'}
s_mvdict['Ashguard Garrison'] = {'w':5,   'size':'Military outpost', 'pop':5720,  'gov':'Kryn Dynasty'}
s_mvdict['Berleben']          = {'w':7,   'size':'Town',             'pop':3230,  'gov':'Dwendalian Empire'}
s_mvdict['Bladegarden']       = {'w':12,  'size':'City',             'pop':9910,  'gov':'Dwendalian Empire'}
s_mvdict['Deastok']           = {'w':18,  'size':'City',             'pop':10090, 'gov':'Dwendalian Empire'}
s_mvdict['Felderwin']         = {'w':22,  'size':'City',             'pop':8180,  'gov':'Dwendalian Empire'}
s_mvdict['Grimgolir']         = {'w':32,  'size':'City',             'pop':19090, 'gov':'Dwendalian Empire'}
s_mvdict['Hupperdook']        = {'w':40,  'size':'City',             'pop':12090, 'gov':'Dwendalian Empire'}
s_mvdict['Kamordah']          = {'w':44,  'size':'City',             'pop':7440,  'gov':'Dwendalian Empire'}
s_mvdict['Talonstadt']        = {'w':45,  'size':'Town',             'pop':1810,  'gov':'Dwendalian Empire'}
s_mvdict['Trostenwald']       = {'w':50,  'size':'City',             'pop':8900,  'gov':'Dwendalian Empire'}
s_mvdict['Vol\'antim']        = {'w':52,  'size':'Town',             'pop':3890,  'gov':'Vol\'antim'}
s_mvdict['Zadash']            = {'w':100, 'size':'City',             'pop':89210, 'gov':'Dwendalian Empire'}
s_mv = list()
s_mvw = list()
for x in s_mvdict:
    s_mv += [[x, s_mvdict[x]['size'], s_mvdict[x]['pop'], s_mvdict[x]['gov']]]
    s_mvw += [s_mvdict[x]['w']]

# Marrow Valley Settlement Populations
pop['Alfield']            = ['human',      'halfling', 'gnome',      'other']
pop['Ashguard Garrison']  = ['drow',       'other']
pop['Berleben']           = ['human',      'halfling', 'gnome',      'other']
pop['Bladegarden']        = ['half-orc',   'orc',      'human',      'other']
pop['Deastok']            = ['human',      'dwarf',    'halfling',   'other']
pop['Felderwin']          = ['halfling',   'human',    'dragonborn', 'other']
pop['Grimgolir']          = ['dwarf',      'human',    'halfling',   'other']
pop['Hupperdook']         = ['gnome',      'dwarf',    'human',      'other']
pop['Kamordah']           = ['human',      'halfling', 'dwarf',      'other']
pop['Talonstadt']         = ['dragonborn', 'human',    'halfling',   'other']
pop['Trostenwald']        = ['human',      'halfling', 'half-elf',   'other']
pop['Vol\'antim']         = ['aarakocra',  'other']
pop['Zadash']             = ['human',      'halfling', 'dwarf',      'other']
popw['Alfield']           = list(it.accumulate([61, 22, 11, 6]))
popw['Ashguard Garrison'] = list(it.accumulate([74, 26]))
popw['Berleben']          = list(it.accumulate([63, 17, 12, 8]))
popw['Bladegarden']       = list(it.accumulate([32, 21, 25, 22]))
popw['Deastok']           = list(it.accumulate([60, 26, 10, 4]))
popw['Felderwin']         = list(it.accumulate([58, 21, 6,  15]))
popw['Grimgolir']         = list(it.accumulate([81, 8,  6,  5]))
popw['Hupperdook']        = list(it.accumulate([76, 10, 8,  6]))
popw['Kamordah']          = list(it.accumulate([58, 23, 13, 6]))
popw['Talonstadt']        = list(it.accumulate([82, 11, 4,  3]))
popw['Trostenwald']       = list(it.accumulate([66, 13, 8,  13]))
popw['Vol\'antim']        = list(it.accumulate([96, 4]))
popw['Zadash']            = list(it.accumulate([70, 11, 9,  10]))

# Zemni Fields Settlements
s_zfdict = {}
s_zfdict['Blumenthal']         = {'w':1,   'size':'Town',             'pop':3850,   'gov':'Dwendalian Empire'}
s_zfdict['Bysaes Tyl']         = {'w':7,   'size':'City',             'pop':19090,  'gov':'Dwendalian Empire'}
s_zfdict['Druvenlode']         = {'w':11,  'size':'City',             'pop':12110,  'gov':'Dwendalian Empire'}
s_zfdict['Icehaven']           = {'w':13,  'size':'Town',             'pop':5090,   'gov':'Dwendalian Empire'}
s_zfdict['Nogvurot']           = {'w':18,  'size':'City',             'pop':15270,  'gov':'Dwendalian Empire'}
s_zfdict['Odessloe']           = {'w':20,  'size':'City',             'pop':6970,   'gov':'Dwendalian Empire'}
s_zfdict['Pride\'s Call']      = {'w':26,  'size':'City',             'pop':16090,  'gov':'Dwendalian Empire'}
s_zfdict['Rexxentrum']         = {'w':96,  'size':'City',             'pop':205200, 'gov':'Dwendalian Empire'}
s_zfdict['Rockguard Garrison'] = {'w':98,  'size':'Military outpost', 'pop':6800,   'gov':'Dwendalian Empire'}
s_zfdict['Velvin Thicket']     = {'w':99,  'size':'Nomadic diaspora', 'pop':850,    'gov':'Velvin Thicket'}
s_zfdict['Yrrosa']             = {'w':100, 'size':'Town',             'pop':3220,   'gov':'Dwendalian Empire'}
s_zf = list()
s_zfw = list()
for x in s_zfdict:
    s_zf += [[x, s_zfdict[x]['size'], s_zfdict[x]['pop'], s_zfdict[x]['gov']]]
    s_zfw += [s_zfdict[x]['w']]

# Zemni Fields Settlement Populations
pop['Blumenthal']          = ['human', 'dwarf',    'elf',      'other']
pop['Bysaes Tyl']          = ['elf',   'human',    'other']
pop['Druvenlode']          = ['human', 'dwarf',    'elf',      'other']
pop['Icehaven']            = ['human', 'elf',      'dwarf',    'other']
pop['Nogvurot']            = ['human', 'dwarf',    'elf',      'other']
pop['Odessloe']            = ['human', 'elf',      'dwarf',    'other']
pop['Pride\'s Call']       = ['dwarf', 'human',    'halfling', 'other']
pop['Rexxentrum']          = ['human', 'dwarf',    'halfling', 'other']
pop['Rockguard Garrison']  = ['human', 'halfling', 'dwarf',    'other']
pop['Velvin Thicket']      = ['gnome', 'other']
pop['Yrrosa']              = ['human', 'dwarf',    'elf',      'other']
popw['Blumenthal']         = list(it.accumulate([71, 12, 11, 6]))
popw['Bysaes Tyl']         = list(it.accumulate([83, 7,  10]))
popw['Druvenlode']         = list(it.accumulate([70, 14, 9,  7]))
popw['Icehaven']           = list(it.accumulate([71, 12, 10, 7]))
popw['Nogvurot']           = list(it.accumulate([70, 17, 8,  5]))
popw['Odessloe']           = list(it.accumulate([73, 12, 8,  7]))
popw['Pride\'s Call']      = list(it.accumulate([81, 8,  6,  5]))
popw['Rexxentrum']         = list(it.accumulate([81, 8,  6,  5]))
popw['Rockguard Garrison'] = list(it.accumulate([71, 12, 12, 5]))
popw['Velvin Thicket']     = list(it.accumulate([98, 2]))
popw['Yrrosa']             = list(it.accumulate([54, 28, 14, 4]))

# Greying Wildlands Settlements
s_gwdict = {}
s_gwdict['Boroftkrah']       = {'w':3,   'size':'Town',    'pop':3060,  'gov':'Boroftkrah'}
s_gwdict['Palebank Village'] = {'w':6,   'size':'Village', 'pop':690,   'gov':'Uthodurn'}
s_gwdict['Shadycreek Run']   = {'w':30,  'size':'City',    'pop':14770, 'gov':'Tribes of Shadycreek Run'}
s_gwdict['Uthodurn']         = {'w':100, 'size':'City',    'pop':26240, 'gov':'Uthodurn'}
s_gw = list()
s_gww = list()
for x in s_gwdict:
    s_gw += [[x, s_gwdict[x]['size'], s_gwdict[x]['pop'], s_gwdict[x]['gov']]]
    s_gww += [s_gwdict[x]['w']]

# Greying Wildlands Settlement Populations
pop['Boroftkrah']        = ['orc',   'half-orc', 'other']
pop['Palebank Village']  = ['dwarf', 'elf',      'gnome', 'other']
pop['Shadycreek Run']    = ['human', 'elf',      'dwarf', 'other']
pop['Uthodurn']          = ['dwarf', 'elf',      'gnome', 'other']
popw['Boroftkrah']       = list(it.accumulate([70, 17, 13]))
popw['Palebank Village'] = list(it.accumulate([61, 32, 3,  4]))
popw['Shadycreek Run']   = list(it.accumulate([56, 15, 14, 15]))
popw['Uthodurn']         = list(it.accumulate([56, 36, 4,  4]))

# Eiselcross Settlements
s_ecdict = {}
s_ecdict['Allowak\'s Sanctuary'] = {'w':1,  'size':'Village', 'pop':532, 'gov':'Allowak\'s Sanctuary'}
s_ecdict['Balenpost']            = {'w':26, 'size':'Outpost', 'pop':205, 'gov':'Cerberus Assembly'}
s_ecdict['Syrinlya']             = {'w':51, 'size':'Outpost', 'pop':182, 'gov':'Uthodurn'}
s_ecdict['Tomb of the Worm']     = {'w':61, 'size':'Village', 'pop':345, 'gov':'Cult of Quajath'}
s_ecdict['Vurmas']               = {'w':86, 'size':'Outpost', 'pop':193, 'gov':'Kryn Dynasty'}
# s_ecw = list(it.accumulate([1, 25, 25, 10, 25]))
s_ec = list()
s_ecw = list()
for x in s_ecdict:
    s_ec += [[x, s_ecdict[x]['size'], s_ecdict[x]['pop'], s_ecdict[x]['gov']]]
    s_ecw += [s_ecdict[x]['w']]

# Eiselcross Settlement Populations
pop['Allowak\'s Sanctuary']  = ['yeti']
pop['Balenpost']             = ['human', 'halfling', 'gnome', 'dragonborn', 'other']
pop['Syrinlya']              = ['dwarf', 'elf',      'other']
pop['Tomb of the Worm']      = ['human', 'halfling']
pop['Vurmas']                = ['drow',  'orc',      'gnoll', 'other']
popw['Allowak\'s Sanctuary'] = list(it.accumulate([100]))
popw['Balenpost']            = list(it.accumulate([69, 11, 7,  7, 6]))
popw['Syrinlya']             = list(it.accumulate([72, 24, 4]))
popw['Tomb of the Worm']     = list(it.accumulate([83, 17]))
popw['Vurmas']               = list(it.accumulate([51, 23, 14, 12]))

# Eastern Wynandir Settlements
s_ewdict = {}
s_ewdict['Asarius']               = {'w':20,  'size':'City',             'pop':48025,  'gov':'Kryn Dynasty'}
s_ewdict['Bazzoxan']              = {'w':21,  'size':'Town',             'pop':2610,   'gov':'Kryn Dynasty'}
s_ewdict['Charis']                = {'w':22,  'size':'Village',          'pop':950,    'gov':'Charis'}
s_ewdict['Igrathad']              = {'w':30,  'size':'Seven villages',   'pop':6750,   'gov':'Kryn Dynasty'}
s_ewdict['Jigow']                 = {'w':36,  'size':'City',             'pop':13210,  'gov':'Kryn Dynasty'}
s_ewdict['New Haxon']             = {'w':37,  'size':'Military Outpost', 'pop':1250,   'gov':'Cerberus Assembly'}
s_ewdict['Rosohna (Ghor Dranas)'] = {'w':89,  'size':'City',             'pop':113190, 'gov':'Kryn Dynasty'}
s_ewdict['Rotthold']              = {'w':93,  'size':'City',             'pop':8800,   'gov':'Rotthold'}
s_ewdict['Urzin']                 = {'w':96,  'size':'Town',             'pop':5930,   'gov':'Kryn Dynasty'}
s_ewdict['Xarzith Kitril']        = {'w':100, 'size':'City',             'pop':9110,   'gov':'Xarzith Kitril'}
s_ew = list()
s_eww = list()
for x in s_ewdict:
    s_ew += [[x, s_ewdict[x]['size'], s_ewdict[x]['pop'], s_ewdict[x]['gov']]]
    s_eww += [s_ewdict[x]['w']]

# Eastern Wynandir Settlement Populations
pop['Asarius']                = ['goblin',     'hobgoblin',  'bugbear',   'gnoll',    'drow',       'other']
pop['Bazzoxan']               = ['drow',       'goblin',     'hobgoblin', 'bugbear',  'other']
pop['Charis']                 = ['dragonborn', 'halfling',   'other']
pop['Jigow']                  = ['goblin',     'hobgoblin',  'bugbear',   'orc',      'other']
pop['Igrathad']               = ['goblin',     'hobgoblin',  'bugbear',   'orc',      'human',      'other']
pop['New Haxon']              = ['human',      'dragonborn', 'other']
pop['Rosohna (Ghor Dranas)']  = ['drow',       'goblin',     'duergar',   'other']
pop['Rotthold']               = ['human',      'drow',       'goblin',    'tiefling', 'hollow one', 'other']
pop['Urzin']                  = ['goblin',     'hobgoblin',  'bugbear',   'gnoll',    'orc',        'other']
pop['Xarzith Kitril']         = ['dragonborn', 'other']
popw['Asarius']               = list(it.accumulate([13.7, 13.6, 13.7, 32,  10, 17]))
popw['Bazzoxan']              = list(it.accumulate([81,   2.7,  2.6,  2.7, 11]))
popw['Charis']                = list(it.accumulate([53,   41,   6]))
popw['Jigow']                 = list(it.accumulate([18.7, 18.6, 18.7, 31,  13]))
popw['Igrathad']              = list(it.accumulate([13.7, 13.6, 13.7, 19,  15, 25]))
popw['New Haxon']             = list(it.accumulate([70,   20,   10]))
popw['Rosohna (Ghor Dranas)'] = list(it.accumulate([66,   9,    7,    18]))
popw['Rotthold']              = list(it.accumulate([30,   15,   15,   15,  5,  20]))
popw['Urzin']                 = list(it.accumulate([20.7, 20.6, 20.7, 21,  10, 7]))
popw['Xarzith Kitril']        = list(it.accumulate([93,   7]))

# Dict of all settlements
all_s = {}
for x in [s_mcdict, s_mvdict, s_zfdict, s_gwdict, s_ecdict, s_ewdict]:
    all_s.update(x)
    
# Dict of all settlements, by region
reg_s = {}
reg_s['Menagerie Coast']   = s_mcdict
reg_s['Marrow Valley']     = s_mvdict
reg_s['Zemni Fields']      = s_zfdict
reg_s['Greying Wildlands'] = s_gwdict
reg_s['Eiselcross']        = s_ecdict
reg_s['Xhorhas']           = s_ewdict

# Dict of settlement weights, by region
reg_sw = {}
reg_sw['Menagerie Coast']   = s_mcw
reg_sw['Marrow Valley']     = s_mvw
reg_sw['Zemni Fields']      = s_zfw
reg_sw['Greying Wildlands'] = s_gww
reg_sw['Eiselcross']        = s_ecw
reg_sw['Xhorhas']           = s_eww

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
        'life was saved by an agent of the Cobalt Soul, who could not cure '
        'the disease, but who gave you a periapt of health that suppresses '
        'it.'),
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
        'you found a treasure map that points toward a place in Wildemount '
        'of the DM\'s choice.'),
        []],
      [('You received a letter revealing that you were the secret child of a '
        'wealthy noble family living in Rexxentrum within the Dwendalian '
        'Empire. They enclosed 100 gp to ensure your safe passage to the '
        'imperial capital, and a signet ring bearing your true family\'s '
        'seal.'),
        []]]
indefmadness = []
lycancurse = ['wereboar', 'wererat', 'werewolf']
lycangift = ['werebear', 'weretiger']
disease = ['cackle fever', 'sewer plague', 'sight rot']

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

#%% Define helper functions

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

#%% Define character object class

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
        if 'ally' in preset:
            self.ally = preset('ally')
        else:
            if self.background == 'Acolyte':
                if self.homeland == 'Menagerie Coast':
                    self.ally = True
                elif (self.homeland == 'Marrow Valley') or (self.homeland == 'Zemni Fields'):
                    self.ally = rng.choice([True, False])
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
            
        # Determine Rival
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
        if self.birthland == 'Menagerie Coast':
            text += 'on the '
        elif (self.birthland == 'Xhorhas') or (self.birthland == 'Eiselcross'):
            text += 'in '
        else:
            text += 'in the '
        text += self.birthland
        if self.birthsettlement != self.settlement:
            text += ', and grew up in the '
            if self.settlement == self.government:
                text += 'independent '
            text += self.hometownsize.lower() + ' of ' + self.settlement + ', '
            if self.homeland == 'Menagerie Coast':
                text += 'on the '
            elif (self.homeland == 'Xhorhas') or (self.homeland == 'Eiselcross'):
                text += 'in '
            else:
                text += 'in the '
            text += self.homeland
        if self.settlement != self.government:
            text += ', under the rule of the '
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
        
        