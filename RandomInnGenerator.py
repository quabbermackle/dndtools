# -*- coding: utf-8 -*-
"""
Created on Fri Aug  6 10:23:15 2021

@author: Matthew

Adaptation of tables in Dragon magazine, issue 418:
    "Inns in an Instant" by John Hasznosi
"""

import itertools as it
import random as rng
rng.seed()

from treasuretools import roll
from chargentools_eberron import favfoods
wildemountregions = ['Menagerie Coast',
                     'Marrow Valley',
                     'Greying Wildlands',
                     'Xhorhas']
# don't include Zemni Fields - it's a copy of Marrow Valley

#%% Tables

# INN NAME
# word A: adjective
adj = ['Crafty',   'Angry',       'Bloody',     'Brave',     'Sleepy',
       'Sly',      'Lonely',      'Greasy',     'Clumsy',    'Thirsty',
       'Hungry',   'Grinning',    'Little',     'Quiet',     'Shady',
       'Happy',    'Drunken',     'Laughing',   'Clever',    'Dead',
       'Prancing', 'Gentle',      'Lost',       'Dark',      'Giggling',
       'Flying',   'Dirty',       'Shifty',     'Noisy',     'Faithful',
       'Singing',  'Iron',        'Lazy',       'Friendly',  'Ethereal',
       'Green',    'Silly',       'Ebon',       'Sad',       'Tipsy',
       'Filthy',   'Quick',       'Boisterous', 'Dusty',     'Young',
       'Purple',   'Timid',       'Enchanted',  'Three',     'Red',
       'Salty',    'Dancing',     'Jolly',      'Scarlet',   'Lucky',
       'Silver',   'Pious',       'Charming',   'Grim',      'Golden',
       'Old',      'Treacherous', 'Nervous',    'Careful',   'Crystal',
       'Nimble',   'Honest',      'Ancient',    'Swift',     'Eager',
       'Bronze',   'Fat',         'Bold',       'Zealous',   'Lewd',
       'Empty',    'Somber',      'Stern',      'Emerald',   'False',
       'Grateful', 'Crimson',     'Ruthless',   'Grumpy',    'Ugly',
       'Lively',   'Amber',       'Obedient',   'Two',       'Greedy',
       'Fair',     'Gray',        'Ruby',       'Whistling', 'Stubborn',
       'Ten',      'Naughty',     'Brass',      'Crooked',   'Slimy']
number = ['Two', 'Three', 'Ten'] # number adjectives

# word B: noun
noun = ['Lizard',   'Ploughman', 'Fountain',   'Bird',     'Barrel',
        'Boar',     'Ogre',      'Cartwright', 'Demon',    'Miller',
        'Mare',     'Stallion',  'Dagger',     'Pony',     'Cauldron',
        'Troll',    'Griffon',   'Goblin',     'Skull',    'Rogue',
        'Nymph',    'Harpy',     'Orc',        'Spoon',    'Hearth',
        'Bard',     'Devil',     'Squire',     'Frog',     'Bottle',
        'Artisan',  'Haven',     'Rabbit',     'Poet',     'Castle',
        'Priest',   'Wolf',      'Oak',        'Giant',    'Eagle',
        'Captain',  'Falcon',    'Skillet',    'Fairy',    'Princess',
        'Garden',   'Dragon',    'Prince',     'Wench',    'Maiden',
        'Queen',    'Knight',    'Wizard',     'Unicorn',  'Swan',
        'Hound',    'Arms',      'Temple',     'King',     'Tankard',
        'Fool',     'Tanner',    'Shield',     'Hawk',     'Archer',
        'Sandals',  'Fox',       'Flagon',     'Pirate',   'Warlock',
        'Hedgehog', 'Cobbler',   'Bear',       'Hunter',   'Hero',
        'Keg',      'Gardener',  'Wanderer',   'Monkey',   'Heroine',
        'Blade',    'Jester',    'Serpent',    'Greaves',  'Guard',
        'Liar',     'Toad',      'Crier',      'Sailor',   'Farmer',
        'Spirit',   'Squirrel',  'Fletcher',   'Huntress', 'Snake',
        'Drunkard', 'Galley',    'Bowl',       'Warlord',  'Vulture']
plural = ['Arms', 'Sandals', 'Greaves']
ies = ['Pony', 'Harpy', 'Fairy']
es = ['Princess', 'Wench', 'Fox', 'Hero', 'Huntress']

# BARKEEP/SERVERS/BOUNCERS
races = ['Tiefling', 'Elf', 'Halfling', 'Dwarf', 'Human', 'Half-elf', 'Eladrin', 'Dragonborn']
r_w = [2, 4, 6, 8, 14, 16, 18, 20]
genders = ['m', 'f', 'nb']
pronouns = ['he/him',      'she/her',    'they/them',   'he/they', 'she/they',
            'xe/xir',      'he/xe',      'she/xe',      'they/xe', 'he/she',
            'he/she/they', 'he/xe/they', 'she/xe/they', 'all']
ages = {'Dragonborn':'5d10+13',
       'Dwarf':     '2d100+19',
       'Eladrin':   '3d100+18',
       'Elf':       '2d100+19',
       'Halfling':  '5d10+16',
       'Human':     '5d10+16',
       'Half-elf':  '5d10+16',
       'Tiefling':  '5d10+16'}
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
honorifics = ['the Perceiver',
              'Veteran of Shavarath',
              'the Insightful',
              'Collector of Debts',
              'the Summoner',
              'Speaker of Profit',
              'Chainer of Demons',
              'the Conqueror',
              'Glory Seeker',
              'the Victorious',
              'the Infiltrator',
              'the Voluminous',
              'the Stoic',
              'the Shatterer',
              'the Keeper',
              'the Faithful',
              'the Clever',
              'the Chanter',
              'the Indomitable',
              'the Vicious']

# INN ATMOSPHERE
atmosphere = ['Depressing', 'Down',    'Dark',        'Angry', 'Fearful',
              'Tense',      'Anxious', 'Strange',     'Sad',   'Boring',
              'Quiet',      'Calm',    'Comfortable', 'Light', 'Upbeat',
              'Pleasant',   'Serene',  'Fun',         'Loud',  'Exciting']
atmreason = {'Depressing':'All alcohol shipments have been delayed, resulting in a low supply and increased prices',
             'Down':'Poor trade, bad weather, and the slow flow of coin has soured people\'s mood',
             'Dark':'Patrons reflect on a previous war that ravaged the land. Entire families lost their lives, and gruesome tales dominate the conversation.',
             'Angry':'A rival settlement has been encroaching on local trade, causing businesses to suffer.',
             'Fearful':'An ominous chill permeates the air. People speak in hushed tones, whispering queitly among themselves.',
             'Tense':'A patron complains profusely to the innkeeper about the poor quality of the food, drink, and service and refuses to pay his tab.',
             'Anxious':'The weather has been unfavorable for the local crops and outlying farms. This not only hurts trade, but could cause a severe food shortage.',
             'Strange':'The music played by the bard is... eerie. People laugh at nothing in particular. A child in the corner sits alone, rocking back and forth on the floor.',
             'Sad':'The passing of a local priest hit the community hard, and today is the anniversary of her death.',
             'Boring':'The food is bland and uninspired, as is the drink. No one seems capable of cracking a smile or talking to one another.',
             'Quiet':'The previous night of revelry and merriment has caused most patrons to simply sit quietly and try not to make sudden moves - at least, until the next big party.',
             'Calm':'The mood is low-key but not somber, and all the patrons are behaving themselves.',
             'Comfortable':'Due to improved trade, food and ale is in good supply and of fine quality. Prices are fair, the lasses and lads fairer, and customers are happy.',
             'Light':'With the crops in, the populace healthy, and the mead flowing, smiles are exchanged as often as coin.',
             'Upbeat':'Business is looking up, and the troubles of yesterday seem far in the past.',
             'Pleasant':'Whether it\'s the menu, the mead, the large pitchers, or the prices, the owner is clearly doing something right.',
             'Serene':'The sound of song resonates within the walls as if the building and the voice were a single instrument.',
             'Fun':'The innkeeper has decided to share a humorous tale or two, causing sudden bursts of laughter and the pounding of fists on tables.',
             'Loud':'Drink up! There\'s another keg on its way! A party is in full swing, with strangers and friends alike sharing tales, beer, and merriment.',
             'Exciting':'Preparations for a lcoal celebration are being made. Naturally, the beer and wine have to be thoroughly tested and tasted to ensure their quality.'}

# INN QUALITY (5e)
lifestyles = ['Wretched',
              'Squalid',
              'Poor',
              'Modest',
              'Comfortable',
              'Wealthy',
              'Aristocratic']
itemprices = {}
itemprices['Ale'] = {'Gallon':  '2 sp',
                     'Mug':     '4 cp'}
itemprices['Wine'] = {'Common': '2 sp', # pitcher
                      'Fine':   '10 gp'} # bottle
itemprices['Banquet'] =         '10 gp' # per person
itemprices['Loaf of bread'] =   '2 cp'
itemprices['Hunk of cheese'] =  '1 sp'
itemprices['Chunk of meat'] =   '3 sp'
# room prices per day
itemprices['Inn stay'] = {'Squalid':      '7 cp',
                          'Poor':         '1 sp',
                          'Modest':       '5 sp',
                          'Comfortable':  '8 sp',
                          'Wealthy':      '2 gp',
                          'Aristocratic': '4 gp'} # per day
