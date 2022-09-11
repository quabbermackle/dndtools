# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 12:33:58 2021

@author: Matthew Gunther

Random Loot Tables from the 5e Dungeon Master's Guide
"""

import math
import random as rng
rng.seed()

#%% define helper functions

# Currency Definitions (5e DMG)
# key = name, value = value
currency = {'copper piece':     '1 cp', # standard, square copper w/ center hole
            'silver piece':     '1 sp', # standard, triangular silver w/center hole
            'electrum piece':   '5 sp', # standard, barrel-shaped electrum w/bottom center hole
            'gold piece':       '1 gp', # standard, smooth hourglass-shaped gold, no hole
            'platinum piece':   '10 gp', # standard, diamond/kite-shaped platinum, no hole
            'copper':           '1 cp', # standard, square copper w/ center hole
            'silver':           '1 sp', # standard, triangular silver w/center hole
            'electrum':         '5 sp', # standard, barrel-shaped electrum w/bottom center hole
            'gold':             '1 gp', # standard, smooth hourglass-shaped gold, no hole
            'platinum':         '10 gp', # standard, diamond/kite-shaped platinum, no hole
            'copper crown':     '1 cp', # Eberron, depicts the crown of Galifar
            'silver sovereign': '1 sp', # Eberron, depicts a living or recent ruler, typical day's pay for an unskilled laborer
            'gold galifar':     '1 gp', # Eberron, depicts Galifar I
            'platinum dragon':  '10 gp', # Eberron, depicts a dragon of legend
            'double crown':     '2 cp', # Breland
            'silver throne':    '5 sp', # Cyre
            'crown':            '1 cp', # Eberron, depicts the crown of Galifar
            'sovereign':        '1 sp', # Eberron, depicts a living or recent ruler, typical day's pay for an unskilled laborer
            'galifar':          '1 gp', # Eberron, depicts Galifar I
            'penny':            '1 cp', # 1920s US
            'nickel':           '5 cp', # 1920s US
            'dime':             '1 sp', # 1920s US
            'quarter':          '25 cp', # 1920s US
            'half-dollar':      '5 sp', # 1920s US
            'dollar':           '1 gp', # 1920s US
            'gold double-eagle':'1 gp',
            'steelpence':       '1 cp', # Sembia, square iron
            'raven':            '1 sp', # Sembia, triangular silver
            'harmark':          '5 sp', # Sembia, diamond-shaped electrum
            'blue eye':         '5 sp', # Sembia, Cormyr, diamond-shaped electrum
            'noble':            '1 gp', # Sembia, five-sided gold
            'nib':              '1 cp', # Waterdeep
            'shard':            '1 sp', # Waterdeep
            'moon':             '5 sp', # Waterdeep
            'dragon':           '1 gp', # Waterdeep
            'sun':              '10 gp', # Waterdeep
            'toal':             '2 gp', # Waterdeep, square brass w/central hole
            'harbor moon':      '50 gp', # Waterdeep, platinum crescent w/central hole & electrum inlay
            'electrum moon':    '1 gp', # Silverymoon, crescent blue(electrum?)
            'eclipsed moon':    '5 ep', # Silverymoon, electrum moon plus dark silver wedge to make a round coin
            'thumb':            '1 cp', # Cormyr
            'silver falcon':    '1 sp', # Cormyr
            'golden lion':      '1 gp', # Cormyr
            'tricrown':         '10 gp', # Cormyr
            'thalver':          '1 cp', # Cormanthyr (ancient elven)
            'bedoar':           '1 sp', # Cormanthyr (ancient elven)
            'thammarch':        '5 sp', # Cormanthyr (ancient elven)
            'shilmaer':         '1 gp', # Cormanthyr (ancient elven)
            'ruendil':          '10 gp', # Cormanthyr (ancient elven)
            'silver bar':       '10 gp', # 2lb, 5" x 2" x .5"
            '5lb silver bar':   '25 gp', # 6" x 2" x 1"
            'gold bar':         '250 gp', # 5 lb, 5" x 2" x .5"
            'iron spindle':     '10 gp', # Mirabar, 2lb black spindle-shaped bars w/square ends
            'gond bell':        '10 gp', # brass bell
            'shaar ring':       '3 gp', # Shaar, pierced & polished ivory slices
            '1lb wheat':        '1 cp',
            '1lb flour':        '2 cp',
            'chicken':          '2 cp',
            '1lb salt':         '5 cp',
            '1lb iron':         '1 sp',
            '1sqyd canvas':     '1 sp',
            '1lb copper':       '5 sp',
            '1sqyd cotton':     '5 sp',
            '1lb ginger':       '1 gp',
            'goat':             '1 gp',
            '1lb cinnamon':     '2 gp',
            '1lb pepper':       '2 gp',
            'sheep':            '2 gp',
            '1lb cloves':       '3 gp',
            'pig':              '3 gp',
            '1lb silver':       '5 gp',
            '1sqyd linen':      '5 gp',
            '1sqyd silk':       '10 gp',
            'cow':              '10 gp',
            '1lb saffron':      '15 gp',
            'ox':               '15 gp',
            '1lb gold':         '50 gp',
            '1lb platinum':     '500 gp',
            'adamantine bar':   '1000 gp', # 10lb
            }

def dice(sides=6, num=1):
    # random roll of n dice with s sides each
    tot = 0
    for _ in range(num): tot += rng.choice(list(range(1, sides+1)))
    return tot

def roll(string='1d6', avgroll=False, maxroll=False):
    """
    nds(+/-/xC) string is parsed as
        n dice
        s sides
        plus/minus/times constant C
    avgroll returns the calculated average result
    maxroll returns the maximum possible result
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
    
    if avgroll:     result = num * (sum(list(range(1,sides+1)))/sides)
    elif maxroll:   result = num * sides
    else:           result = dice(sides, num)
    
    return (result + const) * mult

def coin2decgp(coins = '0 pp, 0 gp, 0 ep, 0 sp, 0 cp'):
    # convert a string of coin amounts to a decimal number of gp
    c = coins.split(', ') # split by currency
    gp = 0.
    for i in c: # for each currency type
        x = i.partition(' ') # split into number and value
        n = float(x[0]) # number of coins of this value
        v = x[-1] # value of current currency
        if v in ['pp', 'p', 'platinum']:   n = n*10. # 1 pp = 10 gp
        elif v in ['gp', 'g', 'gold']:     n = n     # 1 gp = 1.0 gp
        elif v in ['ep', 'e', 'electrum']: n = n*.5  # 1 ep = 0.5 gp
        elif v in ['sp', 's', 'silver']:   n = n*.1  # 1 sp = 0.1 gp
        elif v in ['cp', 'c', 'copper']:   n = n*.01 # 1 cp = 0.01 gp
        gp += n # add adjusted value of current coins to total
    return round(gp,2) # output total value of coins, converted to gp

def decgp2coin(decgp = 0., p=False, e=False):
    # convert a decimal number of gp to a string of coin amounts
    # set p = True to display platinum
    # set e = True to display electrum
    
    intpp = math.floor(decgp/10) # integer number of platinum pieces
    if p and (intpp != 0):
        pp = str(intpp) + ' pp, ' # convert number of pp to string
        decgp = decgp - (intpp*10) # remove pp from remaining decimal gp
    else: pp = '' # only show gp if desired
    
    intgp = math.floor(decgp) # integer number of gold pieces
    if intgp != 0:
        gp = str(intgp) + ' gp, ' # convert number of gp to string
        decgp = decgp - intgp # remove gp from remaining decimal gp
    else: gp = '' # display nothing if there are no gp
    
    intep = math.floor(decgp*2) # integer number of electrum pieces
    if e and (intep != 0):
        ep = str(intep) + ' ep, ' # convert number of ep to string
        decgp = decgp - (intep/2) # remove ep from remaining decimal gp
    else: ep = '' # only show ep if desired
    
    intsp = math.floor(decgp*10) # integer number of silver pieces
    if intsp != 0:
        sp = str(intsp) + ' sp, ' # convert number of sp to string
        decgp = decgp - (intsp/10) # remove sp from remaining decimal gp
    else: sp = '' # display nothing if there are no sp
    
    intcp = int(round(decgp*100)) # integer number of copper pieces
    if intcp != 0:
        cp = str(intcp) + ' cp' # convert number of cp to string
    else: cp = '' # display nothing if there are no cp
    
    coins = pp + gp + ep + sp + cp # concatenate all strings
    coins = coins.rstrip(', ') # remove any unnecessary trailing commas/spaces
    if coins == '': coins = '0 cp' # return 0 cp if input was just 0.0
    
    return coins

def simplecoin(coins = '0 pp, 0 gp, 0 ep, 0 sp, 0 cp', p=False, e=False):
    # simplify the representation of a list of coin amounts
    # set p = True to display platinum
    # set e = True to display electrum
    return decgp2coin(coin2decgp(coins), p, e)

#%% Lifestyle Expenses

lifestyles = ['Wretched',
              'Squalid',
              'Poor',
              'Modest',
              'Comfortable',
              'Wealthy',
              'Aristocratic']
# lifestyle expenses [value = price/day]
ls_expenses = {'Wretched':      '0 cp',
               'Squalid':       '1 sp',
               'Poor':          '2 sp',
               'Modest':        '1 gp',
               'Comfortable':   '2 gp',
               'Wealthy':       '4 gp',
               'Aristocratic':  '10 gp'}
ls_sum = {}
for i in lifestyles:
    daily = ls_expenses[i]
    weekly = decgp2coin(7*coin2decgp(daily))
    monthly = decgp2coin(4*coin2decgp(weekly))
    yearly = decgp2coin(12*coin2decgp(monthly))
    ls_sum[i] = {'daily':daily,
                 'weekly':weekly,
                 'monthly':monthly,
                 'yearly':yearly}

#%% Individual Treasure Tables

# list order:         CP,        SP,        EP,         GP,         PP
indiv = {}
indiv_w = {}
indiv['CR 0-4'] =   [['5d6',     '0d0',     '0d0',      '0d0',      '0d0'],
                     ['0d0',     '4d6',     '0d0',      '0d0',      '0d0'],
                     ['0d0',     '0d0',     '3d6',      '0d0',      '0d0'],
                     ['0d0',     '0d0',     '0d0',      '3d6',      '0d0'],
                     ['0d0',     '0d0',     '0d0',      '0d0',      '1d6']]
indiv_w['CR 0-4'] = [30, 60, 70, 95, 100]
indiv['CR 5-10'] =  [['4d6x100', '0d0',     '1d6x10',   '0d0',      '0d0'],
                     ['0d0',     '6d6x10',  '0d0',      '2d6x10',   '0d0'],
                     ['0d0',     '0d0',     '3d6x10',   '2d6x10',   '0d0'],
                     ['0d0',     '0d0',     '0d0',      '4d6x10',   '0d0'],
                     ['0d0',     '0d0',     '0d0',      '2d6x10',   '3d6']]
indiv_w['CR 5-10'] = [30, 60, 70, 95, 100]
indiv['CR 11-16'] = [['0d0',     '4d6x100', '0d0',      '1d6x100',  '0d0'],
                     ['0d0',     '0d0',     '1d6x100',  '1d6x100',  '0d0'],
                     ['0d0',     '0d0',     '0d0',      '2d6x100',  '1d6x10'],
                     ['0d0',     '0d0',     '0d0',      '2d6x100',  '2d6x10']]
indiv_w['CR 11-16'] = [20, 35, 75, 100]
indiv['CR 17+'] =   [['0d0',     '0d0',     '2d6x1000', '8d6x100',  '0d0'],
                     ['0d0',     '0d0',     '0d0',      '1d6x1000', '1d6x100'],
                     ['0d0',     '0d0',     '0d0',      '1d6x1000', '2d6x100']]
indiv_w['CR 17+'] = [15, 55, 100]
CRnames = ['CR 0-4', 'CR 5-10', 'CR 11-16', 'CR 17+']

def indiv_treasure(CR='random'):
    if CR == 'random': CR = rng.choice(CRnames)
    row = rng.choices(indiv[CR], cum_weights=indiv_w[CR])[0]
    denom = ['CP', 'SP', 'EP', 'GP', 'PP']
    text = ''
    for x in range(0, len(denom)):
        coins = roll(row[x])
        if coins != 0: text += str(coins) + ' ' + denom[x] + ', '
    text = text[0:-2]
    return text

#%% Trinkets
    
