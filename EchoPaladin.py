# standard library imports
import numpy as np
import random as rng
from matplotlib import pyplot as plt

rng.seed()

# import Character Simulator
import CharacterSim as char

# TEST ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# platonic = np.array(['1d4', '1d6', '1d8', '1d12', '1d20'])
# print(char.rollvec(platonic))

# tenfireballs = ['8d6'] * 10
# print(char.rollvec(tenfireballs))

# fireball = '8d6'
# plt.figure()
# char.MCdice(fireball, 50000)

# advantage distributions
# plt.figure()
# plt.subplot(411)
# char.MCdice('1d20', ntrials=10000)
# plt.subplot(412)
# char.MCdice('2d20', ntrials=10000, adv='adv')
# plt.subplot(413)
# char.MCdice('3d20', ntrials=10000, adv='adv')
# plt.subplot(414)
# char.MCdice('2d20', ntrials=10000, adv='dis')

# Echo Paladin
maxlvl = 1
class_progression = [   'Paladin',
                        'Paladin',
                        'Sorceror',
                        'Sorceror',
                        'Sorceror',
                        'Paladin',
                        'Paladin',
                        'Paladin',
                        'Fighter',
                        'Fighter',
                        'Fighter']
ASIs = ['STR', 'CHA', 'CON']
for ilvl in range(1, maxlvl+1):
    EchoPal = char.Character(level         = ilvl,
                             classlvls     = class_progression,
                             stats         = [15, 10, 14, 12, 8, 13],
                             ancestrystats = ['CON', 'STR'],
                             ASIrank       = ASIs,
                             weapon        = 'Greatsword')
    EchoPal.Strength += 2 # level 4 ASI
    print(EchoPal)
    print('STR attack: ', EchoPal.AttackRoll())
    plt.figure()
    char.MCdice(EchoPal.AttackRoll(), 100000)

plt.show()