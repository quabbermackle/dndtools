# -*- coding: utf-8 -*-
"""
Created on Tue Aug 24 14:41:35 2021

@author: Matthew
"""

import treasuretools as tt
from treasuretools import roll

# Encounter Type
encounter = {'Sylvan Forest':['1d12', '1d8'],
             'Monument':[]}

# Sylvan Forest Encounters
sylvanforest = {
        2:['1d1','displacer beast'],
        3:['1d1','gnoll pack lord','2d4','gnolls'],
        4:['1d4','gnolls','2d4','hyenas'],
        5:'A grove of burned trees. A DC 10 Wisdom (Survival) check reveals gnoll tracks.',
        6:['1d1','giant owl'],
        7:'An ivy-covered statue of an elven hero',
        8:{'w':[50, 100], 50:['1d1','dryad'], 100:['1d4','satyrs']},
        9:['1d4','centaurs'],
        10:['2d4','scouts (elves)'],
        11:{'w':[50,100], 50:['2d4','pixies'], 100:['2d4','sprites']},
        12:['1d1','owlbear'],
        13:{'w':[75, 100], 75:['1d4','elk'], 100:['1d1','giant elk']},
        14:['1d4','blink dogs'],
        15:{'berries':'2d4', 'desc':'A magical plant with glowing berries. A creature that ingests a berry becomes invisible for 1 hour, or until it attacks or casts a spell. Once picked a berry loses its magic after 12 hours. Berries regrow at midnight, but if all its berries are picked, the plant becomes nonmagical and grows no more berries.'},
        16:'An elven tune carried on a gentle breeze',
        17:{'w':[75, 100], 75:['1d4','orange faerie dragons'], 100:['1d4','blue faerie dragons']},
        18:['1d1','druid (elf)'],
        19:['1d1','treant'],
        20:['1d1','unicorn']
        }

# Monuments
monument = ['Sealed burial mound',
            'Sealed pyramid',
            'Intact obelisk etched with a warning',
            'Intact obelisk etched with historical lore',
            'Intact obelisk etched with dedication',
            'Intack obelisk etched with religious iconography',
            'Ruined obelisk',
            'Toppled obelisk',
            'Intact statue of a person',
            'Intact statue of a deity',
            'Ruined statue of a person',
            'Ruined statue of a deity',
            'Toppled statue of a person',
            'Toppled statue of a deity',
            'Great stone wall, intact, with tower fortifications spaced at one-mile intervals',
            'Great stone wall in ruins',
            'Great stone arch',
            'Fountain',
            'Intact circle of standing stones',
            'Ruined and toppled circle of standing stones',
            'Totem pole']
'''
monument[5] = monument[6]
monument[7] = monument[8]
monument[9] = monument[10]
monument[11] = monument[13]
monument[12] = monument[13]
monumentw = [1,2,3,4,6,8,10,13,14,15,16,17,18,19,20]
'''

# Weird Locales
locale = ['Dead magic zone (similar to Antimagic Field)',
          'Wild magic zone (roll on the Wild Magic Surge table whenever a spell is cast within the zone)',
          'Boulder carved with talking faces',
          'Crystal cave that mystically answers questions',
          'Ancient tree containing a trapped spirit',
          'Battlefield where lingering fog occasionally assumes humanoid forms',
          'Permanent portal to another plane of existence',
          'Wishing well',
          'Giant crystal shard protruding from the ground',
          'Wrecked ship, which might be nowhere near water',
          'Haunted hill or barrow mound',
          'River ferry guided by a skeletal captain',
          'Field of petrified soldiers or other creatures',
          'Forest of petrified or awakened trees',
          'Canyon containing a dragons\'s graveyard',
          'Floating earth mote with a tower on it']
localew = [2,3,4,5,6,8,10,11,12,13,15,16,17,18,19,20]

# Weather
temp = ['Normal for the season',
        ['1d4x10','degrees colder than normal'],
        ['1d4x10','degrees hotter than normal']]
tempw = [14,17,20]
wind = ['None', 'Light', 'Strong']
windw = [12,17,20]
precipitation = ['None', 'Light rain/snow', 'Heavy rain/snow']
precipitationw = [12,17,20]





