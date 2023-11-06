# standard library imports
import numpy as np
import random as rng
from matplotlib import pyplot as plt

rng.seed()
#rng = np.random.default_rng()

# CONSTANTS ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

weapondice = {  'Greatsword':   '2d6',
                'Greataxe':     '1d12', }

stdASIs = [4, 8, 12, 16, 19]
ASIperclass = { 'Artificer':stdASIs,
                'Barbarian':stdASIs,
                'Bard':     stdASIs,
                'Cleric':   stdASIs,
                'Druid':    stdASIs,
                'Fighter':  [4, 6, 8, 12, 14, 16, 19],
                'Monk':     stdASIs,
                'Paladin':  stdASIs,
                'Ranger':   stdASIs,
                'Rogue':    [4, 8, 10, 12, 1, 19],
                'Sorceror': stdASIs,
                'Warlock':  stdASIs,
                'Wizard':   stdASIs}

statnames = {   'STR':  'Strength',
                'DEX':  'Dexterity',
                'CON':  'Constitution',
                'INT':  'Intelligence',
                'WIS':  'Wisdom',
                'CHA':  'Charisma'}

# FUNCTIONS ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# vectorize dice-rolling functions
def dice(   sides=6, 
            num=1, 
            reroll=np.array([]), 
            numrerolls=0, 
            adv=None):
    # random roll of n dice with s sides each
    # if result is in list 'reroll', reroll the result once
    # adv = None returns the sum of all dice
    # adv = 'adv' returns only the highest of the dice
    # adv = 'dis' returns only the lowest of the dice
    tot = []
    for _ in range(num): 
        temp = rng.choice(list(range(1, sides+1)))
        attempts = 0
        while temp in reroll and attempts < numrerolls:
            temp = rng.choice(list(range(1, sides+1)))
            attempts +=1
        tot.append(temp)
    if   adv is None:  return np.sum(tot)
    elif adv == 'adv': return np.max(tot)
    elif adv == 'dis': return np.min(tot)

#dicevec = np.vectorize(dice)

def roll(   string='1d6', 
            avgroll=False, 
            maxroll=False, 
            minroll=False, 
            reroll=np.array([]), 
            numrerolls=0, 
            adv=None):
    """
    nds(+/-/xC) string is parsed as
        n dice
        s sides
        plus/minus/times constant C
    avgroll returns the calculated average result
    maxroll returns the maximum possible result
    minroll returns the minimum possible result
    reroll specifies a list of numbers to reroll (note: not factored into avgroll)
    adv = None has no effect
    adv = 'adv' returns only the highest of the dice
    adv = 'dis' returns only the lowest of the dice
    """
    split = string.rpartition('d')
    num = int(split[0])
    sides = split[-1]
    possplit = sides.rpartition('+')
    negsplit = sides.rpartition('-')
    multsplit = sides.rpartition('x')
    
    if possplit[0] != '':
        sides = int(possplit[0])
        if multsplit[0] != '':
            const = int(possplit[-1].rpartition('x')[0])
            mult = int(multsplit[-1])
        else:
            const = int(possplit[-1])
            mult = 1
    elif negsplit[0] != '':
        sides = int(negsplit[0])
        if multsplit[0] != '':
            const = int(negsplit[-1].rpartition('x')[0])
            mult = int(multsplit[-1])
        else:
            const = -int(negsplit[-1])
            mult = 1
    elif multsplit[0] != '':
        sides = int(multsplit[0])
        const = 0
        mult = int(multsplit[-1])
    else:
        sides = int(sides)
        const = 0
        mult = 1
    
    if avgroll:         result = num * (sum(list(range(1,sides+1)))/sides)
    elif maxroll:
        if adv is None: result = num * sides
        else:           result = sides
    elif minroll:   
        if adv is None: result = num
        else:           result = 1
    else:               result = dice(sides=sides, num=num, reroll=reroll, adv=adv)
    
    return (result + const) * mult

rollvec = np.vectorize(roll, excluded=['reroll', 'numrerolls', 'adv'])