# meal prices per day
itemprices['Meals'] = {'Squalid':      '3 cp',
                       'Poor':         '6 cp',
                       'Modest':       '3 sp',
                       'Comfortable':  '5 sp',
                       'Wealthy':      '8 sp',
                       'Aristocratic': '2 gp'}

# INN QUALITY (4e)
qualities = ['Poor', 'Common', 'Fine']
roomprices = {'Poor':  {'standard':'2 cp', 'best':'5 cp'},
              'Common':{'standard':'2 sp', 'best':'5 sp'},
              'Fine':  {'standard':'2 gp', 'best':'10 gp'}}
sizes = [1,2,3,4,5,6,7,8,9,10,11,12]
numrooms = {1:0,
            2:2,
            3:4,
            4:4,
            5:4,
            6:6,
            7:6,
            8:8,
            9:8,
            10:10,
            11:10,
            12:12}
staffsizes = {1:{'servers':1, 'bouncers':0},
              2:{'servers':1, 'bouncers':0},
              3:{'servers':2, 'bouncers':0},
              4:{'servers':3, 'bouncers':1},
              5:{'servers':4, 'bouncers':2},
              6:{'servers':4, 'bouncers':2},
              7:{'servers':5, 'bouncers':2},
              8:{'servers':5, 'bouncers':2},
              9:{'servers':6, 'bouncers':2},
              10:{'servers':7, 'bouncers':2},
              11:{'servers':7, 'bouncers':4},
              12:{'servers':8, 'bouncers':6}}

# CUISINE
specialprices = {'Poor':  {'Food':'3 cp', 'Drink':'1 cp'},
                 'Common':{'Food':'2 sp', 'Drink':'1 sp'},
                 'Fine':  {'Food':'2 gp', 'Drink':'1 gp'},
                 'Luxe':  {'Food':'5 pp', 'Drink':'1 pp'}}
regions = ['Urban',   'Desert',   'Tundra', 'Roadside', 'Mountain',
           'Plains',  'Coastal',  'Swamp',  'Tropical', 'Cave',
           'Country', 'Woodland', 'Unsavory']
cuisines = {'Aereni':       ['Urban',    'Coastal',  'Tropical', 'Woodland'],
            'Adaran':       ['Tundra',   'Mountain'],
            'Audairian':    ['Urban',    'Roadside', 'Country',  'Woodland'],
            'Brelish':      ['Urban',    'Roadside', 'Coastal',  'Tropical'],
            'Cyran':        ['Urban',    'Roadside', 'Country'],
            'Dhakaani':     ['Mountain', 'Cave'],
            'Droaamite':    ['Mountain', 'Plains',   'Swamp',    'Cave',     'Unsavory'],
            'Druidic':      ['Mountain', 'Country',  'Woodland'],
            'Ghaashkalan':  ['Tundra',   'Mountain', 'Plains',   'Country'],
            'Giantish':     ['Desert',   'Tropical'],
            'Goblin':       ['Urban',    'Mountain', 'Plains',   'Tropical', 'Cave'],
            'Karrnathian':  ['Roadside', 'Mountain', 'Country',  'Woodland', 'Unsavory'],
            'Khoravar':     ['Urban',    'Country'],
            'Lhazaarite':   ['Roadside', 'Coastal',  'Country',  'Unsavory'],
            'Marcher':      ['Coastal',  'Swamp',    'Tropical'],
            'Mroranon':     ['Tundra',   'Mountain', 'Cave'],
            'Qbarran':      ['Coastal',  'Swamp',    'Tropical'],
            'Reacher':      ['Mountain', 'Country',  'Woodland'],
            'Riedran':      ['Desert',   'Plains',   'Tropical', 'Country',  'Unsavory'],
            'Sharn fusion': regions,
            'Shifter':      ['Country',  'Woodland'],
            'Sulatar':      ['Desert'],
            'Syrkarn':      ['Desert',   'Plains'],
            'Tashanan':     ['Tundra',   'Mountain', 'Coastal'],
            'Thranian':     ['Roadside', 'Country'],
            'Umbragen':     ['Cave'],
            'Vulkoori':     ['Swamp',    'Tropical'],
            'Xendrik':      ['Desert',   'Tundra',   'Swamp',    'Tropical', 'Cave'],
            'Zil':          ['Urban',    'Coastal',  'Tropical', 'Woodland']}
