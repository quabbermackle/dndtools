# -*- coding: utf-8 -*-
"""
Created on Mon Aug 23 13:46:31 2021

@author: Matthew

5e DMG Encounter Builder
"""

# combat encounter difficulty
difficulty = {'Easy':  0,
              'Medium':1,
              'Hard':  2,
              'Deadly':3}
dnames = ['Easy', 'Medium', 'Hard', 'Deadly']

# XP threshholds by character level
XPthresholds = {
        '1st': [25,   50,   75,   100],
        '2nd': [50,   100,  150,  200],
        '3rd': [75,   150,  225,  400],
        '4th': [125,  250,  375,  500],
        '5th': [250,  500,  750,  1100],
        '6th': [300,  600,  900,  1400],
        '7th': [350,  750,  1100, 1700],
        '8th': [450,  900,  1400, 2100],
        '9th': [550,  1100, 1600, 2400],
        '10th':[600,  1200, 1900, 2800],
        '11th':[800,  1600, 2400, 3600],
        '12th':[1000, 2000, 3000, 4500],
        '13th':[1100, 2200, 3400, 5100],
        '14th':[1250, 2500, 3800, 5700],
        '15th':[1400, 2800, 4300, 6400],
        '16th':[1600, 3200, 4800, 7200],
        '17th':[2000, 3900, 5900, 8800],
        '18th':[2100, 4200, 6300, 9500],
        '19th':[2400, 4900, 7300, 10900],
        '20th':[2800, 5700, 8500, 12700],}

# Determining the Party's XP Threshold
def partyXPthreshold(chars = '1 1st'):
    # chars has format '# lvl # lvl # lvl'
    members = chars.split(' ')
    num = members[::2]
    for x in range(len(num)): num[x] = int(num[x])
    lvl = members[1::2]
    XP = {}
    for d in dnames:
        _xp = 0
        for x in range(len(num)):
            _xp += num[x]*XPthresholds[lvl[x]][difficulty[d]]
        XP[d] = _xp
    return XP

# XP by CR (Monster Manual)
CR2XP = {'CR 0':  10,
         'CR 1/8':25,
         'CR 1/4':50,
         'CR 1/2':100,
         'CR 1':  200,
         'CR 2':  450,
         'CR 3':  700,
         'CR 4':  1100,
         'CR 5':  1800,
         'CR 6':  2300,
         'CR 7':  2900,
         'CR 8':  3900,
         'CR 9':  5000,
         'CR 10': 5900,
         'CR 11': 7200,
         'CR 12': 8400,
         'CR 13': 10000,
         'CR 14': 11500,
         'CR 15': 13000,
         'CR 16': 15000,
         'CR 17': 18000,
         'CR 18': 20000,
         'CR 19': 22000,
         'CR 20': 25000,
         'CR 21': 33000,
         'CR 22': 41000,
         'CR 23': 50000,
         'CR 24': 62000,
         'CR 25': 75000,
         'CR 26': 90000,
         'CR 27': 105000,
         'CR 28': 120000,
         'CR 29': 135000,
         'CR 30': 155000}

# Monster CR list
# Eberron RFLW
monsterCR = {'Belashyrra':'CR 22',
             'Dyrrn':     'CR 24',
             'Clawfoot':  'CR 1',
             'Fastieth':  'CR 1/4',
             'Dolgaunt':  'CR 3',}

# Monster XP list
monsterXP = {}
for x in monsterCR.keys():
    monsterXP[x] = CR2XP[monsterCR[x]]






















# TEST
print(partyXPthreshold('3 3rd 1 2nd'))
# should print Easy:275, Medium:550, Hard:825, Deadly:1400