trinket = {'Standard':['A mummified goblin hand',
                       'A piece of crystal that faintly glows in the moonlight',
                       'A gold coin minted in an unknown land',
                       'A diary written in a language you don\'t know',
                       'A brass ring that never tarnishes',
                       'An old chess piece made from glass',
                       'A pair of knucklebone dice, each with a skull symbol on the side that would normally show six pips',
                       'A small idol depicting a nightmarish creature that gives you unsettling dreams when you sleep near it',
                       'A rope necklace from which dangles four mummified elf fingers',
                       'The deed for a parcel of land in a realm unknown to you',
                       'A 1-ounce block made from an unknown material',
                       'A small cloth doll skewered with needles',
                       'A tooth from an unknown beast',
                       'An enormous scale, perhaps from a dragon',
                       'A bright green feather',
                       'An old divination card bearing your likeness',
                       'A glass orb filled with moving smoke',
                       'A 1-pound egg with a bright red shell',
                       'A pipe that blows bubbles',
                       'A glass jar containing a weird bit of flesh floating in pickling fluid',
                       'A tiny gnome-crafted music box that plays a song you dimly remember from your childhood',
                       'A small wooden statuette of a smug halfling',
                       'A brass orb etched with strange runes',
                       'A multicolored stone disk',
                       'A tiny silver icon of a raven',
                       'A bag containing forty-seven humanoid teeth, one of which is rotten',
                       'A shard of obsidian that always feels warm to the touch',
                       'A dragon\'s bony talon hanging from a plain leather necklace',
                       'A pair of old socks',
                       'A blank book whose pages refuse to hold ink, chalk, graphite, or any other substance or marking',
                       'A silver badge in the shape of a five-pointed star',
                       'A knife that belonged to a relative',
                       'A glass vial filled with nail clippings',
                       'A rectangular metal device with two tiny metal cups on one end that throws sparks when wet',
                       'A white, sequined glove sized for a human',
                       'A vest with one hundred tiny pockets',
                       'A small, weightless stone block',
                       'A tiny sketch portrait of a goblin',
                       'An empty glass vial that smells of perfume when opened',
                       'A gemstone that looks like a lump of coal when examined by anyone but you',
                       'A scrap of cloth from an old banner',
                       'A rank insignia from a lost legionnaire',
                       'A tiny silver bell without a clapper',
                       'A mechanical canary inside a gnomish lamp',
                       'A tiny chest carved to look like it has numerous feet on the bottom',
                       'A dead sprite inside a clear glass bottle',
                       'A metal can that has no opening but sounds as if it is filled with liquid, sand, spiders, or broken glass (your choice)',
                       'A glass orb filled with water, in which swims a clockwork goldfish',
                       'A silver spoon with an M engraved on the handle',
                       'A whistle made from gold-colored wood',
                       'A dead scarab beetle the size of your hand',
                       'Two toy soldiers, one with a missing head',
                       'A small box filled with different-size buttons',
                       'A candle that can\'t be lit',
                       'A tiny cage with no door',
                       'An old key',
                       'An indecipherable treasure map',
                       'A hilt from a broken sword',
                       'A rabbit\'s foot',
                       'A glass eye',
                       'A cameo carved in the likeness of a hideous person',
                       'An alabaster mask',
                       'A pyramid of sticky black incense that smells very bad',
                       'A nightcap that, when worn, gives you pleasant dreams',
                       'A single caltrop made from bone',
                       'A gold monocle frame without the lens',
                       'A 1-inch cube, each side painted a different color',
                       'A crystal knob from a door',
                       'A small packet filled with pink dust',
                       'A fragment of a beautiful song, written as musical notes on two pieces of parchment',
                       'A silver teardrop earring made from a real teardrop',
                       'The shell of an egg painted with scenes of human misery in disturbing detail',
                       'A fan that, when unfolded, shows a sleeping cat',
                       'A set of bone pipes',
                       'A four-leaf clover pressed inside a book discussing manners and etiquette',
                       'A sheet of parchment upon which is drawn a complex mechanical contraption',
                       'An ornate scabbard that fits no blade you have found so far',
                       'An invitation to a party where a murder happened',
                       'A bronze pentacle with an etching of a rat\'s head in its center',
                       'A purple handkerchief embroidered with the name of a powerful archmage',
                       'Half of a floorplan for a temple, castle, or some other structure',
                       'A bit of folded cloth that, when unfolded, turns into a stylish cap',
                       'A receipt of deposit at a bank in a far-flung city',
                       'A diary with seven missing pages',
                       'An empty silver snuffbox bearing an inscription on the surface that says "dreams"',
                       'An iron holy symbol devoted to an unknown god',
                       'A book that tells the story of a legendary hero\'s rise and fall, with the last chapter missing',
                       'A vial of dragon blood',
                       'An ancient arrow of elven design',
                       'A needle that never bends',
                       'An ornate brooch of dwarven design',
                       'An empty wine bottle bearing a pretty label that says, "The Wizard of Wines Winery, Red Dragon Crush, 331422-W"',
                       'A mosaic tile with a multicolored, glazed surface',
                       'A petrified mouse',
                       'A black pirate flag adorned with a dragon\'s skull and crossbones',
                       'A tiny mechanical crab or spider that moves about when it\'s not being observed',
                       'A glass jar containing lard with a label that reads, "Griffon Grease"',
                       'A wooden box with a ceramic bottom that holds a living worm with a head on each end of its body',
                       'A metal urn containing the ashes of a hero'],
           'Aerenal':['A bronzewood ring inscribed with the Elvish word for "hope"',
                      'A dried flower; if it\'s placed in water, it blooms',
                      'An ebony locket; when it\'s opened, an elven voice whispers "Always"',
                      'A tiny skull carved from dark wood',
                      'A finger bone inscribed with an unknown sigil',
                      'An ivory flute which produces no sound',
                      'A small journal made from preserved leaves',
                      'A book of poetry written by undead elves'],
           'Argonnessen':['A pierced dragon scale on a cord',
                          'A statuette of a dragon carved from black bone',
                          'A dragon\'s tooth, engraved with an unknown sigil',
                          'A child\'s doll of a dragon, woven from leather cords',
                          'A dagger carved from a dragon\'s talon',
                          'A brass disk bearing the silhouette of a black dragon',
                          'A small egg-shaped piece of polished bone',
                          'A bone fragment with brass inlaid runes',
                          'A leather pouch filled with tiny draconic teeth',
                          'A single large seed that\'s warm to the touch'],
           'Khyber':['A pressed flower with vivid green petals; when you smell it, you hear eerie music',
                     'A tiny ball of putty; if you set it down, it begins to slowly crawl around',
                     'A perpetually warm disk of dark iron',
                     'A small journal with leathery pages; any words you write in it slowly disappear',
                     'A four-sided die carved with strange markings',
                     'A cameo with the silhouette of an unknown species',
                     'A preserved finger with purple flesh and four joints',
                     'A perfectly preserved eye; if you set it down, it rotates to follow your movement',
                     'A small box; when opened, you alone hear screaming',
                     'A preserved insect; you\'ve never seen another like it'],
           'Frostfell':['A small prism carved from ice that doesn\'t melt',
                        'A rusted iron coin, depicting a dwarf lord and the words "Five Rex Undra"',
                        'A pair of eight-sided dice carved from ice that doesn\'t melt',
                        'A swatch of silvery fur that\'s cold to the touch, possibly from a winter wolf',
                        'A snowball; it doesn\'t melt and can\'t be compressed into ice',
                        'A tiny white dragon sculpted from ice that doesn\'t melt',
                        'A key carved from ice that doesn\'t melt',
                        'A single scale from a white dragon'],
           'Sarlona':['A polished crystal sphere; when you clutch it in your fist, a telepathic voice recites a story in your mind',
                      'A teardrop pendant made from polished shell; when you hold it, you see the image of a young Riedran man',
                      'A six-sided crystal die; when you roll it, you feel a surge of emotion for six seconds',
                      'A sealed vial filled with faintly luminescent blue mist',
                      'A crystal disk engraved with a labyrinthine pattern',
                      'A leather-bound collection of kalashtar poetry called "Shards of the Light"',
                      'A sphere of polished crystal; when you hold it in your palm, you feel that it knows you and understands you',
                      'A cup and ball toy; when you successfully catch the ball in the cup, you feel a momentary surge of joy'],
           'Xendrik':['A punched ticked for a voyage from Sharn to Stormreach',
                      'A scorpion\'s barb engraved with a single Elvish letter',
                      'A copper coin so big you could use it as a dinner plate',
                      'An image of an elf warrior engraved on a giant\'s tooth',
                      'A single page from a giant wizard\'s spellbook, bearing an incomplete spell',
                      'A scrap of parchment, part of a map of Stormreach',
                      'A small book entitled "Feersome Beests of Zendrik"',
                      'A scrimshaw carving of a sahuagin'],
           'Horror':['A picture you drew as a child of your imaginary friend',
                     'A lock that opens when blood is dripped in its keyhole',
                     'Clothes stolen from a scarecrow',
                     'A spinning top carved with four faces: happy, sad, wrathful, and dead',
                     'The necklace of a sibling who died on the day you were born',
                     'A wig from someone executed by beheading',
                     'The unopened letter to you from your dying father',
                     'A pocket watch that runs backward for an hour every midnight',
                     'A winter coat stolen from a dying soldier',
                     'A bottle of invisible ink that can only be read at sunset',
                     'A wineskin that refills when interred with a dead person for a night',
                     'A set of silverware used by a king for his last meal',
                     'A spyglass that always shows the world suffering a terrible storm',
                     'A cameo with the profile\'s face scratched away',
                     'A lantern with a black candle that never runs out and that burns with a green flame',
                     'A teacup from a child\'s tea set, stained with blood',
                     'A little black book that records your dreams, and yours alone, when you sleep',
                     'A necklace formed of the interlinked holy symbols of a dozen deities',
                     'A noose that feels heavier than it should',
                     'A birdcage into which small birds fly but once inside never eat or leave',
                     'A lepidopterist\'s box filled with dead moths with skull-like patterns on their wings',
                     'A jar of pickled ghouls\' tongues',
                     'The wooden hand of a notorious pirate',
                     'An urn with the ashes of a dead relative',
                     'A hand mirror backed with a bronze depiction of a medusa',
                     'Pallid leather gloves crafted with ivory fingernails',
                     'Dice made from the knuckles of a notorious charlatan',
                     'A ring of keys for forgotten locks',
                     'Nails from the coffin of a murderer',
                     'A key to the family crypt',
                     'A bouquet of funerary flowers that always looks and smells fresh',
                     'A switch used to discipline you as a child',
                     'A music box that plays by itself whenever someone holding it dances',
                     'A walking cane with an iron ferrule that strikes sparks on stone',
                     'A flag from a ship lost at sea',
                     'A porcelain doll\'s head that always seems to be looking at you',
                     'A wolf\'s head wrought in silver that is also a whistle',
                     'A small mirror that shows a much older version of the viewer',
                     'A small, worn book of children\'s nusery rhymes',
                     'A mummified raven claw',
                     'A broken pendant of a silver dragon that\'s always cold to the touch',
                     'A small locked box that quietly hums a lovely melody at night, but you always forget it in the morning',
                     'An inkwell that makes one a little nauseous when staring at it',
                     'An old doll made from a dark, dense wood and missing a hand and foot',
                     'A black executioner\'s hood',
                     'A pouch made of flesh, with a sinew drawstring',
                     'A tiny spool of black thread that never runs out',
                     'A tiny clockwork figuring of a dancer that\'s missing a gear and doesn\'t work',
                     'A black wooden pipe that creates puffs of smoke that look like skulls',
                     'A vial of perfume, the scent of which only certain creatures can detect',
                     'A stone that emits a single endless sigh',
                     'A rag doll with two red dots on its neck',
                     'A spring-loaded toy with a missing crank',
                     'A mason jar containing a harmless but agitated, animate ooze',
                     'A black wooden die with 1\'s on all the faces',
                     'A child\'s portrait with "born" written on the back, along with next year\'s date',
                     'A dagger-sized shark tooth',
                     'A finger that\'s taken root in a small pot',
                     'A toolbox containing the remains of a dangerous but broken clockwork arachnid',
                     'A pitcher-sized, opalescent snail shell that occasionally, inexplicably shudders or tips over',
                     'The logbook of an ice-breaking ship called The Haifisch',
                     'A small portrait of you as a child, alongside your identically dressed twin',
                     'A silver pocket watch with thirteen hours marked on the face',
                     'A woodcut of a wolf devouring its own hind leg',
                     'A planchette etched with raven skulls',
                     'A moist coral figurine of a lamprey with arms, legs, and a bipedal stance',
                     'A bronze fingertrap sculpted with roaring tigers',
                     'A pearl necklace that turns red under the full moon',
                     'A fossil of a fish with humanoid features'
                     'A plague doctor\'s mask',
                     'A paper talisman with smudged ink',
                     'A locket containing the smeared image of an eyeless figure',
                     'A canopic jar with a lid sculpted like a goat',
                     'A jack-o-lantern made from a small, pale gourd',
                     'A single high-heeled, iron shoe',
                     'A candle made from a severed hand',
                     'A clockwork device that beats like a heart',
                     'A blank masquerade mask',
                     'A glass eye with a live worm inside',
                     'A sheet with two eyeholes cut in it',
                     'The deed to someplace called Tergeron Manor',
                     'An ornate, wax-sealed crimson envelope that resists all attempts to open it',
                     'A mourning veil trimmed in black lace',
                     'A straitjacket covered in charcoal runes',
                     'A tattered, burlap mask with a crooked smile painted on it',
                     'A green ribbon designed to be worn as a choker',
                     'Dentures with mismatched, sharpened teeth',
                     'A warm, fist-sized egg case',
                     'A copper ring with "mine" engraved on the inside',
                     'A glass ampoule containing a neon green fluid',
                     'An eye patch embroidered with a holy symbol',
                     'A severed big toe with a nail that continues to grow',
                     'A journal that has been heavily redacted',
                     'A glove with a mouth-like design stitched on the palm',
                     'An ornate but empty reliquary made of silver and fractured glass',
                     'A ceramic figure of a cat with too many eyes',
                     'A crumpled paper ticket bearing the words "admit none"',
                     'An electrum coin with your face on one side',
                     'A shrunken gremishka head that twitches when anyone casts magic nearby',
                     'A sunburst amulet with a red stone at the center'],
           'Elemental': ['A compass that always points to the holder\'s hometown',
                         'A paper fan that won\'t produce a breeze no matter how hard it\'s waved',
                         'A petrified potato that resembles someone important to you',
                         'A glass cup that can only be filled halfway no matter how much liquid is poured into it',
                         'A mirror that only shows the back of your head',
                         'A small glass bird that when set down near water dips its head in as if to get a drink',
                         'A lady\'s coin purse containing two sharp fangs',
                         'A small sea conch with the words "From the beginning" painted on the lip',
                         'A frost-covered silver locket that\'s frozen shut',
                         'A seal which imprints a mysterious, unknown coat of arms into hard rock',
                         'A small wooden doll that when held brings back fond memories',
                         'A small hand mirror which only reflects inanimate objects',
                         'A glass eyeball that looks about of its own accordance, and can roll around',
                         'A glass orb that replicates yesterday\'s weather inside itself',
                         'A drinking cup that randomly refills with fresh or salt water once emptied',
                         'A deep blue piece of flint, that when struck with steel produces not a spark but a drop of water',
                         'A conch shell which is always damp and constantly drips saltwater',
                         'A charred, half-melted pewter clasp that glows as if smoldering but releases no heat',
                         'A clockwork finch that flaps its wings in the presence of a breeze',
                         'An unbreakable sealed jar of glowing water that hums when shaken',
                         'A small, finely polished geode whose crystals slowly fade between every color of the spectrum',
                         'A rough stone eye pulled from a petrified creature',
                         'A stone smoking pipe that never needs lighting',
                         'A small whistle that, when blown, whispers a name of a person or place unknown to you',
                         'A fist sized rock that beats like a heart',
                         'A pair of bronze scissors in the shape of a pair of leaping dolphins',
                         'A bronze oil lamp which is rumored to have once held a genie',
                         'A single gauntlet inscribed with a fire motif and an unfamiliar name in Primordial',
                         'A one-eyed little fish inside a spherical vial, much bigger than the vial\'s neck; he has a cunning look to him',
                         'The tiny skull of a rabbit that whispers scathing insults when nobody is looking',
                         'A rag doll in the likeness of an owlbear',
                         'The desiccated body of a small eight-legged black lizard',
                         'A small toy boat made with a walnut shell, toothpick, and piece of cloth',
                         'A small pocket mirror that slowly fogs over while held',
                         'Wind chimes that glow when the wind blows',
                         'A small, clay square with an unknown rune etched onto one side',
                         'A tea kettle that heats itself when filled with water',
                         'An old scratched monocle which shows an underwater landscape whenever someone looks through it',
                         'A rose carved from coral',
                         'A set of dice with elemental symbols and primordial runes instead of pips or numbers',
                         'An amulet filled with liquid that churns, freezes, or boils to match its wearer\'s mood',
                         'A small silver bell that makes a sound like quiet, distant thunder when it\'s struck',
                         'A small vial of black sand that glows slightly in the moonlight',
                         'A small whale tooth etched with an image of waves crashing upon a beach',
                         'An hourglass in which the sands pour upward instead of downward',
                         'A glass pendant with a hole in the center that a mild breeze always blows out of',
                         'A soft feather that falls like a stone when dropped',
                         'A large transparent gem that, when gripped tightly, whispers in Terran',
                         'A small crystal snowglobe that, when shaken, seems to form silhouettes of dancing forms',
                         'Half of a palm-sized geode that pulses dimly with purple light',
                         'A book filled with writing that only appears when the book is held underwater',
                         'A sealed envelope made of red leather that you haven\'t been able to open, but which smells of a campfire',
                         'A locket of hair that is rumored to have come from a famed fire genasi',
                         'Flint and steel that, when used to start a fire, creates a random colored flame',
                         'A blank piece of wet parchment that never seems to dry',
                         'A small puzzle box made of brass that is slightly warm to the touch',
                         'A cloudy chunk of glass that is said to hold a spark of breath from a blue dragon',
                         'A crude chalice made of coal',
                         'A miniature brass horn, silent when played, but which fills the air with the scent of warm and exotic spices',
                         'An eye-sized blue pearl that floats in salt water',
                         'A tuning fork made from a dark metal which glows with a pale, white light during thunderstorms',
                         'A small vial that is always filled with the smell of autumn wind',
                         'A clear marble that slowly rolls toward the nearest source of running water',
                         'A small collapsible silver cup that perspires constantly when opened',
                         'An hourglass that tells time with falling mist instead of sand',
                         'An ornate razor, which only cuts in freezing cold temperatures',
                         'A shark tooth covered in tiny etched words from a lost language',
                         'A large brass coin with no markings or images on it',
                         'A small wooden box filled with a strange red clay',
                         'A necklace with a small, rusted iron anchor',
                         'A small brass flute adorned with silver wire that is always faintly sounding',
                         'A red and black Aarakocra feather',
                         'A palm-sized stone with a hole in it, through which can be heard a constantly whispering wind',
                         'A small conch shell covered in black crystal',
                         'A small music box made of brass, featuring a pair of tiny automatons that resemble Azer working at a forge',
                         'A glass jar containing the preserved corpse of an unfamiliar aquatic creature',
                         'A piece of petrified wood carved into the shape of a seashell',
                         'A wooden puzzle cube covered in elemental symbols',
                         'A small stone cube that acts as a magnet when placed against another stone',
                         'A ring made of a white metal, with a name etched in Auran on the inside of the band',
                         'A bracelet made of silvered fish hooks',
                         'A journal filled with poetry hand-written in Primordial',
                         'A yellow gemstone that glows dimly when a storm is nearby',
                         'A charred chisel with an unfamiliar symbol stamped onto its base',
                         'A canteen filled with a foul smelling orange mud',
                         'A faceless doll made of driftwood',
                         'A heavy iron key bearing the name of a ship long lost to the sea',
                         'A small jewelry box made from the shell of a turtle',
                         'A chess piece fashioned to look like a fire myrmidon',
                         'A spinning top with an image of one of the four elements on each side',
                         'A single hoop earring made of a porous red stone',
                         'An arrowhead carved from sea salt',
                         'A small comb made of blue coral',
                         'Seven small beads of sandstone on a string, all different colors',
                         'A romance chapbook written in Undercommon titled "Just one Layer of Grey"',
                         'A tiny, broken clockwork Harpy',
                         'An ivory whale statuette',
                         'A fist-sized cog, covered in barnacles',
                         'An eyepatch made of obsidian and a black leather cord',
                         'A glass bottle with a tiny ship of unfamiliar design inside'],
           'Alternate':['A perfect skipping stone',
                        'Three weighted dice that always roll low',
                        'A locket with a picture of King Boranel',
                        'A tiny anvil and a smith\'s hammer',
                        'A nonfunctional immovable rod',
                        'An acupuncture kit',
                        'A stuffed dragon toy',
                        'A diagram for a new war lute',
                        'A declaration of war against a nation no one has ever heard of',
                        'A pipe that emits green smoke',
                        'A glass eye',
                        'A crystal from the chandelier of a famous theater',
                        'A fine cane with a secret compartment',
                        'A letter written by Merrix d\'Cannith',
                        'A coin that always lands on its edge',
                        'The deed and title to an abandoned windmill and three acres of tillable land that you\'ve never been able to find',
                        'A menu from Big Daddy Donaar\'s Yum Yum Hut',
                        'A small purse that screams loudly when opened',
                        'A raven-feather quill',
                        'A pair of breeches that always smells faintly of honey',
                        'A one-armed Dark Lantern doll (dagger accessory missing)',
                        'A leather pouch filled with various finger bones of unknown provenance',
                        'The collar of your childhood pet, Nutmeg',
                        'A seashell that, when pressed to the ear, speaks in flowing rhymes',
                        'A recipe book for cooking with mushrooms',
                        'One expired coupon for "A Free Cornerstone"',
                        'A portable beehive',
                        'Goggles that literally tint everything rose colored',
                        'A wand that allows you to cast the Mending cantrip',
                        'A bracelet woven from mistletoe',
                        'A curved claw from an unknown beast that small children are always frightened of',
                        'A longsword that can be folded down in 1 minute and hidden in your pocket',
                        'A living graft of what you believe to be the World Tree',
                        'A tattered scarf with the House Cannith logo',
                        'A box containing a torn-up letter',
                        'An old contract marked "Void"',
                        'A small pigeon in a cage',
                        'A House Ghallanda "Golden Dragon" foam claw',
                        'A lunchbox marked "Team C"',
                        'A potted plant that grows different fruit on every branch',
                        'A book of adventures for children',
                        'A Tira Miron action figure with detachable sword and holy symbol',
                        'A pint glass engraved with a picture of a keg robot',
                        'A giant hrazhak idol',
                        'A miniature siege staff that actually fires',
                        'A very fancy red scarf and matching handkerchief',
                        'A Thrane army surplus arrow',
                        'A purple worm toy',
                        'A burned doll whose eyes follow you around the room',
                        'An infinite inkwell',
                        'A band embroidered with the symbol of the Dark Six',
                        'A squishy cactus',
                        'A velvet blindfold',
                        'A dirty figurine of a triceratops that can\'t be cleaned',
                        'A nonmagical noble\'s knife',
                        'A quill that rotates through all the colors of the rainbow',
                        'A twenty-sided die that only rolls the number 4',
                        'A pointed hat that glows in the dark',
                        'A cup that hums when filled with water',
                        'A mug fashioned from a humanoid skull',
                        'A small glass jar containing an immortal firefly',
                        'A fake mustache made from gnome facial hair',
                        'A petrified troll finger',
                        'The left half of a map',
                        'The right half of a map',
                        'An unreasonable amount of pocket lint',
                        'A dozen flyers for a local Zil food place',
                        'Evix ir\'Marasha\'s business card',
                        'A lock of hair from a changeling',
                        'A marble that rolls uphill',
                        'A piece of parchment listing a command word for an unknown magic item',
                        'A book titled "Conversational Giant"',
                        'A user\'s manual for a warforged colossus',
                        'A signed headshot of famous performer Matriarch Elvinor Elorrenthi d\'Phiarlan',
                        'The eye of a basilisk in a crystal box',
                        'A postcard from the Amaranthine City of Irian',
                        'A stamp collection',
                        'A small piece of solidified smoke',
                        'A six-sided die that sometimes rolls a seven',
                        'A left-hand gauntlet',
                        'A music box that plays nursery rhymes',
                        'A locket that\'s bigger on the outside than the inside',
                        'A potted plant that grows hair instead of leaves',
                        'A collection of teeth',
                        'A coin whose minting date always shows three years in the future',
                        'A green drinking horn taken from a very large bull',
                        'A small book containing pressed and dried botanical samples',
                        'A hatched chimera egg',
                        'A slightly used red bandit mask',
                        'A tiny stirge encased in amber',
                        'A large bottle of Red Larch Ale that can\'t be opened',
                        'A cane topped with a stylized golden bulldog',
                        'A note in your own hand that you don\'t remember writing',
                        'A sprig of herbs from your family\'s garden',
                        'A tankard stolen from the Drunken Dragon in Clifftop, Upper Dura',
                        'A small, severed tentacle preserved in alcohol',
                        'A walnut with a face drawn on it',
                        'A small flask of liquid from the Lake of Radiant Mists',
                        'An ice cube that never melts',
                        'An expertly carved sword hilt with the blade snapped cleanly off'],
           'Northern':['A small wooden figurine of a yawning walrus, painted in red and black',
                       'A pair of scrimshaw cufflinks with an image of a fisherman on a boat engraved on them',
                       'A small iron key with a frayed blue and gold cord tied to it',
                       'A small illustrated book of Farlnen myths that has pages missing',
                       'A damaged scrimshaw cameo depicting a merfolk',
                       'A stone from a burial cairn with a tiny Dwarvish rune carved into it',
                       'A ripped cloth sail with a symbol you don\'t recognize',
                       'A Tashana knife with a scrimshaw handle',
                       'A jar containing an unidentifiable sweet, sticky substance',
                       'A delicate glass ball painted with snowflakes, capped by a metal loop with a tiny hook attached to it',
                       'An expedition log with missing pages and a pressed flower used as a bookmark',
                       'An owl figuring carved from whalebone',
                       'A sewing box that smells of old wood and has three spools of blue thread inside',
                       'A scrimshaw-handled ink pen with black runic designs along its length',
                       'A brooch made from a small insect encased in amber',
                       'A scrimshaw pepper shaker etched with the letter W',
                       'An old, wooden-handled ice pick stained with blood that won\'t wash off',
                       'A fabric doll bearing an angry expression',
                       'A set of wind chimes made from seashells',
                       'A beautiful silver tin that, when opened, emits the smell of rotting fish',
                       'A bloodstained dreamcatcher made from fishing line, gold wire, and snowy owlbear feathers',
                       'A figurine of a polar bear made of ice that never melts',
                       'A snow globe that does\'t need to be shaken',
                       'A piece of sea glass shaped like a unicorn\'s horn',
                       'A dark blue scarf that gets lighter in shade the higher the altitude of the wearer'],
           'Elven':['A small notebook that causes anything written in it to disappear after 1 hour',
                    'A crystal lens made of ivory and gold that causes anything observed through it to appear to be surrounded by motes of multicolored light',
                    'A small golden pyramid inscribed with elven symbols and about the size of the walnut',
                    'A cloak pin made from enamel in the shape of a butterfly; when you take the pin off, it turns into a real butterfly, and returns when you are ready to put your cloak back on again',
                    'A golden compass that points toward the nearest Thelanian manifest zone within 10 miles',
                    'A small silver spinning top that, when spun, endlessly spins until interrupted',
                    'A small songbird made of enamel, gold wire, and precious stone; uttering the songbird\'s name in Elvish causes the trinket to emit that bird\'s birdsong',
                    'A small enamel flower that, when put in one\'s hair, animates, tying back the wearer\'s hair with a living vine with flowers; plucking a single flower from this vine returns it to its inanimate form'],
           'Dhakaan':['A large, well-worn copper coin; one side bears the profile of a stern female hobgoblin, the other shows six intertwined crowns',
                      'The hilt of an ancient dagger; the pommel is inscribed with the word "chot" and the image of an eye',
                      'A collar of black leather with adamantine spikes, sized to fit the neck of a large creature',
                      'A miniature set of sturdy mason\'s tools designed for the use of a small creature; the tools are in perfect condition - an enchantment repels the effects of age and minor damage',
                      'A brass hair pin in the shape of a sword, nicked and worn with age',
                      'A black leather mask designed to cover the lower face of a small humanoid, depicting the mouth of a snarling wolf',
                      'A mithral armband in the shape of a serpent; the snake\'s short fangs pierce the skin of its wearer',
                      'An eight-sided bone die inscribed with Goblin numerals',
                      'A small, well-worn adamantine flask; if you pour any sort of dairy product into it, it immediately evaporates',
                      'A rusted iron coin; the word "muut" is inscribed on one side, and "atcha" on the other',
                      'A worg\'s tooth dipped in bronze',
                      'A pair of nearly indestructible socks, woven from a clever form of adamantine mesh'],
           'Sol Udar':['An ancient compass-like tool points unerringly toward a location in Sol Udar',
                       'A scarab-like creature, the size of a small gold coin; if you attach it to your neck, it telepathically projects eerie music into your mind',
                       'A hexagonal playing card of unfamiliar design, bearing the number 5 and the image of a dwarven woman in heavy armor',
                       'A set of living thieves\' tools, with flexible tentacles instead of steel picks',
                       'An adamantine key of ancient design',
                       'An eel-like symbiont that wraps around your wrist like a bracelet, reducing the effects of motion sickness and hangovers',
                       'A battered locket that contains an animated image of a dwarf; it\'s possible it\'s sentient and understands what you say - but probably not',
                       'A leather choker with leech-like mouths on the inside; while attached to your throat, it amplifies your voice to three times its normal volume',
                       'A battered brass mug that chills any liquid placed inside, but with a hole punched through the bottom',
                       'A preserved eye of an unknown creature; the iris still expands and contracts',
                       'A hexagonal metal disk engraved with a Dwarven word that means "play"; when you hold it and speak that word, it loudly plays an ancient marching tune that can be heard up to 60 feet away',
                       'An organic pen made of a leathery substance, with a talon as the nib; it generates ink as you write - which seems to be made of blood'],
           'Dolurrh':['A hand mirror periodically shows the reflection of a particular dead person or an event from their memories',
                      'A monocle shows the last thing seen by its previous owner before they died',
                      'A stuffed toy sings softly when it\'s placed in darkness',
                      'A pen writes a specific message when dipped in ink and left untouched',
                      'A small leather journal contains a poem, story, or piece of music by a beloved creator - written after they died',
                      'A battered copper coin flips itself if placed heads-down',
                      'A battered steel locket depicts two images - one is someone who has died, and the other, someone who\'s about to die',
                      'A pouch of ashes; when a pinch is thrown on the ground, it forms a specific word or symbol'],
           'Useless':['Large pile of dried assassin vines',
                      'A map of your childhood bedroom',
                      'A large fake beholder made of straw and cloth',
                      'Two hundred rusty nails',
                      'A pair of broken bellows with a spider living inside',
                      'A set of false teeth in a jar labeled "teeth of Olath the terrible"',
                      'A bald mop with the word "Karreen" scratched into the handle',
                      'A broken bucket plugged up with an old oily scrap of ermine',
                      'A 4-pint tankard with a hole in the bottom',
                      'Sixteen clay stirge statues',
                      'A jar of ointment labelled "pig soother"',
                      'A scarf made of owlbear fur that is incredibly itchy',
                      'A mirror with the words "I am the most" written on the face in Goblin',
                      'Two dozen stuffed mice in a clay jar',
                      'A flag of no discernable country',
                      'Seven chess boards all broken in half with dried blood on them',
                      'A large pile of worn flagstones labelled "trap this way up"',
                      'A broken stone lintel from a window or stove',
                      'A mummified rat corpse astride a ship in a bottle',
                      'A very poor painting of a sheep',
                      'A pair of billhooks bent into the shape of a heart',
                      'Two large dried catfish with mousetraps in their mouths',
                      'A pair of papier-mache greataxes',
                      'A huge stuffed hippogriff with a treasure chest instead of a head',
                      'A stained glass window depicting a prancing spider eater',
                      'A mop bucket filled with giant frogspawn',
                      'A necklace of troll teeth',
                      'Ninety-seven dead large centipedes on a hat pin',
                      'A glass helm',
                      'A statue of a gargoyle with eleven heads',
                      'A small collection of mildewed tomes about cheese',
                      'Six badger leg bones in a leather bag',
                      'A cat saddle',
                      'Three melted iron bottle stoppers labelled "efreeti! - do not remove"',
                      'A pair of theatrical shields made of cotton',
                      'An enormous cheese-grater for a Huge or larger creature',
                      'A huge iron collar',
                      'A collection of various-sized manticore spikes',
                      'A headless hammer',
                      'A wooden carving of the tarrasque',
                      "An executioner's hood with the eyeholes sewn up",
                      'Four hundred and eight spent sunrods',
                      'A wand of magic missile with no charges',
                      'Two naga skeletons on wooden frames',
                      'A clock face set to 4:00',
                      'A collection of clothes pegs of Huge size',
                      'An hourglass without sand',
                      'A halfling clay pipe with two stems',
                      'A set of breeches for a storm giant',
                      'Thirteen black cat silhouettes made of iron',
                      'The stretched skin of an otyugh',
                      "A ship's anchor that has been broken in two",
                      'A large glass eye with a slit instead of a round pupil',
                      'An octopus tentacle painted yellow',
                      'A long bench covered with obscene graffiti in Aquan',
                      'A 10-foot long wooden shortsword',
                      'A wardrobe filled to the brim with hats of various descriptions',
                      'Two drawers of carefully wrapped deceased stiffened Large snakes',
                      'A pillow stuffed with cockatrice feathers and labelled as such',
                      'A broken window shutter with the word "Keep" written upon it',
                      'A scarecrow head in your likeness',
                      'A pantomime horse costume',
                      'A pantomime nightmare costume',
                      'Six corn dolls with rat skull heads',
                      'Five large knitted moons with cows jumping over, labeled "moooon"',
                      'A set of full plate for a ferret',
                      'A book with eleven recipes for chuul written in Infernal',
                      'A cowbell for a titanic cow',
                      'Three brass figurines of imps blowing raspberries at each other',
                      'A mask designed to look like a beholder with glass eyes on stalks',
                      'A 12-pound green candle',
                      'A carved wooden loaf of bread 6 feet wide',
                      'A pair of iron spoons, one marked "good" and one marked "bad"',
                      'A doormat with "not welcome" written on it in Goblin',
                      'A large jar of liquefied grick going slightly mouldy',
                      'Three painted blue harps without strings',
                      'A torn tapestry depicting a battle between badgers and mummies',
                      'A Tiny ale tankard incorrectly stating that it holds a quart',
                      'A selection of rusty bent saws',
                      'A battered carpet with "speak and I shall fly" written upon it',
                      'Thirty-seven stones carved to look like crows',
                      'Two hat-stands of enormous size',
                      'A black cloth bag filled with odd shoes and gloves',
                      'A flat cap made of dire rat skins',
                      'An often-repaired raft for a single Small creature with "da" painted on it',
                      'A small iron castle with a pair of iron dragons circling it',
                      'A charred piece of wood labelled "Last of Snurre\'s Steading"',
                      'A small chest filled with lead discs',
                      'An empty jar labelled "do not open, contains wail of the banshee"',
                      'An owl teddy bear of great size, possibly for a giant child',
                      'A roc-call whistle without a pea but labelled as such',
                      'A pair of fishing flies made from griffon feathers',
                      'A 20-foot iron ladder which deliberately only has three rungs',
                      'A stirge mobile made of wax',
                      'A set of iron shoes with steel laces',
                      'A jar with eleven eyes in it labelled "Uncle Orb RIP"',
                      'A wooden earring carved in the likeness of an anvil and axes',
                      'A battered steel horn labelled "call of the xorn"',
                      'A weather vane depicting a beholder chasing gnomes',
                      'A miniature iron golem carved to look like a milk-maid'],
           'Less-useful':['Bagpipe made from a dead roper',
                          'Knitted nightmare with red wool flames',
                          'Bucket of horseshoes that have been cut in half',
                          "Giant's coat hanger made of dire boar tusks",
                          "Large model of a hill giant's stockade constructed of spent torches",
                          'Pair of shields decorated with chicken motifs',
                          'Unusable ten-bladed scimitar labeled "Deathreaper" on each blade in mystic runes',
                          'Painting of an yrthak ridden by gnomes',
                          'Eleven left boots',
                          'Outrageously colorful outfit of hat, cloak, and breeches sewn with peacock feathers and labelled "Property of Ceswick the Dowdy"',
                          'Sixty-eight wooden spoons painted green and numbered 12 through 80',
                          'Impossibly wide-brimmed hat fitted for a small humanoid head and covered in pictures of steaming pies',
                          'Quartet of cartoons depicting gnomes with their noses held aloft on stilts',
                          'Huge left boot made to resemble a house',
                          'Life-sized topiary badger',
                          'Two stuffed bugbears that, by the look of them, might have been used as toys by a giant child',
                          'Skull set with cheap fake gemstones, labeled "swearskull" in Orc',
                          'Pair of 12-foot-high knitting needles',
                          'Set of shocker lizard toys',
                          'Large pot of purple ink',
                          'Stone helm fashioned like a hydra with the Goblin inscription "To Jhazaan XXXII, on the occasion of her fifth birthday - Roar! Roar! Roar!"',
                          'Bucket of gorgon scales',
                          'Collection of lewd kobold statuettes',
                          'Daisy chain made of dead centipedes',
                          'Clay helm',
                          'Bag of bent and rusted iron spikes',
                          'Huge bucket filled with dried and flattened frogs',
                          'Double-ended trumpet',
                          'Ninety-eight clay naga miniatures',
                          'Twelve broken broomsticks stuffed in a tall, pointy black hat',
                          'Lute decorated with leopard fur and missing its strings',
                          "Large dead constrictor snake with a gnome-shaped bulge in the middle (actually a dressmaker's dummy)",
                          'Huge copper plug for a colossal sink',
                          'Fur hat large enough for two small creatures to camp under',
                          'Milk churn full of stuffed voles',
                          'Trio of candlesticks made from mummified rats',
                          'Length of bunting with the words "Welcome home, Hubert" on it',
                          'Ornate, bat-themed mirror with engraving that reads "only reflects vampires"',
                          "Selection of miniature toy alchemist's tools and nonmagical potions",
                          'Kite made to resemble a gnome riding a badger',
                          'Wicker fireguard',
                          'Beaten-copper tojanida-shaped lamp stand and matching wash-basin',
                          'Quartet of silhouette puppets made to look like otyughs',
                          'Four jars labelled "kobold repellant" and filled with soap',
                          'Legless tabletop painted in yellow and blue stripes',
                          'Huge book filled with pressed and dried assassin vines',
                          'Pile of mummy wrappings',
                          'Fake wooden pie of considerable size that smells like ale',
                          'Locathah sock puppet',
                          'Two-foot-long wooden baton carved at one end to resemble a tongue',
                          'Chess set carved to resemble gelatinous cubes and black puddings',
                          'Trio of embroidered pictures of a blue manticore in flight',
                          'Giant eagle feather',
                          'Dead mephit squished flat and inflated like a balloon',
                          'Sack full of two-inch lengths of string',
                          'Poem written on parchment which claims to reveal "the location of the Machine of Lum the Mad"',
                          'Tin torch sconce in the shape of an illithid head',
                          'Twenty-foot-long hunting horn',
                          'Large wooden skunk',
                          'Twelve black sheepskins',
                          'Iron goblet carved to resemble a crow',
                          'Staff with the words "Mnnmff Phatarn" carved on its sides over and over',
                          'Sheperd\'s crook with the words "Beware Zed, Prince of Rams" carved on its crook',
                          'Battle helm for a dire bear',
                          "Pair of giant's socks with many sewn holes and a family of cats living inside them",
                          'Jar of perfume labeled "Elixir of the Planes"',
                          'Red scarf with tassels made to look like roper tentacles',
                          'Mangle with a battleaxe stuck halfway through it',
                          'Twenty gravestones with spelling errors riddling the epitaphs',
                          'Fake skybleeder larva made from an inflated pigskin embroidered with strips of seaweed',
                          'Book of obscure heraldic symbols that incorporate unlikely devices, such as Girallon Rampant, Polar Bear Passant, Gelatinous Cube Courant...',
                          'Pit fiend scarecrow',
                          'Collection of bent forks in a scroll case labeled, "Don\'t forget to eat!"',
                          'Large collection of ferret masks, ferret costumes, and ferret puppets in a ferret-shaped trunk',
                          'Set of manacles for a six-armed creature',
                          'Bag of dried acorns',
                          'Tome titled "The Tale of Zord, Mightiest of the Yak Folk"',
                          'Weathered chapbook of what appears to be modron poetry',
                          'Huge, elaborate xorn puppet held aloft on great poles',
                          'Tankard filled with lard',
                          'Set of maps of duck ponds of various sizes in dangerous regions',
                          'Dwarven hat stand',
                          'Small set of modular steps for a halfling, complete with wheels',
                          'Eighty pebbles arranged by size and kept in separate bags',
                          'Welcome mat with "leave or die" written in Goblin',
                          'Book telling the story of Prince Rosewater, Lord of the mighty order of Celestial Kobold Paladins',
                          'Pillow stuffed with hippogriff feathers',
                          'Pile of stone cubes, each emblazoned with with a different letter',
                          'Trio of broken dungeon doors',
                          'Milking stool labeled "Property of Tom Huddle"',
                          'Belaying cleat, broken section of a pier, and severed rope, all still tied together',
                          'Large pile of ornate and colorful tiles bearing designs of writhing green worms',
                          'What appears to be a giant mouse wheel made of cart wheels, timbers, and rope',
                          'Chest full of broken swords',
                          'Selection of nasty-looking clown costumes sized for gnomes',
                          'Quartet of mind flayer masks',
                          'Stained-glass window depicting huge, bat-mounted goblins chasing gnomes riding enormous hedgehogs',
                          'Large glass jar containing a live slithering tracker',
                          'Moveable coat hanger for a person with three heads',
                          'Pantomime hellhound costume'],
           'Wizardly':['Moth-eaten barghest pelt used as a table covering',
                       'Boots made from baby dragon skin',
                       'Articulated brass shield-guardian arm',
                       'Stuffed grig in a fierce pose',
                       'A petrified succubus head',
                       'Jar of roper filaments in murky oil',
                       'Dried gorgonbane tea leaves (adv on saves vs petrification for 24 hrs)',
                       'Single fiendish wasp in a honey jar, with holes punched in the top',
                       'Tapestry depicting a fight between two warriors. The scene changes incrementally from one viewing to the next.',
                       'Gold apple with a gold worm inside',
                       'Stirge mounted on a plaque, engraved with the name "Stabby"',
                       'Cracked shield mounted on the wall and emblazoned with a rampant boar',
                       'Glass angel-shaped oil lamp',
                       'Dissected imp pinned to a board',
                       'Wooden box containting a set of surgical tools and a mostly-used bottle of oil of magic weapon with enough left for one piece of ammunition',
                       'Spent wand made of redwood and inlaid with chips of jade',
                       'Potted assassin vine seedling that undulates and can trap mice or fingers',
                       'Mithral spyglass with blue lenses',
                       'Adamantine cage for a cat-sized animal',
                       'Darkwood violin',
                       'Jug of green slime along with two partially-dissolved paintbrushes',
                       'Green glass goggles',
                       'Diary with most of its pages ripped out. The remaining page reads, "Today I, Mordenkainen d\'Phiarlan, begin to record my epic progress towards world domination..."',
                       'Animated satin-covered stool',
                       'Masterwork sextant',
                       'Quarter-inch lump of ochre jelly, squirming around in a glass flask sealed with lead',
                       'Defaced holy symbol of Dol Arrah',
                       'Silk shawl patterned with images of yochlols and made of drider silk',
                       'Shattered ioun stone',
                       'Cracked crystal that makes skin tingle when touched',
                       'Large petrified dragonfly used as a table',
                       'Lead mold for a ring carved with manticore designs',
                       'Small sketchbook filled with unlabeled pictures of otherworldly beings',
                       'Basilisk egg that has been drained through a tiny hole',
                       'Pipe with a bowl carved in the shape of a nameless squid god',
                       'A bird perch made from achaierai bone',
                       'Elaborately carved hourglass filled with opalescent silt',
                       'Howler skull with continual flame cast on it',
                       'Deck of cards bearing illustrations of constellations',
                       'A stack of books on alchemy infested with tiny shrieker sporelings',
                       "Storm giant's molar that lets off tiny bolts of electricity when metal is nearby",
                       'Clay jar of stale gorgon breath',
                       'Mummified hawk',
                       'Dried hellhound paw on a chain, with several large keys attached to it',
                       'Small amber sculpture of a lillend',
                       'Silent whistle that only blink dogs can hear',
                       'Statue of a voluptuous orc goddess',
                       'Fist-sized dodecahedron carved from a shard of obsidian',
                       'Dinosaur tooth',
                       'Murky, algae-infested tank swarming with illithid tadpoles',
                       'Miniature portrait of a beautiful young noblewoman. On the back are the words "To the charming scholar who has bound my heart."',
                       'Tiny lightning bolt ricocheting around inside a green glass ball. If the ball is smashed, the bolt strikes the nearest creature for 1d4+1 points of lightning damage',
                       'Larval rust monster set up for dissection',
                       'Clay seals with the name Hektula written in Infernal',
                       'Pseudodragon skeleton mounted in a childish diorama',
                       'Alchemically silvered hypodermic needle containing a magically preserved red slaad egg',
                       'Small cactus in a pot sculpted into a leering demon face',
                       'Umber hulk claw in the process of being fashioned into a shield',
                       'Nonmagical stainless steel flask emblazoned with a stylized tarrasque',
                       'Chunk of glass with an eye in it. The eye turns to follow whoever is closest to it.',
                       'Box filled with clay beads inscribed with draconic letters',
                       'A small box growing spotty orange mushrooms, along with an ashtray filled with chewed mushroom stems',
                       'A chapbook of hymns to the Mockery',
                       'A masterwork morningstar being used as a fire poker',
                       'Scale model of a palace labeled "My Future Home"',
                       'Two couatl feathers prepared as quills',
                       'Half-finished scroll of fireball',
                       'Twitching length of kyton chain',
                       'Animated monkey skeleton',
                       'Copper dragon scale holding a moldy wedge of cheese',
                       'Bonsai tree sculpted in the shape of a harpy',
                       'Massive tome on diabolical contracts. Pressed between its pages like a flower is the corpse of a long-dead kobold.',
                       'A book of elven love poems',
                       'Broken homunculus in a box',
                       'Severed gargoyle claw being used as a paperweight',
                       'Cracked stone cylinder engraved with glyphs. The glyphs tell the story of the Crimson Covenant lich whose phylactery it once was.',
                       'Fire-blackened nightmare hoof',
                       "Lock of nymph's hair in a small, velvet-lined jewelry box",
                       'Purple worm stinger wedged in a leathery chunk of dragon hide',
                       'Pan pipes attached to a bellows contraption mounted on a small bicycle',
                       'Sealed glass trunk full of spider eater eggs',
                       'Gold-plated unicorn horn',
                       'Drinking mug fashioned out of a troll skull and lined with patterned lead',
                       'Slate covered with ideographic equations in bioluminescent chalk',
                       'Ivory cane topped with a silver sphinx',
                       'Tiny stone teapot shaped like a grinning, portly goblin',
                       'What appears to be a hot round rock in a stone box, but is actually a thoqqua egg',
                       'Rug woven with kaleidoscopic patterns that change over time',
                       'Living vargouille attached to a three-foot long chain ending in a large iron weight',
                       'Diminutive model windmill that generates tiny fields of electricity, heat, or cold',
                       'Sealed glass tubes filled with free-floating dancing lights',
                       'Silver pyramid frame, one foot on a side, with a plate of food inside',
                       'Crystal that generates a diminutive illusion of a dragon when light shines on it',
                       'Ebonwood carving of a xill',
                       'Mirror endowed with an illusion that makes the owner appear to be standing behind anyone looking into it',
                       "Small porcelain statue of a unicorn marked with all the standard butcher's cuts in dotted red lines",
                       "Piece of paper listing the party's names. Next to their names are the names of their friends and family.",
                       'Half-finished painting of an alien landscape. At the center of the landscape stands a single young girl dressed in white and holding a large leather tome tightly to her chest.',
                       'Barrel filled with roc feathers',
                       'Dried toad on a leather thong. The name "Spivey" is inked on the toad.'],
           'Bookshelves':['A set of "books" that is actually a disguised drawer',
                          'A set of sopping wet, ruined books',
                          'Dried gore encrusting shattered jars',
                          'Several rows of tightly rolled scrolls',
                          'Numerous framed anatomical sketches',
                          'A set of heavy tomes, each detailing a different creature - some real, some imaginary',
                          'A worn box of soil filled with thick yellow grass',
                          'A frame with two pictures - one of a small girl and the other of a bifurcated skull',
                          'A pile of worm-eaten books that fall apart when disturbed',
                          'Two dozen prayer books written in Celestial',
                          'A set of books containing only pictures',
                          'A trio of books with the corners of all the pages trimmed off',
                          'A tiny bed',
                          'A simple hourglass and a large origami lily',
                          'Half a dozen small, pocket-sized books',
                          'Three delicate porcelain dolls in elegant lace dresses, with their faces deliberately sanded off',
                          'A series of books ruined by a thick green-white fungus',
                          'Librettos from several well-known dwarven operas',
                          'Six books constructed of copper plates and perforated with Terran text',
                          'A glob of multicolored melted wax',
                          'A handful of books, their contents rendered undreadable by long-dried, red-brown ichor',
                          'Several dozen copies of the same priestly chapbook, extolling the virtues of the benevolent church of the Pure Flame',
                          "A pile of books that has been hollowed out into a rats' nest",
                          'A pair of bookends stylized as rampant lions',
                          'A plank of wood from which sprout numerous roots and budding leaves',
                          'A number of quartos containing several handwritten plays',
                          'Three massive history books, each almost a perfect 2-foot cube',
                          'Three rows of skulls, each from a different creature',
                          'An empty horizontal wooden rack for a curved sword',
                          'Three stacks of neatly folded shirts and pants',
                          'Two dozen volumes of excessively sentimental poetry',
                          'A series of holy writings, each defaced with childish and offensive charcoal drawings',
                          'A thick steel panel and a sturdy lock bind several tomes together',
                          'Twenty bottles of unlabeled multicolored liquids',
                          'A tome encased in a thick block of ice',
                          'Hundreds of pages of mathematical calculations',
                          "A large aquarium, murky with algae - bubbles irregularly break the water's surface",
                          'Dozens of crudely made stuffed animals',
                          'Thirteen novels of poorly written fiction',
                          'An empty journal that glows when opened - enough to read by',
                          'Nearly two hundred thin, brightly colored folios',
                          'A pot of pungent vanilla potpourri',
                          'Three hat boxes, each containing a mummified kobold head',
                          'An ancient atlas, the maps within bearing no resemblance to the known world',
                          'A sculpture of a dismembered human torso',
                          'Eighteen years of ledgers from a profitable butcher shop',
                          'A "Dear John" letter, written in Goblin',
                          'A set of history books with vast sections cut out',
                          'A collection of halfling cookbooks',
                          'Half a dozen journals that have been scrawled through, repeating the word "betrayer" countless times in dark red ink',
                          'A set of simple reading primers',
                          'Stacks of tawdry yellowed romance paperbacks',
                          'A number of books that have been reduced to ash, with only blackened covers remaining',
                          'A series of travelogues written in Infernal',
                          'A variety of maps of the local region',
                          'Numerous rolls of papyrus outline a particularly harsh code of laws in Draconic',
                          'A collection of delicate, spotless wine flutes',
                          "A wooden case within which books don't age, molder, or grow dusty, and can't get wet. Two ancient Dhakaani tomes that look practically new attest to the case's properties.",
                          'The fragments of four shattered marble busts',
                          'A crate of various kinds of fresh fruit',
                          'A set of books made of large white leaves',
                          'A miniature shrine to the Keeper',
                          'A scroll case that bursts into flames when touched, immolating its contents',
                          "A particularly libidinous autobiography penned by Queen Aurala ir'Wynarn of Aundair",
                          'Several detailed family histories',
                          'A dozen miniature ships in glass bottles',
                          'A set of texts comprising an extensive medical library',
                          'A dense iron safe, 1 cubic foot in volume',
                          'Numerous tomes of outrageous and wholly faulty arcane theories',
                          'Death records from a nearby town, dating back nearly a hundred years',
                          'Hundreds of tiny glass animals',
                          'A collection of geodes and shiny rocks',
                          'Several large clam shells, etched with the names of all those who have looked upon them',
                          'A variety of treatises on mining and blacksmithing',
                          'Eight fake books that are nothing more than wooden carvings',
                          'A collection of aerial navigation charts',
                          'Two complete quasit skeletons, each mounted on a stand',
                          'An empty, padded scroll case',
                          'Several detailed maps of an unnamed island',
                          'A dozen cookbooks focusing on ways to prepare horse',
                          'A set of grimoires bound in the stitched skins of sentient creatures',
                          'Alchemical equipment interconnected with glass tubes',
                          'Piles of insect carapaces',
                          'A set of books whose text only reveals itself to creatures of lawful alignment. Readers of other alignments see only blank pages.',
                          'A series of books set in mirror-image typeface',
                          'Dozens of bottles, each filled with a tiny humanoid skeleton',
                          'A prayer book of the Sovereign Host. Upon opening it, a disembodied voice begins reading from the text.',
                          'Numerous shattered display bottles labeled "danger"',
                          'A deck of disturbingly illustrated cards wrapped within a silk scarf',
                          'An ornate metallic skull that floats six inches above whatever surface it is placed upon, and which rotates to watch passersby',
                          'A series of seven books, each of which casts a random 1st-level spell from the wizard spell list on any creature who opens it, then crumbles to dust after the spell is cast',
                          "A row of fifteen scrapbooks filled with patches from children's clothing",
                          'A massive book with a strange starlike rune emblazoned upon the cover',
                          'The text within this set of five books changes each time they are opened'],
           }