# random food & drink specials
#   Urban: 10% chance to roll a random cuisine
#   Mountain: 10% chance to roll on Cave cuisine
#   Cave: 10% chance to roll on Mountain cuisine
#   Coastal: 10% chance to roll on random cuisine
specials = {'Urban':{'Food':['Braised beef and pears with ginger',
                             'Roasted cod and mashed potatoes',
                             'Minted pea soup',
                             'Beef steak and kidney pie',
                             'Poached duck with farro',
                             'Rib roast and vegetables',
                             'Clams and garlic',
                             'Cedar planked salmon',
                             'Rack of lamb and baked potato',
                             'rand'],
                     'Drink':['Fire mead',
                              "King's ale",
                              'Dwarven double draft',
                              'Aerenal reserve',
                              'Spiced apple cider',
                              'Fey wine',
                              'Star wine',
                              "Lord's lager",
                              'Royal reserve',
                              'rand']},
            'Desert':{'Food':['Raw horse sushi with rock cress',
                              'Baked rattlesnake and spring parsley',
                              'Baked camel meat and brittlebrush salad',
                              'Barbecued gopher legs on a stick',
                              'Iguana bits with rattleweed sauce',
                              'Fried ostrich and egg omelet',
                              'Meerkat dumplings with sage',
                              'Salted camel and blue flax bread',
                              'Scorpion soup and blister beetle crackers',
                              'Spiced baked coyote with jewelflower'],
                      'Drink':['Scorpionweed reserve',
                               'Desert star wine',
                               'Cactus spirits',
                               'Poppy port',
                               'Purple sand juice',
                               'Mariposa mead',
                               'Flax mead',
                               'Chia tea',
                               'Desert lily brandy',
                               'Keysia liqueur']},
            'Tundra':{'Food':['Muxk ox soup and bearberries',
                              'Braised pike and thistle stems',
                              'Grilled muksun with reed root',
                              'Hare stew and willow crackers',
                              'Boiled walrus and fireweed seeds',
                              'Seal chunks with lichen dip',
                              'Caribou stew and dried mossbread',
                              'Lemming and berry soup',
                              'Reindeer ribs with acorn broth',
                              'Crowberry pie with smoked elk'],
                      'Drink':['Caribou special reserve',
                               'Fireweed whiskey',
                               'Berry brandy',
                               'North ice wine',
                               'Moss mead',
                               'Willow tea',
                               'Crowberry cider',
                               'Thistle port',
                               'Glacial lichen liqueur',
                               'Juniper juice']},
            'Roadside':{'Food':['Salted onions and bread',
                                'Rabbit stew and crusts',
                                'Leeks and berries',
                                'Scrambled eggs and sprouts',
                                'Peppered milk-toast',
                                'Cabbage in a cup',
                                'Rice and peas',
                                'Cauliflower soup and corn',
                                'Barbecue elk and broccoli',
                                'Venison pie and bread'],
                        'Drink':['Dark road ale',
                                 "Star's moonshine",
                                 'Apple cider',
                                 'Apricot cider',
                                 'Spiced ale',
                                 'Wanderer whiskey',
                                 "Traveler's spirits",
                                 'Honeysuckle mead',
                                 'Plum cider',
                                 'Drifter draft']},
            'Mountain':{'Food':['Wild parsnip stew',
                                'Sable and hawthorn pie',
                                'Grilled elk and ground orchids',
                                'Roast grouse and turnips',
                                'Thistle salad with roasted grubs',
                                'Crisped worm skewers and potatoes',
                                'Baked goat flank',
                                'Moss biscuits with syrup',
                                'Roast antelope with root salad',
                                'Cave'],
                        'Drink':['Wombat berry cider',
                                 "Goat's milk and brandy",
                                 'Sable spirits',
                                 'Dwarven double draft',
                                 'Wild orchid wine',
                                 'Mroranon mead',
                                 'Earthen brandy',
                                 'Triple tankard',
                                 'Silvermoon mead',
                                 'Cave']},
            'Plains':{'Food':['Roast buffalo and sage bread',
                              'Rabbit and baked pumpkin',
                              'Moose flank and wild green salad',
                              'Green chili stew',
                              'Blue corn dumplings',
                              'Bison horn soup',
                              'Grilled moose steak',
                              'Buffaloaf and honeyed corn',
                              'Poached and peppered quail eggs',
                              'Smoked salmon and wild berries'],
                      'Drink':['Bison hunter brandy',
                               'Spiced apple cider',
                               'Wanderer whiskey',
                               'Plainsman\'s port',
                               'Wild berry brandy',
                               'Honey mead',
                               'Tracker tea',
                               'Pumpkin cider',
                               'Sage spirits',
                               'Moose horn moonshine']},
            'Coastal':{'Food':['Roast chicken with thyme',
                               'Lobster in tomato cream sauce',
                               'Rack of lamb platter',
                               'Crab-stuffed lobster tail',
                               'Rock salt-encrusted prime rib',
                               'Baked loin of pork with gravy',
                               'Steamed mussels with fennel',
                               'Roast pheasant in oyster sauce',
                               'Celery and octopus salad with lemon',
                               'rand'],
                       'Drink':['Aerenal reserve',
                                'Apricot cider',
                                'Wight wine',
                                'Archon ale',
                                'Dwarven double draft',
                                'Royal reserve',
                                'Westgate wine',
                                'High spirits',
                                "King's ale",
                                'rand']},
            'Swamp':{'Food':['Grilled water snake in marigold sauce',
                             "Frogs' legs and bulrush stems",
                             'Roast heron and chopped sundew',
                             'Lily-wrapped butterfly chips',
                             'Bog beetle dumplings',
                             'Wren pot pie and cattail soup',
                             'Black currant braised alligator',
                             'Toasted dragonflies and cranberries',
                             'Warbler stew and blueberry bread',
                             'Grilled crocodile and wild rose puree'],
                     'Drink':['Swamplight spirits',
                              'Trollbane ale',
                              'Cranberry cider',
                              'Lily liqueur',
                              'Bulrush brandy',
                              'Black currant juice',
                              'Wild rose reserve',
                              'Red currant lager',
                              'Black tupelo tea',
                              'Sundew mead']},
            'Tropical':{'Food':['Smashed cinnamon potatoes',
                                'Grilled snake and macadamia',
                                'Roasted crocodile in coconut milk',
                                'Frogs on sugar cane skewers',
                                'Chocolate covered ants and roast pelican',
                                'Stewed bandicoot with cocoa',
                                'Alligator soup and melon pastry',
                                'Barbecued tiger fish and papaya',
                                'Spiced monkey tail and cashews',
                                'Lizard gruel with nutbread'],
                        'Drink':['Coffee',
                                 'Tangerine brandy',
                                 'Rice wine',
                                 "Orchid's tear spirits",
                                 'Mango cider',
                                 'Maize liqueur',
                                 'Plum leaf tea',
                                 'Chocolate milk and brandy',
                                 'Lotus leaf wine',
                                 'Papaya tea']},
            'Cave':{'Food':['Fluorescent fungus salad with cave grubs',
                            'Diced blind eel and deep salts',
                            'Amber lichen and softrock bread',
                            'Translucent crayfish stew',
                            'Crimson moss cakes and cave jelly',
                            'Crustacean broth with ironloaf',
                            'Roasted deeps beetles with algae dip',
                            'Toasted salamander in mineral pepper',
                            'Arachnidumplings and fried fungus',
                            'Mountain'],
                    'Drink':['Lichen liqueur',
                             'Mineral mead',
                             'Algae ale',
                             'Mushroom moonshine',
                             'Dwarven double draft',
                             'Deeps ale',
                             'Mroranon mead',
                             'Shadow stein',
                             'Softrock spirits',
                             'Mountain']},
            'Country':{'Food':['Roast chicken and potatoes',
                               'Beef stew and sourdough',
                               'Cheese pie and onion soup',
                               'Mushroom soup and garlic toast',
                               'Pork loin and dumplings',
                               'Mutton meatloaf',
                               'Baked boar and greens',
                               'Squash and fish soup',
                               'Rabbit curry',
                               'Venison and bean stew'],
                       'Drink':['Shepherd spirits',
                                'Rice wine',
                                "Ploughman's port",
                                "Miller's moonshine",
                                'Herb and mint tea with brandy',
                                'Spiced apple cider',
                                'Wainwright whiskey',
                                'Vitae juice',
                                'Paddock plum wine',
                                'Royal reserve']},
            'Woodland':{'Food':['Acorn soup',
                                'Honey braised boar ribs',
                                'Baked pheasant with leeks',
                                'Grilled wild boar chops',
                                'Cashews and berry pie',
                                'Roast stag in antler sauce',
                                'Grilled moose skewers',
                                'Broiled salmon and potatoes',
                                'Mushroom stew with corn bread',
                                'Fried turkey legs'],
                        'Drink':['Honey mead',
                                 'Spiced apple cider',
                                 'Silvermoon mead',
                                 'Fey wine',
                                 "Star's moonshine",
                                 'Glitter mead',
                                 "Woodsman's whiskey",
                                 'Ranger reserve',
                                 'Tracker tea',
                                 'Aerenal reserve']},
            'Unsavory':{'Food':['Crunchy critters and grub pudding',
                                'Smashed guts and cabbage',
                                "Not-so-old rice in sour goat's milk",
                                'Green beaf and brown leek stew',
                                'Fried chunks and lard bread',
                                'Grilled ins-and-outs',
                                'Salted eyes and carrot ends',
                                'Bone and blood mix stew',
                                'Lettuce, liver, and lung pie',
                                'Bloated boar bits and eggs'],
                        'Drink':['All-sorts',
                                 'Cool grog',
                                 'Dregs and water',
                                 'Angel spit ale',
                                 'Orc spirits',
                                 'Quarter-mead',
                                 'Bacon beer',
                                 '"Almost" ale',
                                 'Turnip wine',
                                 'Abyssal ale']},
            'Aundair':{'Food':['Pan-seared rabbit with Aundairian wood-nut sauce',
                               'Gold pheasant stuffed with sparkle mushrooms and rice',
                               'Dragon salmon in butter and dark wine sauce',
                               'Aundairian tarts',
                               'Cremfels - thin, fruit-and-cream-filled pancakes'],
                       'Drink':['Bluevine wine',
                                'Mount and Moon Enterprises rare vintage',
                                'Arcanix fireburst wine',
                                'Orla-un wine - dark and fruity sweet',
                                'Windshire rainbow wine - mursi (red); continuously changes color and flavor',
                                'Fairhaven Vintners wine',
                                "Aundair's Finest wine"]},
            'Breland':{'Food':['Beef Boranel - bread and mushroom stuffing roasted inside a full side of beef',
                               "Farmer's stew",
                               'Thrice-poached eggs',
                               'Thrice-poached eggs and sizzling pheasant', 
                               'Kettle fried spider and redeye berries', 
                               'Fire-wrapped golden fish', 
                               'Spiced pork and orange peppers', 
                               'Hot-spiced chicken in panya leaves']},
            'Karrnath':{'Food':['Karrnathi sausage',
                                'Karrnathi cheese',
                                'Karrnathi stew',
                                'Karrnathi multilayered casserole',
                                'Vedbread - crusty bread with sharp ved cheese',
                                'Vedbread slathered with onion butter',
                                'Karrnathi pie',
                                'Doomvault Swine Run cured pork',
                                'Dream pie',
                                'Barovian butterscotch pudding'],
                        'Drink':['Karrnathi brew',
                                 'Nightwood ale',
                                 'Brinter Distillery Nightwood Ale',
                                 'Hyruvi and Sons Nightwood Ale',
                                 'Red Dragon Crush wine',
                                 'Purple Grapemash No. 3 - Wizard of Wines vineyard']},
            'Thrane':{'Food':['Thrakel-seared beef in red sauce',
                              'Three-thrakel fish stew',
                              'Silvered vegetable skewers',
                              'Beesh-berry sorbet',
                              'Silverfruit pie',
                              'Silverfruit pie with beesh-berry sorbet']},
            'Human':{'Food':["Traveler's stew - beef, carrots, potatoes, and onions in a dark beer broth",
                             'Iron rations - cured meats, dried fruits, nuts, and cheeses with biscuits, crackers, or hardtack',
                             'Sharn seafood bouillabaisse - haddock, clams, and mussels simmered in a light fish and tomato stock with a licorice-flavored aperitif and a pinch of fennel',
                             'Pan-fried knucklehead trout with shallots, lemon, salt, pepper, and paprika',
                             'Arcanix braised beef with cider, pear, and ginger',
                             'Havenglen golden brown roasted turkey with sausage stuffing and drippings',
                             'Gurdats - mushrooms with cheese filling',
                             'Hand pies - venison, chicken, beef, lamb, or peacock',
                             'Sharn dark molasses nutbread with whipped, salted butter',
                             'Wildnight candied apples',
                             'Vedbread - crusty bread with sharp ved cheese',
                             "Lhazaar's skillet-fried spiced potatoes",
                             'Stormreach buttermilk biscuits with rose-apple butter spread, elderberry preserves, or brackleberry jam',
                             'Stormreach buttermilk biscuit sandwich with eggs and ham or pork'
                             'Adaran noodles fried with chicken, vegetables, and fish sauce',
                             "Zarash'ak honey-grilled rothe ribs",
                             'Karrnwood venison pot roast',
                             'Fairhold onion soup',
                             'Tavern "steak" with bun, dill-yogurt sauce, crushed tomatoes, or black olive and fig sauce',
                             'Gingerbread man'],
                     'Drink':['Beer',
                              'Ale',
                              'Port',
                              'Whiskey',
                              'Wine',
                              'Licorice aperitif',
                              'Perry - hard pear cider',
                              'Apple cider',
                              'Tea',
                              'Amber wine']},
            'Elven':{'Food':['Quith-pa - balls of chopped dried fruits, seeds, and nuts',
                             'Thelanian whipped eggs with herbs and cheese',
                             'High Harvest puree - butternut squash, garlic, and thyme',
                             'Elven bread with cinnamon or cardamom swirl',
                             'Tairnadal forest salad with citrus and flowers',
                             'Elven marruth - vegetable pastries rolled in rallow leaves',
                             'Drow ripplebark mushroom steaks',
                             'Cherrybread with fruits and nuts marinated in rum',
                             'Khoravar greenspear bundles in bacon',
                             'Aereni seafood rice - shrimp and scallop risotto',
                             'Aundairian dragon salmon',
                             'Cremfel - thin pancake stuffed with cream and fruit',
                             'Khoravar vegetable stew - sliced and layered eggplant, zucchini, squash, tomato, and basil',
                             "Meal's end - heavy cream, fruit, and crushed meringue",
                             'Elven fritto misto - vegetables, citrus, seafood, and herbs, all deep-fried',
                             'Aereni surrogate steaks'],
                     'Drink':['Feywine - nectar of flowers and honey',
                              'Elverquist',
                              "Nature's dew",
                              'Dark rum',
                              'Amber rum',
                              'Elven dry white wine',
                              'Evermead - honey, ginger, clove, cinnamon, & berry',
                              'Hot spiced amber cider',
                              'Evermead with a shot of vodka or brandy',
                              'Sprucebark quaff']},
            'Dwarven':{'Food':['Bangers and smash',
                               'Mroranon "tide-me-overs" - meatballs and gravy',
                               'Underdark lotus with fire lichen spread',
                               "Miner's pie - beef, lamb, or venison with vegetables, potato mash, and cheese",
                               'Potato leek soup',
                               'Smoked sausages and kraut with dwarven mustard',
                               'Corned beef and cabbage',
                               'Gully dwarf homestyle porridge',
                               'Dwarven flatbread with cheese or fire lichen spread',
                               'Orange mountain duck',
                               'Plate-of-gold - battered, fried vegetables with sweet citrus sauce',
                               'Black pudding - coffee and chocolate mousse',
                               'Dwarven dark bread',
                               'Dry-aged meats',
                               'Dwarven mustard'],
                       'Drink':['Dwarven ale',
                                'Dwarven mead',
                                'Dwarven stout',
                                "Dragon's wine",
                                'Dwarven mulled wine',
                                'Hot spiked cider']},
            'Halfling':{'Food':['Community cheeses - melted, with fruit, meat or bread for dipping',
                                'Stuffed egg-battered toast',
                                'Chicken-something dumplings',
                                'Hogs in bedrolls',
                                'Melted cheeses with chunky tomato broth',
                                'Halfling oatmeal sweet nibbles - chocolate chip and butterscotch',
                                'Talenta Plains salad',
                                'Everything soup - vegetables and poultry',
                                'Honeyed ham with pineapple gravy',
                                'Heartlands rose apple and blackberry pie',
                                'Honey-drizzled cream puffs',
                                'Boromar butterscotch',
                                'House Ghallanda artisanal cheeses',
                                'Fluffy morning buns',
                                'Talenta Plains honey'],
                        'Drink':['Talentan tea',
                                 'Talentan coffee',
                                 'Malted milk',
                                 'Malted milkshake',
                                 'Spiced cocoa broth',
                                 'Moonslake - mint & apple cider cocktail']},
            'Uncommon':{'Food':["Malleon the Reaver's flame-roasted turkey chili", # dragonborn
                                "Goliath bacon - brown sugar, garlic, pepper, and citrus", # goliaths
                                'Fire-spiced abyssal chicken kebabs', # tiefling
                                'Hardbuckler stew - potatoes, mushrooms, lichen, turnips, and a meat medley', # gnome
                                'Twice-baked cockatrice wings', # tabaxi
                                'Braised lamb', # half-orc
                                'Deep gnome trillimac pods', # gnome
                                'Aereni surrogate steaks', # elven
                                'Barovian butterscotch pudding', # Karrnathi
                                'Fried fingers - poultry strips with plum sauce', # Saltmarsh lizardfolk
                                "Irian shepherd's bread", # aasimar
                                'Hellhound marrow', # tiefling
                                "Q'barran flambe crispy turkey flesh", # dragonborn
                                'Live seafood bouillabaisse', # triton
                                'Fire fruit with fiendspice', # tiefling
                                'Skewers of barbecued meats', # dragonborn
                                'Goat cheese-stuffed mushrooms', # gnome
                                ], 
                        'Drink':[]},
            'Dragonborn':{'Food':["Q'barran flambe crispy turkey flesh",
                                  'Skewers of barbecued meats',
                                  "Malleon the Reaver's flame-roasted turkey chili"],
                          'Drink':[]},
            'Gnome':{'Food':['Goat cheese-stuffed mushrooms',
                             'Hardbuckler stew - potatoes, mushrooms, lichen, turnips, and a meat medley',
                             'Deep gnome trillimac pods',
                             'Trillimac stalk loaf',
                             'Mushroom & cheese platter'],
                     'Drink':[]},
            'Tiefling':{'Food':['Hellhound marrow',
                                'Fire fruit with fiendspice',
                                'Seasoned raw meat in marrow & blood sauce',
                                'Blackened vegetables',
                                'Minerals and charcoal',
                                'Fire-spiced abyssal chicken kebabs',
                                'Tiefling tomato-molasses'],
                        'Drink':['Sulfurous wine',
                                 'Ash-infused ale',
                                 'Absinthe of oil']},
            'Half-orc':{'Food':['Salted grubs',
                                'Chocolate-drizzled fireflies',
                                'Braised lamb'],
                        'Drink':[]},
            'Triton':{'Food':['Valraean live seafood bouillabaisse'],
                      'Drink':[]},
            'Sahuagin':{'Food':['Dominion live seafood bouillabaisse'],
                        'Drink':[]},
            'Tabaxi':{'Food':['Twice-baked cockatrice wings'],
                      'Drink':[]},
            'Lizardfolk':{'Food':['Fried fingers - poultry strips with plum sauce'],
                          'Drink':[]},
            'Aasimar':{'Food':["Irian shepherd's bread",
                               'Shiftspice',
                               "Irian shepherd's bread with shiftspice"],
                       'Drink':[]},
            'Elixirs':{'Food':[],
                       'Drink':["Mage's tea - elm bark with honey, chamomile, lemon, and orange",
                                "Archmage's tea - psychedelic bekial seed with honey, chamomile, lemon, and orange",
                                'Mushroom tea with kelp and savory sauce', # drow
                                'Evermead - honey, ginger, clove, cinnamon, & berry', # elven
                                'Evermead with a shot of vodka or brandy', # elven
                                'Dwarven mulled wine', # dwarven
                                'Spiced cocoa broth', # halfling
                                'Hot spiced cider',
                                'Reacher goodberry blend', # druidic
                                'Delayed blast fireball',
                                'Firestar wine',
                                'Hot toddy - firestar wine with spiced chai',
                                'The Mindflayer - iced vodka with ginger',
                                'Cone of Cold - iced vodka with ginger',
                                'Icewine',
                                'Sharn rollrum - herbal licorice tonic',
                                'Potion of restoration - gin with blackberry and lemon',
                                'Zzar - sluth with almond liqueur',
                                'Sluth - sparkling white wine',
                                "Q'barran zombie - rum with fruit medley"]},
            'Drow':{'Food':['Underdark lotus with fire lichen spread',
                            'Deep gnome trillimac pods',
                            'Trillimac stalk loaf',
                            'Mushroom & cheese platter',
                            'Drow ripplebark mushroom steaks',
                            'Gurdats - mushrooms with cheese filling'],
                    'Drink':['Mushroom tea with kelp and savory sauce']},
            '100Meals':{'Food':['Roasted tarantula with hairs carefully singed off and fangs used as toothpicks', # Droaam
                                'Centipede-wrapped onions roasted over coals and served with onion wine', # Stormreach/Xendrik
                                'Chicken cooked with thyme and ocher, wild carrots, and spring water', # Eldeen/Aundair/Breland
                                '"Devil\'s Tail" - venison sausages soaked in a salt and hot pepper brine', # Karrnath
                                'Rye bread spread with lard, washed down with a strong, dark ale', # Karrnath/Mror
                                'Rye bread',
                                'Bean stew thickened into a pudding with tapioca flour, scooped up with hollowed-out stale bread', # Riedra
                                'Stale bread',
                                'Strips of fried small game meat and mashed turnips, all covered in gravy', # Eldeen/Aundair/Karrnath
                                'Roasted hazelnuts and fresh apples with a small strip of bear jerky and a wedge of ripe cheese', # Eldeen/Zilargo/Breland
                                'Ripe cheese',
                                'Wild bison steaks, cooked up rare and seasoned with onions and garlic salts', # Droaam/Darguun/Talenta
                                'Large pieces of oat bread and a viscera pate served inside small badger skulls', # Karrnath
                                'Oat bread',
                                'Roasted pigeon served with small tomatoes, wide grasses, and crumbled goat cheese', # Talenta/Zilargo/Thrane
                                'Crumbled goat cheese',
                                'Pickled herring, pickled onions, pickled carrots, and plain rice', # Karrnath/Mror
                                'Pickled herring',
                                'Pickled onion',
                                'Pickled carrots',
                                'Spit-roasted dire boar, served with cheese and sweet wine and eaten communally', # Marches
                                'Thin, dried fish served with green beans and spiced apple cider', # Aundair/Thrane
                                'Stew of skinned bats and black morel mushrooms, served over toasted bread', # Mror/Umbragen/Xendrik/Darguun
                                'Toasted bread',
                                'Large turkey leg and boiled potatoes, served with thin mead', # Thrane/Breland
                                'Slow-roasted badger, split and filled with oat and potato mash', # Zilargo
                                'Oat and potato mash',
                                'Roast duck and artichokes served on silver plates, plus large silver mugs filled from a fountain of fine red wine', # Aundair
                                'Fried trout stuffed with smaller fish and a single olive, served on a bed of celery and chard', # Aundair
                                'Squirrel and onion soup served in large mugs, with cheese curds and rye bread on the side', # Karrnath/Eldeen/Marches
                                'Cheese curds',
                                'Shish kabobs of swamp grasses, tulip bulbs, and breaded frogs', # Marches
                                'Boiled clams and lobster served with yaga, a drink made by draining the sap and brewing the leaves of a local vine', # Sharn/Breland/Lhazaar
                                'Mutton cooked in garlic and large chunks of bread fried in lard', # Thrane/Karrnath
                                'Large chunks of bread fried in lard',
                                'Fried bacon and eggplant served with lots of ale', # Breland
                                'Smoked fish served with peas and strips of dried melon', # Breland
                                'Ox ribs, cheese, and black bread', # Karrnath
                                'Black bread',
                                'Boiled crayfish and porpoise pudding, served with lemon water or wine', # Sharn/Breland/Lhazaar
                                'Vultures stuffed with saffron rice and covered in paprika', # Thrane
                                'Overripe plums, almonds, dried oatcakes, and mead', # Eldeen/Droaam/Zilargo
                                'Dried oatcakes',
                                'Shark steaks with asparagus and sliced tomatoes, followed by tea and small raisin pastries', # Sharn/Stormreach/Lhazaar
                                'Small raisin pastries', # Breland
                                "Shepherd's pie made with ox meat, peas, and mashed turnips", # Breland/Karrnath
                                'Duck eggs fried in fat and red peppers, served with apple cider and cranberry juice', # Aundair/Thrane
                                'Jellyfish, scallops, and red kelp, all fried in drake-turtle oil', # Lhazaar
                                'Figs and dates with flaky pastries and rice', # Breland/Thrane/Karrnath/Aundair
                                'Flaky pastries',
                                'Roasted asparagus, tomatoes, eggplant, and artichokes, followed by coffee and almond tarts', # Aundair
                                'Almond tarts',
                                'Boiled beans and strips of roc jerky', # Xendrik/Dor Maleer/Riedra
                                'Roc jerky',
                                'Shelled snails and thick chunks of octopus tentacles wrapped in seaweed and roasted',
                                'Sylvan stag meat spit-roasted over aged treant wood and served on a clean bed of dryad hair',
                                'Cobra soaked in strong wine and roasted in the skin, served with olives and pickled lemons',
                                'Olives',
                                'Pickled lemons',
                                'Roast mutton stew with wild carrots, lettuce, and celery, served with fresh bread',
                                'Fresh bread',
                                'Griffon meat boiled with red peppers and whey and heavily salted',
                                'Bear liver with onions and garlic, grilled over an open fire and served with pickled peppers and ale',
                                'Pickled peppers',
                                'Otyugh thighs soaked in brine for a year and tenderized with a warhammer before roasting',
                                'Mushroom pasta with sauce made from minced lizards, garlic, and zucchini',
                                'Mushroom pasta',
                                'Rat meat stew',
                                'Roasted horse legs and horse marrow pudding served with black bread and ale',
                                'Horse marrow pudding',
                                'Spit-roasted monitor lizard basted with salt water and seal oil', # Tashana
                                'Fried drake-turtle meat served with large chunks of blubber and dried berries', # Lhazaar
                                'Dried berries',
                                'Soup made with hyena meat, wild rice, and wild carrots, followed by fresh fruit', # Droaam
                                'Fresh fruit',
                                'Pastry made from salted fish meats and dried coconut', # Sharn/Stormreach
                                'Mastodon steaks roasted and served on the spears that brought the animal down', # Tashana/Ghaashkala
                                'Crocodile meat sliced thin and seared in peanut oil, served with sliced turnips and fresh berries',
                                'Sliced turnips and fresh berries',
                                'Bread soaked in horse blood and milk and lightly fried',
                                'Pig brains mashed in wooden troughs and cooked by adding boiling pepper water',
                                'Boiled eels slit down the middle and filled with rice and beans',
                                'Rice and beans',
                                'Pastries made with almonds, pine nuts, and honey, served with wine',
                                'Elk ribs covered in gravy made from blood and ground oats',
                                'Scorpion roasted in the shell and served with goat meat and potatoes',
                                'Goat meat and potatoes',
                                'Chopped shrieker, soaked in a beef bullion and fried with beans', # Mror/Umbragen/Xendrik 
                                'Mutton and "ink pudding" made from chopped walnuts and aged walnut husks',
                                '"Ink pudding" made from chopped walnuts and aged walnut husks',
                                '"Gorgon Breath" stew made from lizard meat, hot peppers, and onions, served with a mixture of water and goat\'s milk',
                                'Goat cheese, baked pears, and bread', # Aundair
                                'Goat cheese',
                                'Sea turtle stew cooked in the shell and eaten communally with pieces of flatbread',
                                'Flatbread',
                                'Hard-boiled ostrich eggs, sliced and served with tomatoes and asparagus', # Talenta
                                'Hippogriff jerky boiled with peanuts, barley, and hops',
                                'Hippogriff jerky',
                                'Giant shrimp grilled in sunflower oil and covered in coarse salt', # Stormreach/Xendrik
                                'Sliced plantain fried with coconut and nuts', # Sharn
                                'Seven small courses of freshly boiled fish, followed by kelp pudding and soft-boiled turtle eggs', # Lhazaar/Syrkarn/Riedra
                                'Beef tenderized with black peppers and cloves, wrapped in fern leaves and baked in clay ovens', # Eldeen/Marches/Zilargo
                                'Thick squirrel meat and cabbage stew covered with melted cheese and breadcrumbs',
                                'Dried chunks of salted pork, covered in cassava paste and aged, served with plenty of cider',
                                'Large beetles seared in peanut oil and spices, crushed to a paste, then molded into small balls and deep fried',
                                'Locusts fried with butter and yams',
                                "Goat's tongue sliced thin and boiled with bamboo shoots and basil, served with weak wine",
                                'Live, juicy beetles in a sticky bed made from tapioca flour and mustard',
                                'Roasted mealworms and waxworms, seasoned with salt and paprika',
                                'Spit-roasted stork, with the head cooked separately',
                                'Raw, freshly killed wild boar, served with lemons and salt',
                                'Onions with cumin sauce and hard bread',
                                'Hard bread',
                                'Venison custard with peas and beans',
                                'Bread pudding with eggs and gooseberry tarts',
                                'Bread pudding',
                                'Gooseberry tarts',
                                'Deviled eggs stuffed with cheese and manticore meat, served with fried tomatoes',
                                'Deviled eggs',
                                'Fried tomatoes',
                                'Egg and spinach pie',
                                'Mastodon meat pies, with ale served in tall ivory mugs',
                                'Beef meatballs in a sauce of almond milk and rice',
                                'Black bread and chicken candied with cinnamon and honey, served with coffee',
                                'Flat breads, nuts, melon slices, and tea',
                                'Songbird pudding and roast mutton with soft cheese and oatcakes', # Thrane
                                'Oatcakes',
                                'Cooked root vegetables with breadcrumbs and gingerbread for dessert',
                                'Gingerbread',
                                'Spinach and egg tarts with honey-roasted walnuts',
                                'Beef and marrow pies served with hare soup and bread slices fried in butter and wine',
                                'Beef and marrow pies',
                                'Hare soup',
                                'Bread slices fried in butter and wine',
                                "Roasted boar's tail with hot sauce and cold fish soup",
                                'Cold fish soup',
                                'Silk grubs cooked in peanut oil and mint, served with fermented yogurt drinks',
                                'Roast lamb stuffed with bread, walnuts, peanuts, and coriander',
                                'Asparagus soup and pan-fried mackerel with gooseberry sauce',
                                'Curried goat with rice and peas, served with wine or strong rum',
                                'Thick slices of giant beans, roasted and served with vinegar and salt',
                                'Monkfish stuffed with mushrooms in a mint dressing',
                                'Roasted lizard on a stick and wine served from a bottle containing a snake'],
                        'Drink':['Onion wine', # Stormreach
                                 'Spring water',
                                 'Strong dark ale',
                                 'Sweet wine',
                                 'Spiced apple cider',
                                 'Thin mead',
                                 'Fine red wine',
                                 'Yaga - a drink made by draining the sap and brewing the leaves of a local vine',
                                 'Ale',
                                 'Lemon water',
                                 'Wine',
                                 'Mead',
                                 'Tea',
                                 'Apple cider',
                                 'Cranberry juice',
                                 'Coffee',
                                 'Strong wine',
                                 'Milk',
                                 "Mixture of water and goat's milk",
                                 "Goat's milk",
                                 'Ox blood mixed with ox milk and a little cinnamon',
                                 'Ox milk',
                                 'Cider',
                                 'Weak wine',
                                 'Ale served in tall ivory mugs',
                                 'Fermented yogurt drink',
                                 'Strong rum',
                                 'Wine served from a bottle containing a snake']},
            }

