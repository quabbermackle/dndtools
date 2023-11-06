"""
This file defines objects for Monte Carlo simulation of character builds
"""

# Matthew Gunther
# 2023/11/04

# DEPENDENCIES----------------------------------------------------------------------------------

import numpy as np
import random as rng
rng.seed()
import matplotlib.pyplot as plt

from treasuretools import roll

# FUNCTIONS-------------------------------------------------------------------------------------

vecroll = np.vectorize(roll, excluded=['avgroll', 'maxroll'])

def rolln(dicestr, ndice):
    # roll dice n times, return array of results
    dicearray = [dicestr] * ndice
    return vecroll(dicearray)

# OBJECTS---------------------------------------------------------------------------------------

class Attack():
    def __init__(self, hitbonus:int, dmgdice:str, **kwargs) -> None:
        self.hitbonus = hitbonus # proficiency plus stat bonus
        self.dmgdice = dmgdice # currently restricted to n dice of 1 type, plus modifier
        if 'advantage' in kwargs.keys():
            self.advantage = kwargs['advantage'] # roll 2d20 to hit, take higher
        else: self.advantage = False
        if 'disadvantage' in kwargs.keys():
            self.disadvantage = kwargs['disadvantage'] # roll 2d20 to hit, take lower
        else: self.disadvantage = False
        if 'extraadvantage' in kwargs.keys():
            # use to add a third die or more, in case of Elven Accuracy, Fortune's Favor, Luck, etc
            self.extraadvantage = kwargs['extraadvantage']
        else: self.extraadvantage = 0
        
        # advantage and disadvantage cancel each other out
        if self.advantage and self.disadvantage:
            self.advantage = False
            self.disadvantage = False
        
    def atkroll(self):
        if self.advantage or self.disadvantage:
            d20s = rolln('1d20', 2+self.extraadvantage)
            if self.advantage: d20 = np.max(d20s)
            if self.disadvantage: d20 = np.min(d20s)
        else: d20 = roll('1d20')
        tohit = d20 + self.hitbonus
        return tohit
                            

# PLOTS-----------------------------------------------------------------------------------------
    
def genhist(dicestr, ndice):
    # calculate histogram counts but do not plot
    # binned in integers from min to max roll
    # does not currently handle modifiers to roll
    split = dicestr.rpartition('d')
    num = int(split[0])
    sides = int(split[-1])
    minroll = num
    maxroll = num*sides
    bins = np.arange(minroll - 0.5, maxroll + 1.5)
    
    resultarray = rolln(dicestr, ndice)
    
    counts, bins = np.histogram(resultarray, bins)
    return counts, bins

def rollandplot(dicestr, ndice, ax):
    # roll dice n times and plot histogram
    counts, bins = genhist(dicestr, ndice)
    bars = bins[:-1]+0.5
    
    titlestr = dicestr + ', ' + str(ndice) + ' trials'
    ax.bar(bars, counts)
    ax.set_title(titlestr)
    ax.set_xlabel('Result')
    ax.set_ylabel('Count')

# TEST------------------------------------------------------------------------------------------

if __name__ == '__main__':
    print(rolln('1d6', 10))
    
    fig, ax = plt.subplots()
    rollandplot('8d6',10000,ax)
    plt.show()