alltrinkets = []
for key in trinket.keys():
    for i in range(len(trinket[key])):
        alltrinkets.append(trinket[key][i])
trinket['Everice'] = trinket['Frostfell']

#%% Bookshelf contents

books = ['Tome titled "The Tale of Zord, Mightiest of the Yak Folk"',
         'Weathered chapbook of what appears to be modron poetry',
         'Book of obscure heraldic symbols that incorporate unlikely devices, such as Girallon Rampant, Polar Bear Passant, Gelatinous Cube Courant...',
         'Poem written on parchment which claims to reveal "the location of the Machine of Lum the Mad"',
         'Huge book filled with pressed and dried assassin vines',
         'Quartet of cartoons depicting gnomes with their noses held aloft on stilts',
         'A book with eleven recipes for chuul written in Infernal',
         'A small collection of mildewed tomes about cheese',
         'A small leather journal contains a poem, story, or piece of music by a beloved creator - written after they died',
         'A small notebook that causes anything written in it to disappear after 1 hour',
         'A small illustrated book of Farlnen myths that has pages missing',
         'A small book containing pressed and dried botanical samples',
         'A book titled "Conversational Giant"',
         'A user\'s manual for a warforged colossus',
         'A dozen flyers for a local Zil food place',
         'A note in your own hand that you don\'t remember writing',
         'The left half of a map',
         'The right half of a map',
         'A book of adventures for children',
         'A box containing a torn-up letter',
         'An old contract marked "Void"',
         'A recipe book for cooking with mushrooms',
         'One expired coupon for "A Free Cornerstone"',
         'A letter written by Merrix d\'Cannith',
         'The deed and title to an abandoned windmill and three acres of tillable land that you\'ve never been able to find',
         'A menu from Big Daddy Donaar\'s Yum Yum Hut',
         'A diagram for a new war lute',
         'A declaration of war against a nation no one has ever heard of',
         'A romance chapbook written in Undercommon titled "Just one Layer of Grey"',
         'A journal filled with poetry hand-written in Primordial',
         'A shark tooth covered in tiny etched words from a lost language',
         'An expedition log with missing pages and a pressed flower used as a bookmark',
         'A blank piece of wet parchment that never seems to dry',
         'A book filled with writing that only appears when the book is held underwater',
         'A sealed envelope made of red leather that you haven\'t been able to open, but which smells of a campfire',
         'A journal that has been heavily redacted',
         'The deed to someplace called Tergeron Manor',
         'An ornate, wax-sealed crimson envelope that resists all attempts to open it',
         'The logbook of an ice-breaking ship called The Haifisch',
         'A small, worn book of children\'s nusery rhymes',
         'A little black book that records your dreams, and yours alone, when you sleep',
         'The unopened letter to you from your dying father',
         'A single page from a giant wizard\'s spellbook, bearing an incomplete spell',
         'A scrap of parchment, part of a map of Stormreach',
         'A small book entitled "Feersome Beests of Zendrik"',
         'A leather-bound collection of kalashtar poetry called "Shards of the Light"',
         'A polished crystal sphere; when you clutch it in your fist, a telepathic voice recites a story in your mind',
         'A small journal with leathery pages; any words you write in it slowly disappear',
         'A small journal made from preserved leaves',
         'A book of poetry written by undead elves',
         'A book that tells the story of a legendary hero\'s rise and fall, with the last chapter missing',
         'A sheet of parchment upon which is drawn a complex mechanical contraption',
         'An invitation to a party where a murder happened',
         'Half of a floorplan for a temple, castle, or some other structure',
         'A receipt of deposit at a bank in a far-flung city',
         'A diary with seven missing pages',
         'A four-leaf clover pressed inside a book discussing manners and etiquette',
         'A fragment of a beautiful song, written as musical notes on two pieces of parchment',
         'An indecipherable treasure map',
         'A blank book whose pages refuse to hold ink, chalk, graphite, or any other substance or marking',
         'The deed for a parcel of land in a realm unknown to you',
         'A diary written in a language you don\'t know',
         '"A Brief History of Galifar" by Bal Thurin', # Morgrave Miscellany
         '"Beginner\'s Guide to Prophecy" by Ohnal Caldyn', # Morgrave Miscellany
         '"Arcane Anomalies and You" by Professor Tym Bessel', # Morgrave Miscellany
         '"Galifar Evolved" by Professor Ange Thornlong', # Morgrave Miscellany
         '"Heroines & Heretics in the Modern World" by Sharn Inquisitive Jerion Phious', # Morgrave Miscellany
         '"An Oratory Opus" by Lord Dirge Tiriandara d\'Kundarak', # Morgrave Miscellany
         '"Pulpits or Puppets" by Sharn Inquisitive Jerion Phious', # Morgrave Miscellany
         '"Seven Schools: Basics of Arcane Principles" by Cord Ennis', # Morgrave Miscellany
         '"Analects of War" by Karrn the Conqueror', # Morgrave Miscellany
         '"A Kink in the Cogs: A Narrative on the Political Underbelly of the Five Nations" by Ytur Enitas & Ezam Anacra', # Morgrave Miscellany
         '"Competition in Callestan" by Tig Boromar', # Morgrave Miscellany
         '"Cyre and Loathing" by Kessler', # Morgrave Miscellany
         '"Malleon\'s Legacy" by Jolan Hass Holan', # Morgrave Miscellany
         '"The Broken Sword: Secrets of Sharn" by Kessler', # Morgrave Miscellany
         'Set of maps of duck ponds of various sizes in dangerous regions',
         'Book telling the story of Prince Rosewater, Lord of the mighty order of Celestial Kobold Paladins',
         'Diary with most of its pages ripped out. The remaining page reads, "Today I, Mordenkainen d\'Phiarlan, begin to record my epic progress towards world domination..."',
         'Small sketchbook filled with unlabeled pictures of otherworldly beings',
         'A stack of books on alchemy infested with tiny shrieker sporelings',
         'A chapbook of hymns to the Mockery',
         'Half-finished scroll of fireball',
         'Massive tome on diabolical contracts. Pressed between its pages like a flower is the corpse of a long-dead kobold.',
         'A book of elven love poems',
         'Cracked stone cylinder engraved with glyphs. The glyphs tell the story of the Crimson Covenant lich whose phylactery it once was.',
         'Slate covered with ideographic equations in bioluminescent chalk',
         'A set of "books" that is actually a disguised drawer',
         'A set of sopping wet, ruined books',
         'Several rows of tightly rolled scrolls',
         'Numerous framed anatomical sketches',
         'A set of heavy tomes, each detailing a different creature - some real, some imaginary',
         'A pile of worm-eaten books that fall apart when disturbed',
         'Two dozen prayer books written in Celestial',
         'A set of books containing only pictures',
         'A trio of books with the corners of all the pages trimmed off',
         'Half a dozen small, pocket-sized books',
         'A series of books ruined by a thick green-white fungus',
         'Librettos from several well-known dwarven operas',
         'Six books constructed of copper plates and perforated with Terran text',
         'A handful of books, their contents rendered undreadable by long-dried, red-brown ichor',
         'Several dozen copies of the same priestly chapbook, extolling the virtues of the benevolent church of the Pure Flame',
         "A pile of books that has been hollowed out into a rats' nest",
         'A number of quartos containing several handwritten plays',
         'Three massive history books, each almost a perfect 2-foot cube',
         'Two dozen volumes of excessively sentimental poetry',
         'A series of holy writings, each defaced with childish and offensive charcoal drawings',
         'A thick steel panel and a sturdy lock bind several tomes together',
         'A tome encased in a thick block of ice',
         'Hundreds of pages of mathematical calculations',
         'Thirteen novels of poorly written fiction',
         'An empty journal that glows when opened - enough to read by',
         'Nearly two hundred thin, brightly colored folios',
         'An ancient atlas, the maps within bearing no resemblance to the known world',
         'Eighteen years of ledgers from a profitable butcher shop',
         'A "Dear John" letter, written in Goblin',
         'A set of history books with vast sections cut out',
         'A collection of halfling cookbooks',
         'Half a dozen journals that have been scrawled through, repeating the word "betrayer" countless times in dark red ink',
         'A set of simple reading primers',
         'Stacks of tawdry yellowed romance paperbacks',
         'A number of books that have been reduced to ash, with only blackened covers remaining',
         'A series of travelogues written in Infernal',
         'A variety of maps of the local region',
         'Numerous rolls of papyrus outline a particularly harsh code of laws in Draconic',
         "A wooden case within which books don't age, molder, or grow dusty, and can't get wet. Two ancient Dhakaani tomes that look practically new attest to the case's properties.",
         'A set of books made of large white leaves',
         "A particularly libidinous autobiography penned by Queen Aurala ir'Wynarn of Aundair",
         'Several detailed family histories',
         'A set of texts comprising an extensive medical library',
         'Numerous tomes of outrageous and wholly faulty arcane theories',
         'Death records from a nearby town, dating back nearly a hundred years',
         'A variety of treatises on mining and blacksmithing',
         'Eight fake books that are nothing more than wooden carvings',
         'A collection of aerial navigation charts',
         'Several detailed maps of an unnamed island',
         'A dozen cookbooks focusing on ways to prepare horse',
         'A set of grimoires bound in the stitched skins of sentient creatures',
         'A set of books whose text only reveals itself to creatures of lawful alignment. Readers of other alignments see only blank pages.',
         'A series of books set in mirror-image typeface',
         'A prayer book of the Sovereign Host. Upon opening it, a disembodied voice begins reading from the text.',
         'A series of seven books, each of which casts a random 1st-level spell from the wizard spell list on any creature who opens it, then crumbles to dust after the spell is cast',
         "A row of fifteen scrapbooks filled with patches from children's clothing",
         'A massive book with a strange starlike rune emblazoned upon the cover',
         'The text within this set of five books changes each time they are opened',
         ]