# ADD WILDEMOUNT FOODS/DRINKS
for region in wildemountregions:
    specials[region] = {'Food':[], 'Drink':[]} # initialize empty entry in specials
    _list = favfoods[region]
    if region == 'Menagerie Coast':
        specials[region]['Food'].append(_list[:6])
        specials[region]['Drink'].append(_list[6:])
    elif region == 'Marrow Valley':
        specials[region]['Food'].append(_list[:7])
        specials[region]['Drink'].append(_list[7:])
    elif region == 'Greying Wildlands':
        specials[region]['Food'].append(_list[:6])
        specials[region]['Drink'].append(_list[6:])
    elif region == 'Xhorhas':
        specials[region]['Food'].append(_list[:6])
        specials[region]['Drink'].append(_list[6:])

# MENUS
menus = {'The Yawning Portal':{
            'Morningfeast':['Eggs and chives                            - 4 cp',
                            'Biscuit, ham & egg                         - 3 cp',
                            'Porridge and cream                         - 3 cp',
                            'Ham platter                                - 4 cp',
                            'Talyth                                     - 5 cp'],
            'Cheeses':[     'Luiren Spring cheese (wheel)               - 1 sp',
                            'Waterdhavian cheese (wheel)                - 8 cp',
                            'Elturian Grey cheese (wedge)               - 4 cp',
                            'Turmish cheese (wedge)                     - 3 cp'],
            'Breads':[      'Blackbread and yak butter                  - 6 cp',
                            'Onion loaf                                 - 4 cp',
                            'Buttermilk biscuits (basketfull)           - 6 cp',
                            'Spiced crabapple butter                    - 1 cp',
                            'Dwarven flatbread with fire lichen spread  - 6 cp',
                            'Dark molasses nutbread                     - 5 cp'],
            'Evenfeast':[   'Melted cheeses                             - 3 cp',
                            "Traveler's stew                            - 3 cp",
                            'Soup, onion & cheese                       - 3 cp',
                            'Broth in tankard                           - 1 cp',
                            "Cuttle's hand pies (beef)                  - 2 cp",
                            'Tavern "steak" (pork & beef)               - 5 cp',
                            'Hardbuckler stew                           - 7 cp',
                            'Quipper, pan-fried                         - 6 cp',
                            'Pot roast with drippings                   - 1 sp',
                            'Pheasant, fennel sausage stuffing, gravy   - 9 cp',
                            'Catch of the week, smoked, herb sauce      - Marker',
                            'Prawns and butter sauce                    - 8 cp',
                            'Pan-fried knucklehead trout                - Marker',
                            'Rothe steak                                - 1 sp',
                            'Gurdats                                    - 1 sp',
                            'Verbeeg mutton stew                        - 7 cp',
                            'Harpell Farms mini steaks                  - 2 sp',
                            'Hot river crabs                            - 1 sp'],
            'Afters':[      'Pear & roseapple cobbler crumble           - 4 cp',
                            'Rum pudding                                - 4 cp',
                            'Assorted sweet buns                        - 3 cp',
                            'Pie of the week                            - 5 cp',
                            'Wildnight candied apple                    - 2 cp'],
            'Drinks':[      'Mulled cider           - 2 cp / 6 cp',
                            'Tavern punch           - 1 cp / 4 cp',
                            'Bitter black ale       - 1 cp / 4 cp',
                            'Shadowdark ale         - 2 cp / 6 cp',
                            'Stout                  - 2 cp / 8 cp',
                            'Mead                   - 3 cp / 12 cp',
                            'Evermead               - 12 gp / 50 gp',
                            'Rollrum                - 2 cp / 8 cp',
                            'Clarry                 - 6 cp / 1 sp'
                            'Zzar                   - 6 cp / 1 sp',
                            'Sherry                 - 7 cp / 1 sp',
                            'Moonshae almond brandy - 7 cp / 1 sp',
                            'Mintarn amond brandy   - 6 cp / 1 sp',
                            'Apricot liqueur        - 4 cp / 1 sp',
                            'Cherry liqueur         - 4 cp / 1 sp',
                            'Gooseberry liqueur     - 4 cp / 1 sp',
                            'Peach liqueur          - 4 cp / 1 sp',
                            'Pear liqueur           - 4 cp / 1 sp',
                            'Whiskey                - 1 sp / 1 gp',
                            'Firewine               - 1 gp / 9 gp',
                            'Undermountain Aluryath - 5 gp / 20 gp',
                            'Arabellan Dry Wine     - 2 sp / 8 sp',
                            'Saerloonian Glowfire   - 2 gp / 12 gp',
                            'Winter Wine            - 2 sp / 8 sp',
                            'Elverquist             - 4 gp / 20 gp',
                            'Moonlight Knight       - 5 gp / 20 gp',
                            'Mintwater              - 1 cp',
                            'Sprucebark quaff       - 3 cp',
                            'Pale jade tea          - 2 cp',
                            'Local leaf tea         - 3 cp'],
            'Lodging':['Standard room (includes morningfeast) - 1 gp',
                       'Luxury room (includes morningfeast and evenfeast) - 3 gp'],
            'Portal':['Descend - 1 gp per person',
                      'Return - 1 gp per person (placed in bucket in advance)']},
         'The Inn of the Last Home':{
            'Foods':['Daybreak meat platter                       - 4 stl',
                     'Gully dwarf porridge with fruits and nuts   - 3 stl',
                     'Cornbread and butterwhip                    - 1 stl',
                     'Beer bread (by the loaf)                    - 2 stl',
                     'Flat bread with seasonal toppings           - 1 stl',
                     "Otik's spiced fried potatoes                - 3 stl",
                     'Meat stuffed mushrooms and cheese           - 2 stl',
                     'Daily dumplings (inquire)                   - 3 stl',
                     'Dwarven tide-me-overs                       - 3 stl',
                     'Stuffed shirts (spinach pie)                - 3 stl',
                     'Green onion pancakes fried with fresh cream - 3 stl',
                     "Traveler's stew with beef, carrot & onion   - 3 stl",
                     'Venison & bean stew                         - 4 stl',
                     'Rabbit, mustard-rubbed and long rice        - 5 stl',
                     'Pheasant with breads and wine gravy         - 6 stl',
                     'Shrimp (Tarsis style)                       - 7 stl',
                     'Twice-fried sausages & twice-baked potatoes - 5 stl',
                     "Tika's stewed woodchuck with seasonal roots - 5 stl",
                     'Quince cheese hand pie                      - 5 stl',
                     'Honeyed fig tart                            - 2 stl',
                     'Sour cream walnut cake (by the slice)       - 2 stl',
                     'Dortberry pie (by the slice)                - 2 stl',
                     'Sliced fruits and fresh cream               - 1 stl',
                     'Kender kiffles                              - 2 stl',
                     'Quith-pa table nosh     - On the house (if drinking)'],
            'Drinks':["Irlymeyer's dragonfire punch (pitcher) - 2 stl",
                      'Ginger root tea                        - 1 stl',
                      "Otik's brandy                          - 2 stl",
                      "Otik's cider                           - 2 stl",
                      'House dark ale                         - 3 stl',
                      'House light ale                        - 3 stl',
                      'Dwarven mulled wine                    - 4 stl',
                      "Par Salian's tea                       - 3 stl"]},
         'Celestial Vista Restaurant':{
            'Daybreak':['15  Blood of Vol - Karrnathi sausage omelet with red pepper sauce',
                        '10  Vedbread - crusty cheese bread with onion butter',
                        '12  Elven bread - cinnamon swirled with honey butter',
                        '8   Ashi flatbread - served with honey'],
            'Mains and Sides':['25  Eldeen Banquet - loaded with vegetables',
                               '30  Pan-seared rabbit with Aundairian wood-nut sauce',
                               '35  Gold Pheasant stuffed with sparkle mushrooms and rice',
                               '40  Dragon salmon in butter and dark wine sauce',
                               "25  Farmer's stew",
                               '25  Thrice-poached eggs and sizzling pheasant',
                               '35  Fire-wrapped golden fish',
                               '35  Spiced pork and orange peppers',
                               '30  Hot-spiced chicken in panya leaves',
                               '40  Thrakel-seared beef in red sauce',
                               '30  Three-thrakel fish stew',
                               '15  Silvered vegetable skewers',
                               '45  Thrane prime sirloin',
                               '45  Karrnathi breaded veal'],
            'Desserts':['8   Skyway Special - a light dessert omelet served atop whipped cream',
                        '7   Cremfels - a creme-filled crepe served with berries or syrup',
                        '6   Kettle fried spider and redeye berries',
                        '4   Beesh-berry sorbet',
                        '5   Silverfruit pie'],
            'Beverages':['5   Talenta Tal',
                         '8   Karrnathi Beer',
                         '8   Nightwood Ale',
                         '10  Aundairian Mursi',
                         '12  Kuryeva gin',
                         '12  Sooka',
                         '10  Mror Ale',
                         '12  Lhazaar',
                         '6   Honey-milk',
                         '15  Arcanix Vineyards Fireburst wine',
                         '20  Dark Orla-un wine',
                         '22  Windshire Rainbow Wine',
                         '15  Aundairian Iltrayan Wine',
                         '12  Zil Brandy']},
         'The Green Dragon Inn':{
            'Foods':['Eggs, boiled and spiced                                - 2 sp',
                     'Sausage/humble pie                                     - 2 sp',
                     '"Orc" Bacon, thick cut (three slices)                  - 1 sp',
                     'Muffins with berries                                   - 5 cp',
                     'Honey butter                                           - 1 cp',
                     'Smoked Okerlund cheese wheel                           - 3 sp',
                     'Perrelander cheese                                     - 3 sp',
                     'Nutbread loaf                                          - 7 cp',
                     'Fried bread and spices                                 - 5 cp',
                     'Greens with garlic                                     - 1 sp',
                     'Soup, leek and boar                                    - 1 sp',
                     'Fried mushroom in garlic sauce                         - 1 sp',
                     "Quij's Plate (sausage and potatoes)                    - 2 sp",
                     'Boar ragout (turnips and onions)                       - 5 sp',
                     "Traveler's stew                                        - 5 sp",
                     'Steak and kidney pie                                   - 5 sp',
                     'Veal, breaded with gravy                               - 1 gp',
                     'Trout, stuffed or as you like it                       - 1 gp',
                     'Poached salmon                                         - 1 gp',
                     'Mutton meatloaf                                        - 7 sp',
                     'Wolf steak                                             - 1 gp',
                     'Venison, marinated in red wine and spices              - 1 gp',
                     'Broiled crayfish in butter and scallions               - 1 gp',
                     'Spit-roast stuffed goose                               - 1 gp',
                     'Pleasures of the deep in red broth and sherry          - 1 gp',
                     'Barrier Peaks Surrogate Steaks                         - 10 gp',
                     "D'Amberville onion soup                                - 1 gp",
                     "Heroes' Feast (Fridays when cleric is present)         - 20 gp",
                     'The Endless Platter: all you can eat smoked river eels - 3 gp',
                     'Bread pudding, warm in milk and butter                 - 3 sp',
                     'Berry tart                                             - 3 sp',
                     'Mincemeat stars                                        - 3 sp',
                     'Ice cake                                               - 3 sp',
                     'Gingerbread man, Greyhawk style                        - 2 sp'],
            'Drinks':['Ale                               - 2 sp',
                      'Stout                             - 1 sp',
                      'Milk stout                        - 1 sp',
                      'Honey mead                        - 1 ep',
                      'House wine                        - 1 ep',
                      'Keoish golden wine                - 15 sp',
                      'Sundish lilac wine                - 5 ep',
                      'Urnst white wine                  - 1 gp',
                      'Celene ruby wine                  - 2 gp',
                      'Furyondian emerald pale wine      - 4 gp',
                      'Velunan fireamber wine            - 1 pp',
                      'Mulled wine                       - 1 ep',
                      'Brandy, local                     - 1 ep',
                      'Keoish brandy, imported           - 1 gp',
                      'Urnst brandy, special aged        - 1 gp',
                      'Ulik elixir liquer                - 5 gp',
                      'Hill giant black wine             - 5 gp',
                      'Purple Grapemash No. 3            - 3 gp',
                      'Herbal tea                        - 5 cp',
                      'Owlbear milk, served warm or cold - 5 cp'],
            'Rooms':['Shared  - 1 sp',
                     'Private - 2 gp',
                     'Suite   - 5 gp']},
        'Infernal Rapture':{
            'Appetizers':['Pickled vine blight salad',
                          'Pan-fried myconid cap with garlic butter',
                          'Spicy shredded stirge sliders'],
            'Main Dishes':['Broiled quippers served in a port reduction',
                           'Roasted wereboar seasoned liberally with pepper and paprika',
                           'Twice-battered axe beak strips with a brandied plum sauce',
                           'Deep fried miniature giant space hamster, seasoned to perfection with rosemary, basil, thyme, and tears'],
            'Desserts':['Candied phase spider eyes in a raspberry liquor reduction',
                        'Sweet apple tart with a celestial caramel drizzle',
                        'Rare miniature stench kow cheese selection'],
            'Drinks':['Coffee',
                      'Tea']}
         }