def MCdice( dicetoroll='1d6', 
            ntrials=10000, 
            reroll=np.array([]), 
            numrerolls=0, 
            adv=None):
    # roll the specified dice a number of times equal to ntrials
    # plots a histogram of the probability density of the results
    resultdist = rollvec([dicetoroll] * ntrials, reroll=reroll, numrerolls=numrerolls, adv=adv)
    minroll = roll(dicetoroll,minroll=True, adv=adv)
    maxroll = roll(dicetoroll,maxroll=True, adv=adv)
    vals = np.arange(minroll, maxroll+2, 1)
    plt.hist(resultdist, bins=vals, density=True, edgecolor='k')
    return resultdist

# CLASSES ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

class Character():
    def __init__(self, 
                 level          = 1, 
                 classlvls      = ['Fighter'], 
                 stats          = [15,14,13,12,10,8], 
                 ancestrystats  = ['CON','STR'],
                 ASIrank        = ['STR'],
                 weapon         = 'Greatsword'):
        self.level      = level
        self.classlvls  = np.array(classlvls)
        self.ASIrank    = ASIrank
        self.weapon     = weapon
        self.dmgdice    = weapondice[self.weapon]
        
        self.Strength       = stats[0]
        self.Dexterity      = stats[1]
        self.Constitution   = stats[2]
        self.Intelligence   = stats[3]
        self.Wisdom         = stats[4]
        self.Charisma       = stats[5]

        tempmod = []
        if len(ancestrystats) == 2:
            tempmod.append(2)
            tempmod.append(1)
        elif len(ancestrystats) == 3:
            for _ in range(3): tempmod.append(1)
        for idx in range(len(ancestrystats)):
            if   ancestrystats[idx] == 'STR': self.Strength     += tempmod[idx]
            elif ancestrystats[idx] == 'DEX': self.Dexterity    += tempmod[idx]
            elif ancestrystats[idx] == 'CON': self.Constitution += tempmod[idx]
            elif ancestrystats[idx] == 'INT': self.Intelligence += tempmod[idx]
            elif ancestrystats[idx] == 'WIS': self.Wisdom       += tempmod[idx]
            elif ancestrystats[idx] == 'CHA': self.Charisma     += tempmod[idx]

        nASIs = 0
        classes = np.unique(self.classlvls[:self.level])
        print(classes)
        for iclass in classes:
            nclass = sum(self.classlvls == iclass)
            nASIs += sum(nclass >= ASIperclass[iclass])
        while nASIs > 0:
            for iASI in range(len(self.ASIrank)):
                if getattr(self, statnames[self.ASIrank[iASI]]) <= 18:
                    setattr(self,
                            statnames[self.ASIrank[iASI]], 
                            getattr(self, statnames[self.ASIrank[iASI]]) + 2)
                    nASIs -= 1
                    continue

    def prof(self):
        # return proficiency bonus based on level
        if self.level < 5:
            return 2
        elif self.level < 9:
            return 3
        elif self.level < 13:
            return 4
        elif self.level < 17:
            return 5
        else: return 6

    def STR(self): return int(np.floor((self.Strength     - 10)/2))
    def DEX(self): return int(np.floor((self.Dexterity    - 10)/2))
    def CON(self): return int(np.floor((self.Constitution - 10)/2))
    def INT(self): return int(np.floor((self.Intelligence - 10)/2))
    def WIS(self): return int(np.floor((self.Wisdom       - 10)/2))
    def CHA(self): return int(np.floor((self.Charisma     - 10)/2))

    def AttackRoll(self, stat='STR', prof=True):
        # specify attack ability score and whether to add proficiency
        if   stat == 'STR': modifier = self.STR()
        elif stat == 'DEX': modifier = self.DEX()
        elif stat == 'CON': modifier = self.CON()
        elif stat == 'INT': modifier = self.INT()
        elif stat == 'WIS': modifier = self.WIS()
        elif stat == 'CHA': modifier = self.CHA()

        if prof: modifier += self.prof()

        return '+'.join(['1d20', str(modifier)])

    def __repr__(self) -> str:
        head = ' '.join(['Level', str(self.level), str(np.unique(self.classlvls))])
        stats = ' '.join([  'STR:', str(self.Strength), \
                            'DEX:', str(self.Dexterity), \
                            'CON:', str(self.Constitution), \
                            'INT:', str(self.Intelligence), \
                            'WIS:', str(self.Wisdom), \
                            'CHA:', str(self.Charisma)])
        proficiency = ' '.join(['Proficiency Bonus:', str(self.prof())])
        return '\n'.join([head, stats, proficiency])