trinket['Books'] = books # add list of books to trinket dictionary
for i in range(len(books)):
    alltrinkets.append(books[i]) # append list of books to list of all trinkets

#%% Gems

gem = {}
gem['10 gp']   = ['Azurite',
                  'Banded agate',
                  'Blue quartz',
                  'Eye agate',
                  'Hematite',
                  'Lapis lazuli',
                  'Malachite',
                  'Moss agate',
                  'Obsidian',
                  'Rhodochrosite',
                  'Tiger eye',
                  'Turquoise']
gem['50 gp']   = ['Bloodstone',
                  'Carnelian',
                  'Chalcedony',
                  'Chrysoprase',
                  'Citrine',
                  'Jasper',
                  'Moonstone',
                  'Onyx',
                  'Quartz',
                  'Sardonyx',
                  'Star rose quartz',
                  'Zircon']
gem['100 gp']  = ['Amber',
                  'Amethyst',
                  'Chrysoberyl',
                  'Coral',
                  'Garnet',
                  'Jade',
                  'Jet',
                  'Pearl',
                  'Spinel',
                  'Tourmaline']
gem['500 gp']  = ['Alexandrite',
                  'Aquamarine',
                  'Black pearl',
                  'Blue spinel',
                  'Peridot',
                  'Topaz']