menus['The Yawning Portal']['Foods'] = (menus['The Yawning Portal']['Morningfeast'] +
                                        menus['The Yawning Portal']['Cheeses'] +
                                        menus['The Yawning Portal']['Breads'] +
                                        menus['The Yawning Portal']['Evenfeast'] +
                                        menus['The Yawning Portal']['Afters'])

for inn in ['The Yawning Portal','The Inn of the Last Home', 'The Green Dragon Inn']:
    for kind in ['Food', 'Drink']:
        menus[inn][kind] = menus[inn][kind+'s']
        for i in range(len(menus[inn][kind])):
            menus[inn][kind][i] = menus[inn][kind][i].split(' - ')[0].rstrip()

inn = 'Celestial Vista Restaurant'            
menus[inn]['Foods'] = (menus[inn]['Daybreak'] +
                       menus[inn]['Mains and Sides'] +
                       menus[inn]['Desserts'])
menus[inn]['Drinks'] = menus[inn]['Beverages']

inn = 'Infernal Rapture'
menus[inn]['Foods'] = (menus[inn]['Appetizers'] +
                       menus[inn]['Main Dishes'] +
                       menus[inn]['Desserts'])

for kind in ['Food', 'Drink']:
    menus[inn][kind] = menus[inn][kind+'s']
    for i in range(len(menus[inn][kind])):
        menus[inn][kind][i] = menus[inn][kind][i].lstrip('1234567890 ')
    