gem['1000 gp'] = ['Black opal',
                  'Blue sapphire',
                  'Emerald',
                  'Fire opal',
                  'Opal',
                  'Star ruby',
                  'Star sapphire',
                  'Yellow sapphire']
gem['5000 gp'] = ['Black sapphire',
                  'Diamond',
                  'Jacinth',
                  'Ruby']
gemvals = ['10 gp', '50 gp', '100 gp', '500 gp', '1000 gp', '5000 gp']

gemdesc = {}
gemdesc['Azurite'] = 'opaque mottled deep blue'
gemdesc['Banded agate'] = 'translucent striped brown, blue, white, or red'
gemdesc['Blue quartz'] = 'transparent pale blue'
gemdesc['Eye agate'] = 'translucent circles of gray, white, brown, blue, or green'
gemdesc['Hematite'] = 'opaque gray-black'
gemdesc['Lapis lazuli'] = 'opaque light and dark blue with yellow flecks'
gemdesc['Malachite'] = 'opaque striated light and dark green'
gemdesc['Moss agate'] = 'translucent pink or yellow-white with mossy gray or green markings'
gemdesc['Obsidian'] = 'opaque black'
gemdesc['Rhodochrosite'] = 'opaque light pink'
gemdesc['Tiger eye'] = 'translucent brown with golden center'
gemdesc['Turquoise'] = 'opaque light blue-green'
gemdesc['Bloodstone'] = 'opaque dark gray with red flecks'
gemdesc['Carnelian'] = 'opaque orange to red-brown'
gemdesc['Chalcedony'] = 'opaque white'
gemdesc['Chrysoprase'] = 'translucent green'
gemdesc['Citrine'] = 'transparent pale yellow-brown'
gemdesc['Jasper'] = 'opaque blue, black, or brown'
gemdesc['Moonstone'] = 'translucent white with pale blue glow'
gemdesc['Onyx'] = 'opaque bands of black and white, or pure black or white'
gemdesc['Quartz'] = 'transparent white, smoky gray, or yellow'
gemdesc['Sardonyx'] = 'opaque bands of red and white'
gemdesc['Star rose quartz'] = 'translucent rosy stone with white star-shaped center'
gemdesc['Zircon'] = 'transparent pale blue-green'
gemdesc['Amber'] = 'transparent watery gold to rich gold'
gemdesc['Amethyst'] = 'transparent deep purple'
gemdesc['Chrysoberyl'] = 'transparent yellow-green to pale green'
gemdesc['Coral'] = 'opaque crimson'
gemdesc['Garnet'] = 'transparent red, brown-green, or violet'
gemdesc['Jade'] = 'translucent light green, deep green, or white'
gemdesc['Jet'] = 'opaque deep black'
gemdesc['Pearl'] = 'opaque lustrous white, yellow, or pink'
gemdesc['Spinel'] = 'transparent red, red-brown, or deep green'
gemdesc['Tourmaline'] = 'transparent pale green, blue, brown, or red'
gemdesc['Alexandrite'] = 'transparent dark green'
gemdesc['Aquamarine'] = 'transparent pale blue-green'
gemdesc['Black pearl'] = 'opaque pure black'
gemdesc['Blue spinel'] = 'transparent deep blue'
gemdesc['Peridot'] = 'transparent rich olive green'
gemdesc['Topaz'] = 'transparent golden yellow'
gemdesc['Black opal'] = 'translucent dark green with black mottling and golden flecks'
gemdesc['Blue sapphire'] = 'transparent blue-white to medium blue'
gemdesc['Emerald'] = 'transparent deep bright green'
gemdesc['Fire opal'] = 'translucent fiery red'
gemdesc['Opal'] = 'translucent pale blue with green and golden mottling'
gemdesc['Star ruby'] = 'translucent ruby with white star-shaped center'
gemdesc['Star sapphire'] = 'translucent blue sapphire with white star-shaped center'
gemdesc['Yellow sapphire'] = 'transparent fiery yellow or yellow-green'
gemdesc['Black sapphire'] = 'translucent lustrous black with glowing highlights'
gemdesc['Diamond'] = 'transparent blue-white, canary, pink, brown, or blue'
gemdesc['Jacinth'] = 'transparent fiery orange'
gemdesc['Ruby'] = 'transparent clear red to deep crimson'

def gem_treasure(gemval='random', describe=False):
    if gemval == 'random': gemval = rng.choice(gemvals)
    gemchosen = rng.choice(gem[gemval])
    text = gemval + ' ' + gemchosen
    if describe: text += ' (' + gemdesc[gemchosen] + ')'
    return text

#%% Art Objects

art = {}
art['25 gp']   = ['Silver ewer',
                  'Carved bone statuette',
                  'Small gold bracelet',
                  'Cloth-of-gold vestments',
                  'Black velvet mask stitched with silver thread',
                  'Copper chalice with silver filigree',
                  'Pair of engraved bone dice',
                  'Small mirror set in a painted wooden frame',
                  'Embroidered silk handkerchief',
                  'Gold locket with a painted portrait inside']
art['250 gp']  = ['Gold ring set with bloodstones',
                  'Carved ivory statuette',
                  'Large gold bracelet',
                  'Silver necklace with a gemstone pendant',
                  'Bronze crown',
                  'Silk robe with gold embroidery',
                  'Large well-made tapestry',
                  'Brass mug with jade inlay',
                  'Box of turquoise animal figurines',
                  'Gold bird cage with electrum filigree']
art['750 gp']  = ['Silver chalice set with moonstones',
                  'Silver-plated steel longsword with jet set in hilt',
                  'Carved harp of exotic wood with ivory inlay and zircon gems',
                  'Small gold idol',
                  'Gold dragon comb set with red garnets as eyes',
                  'Bottle stopper cork embossed with gold leaf and set with amethysts',
                  'Ceremonial electrum dagger with a black pearl in the pommel',
                  'Silver and gold brooch',
                  'Obsidian statuette with gold fittings and inlay',
                  'Painted gold war mask']
art['2500 gp'] = ['Fine gold chain set with a fire opal',
                  'Old masterpiece painting',
                  'Embroidered silk and velvet mantle set with numerous moonstones',
                  'Platinum bracelet set with a sapphire',
                  'Embroidered glove set with jewel chips',
                  'Jeweled anklet',
                  'Gold music box',
                  'Gold circlet set with four aquamarines',
                  'Eye patch with a mock eye set in blue sapphire and moonstone',
                  'A necklace string of small pink pearls']
art['7500 gp'] = ['Jeweled gold crown',
                  'Jeweled platinum ring',
                  'Small gold statuette set with rubies',
                  'Gold cup set with emeralds',
                  'Gold jewelry box with platinum filigree',
                  'Painted gold child\'s sarcophagus',
                  'Jade game board with solid gold playing pieces',
                  'Bejeweled ivory drinking horn with gold filigree']
artvals = ['25 gp', '250 gp', '750 gp', '2500 gp', '7500 gp']

def art_treasure(artval='random', dtype='none'):
    """
    artval = gp value of art: 25 gp, 250 gp, 750 gp, 2500 gp, or 7500 gp
    dtype = type of dragon to pick from: dragontypes, none, or random
    """
    if artval == 'random': artval = rng.choice(artvals)
    if dtype == 'none':
        artchosen = rng.choice(art[artval]) # choose from regular art objects
    elif dtype in dragontypes:
        artchosen = rng.choice(dart[dtype]) # choose from dragon art objects
    elif dtype == 'random':
        _ = rng.choice([True, False]) # random choice of dragon or regular
        if _: # dragon
            dtype = rng.choice(dragontypes) # random dragon type
            artchosen = rng.choice(dart[dtype])
        else: # regular
            tempval = rng.choice(artvals) # random value type
            artchosen = rng.choice(art[tempval])
    return artval + ' ' + artchosen

#%% Random Magic Item tables and weights

# Magic Item Tables A-I
itemA = ['Potion of healing',
         'Spell scroll (cantrip)',
         'Potion of climbing',
         'Spell scroll (1st level)',
         'Spell scroll (2nd level)',
         'Potion of greater healing',
         'Bag of holding',
         'Driftglobe']
itemA_w = [50, 60, 70, 90, 94, 98, 99, 100]
itemB = ['Potion of greater healing',
         'Potion of fire breath',
         'Potion of resistance',
         'Ammunition, +1',
         'Potion of animal friendship',
         'Potion of hill giant strength',
         'Potion of growth',
         'Potion of water breathing',
         'Spell scroll (2nd level)',
         'Spell scroll (3rd level)',
         'Bag of holding',
         'Keoghtom\'s ointment',
         'Oil of slipperiness',
         'Dust of disappearance',
         'Dust of dryness',
         'Dust of sneezing and choking',
         'Elemental gem',
         'Philter of love',
         'Alchemy jug',
         'Cap of water breathing',
         'Cloak of the manta ray',
         'Driftglobe',
         'Goggles of night',
         'Helm of comprehending languages',
         'Immovable rod',
         'Lantern of revealing',
         'Mariner\'s armor',
         'Mithral armor',
         'Potion of poison',
         'Ring of swimming',
         'Robe of useful items',
         'Rope of climbing',
         'Saddle of the cavalier',
         'Wand of magic detection',
         'Wand of secrets']
itemB_w = [15, 22, 29, 34, 39, 44, 49, 54, 59, 64, 67, 70, 73, 75, 77, 79, 81,
           83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99,
           100]
itemC = ['Potion of superior healing',
         'Spell scroll (4th level)',
         'Ammunition, +2',
         'Potion of clairvoyance',
         'Potion of diminution',
         'Potion of gaseous form',
         'Potion of frost giant strength',
         'Potion of stone giant strength',
         'Potion of heroism',
         'Potion of invulnerability',
         'Potion of mind reading',
         'Spell scroll (5th level)',
         'Elixir of health',
         'Oil of etherealness',
         'Potion of fire giant strength',
         'Quaal\'s feather token',
         'Scroll of protection',
         'Bag of beans',
         'Bead of force',
         'Chime of opening',
         'Decanter of endless water',
         'Eyes of minute seeing',
         'Folding boat',
         'Heward\'s handy haversack',
         'Horseshoes of speed',
         'Necklace of fireballs',
         'Periapt of health',
         'Sending stones']
itemC_w = [15, 22, 27, 32, 37, 42, 47, 52, 57, 62, 67, 72, 75, 78, 81, 84, 87,
           89, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]
itemD = ['Potion of supreme healing',
         'Potion of invisibility',
         'Potion of speed',
         'Spell scroll (6th level)',
         'Spell scroll (7th level)',
         'Ammunition, +3',
         'Oil of sharpness',
         'Potion of flying',
         'Potion of cloud giant strength',
         'Potion of longevity',
         'Potion of vitality',
         'Spell scroll (8th level)',
         'Horseshoes of a zephyr',
         'Nolzur\'s marvelous pigments',
         'Bag of devouring',
         'Portable hole']
itemD_w = [20, 30, 40, 50, 57, 62, 67, 72, 77, 82, 87, 92, 95, 98, 99, 100]
itemE = ['Spell scroll (8th level)',
         'Potion of storm giant strength',
         'Potion of supreme healing',
         'Spell scroll (9th level)',
         'Universal solvent',
         'Arrow of slaying',
         'Sovereign glue']
itemE_w = [30, 55, 70, 85, 93, 98, 100]
itemF = ['Weapon, +1',
         'Shield, +1',
         'Sentinel shield',
         'Amulet of proof against detection and location',
         'Boots of elvenkind',
         'Boots of striding and springing',
         'Bracers of Archery',
         'Brooch of shielding',
         'Broom of flying',
         'Cloak of elvenkind',
         'Cloak of protection',
         'Gauntlets of ogre power',
         'Hat of disguise',
         'Javelin of lightning',
         'Pearl of power',
         'Rod of the pact keeper, +1',
         'Slippers of spider climbing',
         'Staff of the adder',
         'Staff of the python',
         'Sword of vengeance',
         'Trident of fish command',
         'Wand of magic missiles',
         'Wand of the war mage, +1',
         'Wand of the web',
         'Weapon of warning',
         'Adamantine armor (chain mail)',
         'Adamantine armor (chain shirt)',
         'Adamantine armor (scale mail)',
         'Bag of tricks (gray)',
         'Bag of tricks (rust)',
         'Bag of tricks (tan)',
         'Boots of the winterlands',
         'Circlet of blasting',
         'Deck of illusions',
         'Eversmoking bottle',
         'Eyes of charming',
         'Eyes of the eagle',
         'Figurine of wondrous power (silver raven)',
         'Gem of brightness',
         'Gloves of missile snaring',
         'Gloves of swimming and climbing',
         'Gloves of thievery',
         'Headband of intellect',
         'Helm of telepathy',
         'Instrument of the bards (Doss lute)',
         'Instrument of the bards (Fochluan bandore)',
         'Instrument of the bards (Mac-Fuimidh cittern)',
         'Medallion of thoughts',
         'Necklace of adaptation',
         'Periapt of wound closure',
         'Pipes of haunting',
         'Pipes of the sewers',
         'Ring of jumping',
         'Ring of mind shielding',
         'Ring of warmth',
         'Ring of water walking',
         'Quiver of Ehlonna',
         'Stone of good luck',
         'Wind fan',
         'Winged boots']
itemF_w = [15, 18, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49,
           51, 53, 55, 57, 59, 61, 63, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74,
           75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91,
           92, 93, 94, 95, 96, 97, 98, 99, 100]
itemG = ['Weapon, +2',
         'Figurine of wondrous power (bronze griffon)',
         'Figurine of wondrous power (ebony fly)',
         'Figurine of wondrous power (golden lions)',
         'Figurine of wondrous power (ivory goats)',
         'Figurine of wondrous power (marble elephant)',
         'Figurine of wondrous power (onyx dog)',
         'Figurine of wondrous power (serpentine owl)',
         'Adamantine armor (breastplate)',
         'Adamantine armor (splint)',
         'Amulet of health',
         'Armor of vulnerability',
         'Arrow-catching shield',
         'Belt of dwarvenkind',
         'Belt of hill giant strength',
         'Berserker axe',
         'Boots of levitation',
         'Boots of speed',
         'Bowl of commanding water elementals',
         'Bracers of defense',
         'Brazier of commanding fire elementals',
         'Cape of the mountebank',
         'Censer of controlling air elementals',
         'Armor, +1 chain mail',
         'Armor of resistance (chain mail)',
         'Armor, +1 chain shirt',
         'Armor of resistance (chain shirt)',
         'Cloak of displacement',
         'Cloak of the bat',
         'Cube of force',
         'Daern\'s instant fortress',
         'Dagger of venom',
         'Dimensional shackles',
         'Dragon slayer',
         'Elven chain',
         'Flame tongue',
         'Gem of seeing',
         'Giant slayer',
         'Glamoured studded leather',
         'Helm of teleportation',
         'Horn of blasting',
         'Horn of Valhalla (silver)',
         'Horn of Valhalla (brass)',
         'Instrument of the bards (Canaith mandolin)',
         'Instrument of the bards (Cli lyre)',
         'Ioun stone (awareness)',
         'Ioun stone (protection)',
         'Ioun stone (reserve)',
         'Ioun stone (sustenance)',
         'Iron bands of Bilarro',
         'Armor, +1 leather',
         'Armor of resistance (leather)',
         'Mace of disruption',
         'Mace of smiting',
         'Mace of terror',
         'Mantle of spell resistance',
         'Necklace of prayer beads',
         'Periapt of proof against poison',
         'Ring of animal influence',
         'Ring of evasion',
         'Ring of feather falling',
         'Ring of free action',
         'Ring of protection',
         'Ring of resistance',
         'Ring of spell storing',
         'Ring of the ram',
         'Ring of X-ray vision',
         'Robe of eyes',
         'Rod of rulership',
         'Rod of the pact keeper, +2',
         'Rope of entanglement',
         'Armor, +1 scale mail',
         'Armor of resistance (scale mail)',
         'Shield, +2',
         'Shield of missile attraction',
         'Staff of charming',
         'Staff of healing',
         'Staff of swarming insects',
         'Staff of the woodlands',
         'Staff of withering',
         'Stone of controlling earth elementals',
         'Sun blade',
         'Sword of life stealing',
         'Sword of wounding',
         'Tentacle rod',
         'Vicious weapon',
         'Wand of binding',
         'Wand of enemy detection',
         'Wand of fear',
         'Wand of fireballs',
         'Wand of lightning bolts',
         'Wand of paralysis',
         'Wand of the war mage, +2',
         'Wand of wonder',
         'Wings of flying']
itemG_w = [11, 11.375, 11.75, 12.125, 12.5, 12.875, 13.625, 14, 15, 16, 17, 18,
           19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35,
           36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 47.5, 48, 49, 50,
           51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67,
           68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84,
           85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]
itemH = ['Weapon, +3',
         'Amulet of the planes',
         'Carpet of flying',
         'Crystal ball (very rare version)',
         'Ring of regeneration',
         'Ring of shooting stars',
         'Ring of telekinesis',
         'Robe of scintillating colors',
         'Robe of stars',
         'Rod of absorption',
         'Rod of alertness',
         'Rod of security',
         'Rod of the pact keeper, +3',
         'Scimitar of speed',
         'Shield, +3',
         'Staff of fire',
         'Staff of frost',
         'Staff of power',
         'Staff of striking',
         'Staff of thunder and lightning',
         'Sword of sharpness',
         'Wand of polymorph',
         'Wand of the war mage, +3',
         'Adamantine armor (half plate)',
         'Adamantine armor (plate)',
         'Animated shield',
         'Belt of fire giant strength',
         'Belt of frost (or stone) giant strength',
         'Armor, +1 breastplate',
         'Armor of resistance (breastplate)',
         'Candle of invocation',
         'Armor, +2 chain mail',
         'Armor, +2 chain shirt',
         'Cloak of arachnida',
         'Dancing sword',
         'Demon armor',
         'Dragon scale mail',
         'Dwarven plate',
         'Dwarven thrower',
         'Efreeti bottle',
         'Figurine of wondrous power (obsidian steed)',
         'Frost brand',
         'Helm of brilliance',
         'Horn of Valhalla (bronze)',
         'Instrument of the bards (Anstruth harp)',
         'Ioun stone (absorption)',
         'Ioun stone (agility)',
         'Ioun stone (fortitude)',
         'Ioun stone (insight)',
         'Ioun stone (intellect)',
         'Ioun stone (leadership)',
         'Ioun stone (strength)',
         'Armor, +2 leather',
         'Manual of bodily health',
         'Manual of gainful exercise',
         'Manual of golems',
         'Manual of quickness of action',
         'Mirror of life trapping',
         'Nine lives stealer',
         'Oathbow',
         'Armor, +2 scale mail',
         'Spellguard shield',
         'Armor, +1 splint',
         'Armor of resistance (splint)',
         'Armor, +1 studded leather',
         'Armor of resistance (studded leather)',
         'Tome of clear thought',
         'Tome of leadership and influence',
         'Tome of understanding']
itemH_w = [10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42,
           44, 46, 48, 50, 52, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65,
           66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82,
           83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99,
           100]
itemI = ['Defender',
         'Hammer of thunderbolts',
         'Luck blade',
         'Sword of answering',
         'Holy avenger',
         'Ring of djinni summoning',
         'Ring of invisibility',
         'Ring of spell turning',
         'Rod of lordly might',
         'Staff of the magi',
         'Vorpal sword',
         'Belt of cloud giant strength',
         'Armor, +2 breastplate',
         'Armor, +3 chain mail',
         'Armor, +3 chain shirt',
         'Cloak of invisibility',
         'Crystal ball (legendary version)',
         'Armor, +1 half plate',
         'Iron flask',
         'Armor, +3 leather',
         'Armor, +1 plate',
         'Robe of the archmagi',
         'Rod of resurrection',
         'Armor, +1 scale mail',
         'Scarab of protection',
         'Armor, +2 splint',
         'Armor, +2 studded leather',
         'Well of many worlds',
         'Armor, +2 half plate',
         'Armor, +2 plate',
         'Armor, +3 studded leather',
         'Armor, +3 breastplate',
         'Armor, +3 splint',
         'Armor, +3 half plate',
         'Armor, +3 plate',
         'Apparatus of Kwalish',
         'Armor of invulnerability',
         'Belt of storm giant strength',
         'Cubic gate',
         'Deck of many things',
         'Efreeti chain',
         'Armor of resistance (half plate)',
         'Horn of Valhalla (iron)',
         'Instrument of the bards (Ollamh harp)',
         'Ioun stone (greater absorption)',
         'Ioun stone (mastery)',
         'Ioun stone (regeneration)',
         'Plate armor of etherealness',
         'Plate armor of resistance',
         'Ring of air elemental command',
         'Ring of earth elemental command',
         'Ring of fire elemental command',
         'Ring of three wishes',
         'Ring of water elemental command',
         'Sphere of annihilation',
         'Talisman of pure good',
         'Talisman of the sphere',
         'Talisman of ultimate evil',
         'Tome of the stilled tongue']
itemI_w = [5, 10, 15, 20, 23, 26, 29, 32, 35, 38, 41, 43, 45, 47, 49, 51, 53,
           55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 75.1666, 75.3333, 75.5,
           75.6666, 75.8333, 75.9166, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85,
           86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]

# list of consumable items
consumable = ['Potion of healing',
              'Spell scroll (cantrip)',
              'Potion of climbing',
              'Spell scroll (1st level)',
              'Spell scroll (2nd level)',
              'Potion of greater healing',
              'Potion of fire breath',
              'Potion of resistance',
              'Ammunition, +1',
              'Potion of animal friendship',
              'Potion of hill giant strength',
              'Potion of growth',
              'Potion of water breathing',
              'Spell scroll (3rd level)',
              'Keoghtom\'s ointment',
              'Oil of slipperiness',
              'Dust of disappearance',
              'Dust of dryness',
              'Dust of sneezing and choking',
              'Elemental gem',
              'Philter of love',
              'Robe of useful items',
              'Potion of poison',
              'Potion of superior healing',
              'Spell scroll (4th level)',
              'Ammunition, +2',
              'Potion of clairvoyance',
              'Potion of diminution',
              'Potion of gaseous form',
              'Potion of frost giant strength',
              'Potion of stone giant strength',
              'Potion of heroism',
              'Potion of invulnerability',
              'Potion of mind reading',
              'Spell scroll (5th level)',
              'Elixir of health',
              'Oil of etherealness',
              'Potion of fire giant strength',
              'Quaal\'s feather token',
              'Scroll of protection',
              'Bag of beans',
              'Bead of force',
              'Chime of opening',
              'Necklace of fireballs',
              'Potion of supreme healing',
              'Potion of invisibility',
              'Potion of speed',
              'Spell scroll (6th level)',
              'Spell scroll (7th level)',
              'Ammunition, +3',
              'Oil of sharpness',
              'Potion of flying',
              'Potion of cloud giant strength',
              'Potion of longevity',
              'Potion of vitality',
              'Spell scroll (8th level)',
              'Nolzur\'s marvelous pigments',
              'Potion of storm giant strength',
              'Potion of supreme healing',
              'Spell scroll (9th level)',
              'Universal solvent',
              'Arrow of slaying',
              'Sovereign glue',
              'Deck of illusions',
              'Gem of brightness',
              'Candle of invocation',
              'Efreeti bottle',
              'Helm of brilliance',
              'Ioun stone (absorption)',
              'Manual of bodily health',
              'Manual of gainful exercise',
              'Manual of golems',
              'Manual of quickness of action',
              'Tome of clear thought',
              'Tome of leadership and influence',
              'Tome of understanding',
              'Ioun stone (greater absorption)',
              'Ring of three wishes',
              'Talisman of pure good',
              'Talisman of ultimate evil']

itemtables = {'A': itemA,
              'B': itemB,
              'C': itemC,
              'D': itemD,
              'E': itemE,
              'F': itemF,
              'G': itemG,
              'H': itemH,
              'I': itemI}
itemtables_w = {'A': itemA_w,
                'B': itemB_w,
                'C': itemC_w,
                'D': itemD_w,
                'E': itemE_w,
                'F': itemF_w,
                'G': itemG_w,
                'H': itemH_w,
                'I': itemI_w}
tablenames = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']

def magicitem_treasure(table='random', nonconsumable=False):
    if table == 'random': table = rng.choice(tablenames)
    item = rng.choices(itemtables[table], cum_weights=itemtables_w[table])[0]
    if nonconsumable:
        if table == 'E':
            print('Table E only contains consumables! Rerolling on table D.')
            table = 'D'
        while item in consumable:
            item = rng.choices(itemtables[table], cum_weights=itemtables_w[table])[0]
    return item

#%% Treasure Hoard Tables
                  # coins:   CP, SP, EP, GP, PP
                  # loot:    num, val, type, num, table, num, table
hoard = {}
hoard['CR 0-4'] = {'Coins': ['6d6x100', '3d6x100', '0d0', '2d6x10', '0d0'],
                   'Loot': [['0d0', '10 gp', 'gem', '0d0', 'A', '0d0', 'A'],
                            ['2d6', '10 gp', 'gem', '0d0', 'A', '0d0', 'A'],
                            ['2d4', '25 gp', 'art', '0d0', 'A', '0d0', 'A'],
                            ['2d6', '50 gp', 'gem', '0d0', 'A', '0d0', 'A'],
                            ['2d6', '10 gp', 'gem', '1d6', 'A', '0d0', 'A'],
                            ['2d4', '25 gp', 'art', '1d6', 'A', '0d0', 'A'],
                            ['2d6', '50 gp', 'gem', '1d6', 'A', '0d0', 'A'],
                            ['2d6', '10 gp', 'gem', '1d4', 'B', '0d0', 'A'],
                            ['2d4', '25 gp', 'art', '1d4', 'B', '0d0', 'A'],
                            ['2d6', '50 gp', 'gem', '1d4', 'B', '0d0', 'A'],
                            ['2d6', '10 gp', 'gem', '1d4', 'C', '0d0', 'A'],
                            ['2d4', '25 gp', 'art', '1d4', 'C', '0d0', 'A'],
                            ['2d6', '50 gp', 'gem', '1d4', 'C', '0d0', 'A'],
                            ['2d4', '25 gp', 'art', '1d4', 'F', '0d0', 'A'],
                            ['2d6', '50 gp', 'gem', '1d4', 'F', '0d0', 'A'],
                            ['2d4', '25 gp', 'art', '1d1', 'G', '0d0', 'A'],
                            ['2d6', '50 gp', 'gem', '1d1', 'G', '0d0', 'A']],
                   'Loot_w': [6, 16, 26, 36, 44, 52, 60, 65, 70, 75, 78, 80,
                              85, 92, 97, 99, 100]}
hoard['CR 5-10'] = {'Coins': ['2d6x100', '2d6x1000', '0d0', '6d6x100', '3d6x10'],
                    'Loot': [['0d0', '10 gp',  'gem', '0d0', 'A', '0d0', 'A'],
                             ['2d4', '25 gp',  'art', '0d0', 'A', '0d0', 'A'],
                             ['3d6', '50 gp',  'gem', '0d0', 'A', '0d0', 'A'],
                             ['3d6', '100 gp', 'gem', '0d0', 'A', '0d0', 'A'],
                             ['2d4', '250 gp', 'art', '0d0', 'A', '0d0', 'A'],
                             ['2d4', '25 gp',  'art', '1d6', 'A', '0d0', 'A'],
                             ['3d6', '50 gp',  'gem', '1d6', 'A', '0d0', 'A'],
                             ['3d6', '100 gp', 'gem', '1d6', 'A', '0d0', 'A'],
                             ['2d4', '250 gp', 'art', '1d6', 'A', '0d0', 'A'],
                             ['2d4', '25 gp',  'art', '1d4', 'B', '0d0', 'A'],
                             ['3d6', '50 gp',  'gem', '1d4', 'B', '0d0', 'A'],
                             ['3d6', '100 gp', 'gem', '1d4', 'B', '0d0', 'A'],
                             ['2d4', '250 gp', 'art', '1d4', 'B', '0d0', 'A'],
                             ['2d4', '25 gp',  'art', '1d4', 'C', '0d0', 'A'],
                             ['3d6', '50 gp',  'gem', '1d4', 'C', '0d0', 'A'],
                             ['3d6', '100 gp', 'gem', '1d4', 'C', '0d0', 'A'],
                             ['2d4', '250 gp', 'art', '1d4', 'C', '0d0', 'A'],
                             ['2d4', '25 gp',  'art', '1d1', 'D', '0d0', 'A'],
                             ['3d6', '50 gp',  'gem', '1d1', 'D', '0d0', 'A'],
                             ['3d6', '100 gp', 'gem', '1d1', 'D', '0d0', 'A'],
                             ['2d4', '250 gp', 'art', '1d1', 'D', '0d0', 'A'],
                             ['2d4', '25 gp',  'art', '1d4', 'F', '0d0', 'A'],
                             ['3d6', '50 gp',  'gem', '1d4', 'F', '0d0', 'A'],
                             ['3d6', '100 gp', 'gem', '1d4', 'F', '0d0', 'A'],
                             ['2d4', '250 gp', 'art', '1d4', 'F', '0d0', 'A'],
                             ['3d6', '100 gp', 'gem', '1d4', 'G', '0d0', 'A'],
                             ['2d4', '250 gp', 'art', '1d4', 'G', '0d0', 'A'],
                             ['3d6', '100 gp', 'gem', '1d1', 'H', '0d0', 'A'],
                             ['2d4', '250 gp', 'art', '1d1', 'H', '0d0', 'A']],
                    'Loot_w': [4, 10, 16, 22, 28, 32, 36, 40, 44, 49, 54, 59,
                               63, 66, 69, 72, 74, 76, 78, 79, 80, 84, 88, 91,
                               94, 96, 98, 99, 100]}