# HEROES' FEASTS
feast = {'Human':['Amphail braised beef',
                  'Vedbread',
                  'Castle Amber onion soup',
                  'Gingerbread man'],
         'Elven':['High harvest puree',
                  'Wood elf forest salad',
                  'Dragon salmon',
                  'Meal\'s end'],
         'Dwarven':['Potato leek soup',
                    'Smoked sausages and kraut with dwarven mustard',
                    'Dwarven flatbread',
                    'Black pudding'],
         'Halfling':['Melted cheeses with chunky tomato broth',
                     'Lluirwood salad',
                     'Honeyed ham with pineapple gravy',
                     'Heartlands rose apple and blackberry pie']}

# PATRONS
crowdsize = ['Empty', 'A few people', 'Small crowd', 'Bustling', 'Packed', 'Overcrowded']
crowdsize_w = [2, 7, 10, 15, 19, 20]
numpatrons = {'Empty':       '0d0',
              'A few people':'1d8',
              'Small crowd': '1d6+10',
              'Bustling':    '1d8+5', # x number of inn rooms
              'Packed':      '1d10+10', # x number of inn rooms
              'Overcrowded': '2d10+15'} # x number of inn rooms
xrooms = ['Bustling', 'Packed', 'Overcrowded'] # crowd sizes for which to multiply by number of rooms
patrons = {'Poor':{'NPCs':['Guard', 'Beggar', 'Bard', 'Shady character',
                           'Commoner', 'Adventurer'],
                   'w':[2, 6, 7, 12, 18, 20]},
           'Common':{'NPCs':['Shady character', 'Merchant', 'Bard', 'Commoner',
                             'Adventurer', 'Guard', 'Priest',
                             'Military elite', 'Noble', 'other VIP'],
                     'w':[2, 6, 7, 16, 18, 19, 19.25, 19.5, 19.75, 20]},
           'Fine':{'NPCs':['Shady character', 'Merchant', 'Bard', 'Noble',
                           'Military elite', 'Priest', 'Adventurer', 'Other'],
                   'w':[1, 6, 7, 15, 16, 17, 19, 20]}}