hoard['CR 11-16'] = {'Coins': ['0d0', '0d0', '0d0', '4d6x1000', '5d6x100'],
                     'Loot': [['0d0', '10 gp',   'gem', '0d0', 'A', '0d0', 'A'],
                              ['2d4', '250 gp',  'art', '0d0', 'A', '0d0', 'A'],
                              ['2d4', '750 gp',  'art', '0d0', 'A', '0d0', 'A'],
                              ['3d6', '500 gp',  'gem', '0d0', 'A', '0d0', 'A'],
                              ['3d6', '1000 gp', 'gem', '0d0', 'A', '0d0', 'A'],
                              ['2d4', '250 gp',  'art', '1d4', 'A', '1d6', 'B'],
                              ['2d4', '750 gp',  'art', '1d4', 'A', '1d6', 'B'],
                              ['3d6', '500 gp',  'gem', '1d4', 'A', '1d6', 'B'],
                              ['3d6', '1000 gp', 'gem', '1d4', 'A', '1d6', 'B'],
                              ['2d4', '250 gp',  'art', '1d6', 'C', '0d0', 'A'],
                              ['2d4', '750 gp',  'art', '1d6', 'C', '0d0', 'A'],
                              ['3d6', '500 gp',  'gem', '1d6', 'C', '0d0', 'A'],
                              ['3d6', '1000 gp', 'gem', '1d6', 'C', '0d0', 'A'],
                              ['2d4', '250 gp',  'art', '1d4', 'D', '0d0', 'A'],
                              ['2d4', '750 gp',  'art', '1d4', 'D', '0d0', 'A'],
                              ['3d6', '500 gp',  'gem', '1d4', 'D', '0d0', 'A'],
                              ['3d6', '1000 gp', 'gem', '1d4', 'D', '0d0', 'A'],
                              ['2d4', '250 gp',  'art', '1d1', 'E', '0d0', 'A'],
                              ['2d4', '750 gp',  'art', '1d1', 'E', '0d0', 'A'],
                              ['3d6', '500 gp',  'gem', '1d1', 'E', '0d0', 'A'],
                              ['3d6', '1000 gp', 'gem', '1d1', 'E', '0d0', 'A'],
                              ['2d4', '250 gp',  'art', '1d1', 'F', '1d4', 'G'],
                              ['2d4', '750 gp',  'art', '1d1', 'F', '1d4', 'G'],
                              ['3d6', '500 gp',  'gem', '1d1', 'F', '1d4', 'G'],
                              ['3d6', '1000 gp', 'gem', '1d1', 'F', '1d4', 'G'],
                              ['2d4', '250 gp',  'art', '1d4', 'H', '0d0', 'A'],
                              ['2d4', '750 gp',  'art', '1d4', 'H', '0d0', 'A'],
                              ['3d6', '500 gp',  'gem', '1d4', 'H', '0d0', 'A'],
                              ['3d6', '1000 gp', 'gem', '1d4', 'H', '0d0', 'A'],
                              ['2d4', '250 gp',  'art', '1d1', 'I', '0d0', 'A'],
                              ['2d4', '750 gp',  'art', '1d1', 'I', '0d0', 'A'],
                              ['3d6', '500 gp',  'gem', '1d1', 'I', '0d0', 'A'],
                              ['3d6', '1000 gp', 'gem', '1d1', 'I', '0d0', 'A']],
                     'Loot_w': [3, 6, 9, 12, 15, 19, 23, 26, 29, 35, 40, 45,
                                50, 54, 58, 62, 66, 68, 70, 72, 74, 76, 78, 80,
                                82, 85, 88, 90, 92, 94, 96, 98, 100]}
hoard['CR 17+'] = {'Coins': ['0d0', '0d0', '0d0', '12d6x1000', '8d6x100'],
                   'Loot': [['0d0',  '10 gp',   'gem', '0d0', 'A', '0d0', 'A'],
                            ['3d6',  '1000 gp', 'gem', '1d8', 'C', '0d0', 'A'],
                            ['1d10', '2500 gp', 'art', '1d8', 'C', '0d0', 'A'],
                            ['1d4',  '7500 gp', 'art', '1d8', 'C', '0d0', 'A'],
                            ['1d8',  '5000 gp', 'gem', '1d8', 'C', '0d0', 'A'],
                            ['3d6',  '1000 gp', 'gem', '1d6', 'D', '0d0', 'A'],
                            ['1d10', '2500 gp', 'art', '1d6', 'D', '0d0', 'A'],
                            ['1d4',  '7500 gp', 'art', '1d6', 'D', '0d0', 'A'],
                            ['1d8',  '5000 gp', 'gem', '1d6', 'D', '0d0', 'A'],
                            ['3d6',  '1000 gp', 'gem', '1d6', 'E', '0d0', 'A'],
                            ['1d10', '2500 gp', 'art', '1d6', 'E', '0d0', 'A'],
                            ['1d4',  '7500 gp', 'art', '1d6', 'E', '0d0', 'A'],
                            ['1d8',  '5000 gp', 'gem', '1d6', 'E', '0d0', 'A'],
                            ['3d6',  '1000 gp', 'gem', '1d4', 'G', '0d0', 'A'],
                            ['1d10', '2500 gp', 'art', '1d4', 'G', '0d0', 'A'],
                            ['1d4',  '7500 gp', 'art', '1d4', 'G', '0d0', 'A'],
                            ['1d8',  '5000 gp', 'gem', '1d4', 'G', '0d0', 'A'],
                            ['3d6',  '1000 gp', 'gem', '1d4', 'H', '0d0', 'A'],
                            ['1d10', '2500 gp', 'art', '1d4', 'H', '0d0', 'A'],
                            ['1d4',  '7500 gp', 'art', '1d4', 'H', '0d0', 'A'],
                            ['1d8',  '5000 gp', 'gem', '1d4', 'H', '0d0', 'A'],
                            ['3d6',  '1000 gp', 'gem', '1d4', 'I', '0d0', 'A'],
                            ['1d10', '2500 gp', 'art', '1d4', 'I', '0d0', 'A'],
                            ['1d4',  '7500 gp', 'art', '1d4', 'I', '0d0', 'A'],
                            ['1d8',  '5000 gp', 'gem', '1d4', 'I', '0d0', 'A']],
                   'Loot_w': [2, 5, 8, 11, 14, 22, 30, 38, 46, 52, 58, 63, 68,
                              69, 70, 71, 72, 74, 76, 78, 80, 85, 90, 95, 100]}

# generate a treasure hoard for a given challenge rating
denom = ['CP', 'SP', 'EP', 'GP', 'PP'] # coin denominations
def hoard_treasure(CR='random'):
    
    # CR
    if CR == 'random': CR = rng.choice(CRnames)
    CRtext = CR + ' Treasure Hoard:\n'
    
    # Coins
    cointext = 'Coins: '
    for x in range(0, len(denom)):
        coins = roll(hoard[CR]['Coins'][x])
        if coins != 0: cointext += str(coins) + ' ' + denom[x] + ', '
    cointext = cointext[0:-2] + '\n'
    
    # Hoard Table Row
    row = rng.choices(hoard[CR]['Loot'], cum_weights=hoard[CR]['Loot_w'])[0]
    
    # Gems / Art Objects
    numartgem = roll(row[0])
    artgemval = row[1]
    if row[2] == 'gem': artgemtext = 'Gems: '
    elif row[2] == 'art': artgemtext = 'Art objects: '
    for _ in range(0, numartgem):
        if row[2] == 'gem': artgemtext += gem_treasure(artgemval) + ', '
        elif row[2] == 'art': artgemtext += art_treasure(artgemval) + ', '
    if artgemtext == 'Gems: ' or artgemtext == 'Art objects: ':
        artgemtext += 'none\n'
    else: artgemtext = artgemtext[0:-2] + '\n'
    
    # Magic Items
    numitems1 = roll(row[3])
    table1 = row[4]
    itemtext = 'Magic Items: '
    for _ in range(0, numitems1):
        itemtext += magicitem_treasure(table1) + '; '
    numitems2 = roll(row[5])
    table2 = row[6]
    for _ in range(0, numitems2):
        itemtext += magicitem_treasure(table2) + '; '
    if itemtext == 'Magic Items: ': itemtext += 'none\n'
    else: itemtext = itemtext[0:-2] + '\n'
    
    return print(CRtext + cointext + artgemtext + itemtext)

#%% Campaign Total Rolls

def campaign_treasure():
    for _ in range(0, 7): hoard_treasure('CR 0-4')
    for _ in range(0, 18): hoard_treasure('CR 5-10')
    for _ in range(0, 12): hoard_treasure('CR 11-16')
    for _ in range(0, 8): hoard_treasure('CR 17+')

#%% Fizban's tables
    
coin_origins_list = ['Equivalent value in trade goods rather than coins',
                     'Coins from an ancient culture local to this region, ancestral to the people who live here now',
                     'Coins from an ancient culture in a distant region',
                     'Coins from a nearby contemporary culture',
                     'Coins from a local contemporary culture',
                     'Coins from another world']
coin_origins_w = [1, 3, 5, 7, 9, 10]

def coin_origins(): return rng.choices(coin_origins_list, cum_weights=coin_origins_w)

# dragon hoard contents by age category:
                    # coins:   CP, SP, EP, GP, PP
                    # loot:    mundane, gems, art objects, magic items
dhoard = {}
dhoard['Wyrmling'] = {'Coins': ['12d6x100', '6d6x100', '0d0', '4d6x10', '0d0'],
                      'Loot': ['1d6', '2d8', '1d4', '1d8']
                      }
dhoard['Young'] =    {'Coins': ['12d6x100', '4d6x1000', '0d0', '12d6x100', '6d6x10'],
                      'Loot': ['1d8', '6d6', '2d4', '1d8']
                      }
dhoard['Adult'] =    {'Coins': ['12d6x100', '4d6x1000', '0d0', '8d6x1000', '10d6x100'],
                      'Loot': ['2d6', '6d6', '3d6', '1d8']
                      }
dhoard['Ancient'] =  {'Coins': ['12d6x100', '4d6x1000', '0d0', '6d6x10000', '12d6x1000'],
                      'Loot': ['2d8', '6d6', '2d10', '2d6']
                      }

# mundane items in a dragon's hoard:
mundane = [ 'A painting by an artist long forgotten by everyone except the dragon',
            'A hogshead (large cask) containing 65 gallons of clean drinking water',
            'Several embroidered throw pillows depicting wyrmling dragons',
            'A funerary urn containing remains the dragon can''t identify',
            'A set of seven candlesticks bearing a god''s holy symbol',
            'A tarnished brazier with pleasant-smelling ash',
            'A drum for use in religious rites, with a foreboding echo to its beat',
            'A stuffed Monstrosity appropriate to the local terrain',
            'The skull of a Fiend or Celestial',
            'A spinning wheel',
            'An hourglass filled with sparkling sand',
            'A crude flute with a pleasing sound',
            'Hundreds or thousands of fake coins interspersed with the real treasure',
            'A treatise on alchemy etched on steel cylinders',
            'The battle standard of one of the dragon''s ancient foes',
            'A sketchbook from another world of the Material Plane, depicting unfamiliar creatures and one very familiar dragon',
            'A set of irregular polyhedral dice (with 9, 13, 25, and 34 sides)',
            'A map showing the dragon''s lair in relation to villages and other long-gone landmarks',
            'A kneeling bench, which anyone addressing the dragon is required to use',
            'A scroll containing a long epic poem in praise of the dragon',
            'A star chart showing Bahamut and a one-headed Tiamat as constellations, with "Elegy for the First World" written between the stars',
            'A large, noisy wind chime',
            'A small shrine with a statuette, a brazier, and an altar dedicated to a god worshiped by many of the dragon''s minions',
            'A jar with a dead illithid tadpole floating in preserving chemicals',
            'An extensive historical record in the form of carefully knotted strings']
# note that these weights are all the same, so they're not really needed:
mundane_w = [4,8,12,16,20,24,28,32,36,40,44,48,52,56,60,64,68,72,76,80,84,88,92,96,100]
trinket['Draconic'] = mundane # add to dictionary of trinkets
for i in range(len(mundane)):
    alltrinkets.append(mundane[i]) # add to master list of all trinkets

# art objects by dragon type; can be any value
dart = {}
dart['Amethyst'] = ['A complex orrery of the planes of existence made of engraved movable plates of precious metals and set with gemstones',
                    'A two-foot-long rod of pale crystal that gives off eerie sounds when touched, with the tone varying up and down the length of the rod',
                    'A life-sized human skull carved from a single piece of crystal, including a hollow interior',
                    'A beautifully engraved gong, 3 feet in diameter, suspended from an ornate, inlaid frame',
                    'A crystal singing bowl etched with mantras in Gith, accompanied by an inlaid wooden mallet',
                    'A beautifully illuminated treatise on the planes of existence, bound in ebony covers with metal corner caps and a cover boss set with polished gems',
                    'An etched crystal that projects a star map showing an unfamiliar star field and constellations when set on top of a light source',
                    'A ring in the shape of a coiling dragon, with tiny gemstones for eyes']

dart['Black'] =    ['An elegant necklace owned by a beloved noble who disappeared years ago',
                    'Stone carvings representing a pantheon of deities that passed from common knowledge long ago',
                    'The lost secret to forging an alloy imbued with arcane potential, etched on twelve metal disks the size of dinner plates',
                    'A sealed platinum flask containing the last known aqua vitae created by a master dwarf distiller',
                    'A ceremonial longsword with an embossed silver hilt and a blade of amber',
                    'A lavishly illustrated genealogy kept in a magically sealed container that disputes a current monarch''s right to the throne',
                    'Heretical religious symbols carved on a trio of gemstones the size of apples',
                    'An elaborately carved mask representing a god of harvest and fertility',
                    'Metal horn caps inset with gems, made for the dragon by loyal cultists',
                    'A beautifully enameled urn holding the desiccated heart of the dragon''s former green dragon rival']

dart['Blue'] =     ['An intricately carved seal from a civilization that worshiped the dragon''s ancestors as gods',
                    'An extensive collection of elaborate jewelry, including a tiara, tail rings, and claw covers, which the dragon wears when meeting with supplicants',
                    'A set of sculptures depicting the dragon''s deceased relatives, all adorned with ground-up jewels',
                    'A jeweled mosaic map of the dragon''s territory',
                    'A glass bell that creates the sound of rainstorms and thunder for 1 hour when struck',
                    'An ornately tooled tome recording the lineages of all the blue dragon families in the area',
                    'A massive geode that contains spectacular blue, purple, and black crystals',
                    'A blue silk fan painted with ground gems that creates a briny breeze when hung from the ceiling']

dart['Brass'] =    ['A finely carved bust of a long-dead human ruler, which the dragon has named Cornelius and argues with incessantly',
                    'An elegant locket holding a watercolor portrait of a dragonborn the dragon fondly calls Lux',
                    'A polished platter engraved with an elaborate scene showing a person talking to a sphinx; the dragon likes to imagine being in the scene, dominating the conversation',
                    'A sculpture depicting a pod of dolphins leaping among stone waves, all of which the dragon has named and imagines as pets',
                    'A cameo pendant depicting a human woman the dragon calls "Bruno" and imagines to be a brilliant philosopher',
                    'A statuette of an important deity, which the dragon calls by a diminutive version of the god''s name and baby-talks to',
                    'A large tapestry depicting a party of elves riding stags through the woods; the dragon has named all the stags and offers condolences on their being saddled and mounted',
                    'A sculpted bird in an ornate cage; the dragon calls the bird Fweep and sings to it',
                    'A large mirror in a frame studded with gemstones; the dragon likes to gaze in the mirror and imagine having a mate',
                    'An idol of an obscure minor divinity; the dragon addresses it reverently as "O mighty Froglet" (its shape is only vaguely frog-like)']

dart['Bronze'] =   ['A painting of the bronze dragon alongside a human woman wearing an outdated military uniform',
                    'An ornate, mostly complete collection of Oristene''s multi-volume Military History of the Outer Planes',
                    'A heavy cloak of shimmering blue scales, with an attached half-mask',
                    'An oversized key of living wood, with seemingly natural whorls in the bark that form the words, "For service not forgotten"',
                    'A dragon-sized drinking vessel crafted from a behir horn',
                    'Framed blueprints of a siege engine called the Moonhammer',
                    'An aquatic howdah made of sharkskin and bearing an emblem of a lonely black tower perched high atop a sea stack',
                    'A statue of a dishonored elf general, which is surrounded by historical treatises recounting the general''s disgrace and notes that suggest the dragon has vowed to redeem this former hero',
                    'An idol of an insectile devil, with a blindfold tied carefully around its compound eyes',
                    'An elaborate clockwork zoetrope that, when activated, displays a moving picture of a bronze dragon fighting a red dragon over a burning city']

dart['Copper'] =   ['A jeweled cloak pin bearing the symbol of an ancient secret society',
                    'A smooth piece of amber with what appears to be a tiny sprite frozen inside it',
                    'A metal egg that unfolds into a lotus-like flower',
                    'A harp that plays by itself on command',
                    'A six-foot-tall mirror of silvered glass in a precious frame carved with the shapes of coiling dragons',
                    'A complex puzzle box made of rare woods and inlaid with stone',
                    'The figurehead of a ship, carved in rare woods and set with gemstones — and bearing the likeness of the copper dragon''s head',
                    'A complex astrological clock, with tiny gemstones marking out stars and constellations']

dart['Crystal'] =  ['An armillary sphere revealing the positions of several unknown worlds in the Material Plane (relative to the one the dragon is on)',
                    'A set of handmade tarokka cards depicting the various wizard clans of a magocracy called Glantri',
                    'A dazzling array of crystals carved to refract any light passing through them into star-like patterns',
                    'An oversized monocle custom-made for the crystal dragon, who thinks it looks stylish',
                    'A children''s coin bank shaped like an owlbear, with beautiful blue gemstone eyes',
                    'An ancient water clock that tells the time with perfect accuracy',
                    'A star chart reproducing the night sky of some other Material Plane world',
                    'A magnificent fresco depicting a noble court in the Feywild',
                    'Alabaster panels etched with unusual glyphs, designed to be hung in windows to catch the light',
                    'Astrological birth charts for every year since the dragon was born',
                    'A vast number of colored glass bottles collected from dozens of cultures and historical periods',
                    'A fine divan set with gemstone buttons and stitched with silver thread']

dart['Deep'] =     ['A statue of an unknown winged antelope-like creature carved from a single massive opal',
                    'A preserved juvenile purple worm on an ebony stand set with amethysts',
                    'A cunningly worked metal automaton of a sphinx that, when addressed directly, answers every question with a question referencing forgotten civilizations',
                    'A set of filigreed gold claw covers set with gems that change color according to the wearer''s mood',
                    'A silver pelt that belonged to a long-extinct species of bear and sheds snowflakes when touched',
                    'A painting of a caldera island with unique fauna that shows how to access the interior by swimming through an underwater cave',
                    'A magic chandelier that projects images of the most inaccessible places in the world on the wall, changing the images each time the chandelier is relit',
                    'A magical goblet activated when the creature holding it speaks the name of a country, whereupon the goblet fills with the finest wine from that land''s vineyards',
                    'A set of exquisite miniature dragons made of precious metals, jewels, and stone, with one representing each kind of chromatic, metallic, and gem dragon',
                    'The jewel-encrusted skull of an ancient dragon, which the deep dragon always keeps close at hand and talks to when lonely',
                    'A magnificent set of drums painted with scenes from the folklore of an isolated mountain community',
                    'A beautifully worked statue of the deep dragon in a favorite Humanoid form, made by an artist the dragon knew centuries ago']

dart['Dragon Turtle'] = ['An elven coronet, which the dragon turtle wears as an earring',
                    'A pipe organ that the dragon turtle refers to as "Bubbles," which works underwater',
                    'Cast-metal masks painted with the faces of rulers whose names the dragon turtle constantly misremembers',
                    'A zither fashioned from a conch shell, which the dragon turtle insists visitors play before granting them an audience',
                    'A painted egg decorated with glittering jewels',
                    'An ornate underwater carriage fashioned from coral and seashells, which the dragon turtle pushes back and forth like a toy',
                    'A sculpture depicting a knight on griffonback, whose lance the dragon turtle uses to scrape off barnacles',
                    'An urn engraved with a scowling dwarf''s face, whose expression the dragon turtle mimics comically',
                    'A scepter fashioned to resemble a skeletal arm, which unnerves the dragon turtle for some inexplicable reason',
                    'An elegant candelabra that the dragon turtle thinks is lost, but that is actually wedged into a crack in their shell']

dart['Emerald'] =  ['A traveling cloak worn by an elf apostate named Huwellah Starshine to the trial where she was convicted and executed',
                    'A nonmagical crystal ball used by Firendelbip, a deep gnome seer who predicted the overthrow of a thousand-year-old fomorian empire',
                    'Spurs worn by the famous human cavalier Roganvald, who challenged the dragon Arathimax the Red (Roganvald''s armor now lies in Arathimax''s hoard)',
                    'The ornate badge of office of the lich Zakir, nine-time governor of the city of Durn',
                    'A gravy ladle belonging to Lara Rumpledeep, a famed halfling gourmand',
                    'A sextant used by the renowned dwarf explorer Thavrik Rustbeard',
                    'A jeweled hairnet worn by the cloud giant Ultania, who slew her own mother to claim her throne',
                    'A phoenix-shaped brooch passed down to each of the forty-seven recorded incarnations of Gaz, a githzerai monk',
                    'A trophy cup engraved with a pumpkin, awarded each year at the harvest festival of Riksdell before that settlement fell to a plague',
                    'Rusty chains used to bind the orc master thief Korjus before she escaped and conquered half the lands of the south']

dart['Faerie'] =   ['A fist-sized puzzle box that the dragon hasn''t been able to open, and that holds a tiny clay tablet marked with a mysterious string of numbers',
                    'An illustrated tome titled Hrgold''s Bestiary, which falls open to an oft-read entry on faerie dragons',
                    'A majestic military jacket featuring a dazzling array of medals and five different secret pockets',
                    'A gold-rimmed monocle sized for a cyclops, complete with a gold chain',
                    'A gilded pseudodragon skull that the faerie dragon likes to wear as a mask while pretending to be a different dragon called "Regnus the Unspeakable"',
                    'A cask of wine stamped with the seal of a noble''s private collection',
                    'A framed painting of a red dragon destroying an army, with a hole chewed through the dragon''s face so the faerie dragon can stick their head through it',
                    'A tiny scale model of a castle that opens like a dollhouse to reveal the chambers and secret passages within']

dart['Gold'] =     ['A fine tapestry depicting the intermingled family trees of several royal bloodlines going back multiple generations — and containing surprising revelations',
                    'An orrery showing the world''s place in the solar system — with one gemstone planet too many',
                    'A scroll covered with surrealist imagery, entitled Voyage through the Land of Dreams',
                    'A black dragon skull with a crack down the middle and gems fixed in its eye sockets; a plaque along the bottom reads, "So too shall ye be"',
                    'A metal wheel with various holy symbols affixed to its edges; thin arms at the center of the wheel are made to hold a spherical object that is missing',
                    'A series of nesting metal cylinders, each inscribed with a different proverb or paradox; the central cylinder contains a single gold dragon scale',
                    'An elaborate atlas bound in wyvern hide, with several remote regions circled and labeled in code',
                    'A clever clockwork music box that, when cranked, recites a prophecy in Modron',
                    'An elaborately decorated tea set, each of its cups themed after a different plane of existence',
                    'An elaborate calendar clock with one face burned and cracked and two others that are counting down to unspecified future events, including one less than a month away']

dart['Green'] =    ['The polished skull of a unicorn, latticed with luminescent blooms',
                    'An elaborate necklace of yuan-ti origin, set with gleaming gems and dripping with strands of pearls',
                    'A harp, its pillar carved to resemble a beautiful elf who weeps loudly and inconsolably',
                    'A marble statue that once showed a knight vanquishing a dragon, but due to strategic damage, now looks like a knight tumbling into massive jaws',
                    'The baby teeth of a Humanoid, preserved in amber furred with a golden fungus that smells like gingerbread',
                    'A giant-sized hunting horn scrimshawed with elaborate patterns, the pewter only slightly tarnished',
                    'A stained glass window still set within a fragment of wall depicting the many deaths of an elf monarch',
                    'A triptych of silver mirrors, set in an ornate brambled iron frame sculpted to depict figures in a grotesque bacchanal',
                    'Quartz terrariums carried on the backs of tourmaline jaguars, overgrown with misshapen cacti',
                    'A string of skulls riddled with too many eye sockets, their jaws replaced by carved gemstones']

dart['Moonstone'] = ['A statue of a beautiful Fey who appears to be laughing, crying, or scowling, depending on the viewer''s mood; the dragon requires all who visit to describe the face and sends away anyone who sees an angry visage',
                    'A string of leaves collected from the rarest trees in the Feywild and then dipped in silver',
                    'A small mithral ball that shows significant scuffing, as the dragon plays with it constantly',
                    'A mobile from which hang six figurines of pixies and sprites; the dragon insists that Fey allies address any questions and concerns to the figurines',
                    'A painting of a beautiful Feywild vista; the dragon studies the painting every day for clues about the vista''s whereabouts',
                    'An ornate silver chest that holds a mountain of gold coins; the dragon refuses to open the chest, claiming it can still smell the stink of the "noxious metal"',
                    'A collection of gem-encrusted pitchers, decanters, and goblets; the dragon will not consume faerie nectar unless it is served in one of these items',
                    'A vast bookshelf full of dream journals written by creatures the dragon has befriended over the years; the dragon has each entry illustrated by a different celebrated artist, making the library one of the largest art collections in the world']

dart['Red'] =      ['A hammered metal brazier elaborately etched and set with polished obsidian, which sits atop a stand holding rare incense blends',
                    'A beautifully inlaid mosaic map of the region within a 100-mile radius of the dragon''s lair',
                    'A life-sized basalt statue of a fierce knight, weapon raised to strike, which might be the preserved form of an actual knight turned to stone',
                    'The blackened skull of a young dragon that has been etched with designs and decorated with gems',
                    'A tiered fountain filled with liquid gold that is cool to the touch, but immediately hardens if removed from the fountain',
                    'A statue of the red dragon with gemstones for eyes',
                    'A detailed, life-sized elf skull cast in precious metal',
                    'A game board and a complete set of pieces, all carved and inlaid with precious and semiprecious stones (the dragon is fond of playing the game but has few worthy opponents)',
                    'A fist-sized gemstone carved into a likeness of the dragon''s head',
                    'A set of precious metal tablets containing ancient lore',
                    'A beautifully wrought crown set with fiery gemstones, possibly the legacy of a lost empire',
                    'A beautiful polished sphere of rainbow obsidian, set on a wrought-gold stand']

dart['Sapphire'] = ['A battle standard showing the coat of arms of an ancient realm the dragon failed to protect',
                    'A dragonchess set with the white knights replaced by the symbols of a war god; the board is set up for the start of a new game, and the dragon has been waiting decades for the god to make the first move',
                    'A large tapestry depicting a bloody battle between two realms of the surface world; the dragon claims it is the tiny dragon embroidered in one corner',
                    'A music box that plays a haunting song; the dragon claims the music is very popular on another world',
                    'A necklace made from discarded sapphire dragon horn tips and tail barbs; the dragon refuses to say whether the pieces were donated willingly',
                    'A perfectly polished mirror that the dragon spends hours staring into, hoping to catch glimpses into other worlds']

dart['Shadow'] =   ['An ornate scepter marred by soot and grime',
                    'A priceless painting badly in need of restoration',
                    'A lump of melted precious metal that was once a splendid necklace and holds gemstones inside it',
                    'A series of fine charcoal drawings depicting the royal lineage of a prominent drow house',
                    'A seemingly plain gray tapestry; close inspection reveals a tableau in shades of dove, ash, and slate',
                    'A pair of stonework gargoyles rendered in a grotesquely baroque and terrifying style',
                    'A pile of loose sheet music representing the lost dirges of a famous shadar-kai bard',
                    'An exquisitely crafted mirror that drains all color from the reflections of those who look into it',
                    'A ventriloquist''s dummy made to resemble the Count of Barovia',
                    'A peculiar dragonchess set entirely crafted from onyx, making it extremely difficult to tell one side''s pieces from the other']

dart['Silver'] =   ['A group portrait of nobles set in a faded mahogany frame, one corner of which is etched with signatures',
                    'An ancient shortsword with a pommel in the shape of a goblin''s face, its blade notched with heavy use',
                    'The shattered helm of a dwarf monarch, mended with brazed gold',
                    'A full suit of ancient armor, its breastplate scrimshawed with draconic faces',
                    'A pearl-handled switchblade, its blade eaten away by salt water and its handle emblazoned with a crest',
                    'An elaborate elven crown made to resemble a dragon''s head',
                    'A triptych of tapestries depicting the end of a war, the restoration work that followed, and the sunset flight of a silver dragon leaving the renewed realm',
                    'A cape studded with gemstones and featuring epaulets of egret feathers, set on the shoulders of a battered tailor''s mannequin',
                    'A dramatic portrait of a human noble rendered mostly as shadow and glinting light that reveals the dragon-shaped pendant the figure wears',
                    'A series of detailed obsidian sculptures depicting a human transitioning from childhood to old age']

dart['Topaz'] =    ['An ornate statue of a sea serpent that plays ocean sounds when its gemstone eyes are pressed',
                    'A set of seven levered brass mirrors that can be adjusted to direct light in different directions',
                    'A stained glass window depicting a golden city whose buildings are decorated with statues of dragons and other winged creatures',
                    'A gold scrying bowl that shows random, constantly shifting views of the Elemental Chaos',
                    'A 10-foot-tall statue of the dragon, carved out of a single massive yellow crystal (the dragon thinks it''s flattering, except for the tail)',
                    'A large, shallow dish filled with water on which floats a set of delicate wooden ships; speaking different command words creates waves and whirlpools in the bowl',
                    'A large spherical gold chandelier that gives off sunlight and is surrounded by an intricate and interlocking set of glass bands engraved in an unknown language',
                    'A set of topaz-inlaid gold claw rings engraved with the names of bronze dragons the topaz dragon has killed']

dart['White'] =    ['A war horn carved to resemble a dragon''s head with a wide-open maw, which the dragon calls "Little Toot"',
                    'A statue depicting an elf paladin with the face turned upward; the body has been defaced by the dragon''s claws',
                    'A mammoth tusk engraved with images depicting the history of a nomadic tribe; the dragon uses the tusk to mark the spot where it has buried its pile of gold',
                    'A giant-sized cloak decorated with silver braiding that the dragon uses as a nest lining for its egg',
                    'A wooden throne heaped with furs; any visitors must sit on the throne while the dragon recounts the grisly death of the seat''s previous owner',
                    'A huge wooden door carved and painted to depict a monarch enthroned with sword and scepter; the dragon occasionally raps the door with its knuckles, pauses, and then chortles, "Nobody home"',
                    'A frost giant jarl''s crown with broken horns; the dragon enjoys perching the crown on an icy stalagmite and then knocking it off with its tail',
                    'The prow of a ship carved to look like a pouncing lion; the dragon occasionally roars at the lion',
                    'A gilded shield emblazoned with the holy symbol of a forgotten god; the dragon enjoys flicking the shield with a claw to hear the sound it makes',
                    'A ceremonial anvil of dwarven make; gazing at the anvil, the dragon fondly recounts, "Seven at one blow!"',
                    'A long, embroidered linen tapestry showing the history of an ancient realm''s civil war; the dragon "reads" the tapestry when it has trouble sleeping.',
                    'A bell engraved with images of an angelic host, still attached to its splintered belfry; the dragon tolls the bell with its tail, growling the name of one of its defeated foes with each ring']

dragontypes = ['Amethyst', 'Black', 'Blue', 'Brass', 'Bronze', 'Copper',
               'Crystal', 'Deep', 'Dragon Turtle', 'Emerald', 'Faerie', 'Gold',
               'Green', 'Moonstone', 'Red', 'Sapphire', 'Shadow', 'Silver',
               'Topaz', 'White']

# gem contents of a dragon's hoard by age category:
# weights correspond to values in the 'gemvals' list
#                   gp:  10, 50, 100, 500, 1000, 5000
hgems_w = {'Wyrmling':  [43, 99, 100, 100, 100,  100],
           'Young':     [51, 75, 99,  100, 100,  100],
           'Adult':     [18, 36, 54,  77,  99,   100],
           'Ancient':   [14, 28, 42,  58,  93,   100]}

# art object contents of a dragon's hoard by age category:
# weights correspond to values in the 'artvals' list
#                   gp:  25, 250, 750, 2500, 7500
hart_w = {'Wyrmling':   [95, 100, 100, 100,  100],
          'Young':      [53, 99,  100, 100,  100],
          'Adult':      [49, 75,  99,  100,  100],
          'Ancient':    [22, 42,  58,  93,   100]}

# magic item contents of a dragon's hoard by age category:
# weights correspond to values in the 'tablenames' list
#                 type: com, unc, rare, vr, leg, unc, rare, vr, leg
#                table:  A,  B,  C,  D,  E,  F,  G,   H,   I
hmagic_w = {'Wyrmling': [34, 61, 77, 77, 77, 96, 100, 100, 100],
            'Young':    [21, 49, 64, 72, 72, 91, 97,  100, 100],
            'Adult':    [6,  18, 41, 64, 69, 72, 80,  91,  100],
            'Ancient':  [0,  0,  12, 56, 67, 67, 73,  82,  100]}

# generate a dragon's hoard for a given age category
agenames = ['Wyrmling', 'Young', 'Adult', 'Ancient']
def dragon_hoard(age='random', dtype='random', typeart='only', trinket_type='Draconic', printout=False):
    """
    age = age of dragon: Wyrmling, Young, Adult, Ancient, or random
    dtype = type of dragon: Amethyst, Black, Blue, Brass, Bronze, Copper,
               Crystal, Deep, Dragon Turtle, Emerald, Faerie, Gold,
               Green, Moonstone, Red, Sapphire, Shadow, Silver,
               Topaz, White, or random
    typeart = how much art to pick from type table: only, all, none, or random
    trinket_type = trinket category: Draconic etc, or all/random
    printout = True to print result to commandline, False to return text
    """
    
    # age
    if age == 'random': age = rng.choice(agenames)
    
    # type
    if dtype == 'random': dtype = rng.choice(dragontypes)
    if typeart != 'none':
        if dtype == 'Dragon Turtle':
            headertext = age + ' ' + dtype + ' Treasure Hoard:\n'
        else:
            headertext = age + ' ' + dtype + ' Dragon Treasure Hoard:\n'
    
    # Coins
    cointext = 'Coins: '
    for x in range(0, len(denom)):
        coins = roll(dhoard[age]['Coins'][x])
        if coins != 0: cointext += str(coins) + ' ' + denom[x] + ', '
    cointext = cointext[0:-2] + '\n'
    
    # Mundane Items
    nummundane = roll(dhoard[age]['Loot'][0])
    mundanetext = 'Mundane Items:\n'
    for _ in range(0, nummundane):
        if trinket_type in trinket.keys(): # true if valid trinket table name
            mundanetext += '    ' + rng.choice(trinket[trinket_type]) + '\n'
        elif trinket_type in ['all', 'random']: # choose from all trinkets
            mundanetext += '    ' + rng.choice(alltrinkets) + '\n'
    if mundanetext == 'Mundane Items:\n':
        mundanetext += 'none\n'
    #else: mundanetext = mundanetext[0:-2] + '\n'
    
    # Gems
    numgem = roll(dhoard[age]['Loot'][1])
    gemtext = 'Gems:\n'
    for _ in range(0, numgem):
        gemval = rng.choices(gemvals, cum_weights=hgems_w[age])[0]
        gemtext += '    ' + gem_treasure(gemval) + '\n'
    if gemtext == 'Gems:\n':
        gemtext += 'none\n'
    #else: gemtext = gemtext[0:-2] + '\n'
    
    # Art Objects
    numart = roll(dhoard[age]['Loot'][2])
    arttext = 'Art objects:\n'
    for _ in range(0, numart):
        artval = rng.choices(artvals, cum_weights=hart_w[age])[0]
        if typeart == 'only': # only art from table for dragon type
            arttext += '    ' + art_treasure(artval, dtype) + '\n'
        elif typeart == 'all': # art from dragon table with random type
            temptype = rng.choice(dragontypes)
            arttext += '    ' + art_treasure(artval, temptype) + '\n'
        elif typeart == 'none': # regular art only
            arttext += '    ' + art_treasure(artval) + '\n'
        elif typeart == 'random': # random pick of dragon or regular art
            arttext += '    ' + art_treasure(artval, 'random') + '\n'
    if arttext == 'Art objects:\n':
        arttext += 'none\n'
    #else: arttext = arttext[0:-2] + '\n'
    
    # Magic Items
    numitems = roll(dhoard[age]['Loot'][3])
    itemtext = 'Magic Items:\n'
    for _ in range(0, numitems):
        table = rng.choices(tablenames, cum_weights=hmagic_w[age])[0]
        itemtext += '    ' + magicitem_treasure(table) + '\n'
    if itemtext == 'Magic Items:\n': itemtext += 'none\n'
    #else: itemtext = itemtext[0:-2] + '\n'
    
    if printout:
        print(headertext + cointext + mundanetext + gemtext + arttext + itemtext)
    else:
        return headertext + cointext + mundanetext + gemtext + arttext + itemtext