#%% Classes
    
class menu():
    def __init__(self, r='rand', q='rand'):
        # use supplied region or choose randomly
        if r in regions: self.region = r
        else: self.region = rng.choice(regions)
        
        # use supplied quality or choose randomly
        if q in qualities: self.quality = q
        else: self.quality = rng.choice(qualities)
        
        # Poor:     1 special at "Poor" price
        # Common:   1 special at "Common" price
        #           2 alternates at "Poor" price
        # Fine:     1 special at "Luxe" price
        #           4 alternates at "Fine" price
        # Luxe:     3 specials at "Luxe" price
        self.nspec = 1
        self.nalt = 0
        self.foodspecprice = specialprices[self.quality]['Food']
        self.drinkspecprice = specialprices[self.quality]['Drink']
        self.foodaltprice = self.foodspecprice
        self.drinkaltprice = self.drinkspecprice
        if self.quality == 'Common':
            self.nalt = 2
            self.foodaltprice = specialprices['Poor']['Food']
            self.drinkaltprice = specialprices['Poor']['Drink']
        elif self.quality == 'Fine':
            self.nalt = 4
            self.foodspecprice = specialprices['Luxe']['Food']
            self.drinkspecprice = specialprices['Luxe']['Drink']
        elif self.quality == 'Luxe':
            self.nspec = 3
            
        # randomly determine menu items
        self.foods = randspecial('Food', self.region, self.nspec+self.nalt)
        self.drinks = randspecial('Drink', self.region, self.nspec+self.nalt)
        if self.quality == 'Luxe':
            self.foodspecial = self.foods
            self.drinkspecial = self.drinks
        else:
            self.foodspecial = [self.foods[0]]
            self.drinkspecial = [self.drinks[0]]
            
        # menu descriptions
        self.foodmenu = self.descfoodmenu(False)
        self.drinkmenu = self.descdrinkmenu(False)
        self.description = self.describe(False)
            
    def descfoodmenu(self, p=True):
        string = 'Food:\n'
        for i in range(len(self.foodspecial)):
            string += '- Chef\'s special: ' + self.foodspecial[i]
            string += ' - ' + self.foodspecprice + '\n'
        for i in range(len(self.foods)-1):
            string += '- ' + self.foods[i+1] + ' - ' + self.foodaltprice + '\n'
        
        if p: print(string)
        return string
    
    def descdrinkmenu(self, p=True):
        string = 'Drinks:\n'
        for i in range(len(self.drinkspecial)):
            string += '- House specialty: ' + self.drinkspecial[i]
            string += ' - ' + self.drinkspecprice + '\n'
        for i in range(len(self.drinks)-1):
            string += '- ' + self.drinks[i+1] + ' - ' + self.drinkaltprice + '\n'
            
        if p: print(string)
        return string
    
    def describe(self, p=True):
        string = self.foodmenu + self.drinkmenu
        if p: print(string)
        return string
    
class staff():
    def __init__(self, r='rand', g='rand', a='rand'):
        # random race
        if r == 'rand': self.race = rng.choices(races, cum_weights=r_w)[0]
        else: self.race = r
        
        # random gender
        if g == 'rand': self.gender = rng.choice(genders)
        else: self.gender = g
        
        # random age
        if a == 'rand': self.age = roll(ages[self.race])
        else: self.age = a
        
        # if half-elf, randomly pick either elf or human for name
        if self.race == 'Half-elf': _temp_r = rng.choice(['Elf', 'Human'])
        else: _temp_r = self.race # otherwise can just use self race
        
        # random name
        if self.gender == 'nb':
            # choose either a random name or a single name for nonbinary gender
            _temp_g = rng.choice(genders)
            if _temp_g == 'nb':
                # only goes by one name; choose from the last names
                self.firstname = rng.choice(lastnames[_temp_r])
                self.lastname = ''
            else:
                # pick first name from random gender
                self.firstname = rng.choice(firstnames[_temp_r][_temp_g])
                self.lastname = rng.choice(lastnames[_temp_r])
        else:
            # choose name according to gender
            self.firstname = rng.choice(firstnames[_temp_r][self.gender])
            self.lastname = rng.choice(lastnames[_temp_r])
        
        self.description = self.describe(False)
        
    def describe(self, p=True):
        if self.lastname == '': _s = ''
        else: _s = ' '
        string = self.firstname + _s + self.lastname + ', '
        string += str(self.age) + ' year old ' + self.race
        if self.gender == 'm': string += ' (he/him)'
        elif self.gender == 'f': string += ' (she/her)'
        elif self.gender == 'nb': string += ' (they/them)'
        
        if p: print(string)
        return string

class inn():
    def __init__(self, c='rand'):
        # random barkeep
        self.barkeep = staff()
        
        # random name
        self.name = choose_name(self.barkeep)
        
        # random atmosphere
        self.atm = rng.choice(atmosphere)
        
        # random quality
        self.quality = rng.choice(qualities)
        
        # room pricing
        self.standardroomprice = roomprices[self.quality]['standard']
        self.bestroomprice = roomprices[self.quality]['best']
        
        # random inn size
        size = roll('1d12')
        self.availablerooms = numrooms[size]
        
        # random chef
        self.chef = staff()
        
        # staff members (servers, bouncers, assistant cooks)
        self.numberofservers = staffsizes[size]['servers']
        self.servers = []
        for i in range(self.numberofservers):
            self.servers.append(staff().description) # random servers
        self.numberofbouncers = staffsizes[size]['bouncers']
        self.bouncers = []
        for i in range(self.numberofbouncers):
            self.bouncers.append(staff().description) # random bouncers
        self.numberofcooks = staffsizes[size]['bouncers'] # use bouncer numbers for cooks
        self.cooks = []
        for i in range(self.numberofcooks):
            self.cooks.append(staff().description) # random assistant cooks
        
        # use supplied cuisine type or pick randomly
        if c not in cuisines: self.cuisine = rng.choice(list(cuisines.keys()))
        else: self.cuisine = c
        
        # random menu based on cuisine
        self.menu = menu(rng.choice(cuisines[self.cuisine]), self.quality)
        
        # random crowd
        self.randcrowd()
        
        # description
        self.description = self.describe(False)
        
    def describe(self, p=True):
        string = self.name + '\n'
        string += self.cuisine + ' cuisine\n'
        string += self.atm + ' atmosphere\n'
        string += self.quality + ' quality\n'
        string += str(self.availablerooms) + ' rooms available\n'
        string += '- Standard room ' + self.standardroomprice + '\n'
        string += '- Best room ' + self.bestroomprice + '\n'
        string += self.menu.description
        string += 'Barkeep: ' + self.barkeep.description + '\n'
        string += 'Chef: ' + self.chef.description + '\n'
        string += 'Staff:\n'
        for i in range(self.numberofservers):
            string += '- ' + self.servers[i] + '(server)\n'
        for i in range(self.numberofbouncers):
            string += '- ' + self.bouncers[i] + '(bouncer)\n'
        for i in range(self.numberofcooks):
            string += '- ' + self.cooks[i] + '(cook)\n'
        string += 'Crowd: ' + self.crowd
        string += ' (' + str(self.npatrons) + ' patrons)\n' + self.patrons
        if p: print(string)
        return string
    
    def quickpitch(self, p=True):
        string = self.name + ': '
        string += self.quality + ' quality '
        string += self.cuisine + ' cuisine'
        if p: print(string)
        return string
    
    def randcrowd(self, c='rand'):
        # random crowd size
        if c not in crowdsize:
            c = rng.choices(crowdsize, cum_weights = crowdsize_w)[0]
        self.crowd = c
        
        # random number of patrons
        string = ''
        if c in xrooms: string = 'x' + str(self.availablerooms)
        self.npatrons = roll(numpatrons[c]+string)
        
        # random crowd members
        patronlist = list('' for x in range(self.npatrons))
        for i in range(self.npatrons):
            _p = patrons[self.quality]['NPCs']
            _w = patrons[self.quality]['w']
            patronlist[i] = rng.choices(_p, cum_weights=_w)[0]
        
        # collect crowd into list without duplicates
        patrontypes = set(patronlist)
        string = ''
        for i in patrontypes:
            n = patronlist.count(i)
            string += '- ' + str(n) + ' ' + i
            if n>1: string += 's'
            string += '\n'
        self.patrons = string
        
    def quickcrowd(self, new=False):
        if new: self.randcrowd()
        string = 'Crowd: ' + self.crowd
        string += ' (' + str(self.npatrons) + ' Patrons)\n' + self.patrons
        print(string)

#%% Functions

def choose_name(b = staff()):
    # choose base words
    A = rng.choice(adj) # adjective
    B = rng.choice(noun) # noun
    if (A in number) and not(B in plural):
        # pluralize if adjective is a number
        if B == 'Ploughman': B = 'Ploughmen'
        elif B in es: B += 'es'
        elif B == 'Wolf': B = 'Wolves'
        elif B in ies: B = B[0:len(B)-1] + 'ies'
        else: B += 's'
    
    # choose naming variation
    var = roll('1d8')
    if var == 1:
        name = 'The ' + A + ' ' + B + ' Tavern'
    elif var == 2:
        name = 'The Inn of the ' + A + ' ' + B
    elif var == 3:
        name = 'The ' + A + ' ' + B + ' Inn'
    elif var == 4:
        name = 'The ' + A + ' ' + B
    elif var == 5:
        name = 'The ' + A + ' ' + B + ' and ' + rng.choice(noun)
    elif var == 6:
        name = A + ' ' + B + ' Tap House'
    elif var == 7:
        name = A + ' ' + B + ' Arms'
    elif var == 8:
        end = rng.choice([' Tavern', ' Inn', ' Tap House', ' Arms', ''])
        name = b.firstname + '\'s' + end
    
    return name

def randspecial(spectype='Food', r='rand', n=1):
    # random food & drink generator
    
    # choose cuisine type and either food or drink
    types = ['Food', 'Drink']
    if spectype not in types: spectype = rng.choice(spectype)
    if r not in regions: r = rng.choice(regions)
    
    # randomly determine specials
    special = rng.sample(specials[r][spectype], n)
    
    # roll a second time when required
    while any(x in regions for x in special) or any(x == 'rand' for x in special):
        for i in range(len(special)):
            if special[i] in regions:
                # roll on specified cuisine table
                special[i] = rng.choice(specials[special[i]][spectype])
            elif special[i] == 'rand':
                # roll on random cuisine table
                r = rng.choice(regions)
                special[i] = rng.choice(specials[r][spectype])
    
    return special # always a list, even if only 1 element

#%% Test

print(' ')
staff1 = staff()
staff1.describe()
print(' ')

staff2 = staff()
print(staff2.describe(False))
print(' ')

staff3 = staff()
print(staff3.description)
print(' ')

inn1 = inn()
inn1.describe()
print(' ')

inn2 = inn()
print(inn2.describe(False))
print(' ')

inn3 = inn()
print(inn3.description)
print(' ')

print(randspecial(r='Urban', n=10))
print(' ')

print(randspecial('Drink','Cave',1))
print(' ')

menu1 = menu()
menu1.describe()

stats = {'Urban':0,'Desert':0,'Tundra':0,'Roadside':0,'Mountain':0,
         'Plains':0,'Coastal':0,'Swamp':0,'Tropical':0,'Cave':0,
         'Country':0,'Woodland':0,'Unsavory':0}
for _, x in enumerate(cuisines):
    for y in cuisines[x]:
        stats[y] += 1
print(stats)
print(' ')

options = []
for i in range(10):
    options.append(inn())
    options[i].quickpitch()
    options[i].quickcrowd()
