# -*- coding: utf-8 -*-
"""
Created on Fri Aug 13 13:14:41 2021

@author: Matthew
"""

import math

import treasuretools as tt
roll = tt.roll
qualities = tt.lifestyles

#%% FALLING

# [fall distance, landing location]
falldist = {1:['0d0+200', 'the ground at the base of the towers'],
           2:['3d6x10',  'a bridge'],
           3:['2d4x10',  'a skycoach'],
           4:['4d4x5',   'an outcropping, flagpole, or statue'],
           5:['0d0',     'you land on a hippogriff'],
           6:['0d0',     'a gargoyle or giant owl catches you'],
           7:['0d0',     'a nearby spellcaster casts feather fall on you'],
           8:['0d0',     'you land on an air elemental']}
def fallSharn():
    f = falldist[roll('1d8')]
    dist = roll(f[0])
    land = f[1]
    div10 = math.floor(dist/10)
    if div10 > 20: div10 = 20
    dmgdice = str(div10) + 'd6'
    dmg = roll(dmgdice)
    if dmg==0:
        string = 'You take no damage, as '
        string += land
        string += ', arresting your fall.'
    else:
        string = 'You fall ' + str(dist) + ' feet, '
        string += 'taking ' + str(dmg) + ' damage '
        string += 'as you land on ' + land + '.'
        
    return string

#%% DISTRICTS

# quarters, levels, and wards
quarters = ['Central Plateau', 'Dura Quarter', 'Menthis Plateau',
            'Northedge Quarter', 'Tavick\'s Landing']
levels = ['Upper', 'Middle', 'Lower']
wards = []
for q in quarters:
    for l in levels:
        wards.append(l + ' ' + q.rpartition(' ')[0])
for i in ['Skyway', 'The City of the Dead', 'Cliffside', 'The Cogs', 'The Lava Pools']:
    wards.append(i)

# inter-quarter connections
bridges = {'Central Plateau':['Northedge Quarter', 'Menthis Plateau'],
           'Dura Quarter':['Tavick\'s Landing', 'Menthis Plateau'],
           'Menthis Plateau':['Tavick\'s Landing', 'Dura Quarter', 'Central Plateau'],
           'Northedge Quarter':['Central Plateau', 'Tavick\'s Landing'],
           'Tavick\'s Landing':['Dura Quarter', 'Menthis Plateau', 'Northedge Quarter']}

# DISTRICTS
# district names
districts = ['Highest Towers',
             'Korranath',
             'Platinum Heights',
             'Skysedge Park',
             'Ambassador Towers',
             'Dragon Towers',
             'Sovereign Towers',
             'Sword Point',
             'Tradefair',
             'Boldrei\'s Hearth',
             'Olladra\'s Kitchen',
             'Myshan Gardens',
             'Vallia Towers',
             'Clifftop',
             'Daggerwatch',
             'Highhold',
             'Highwater',
             'Hope\'s Peak',
             'Overlook',
             'The Bazaar',
             'Broken Arch',
             'Hareth\'s Folly',
             'Rattlestone',
             'Stormhold',
             'Tumbledown',
             'Underlook',
             'Callestan',
             'Fallen',
             'Gate of Gold',
             'Malleon\'s Gate',
             'Oldkeep',
             'Precarious',
             'The Stones',
             'Den\'iyas',
             'Ivy Towers',
             'Seventh Tower',
             'University',
             'Cassan Bridge',
             'Everbright',
             'Little Plains',
             'Smoky Towers',
             'Warden Towers',
             'Downstairs',
             'Firelight',
             'Torchfire',
             'Crystal Bridge',
             'Oak Towers',
             'Shae Lias',
             'High Hope',
             'Holdfast',
             'Longstairs',
             'North Market',
             'Stoneyard',
             'Copper Arch',
             'Ocean View',
             'Silvergate',
             'Sunrise',
             'Twelve Pillars',
             'Cornerstone',
             'Deathsgate',
             'Graywall',
             'Tavick\'s Market',
             'Black Arch',
             'Cogsgate',
             'Dragoneyes',
             'High Walls',
             'Terminus',
             'Wroann\'s Gate',
             'Skyway',
             'Cliffside',
             'Ashblack',
             'Blackbones']
# district descriptions
distdesc = {'Highest Towers':       'The seat of city government, this district is also where airships arrive and depart.',
            'Korranath':            'Named for the great temple of Kol Korran that lies at its center, this district is dedicated to wealth and finance. Moneychangers, banks, and grand vaults are found here, in addition to the estates of powerful merchants',
            'Platinum Heights':     'Catering to Sharn\'s elite, this district provides a wide range of shops and services of wealthy to aristocratic quality',
            'Skysedge Park':        'Home to three sprawling rooftop parks, this district provides a touch of wilderness in the heart of the city. A small community of immigrants from the Eldeen Reaches maintains these groves and gardens.',
            'Ambassador Towers':    'This district contains the embassies to the Thronehold nations, along with Aerenal and Riedra. It\'s also the seat of the Citadel and home to the Brelish Museum of Fine Art',
            'Dragon Towers':        'This is the primary place to do business with representatives of the dragonmarked houses. All the houses have outposts here, and Sivis, Tharashk, Jorasco, and Cannith have their primary enclaves in Dragon Towers.',
            'Sovereign Towers':     'A district filled with a vast assortment of temples and shrines. It is home to the two most important temples in Sharn: the Pavilion of the Host and the Cathedral of the Cleansing Flame.',
            'Sword Point':          'This garrison district houses the forces that police and defend Central Plateau, including the Sharn Watch and a detachment of the royal army.',
            'Tradefair':            'A merchant district offering legal goods and services of modest to comfortable quality',
            'Boldrei\'s Hearth':    'A haven for travelers, this district contains reliable inns ranging from modest to comfortable quality.',
            'Olladra\'s Kitchen':   'Neither the best nor the worst Sharn has to offer, Olladra\'s Kitchen is home to a wide number of taverns and restaurants of modest to comfortable quality.',
            'Myshan Gardens':       'Mysan Gardens is a residential district that caters to affluent artists.',
            'Vallia Towers':        'Vallia Towers has a large community of half-elves',
            'Clifftop':             'This district caters to adventurers, with a wide array of businesses aimed at explorers and fortune hunters. It is the home base of the Clifftop Adventurer\'s Guild.',
            'Daggerwatch':          'Daggerwatch holds garrisons for both the Shard Watch and the Brelish army, along with businesses and residences for those who support the garrisons.',
            'Highhold':             'A district built by dwarves for dwarves, Highhold has strong Mror influences in its architecture. It\'s a good place to find Mror goods and is home to talented smiths and brewers.',
            'Highwater':            'The finest residential district in Dura and the seat of House Vadalis, Highwater is largely comfortable in quality with a few wealthy estates.',
            'Hope\'s Peak':         'A relatively new temple district, with shrines and churches that have relocated from Fallen in Lower Dura. Hope\'s Peak includes several monasteries and a sacred grove.',
            'Overlook':             'Overlook is noteworthy for its kalashtar community, which maintains a community center, a shrine devoted to the Path of Light, and a few restaurants serving Sarlonann cuisine.',
            'The Bazaar':           'The largest commercial district in Sharn, an excellent place to buy or sell used - and possibly stolen - goods.',
            'Broken Arch':          'Once a proud residential district, Broken Arch has fallen into disrepair. Its housing is poor to modest in quality, though the shells of wealthy manors can still be seen.',
            'Hareth\'s Folly':      'A jumble of architectural styles, Hareth\'s Folly is a place to gamble and enjoy modest food and drink. The Hollow Tower is a center for aerial sports, and Hareth\'s Folly is where the Race of Eight Winds begins and ends.',
            'Rattlestone':          'Rattlestone is a tenement district. Its people have little but their pride, but there\'s a strong camaraderie between them.',
            'Stormhold':            'A comfortable residential district, Stormhold is home to the few powerful families that have remained in Dura. It\'s in better condition than most of Middle Dura, and Deneith mercenaries protect the streets.',
            'Tumbledown':           'A poor residential district, Tumbledown has experienced recent incursions from Daask.',
            'Underlook':            'The center of Sharn\'s nightlife before Menthis Plateau was built, Underlook is a collection of poor taverns and inns',
            'Callestan':            'Home to an assortment of squalid and poor businesses, Callestan is a nexus for criminal activity and known as a stronghold of the Boromar Clan',
            'Fallen':               'Sharn\'s oldest temple district, Fallen was abandoned after the floating Glass Tower crashed into the district during the Last War. Now it\'s a collection of wretched ruins.',
            'Gate of Gold':         'A squalid slum, providing miserable housing for desperate people.',
            'Malleon\'s Gate':      'A poor district originally inhabited by goblins, Malleon\'s Gate has become a haven for monstrous immigrants from Droaam and Darguun, along with members of Daask.',
            'Oldkeep':              'Another poor slum, largely home to dockworkers from Precarious.',
            'Precarious':           'The skydocks of Precarious pass goods between the towers and the port on the Dagger River below. The district is filled with warehouses, along with a handful of poor taverns. A small community of Sarlonans lives here.',
            'The Stores':           'A warehouse district with a large halfling population, with ties to the Boromar Clan.',
            'Den\'iyas':            'Founded by gnome immigrants from Zilargo, Den\'iyas is a haven for those interested in Zil culture. It\'s home to many sages and artisans, and a hotbed of schemes and intrigue.',
            'Ivy Towers':           'This residential district includes comfortable homes and modest apartments. Many of the students and faculty of Morgrave University live in Ivy Towers.',
            'Seventh Tower':        'A shopping district, with restaurants and goods of comfortable to wealthy quality. Seventh Tower is especially noteworth for Little Xen\'drik, a collection of galleries whose ownerss buy and sell goods from Xen\'drik.',
            'University':           'This district is dominated by Morgrave University. It\'s also a nexus for sophisticated entertainment, including the Art Temple, the Grand Stage, and the Great Hall of Aureon.',
            'Cassan Bridge':        'A mercantile district with goods of modest to comfortable quality. Home to a significant number of immigrants from the Shadow Marches, Cassan Bridge is the place to visit for exotic Marcher herbs and cuisine.',
            'Everbright':           'This district is a source of magical goods and services. Exotic components, magewrights for hire, common or uncommon magic items - all of these and more can be found here.',
            'Little Plains':        'Founded by Talenta halflings, this district includes a central campground for visiting halfling nomads. The permanent residents are mostly halflings as well. Talentan foods and crafts can be found here, along with displays of traditional skills and pastimes.',
            'Smoky Towers':         'Safer than the lower wards and less expensive than Upper Menthis, Smoky Towers has plenty of entertainment options. The Classic Theater is its most popular venue, but Smoky Towers offers a wide variety of more exotic fare. Dinner theater, changeling burlesque, and other diversions can be found in Smoky Towers. Thovanic Hall has begun performing works from Darguun and Droaam featuring monstrous performers. Smoky Towers has also become a haven for Cyran refugees wealthy enough to avoid High Walls.',
            'Warden Towers':        'This district is the primary garrison of the Sharn Watch in Menthis. It\'s home to a community of Lhazaar immigrants, and the Broken Anchor is a tavern catering to Lhazaar travelers.',
            'Downstairs':           'The Downstairs district is primarily known for food and drink. Though most of its taverns and inns are only modest in quality, the Four Sails serves some of the finest seafood in Sharn. The recent success of the Diamond Theater has also drawn travelers to the district.',
            'Firelight':            'This district is a destination for those who seek illicit forms of entertainment. Many forms of illegal gambling and paid companionship can be found in Firelight. It\'s also the most common location of the Burning Ring.',
            'Torchfire':            'A district with a notorious reputation, celebrated for cheap entertainment and infamous for its dangerous alleys. Its theaters specialize in musical comedy and lowbrow entertainment, and there are lots of opportunities for hopeful amateurs to get on a stage in Torchfire.',
            'Crystal Bridge':       'A peaceful residential district with many wealthy and aristocratic estates.',
            'Oak Towers':           'A residential district where housing ranges from comfortable to aristocratic. Construction in Oak Towers uses materials and styles drawn from Aerenal, and the district is home to many of Sharn\'s established elf and half-elf families.',
            'Shae Lias':            'This district is a bastion for the culture and traditions of the elves of Aerenal. It includes a variety of businesses specializing in Aereni goods, as well as a temple of the Undying Court.',
            'High Hope':            'A center for worship for the people of Northedge, High Hope includes temples of the Silver Flame and the Sovereign Host, along with many smaller shrines. It lacks the grandeur of Sovereign Towers in Central Plateau, but has an atmosphere of solemn devotion.',
            'Holdfast':             'Holdfast is the heart of Sharn\'s native dwarf population. The ancestors of the Holdfast dwarves helped build Sharn, and many of its people are stonemasons, architects, and smiths. Holdfast dwarves are proud of their Sharn roots and have little interest in Mror customs or traditions.',
            'Longstairs':           'The population of this peaceful residential district is mostly made up of dwarves, humans, and half-elves. Neighbors here generally stand together to deal with any trouble.',
            'North Market':         'The open marken in this region largely deals in simple, locally produced goods. Due to the significant shifter population in Lower Northedge, North Market offers goods and services aimed at shifters (grooming services, claw care, and so forth) as well as those reflecting an Eldeen influence.',
            'Stoneyard':            'This residential district is home to the majority of Sharn\'s shifters, including both recent immigrants from the Eldeen Reaches and long-established local families. The district includes a makeshift hrazhak court and a shrine devoted to the Wardens of the Wood. Conditions are poor to modest.',
            'Copper Arch':          'This district is built around the Deneith garrison that polices the upper ward. It contains shops and services catering to the wealthy elite.',
            'Ocean View':           'This residential district is home to some of the most influential citizens of Sharn. It has a mix of wealthy mansions and aristocratic estates.',
            'Silvergate':           'This shopping district is patronized by those with gold to spare. All manner of fine jewelry and expensive clothing can be found here, along with aristocratic food and lodging.',
            'Sunrise':              'This district provides housing for the shopkeepers and servants who keep Upper Tavick\'s Landing running. Housing is largely modest in quality, with a few comfortable towers.',
            'Twelve Pillars':       'This is the civic heart of Upper Tavick\'s Landing. The twelve pillars it\'s named for surround a courthouse, the Tower of Law, where visitors can get licenses to carry weapons in the ward.',
            'Cornerstone':          'A haven for travelers, Cornerstone has a range of comfortable inns and taverns. It\'s built around the vast Cornerstone Arena and is a center of activity for many major sporting events.',
            'Deathsgate':           'Named for the nearby City of the Dead, this district houses the Deathsgate Guild and businesses that cater to adventurers. House Deneith recruits mercenaries at its outpost here.',
            'Graywall':             'This district was founded long ago by Karrnathi immigrants, and its people are proud of their heritage. It is a haven for any Karrnathi travelers passing through Sharn. Rumors say there\'s a temple devoted to the Blood of Vol in Graywall, but if that\'s the case, it\'s kept hidden.',
            'Tavick\'s Market':     'This district specializes in produce and other goods brought in by the farmers from the surrounding countryside.',
            'Black Arch':           'This district is filled with checkpoints and enchanted gates. These portals are generally open, but in times of trouble, Black Arch can become an impassable fortress. The Sharn Watch maintains the local garrison. House Orien and House Sivis both maintain outposts here, ensuring that messages can be swiftly delivered through the city and beyond.',
            'Cogsgate':             'This warehouse district is the gateway to the Cogs, and shipments of ore and other goods regularly pass through here. House Kundarak has high-security storage facilities for rent, and a House Deneith outpost hires out Blademark mercenaries for venturing below.',
            'Dragoneyes':           'Dragoneyes tends to the needs of weary travelers, providing a wide range of lodging, food, and entertainment for tourists. It\'s also the home of most of Sharn\'s changeling population, and many changelings use their gifts to entertain and amuse travelers. Some say that it\'s the home of the Tyrants criminal guild, but if so, that place is well hidden.',
            'High Walls':           'This district was converted into an internment center during the Last War. Since the end of the war, it has been transformed into a refugee camp. Most of the residents are Cyrans who fled the Mourning, but High Walls also includes Brelish citizens who lost their homes in the war. It\'s a crowded and dangerous place, but it allows residents to maintain a squalid lifestyle at no cost. Currently the gates are open, but the Sharn Watch could seal them at any time.',
            'Terminus':             'This district is based around Terminus Station, where the lightning rail enters and leaves Sharn. Most local businesses serve the station or travelers.',
            'Wroann\'s Gate':       'Travelers who arrive on the main road enter Sharn through Wroann\'s Gate, passing below a huge statue of the legendary Queen Wroann. Many of the dragonmarked houses maintain shops here so travelers can send messages, hire bodyguards, or make use of other services.',
            'Skyway':               'Skyway is a district that floats above Central Plateau and Menthis, build atop an island of solidified clouds. The richest people in Sharn live here.',
            'Cliffside':            'Boats bring cargo and passengers to the dock at Cliffside, on the edge of the Dagger River. From there, enormous lifts carry people up to Precarious. This dangerous district contains an assortment of taverns, shabby inns, and warehouses.',
            'Ashblack':             'The first foundries in Sharn were built here. The district is devoted to industry, and the environment here is sweltering and claustrophobic.',
            'Blackbones':           'Blackbones is newer than Ashblack, and it shows. The district\'s corridors are wider and better lit. The foundries are well maintained, and the district has a few thriving businesses. Most of the warforged that reside in Sharn work in Blackbones.'
           }
# district wards
distward = {'Highest Towers':   'Upper Central',
            'Korranath':        'Upper Central',
            'Platinum Heights': 'Upper Central',
            'Skysedge Park':    'Upper Central',
            'Ambassador Towers': 'Middle Central',
            'Dragon Towers':    'Middle Central',
            'Sovereign Towers': 'Middle Central',
            'Sword Point':      'Middle Central',
            'Tradefair':        'Middle Central',
            'Boldrei\'s Hearth': 'Lower Central',
            'Olladra\'s Kitchen': 'Lower Central',
            'Myshan Gardens':   'Lower Central',
            'Vallia Towers':    'Lower Central',
            'Clifftop':         'Upper Dura',
            'Daggerwatch':      'Upper Dura',
            'Highhold':         'Upper Dura',
            'Highwater':        'Upper Dura',
            'Hope\'s Peak':     'Upper Dura',
            'Overlook':         'Upper Dura',
            'The Bazaar':       'Middle Dura',
            'Broken Arch':      'Middle Dura',
            'Hareth\'s Folly':  'Middle Dura',
            'Rattlestone':      'Middle Dura',
            'Stormhold':        'Middle Dura',
            'Tumbledown':       'Middle Dura',
            'Underlook':        'Middle Dura',
            'Callestan':        'Lower Dura',
            'Fallen':           'Lower Dura',
            'Gate of Gold':     'Lower Dura',
            'Malleon\'s Gate':  'Lower Dura',
            'Oldkeep':          'Lower Dura',
            'Precarious':       'Lower Dura',
            'The Stones':       'Lower Dura',
            'Den\'iyas':        'Upper Menthis',
            'Ivy Towers':       'Upper Menthis',
            'Seventh Tower':    'Upper Menthis',
            'University':       'Upper Menthis',
            'Cassan Bridge':    'Middle Menthis',
            'Everbright':       'Middle Menthis',
            'Little Plains':    'Middle Menthis',
            'Smoky Towers':     'Middle Menthis',
            'Warden Towers':    'Middle Menthis',
            'Downstairs':       'Lower Menthis',
            'Firelight':        'Lower Menthis',
            'Torchfire':        'Lower Menthis',
            'Crystal Bridge':   'Upper Northedge',
            'Oak Towers':       'Upper Northedge',
            'Shae Lias':        'Upper Northedge',
            'High Hope':        'Middle Northedge',
            'Holdfast':         'Middle Northedge',
            'Longstairs':       'Lower Northedge',
            'North Market':     'Lower Northedge',
            'Stoneyard':        'Lower Northedge',
            'Copper Arch':      'Upper Tavick\'s',
            'Ocean View':       'Upper Tavick\'s',
            'Silvergate':       'Upper Tavick\'s',
            'Sunrise':          'Upper Tavick\'s',
            'Twelve Pillars':   'Upper Tavick\'s',
            'Cornerstone':      'Middle Tavick\'s',
            'Deathsgate':       'Middle Tavick\'s',
            'Graywall':         'Middle Tavick\'s',
            'Tavick\'s Market': 'Middle Tavick\'s',
            'Black Arch':       'Lower Tavick\'s',
            'Cogsgate':         'Lower Tavick\'s',
            'Dragoneyes':       'Lower Tavick\'s',
            'High Walls':       'Lower Tavick\'s',
            'Terminus':         'Lower Tavick\'s',
            'Wroann\'s Gate':   'Lower Tavick\'s',
            'Skyway':           'Skyway',
            'Cliffside':        'Cliffside',
            'Ashblack':         'The Cogs',
            'Blackbones':       'The Cogs'}



#%% SHARN COUNCILORS

# there are 17 members of the City Council
# - one for each ward (the 3 levels of the 5 quarters)
# - plus one each from Skyway and the Cogs
# below table is just 12 members, not the full Council
councilors = {}
councilors['names'] = ['Sorik Sensos',
                       'Sava Kharisa',
                       'Thurik Davandi',
                       'Savia Potellas',
                       'Maza Thadian',
                       'Shassa Tarr',
                       'Bestan ir\'Tonn',
                       'Kilk',
                       'Hruitt',
                       'Ilyra Boromar',
                       'Evix ir\'Marasha',
                       'Nolan Toranak']
councilors['races'] = {'Sorik Sensos':    'human',
                       'Sava Kharisa':    'human',
                       'Thurik Davandi':  'gnome',
                       'Savia Potellas':  'human',
                       'Maza Thadian':    'elf',
                       'Shassa Tarr':     'shifter',
                       'Bestan ir\'Tonn': 'halfling',
                       'Kilk':            'changeling',
                       'Hruitt':          'giant owl',
                       'Ilyra Boromar':   'halfling',
                       'Evix ir\'Marasha':'human',
                       'Nolan Toranak':   'dwarf'}
councilors['wards'] = {'Sorik Sensos':    'Middle Central',
                       'Sava Kharisa':    'Lower Central',
                       'Thurik Davandi':  'Upper Menthis',
                       'Savia Potellas':  'Lower Menthis',
                       'Maza Thadian':    'Upper Northedge',
                       'Shassa Tarr':     'Lower Northedge',
                       'Bestan ir\'Tonn': 'Upper Tavick\'s',
                       'Kilk':            'Lower Tavick\'s',
                       'Hruitt':          'Middle Dura',
                       'Ilyra Boromar':   'Lower Dura',
                       'Evix ir\'Marasha':'Skyway',
                       'Nolan Toranak':   'The Cogs'}
councilors['desc'] = {'Sorik Sensos':'Sorik Sensos (human) represents Middle Central. An elder statesman and a brilliant orator, he is rumored to be involved in a web of bribery and graft.',
                      'Sava Kharisa':'Sava Kharisa (human) is the outspoken councilor from Lower Central. Since taking her seat, she has fought to improve conditions for the lower classes of Sharn, and she has made many enemies on the council and beyond.',
                      'Thurik Davandi':'Thurik Davandi (gnome) represents Upper Menthis. He is known to have ties to Zilargo and the Boromar Clan, and reportedly loves intrigues and blackmail.',
                      'Savia Potellas':'Savia Potellas (human) has her hand in the entertainment industry of Lower Menthis. She hopes to reduce the influence of organized crime in her district, but it\'s a dangerous game.',
                      'Maza Thadian':'Maza Thadian (elf) represents Upper Northedge. A venerable elf and owner of one of the finest restaurants in Sharn, she fights to maintain tradition but definitely puts the needs of the wealthy ahead of the poor',
                      'Shassa Tarr':'Shassa Tarr (shifter), from Lower Northedge, represents the interests of the merchants and shifters of her ward. She is a cunning diplomat and devoted to her constituents.',
                      'Bestan ir\'Tonn':'Bestan ir\'Tonn (halfling) has represented Upper Tavick\'s Landing for thirty years, and largely views his ward as a separate city within the city. He has a reputation for stirring up conflict and setting the other councilors against one another.',
                      'Kilk':'Kilk (changeling) represents the merchants of Lower Tavick\'s Landing. Whispered rumors suggest that the changeling has ties to the mysterious Tyrants. Some insist that Kilk is actually an identity shared by a group of changelings.',
                      'Hruitt':'Hruitt is a giant owl who can assume human form. A former aerial racer, he\'s a clever negotiator who wins fights for the good of the Bazaar and Middle Dura, often opposing the Boromar Clan and its allies.',
                      'Ilyra Boromar':'Ilyra Boromar (halfling) is the councilor for Lower Dura, but it\'s common knowledge that her true allegiance is to her family and its criminal empire. The current ongoing conflict with Daask has weakened her family and her position.',
                      'Evix ir\'Marasha':'Evix ir\'Marasha (human) represents Skyway. Lady Marasha owns the Celestial Vista restaurant, along with several other valuable businesses. She\'s an eloquent speaker who supports many radical positions, including abolishing the monarchy after the death of King Boranel and recognizing Sharn as an independent province.',
                      'Nolan Toranak':'Nolan Toranak (dwarf), the councilor for the Cogs, is largely seen as a tool of the industrialists who own the foundries there. Members of his family were killed by warforged during the Last War, and Toranak harbors a bitter grudge against House Cannith and the warforged. He has tried to have warforged reclassified as property, and seeks to suppress warforged activists in the Cogs.'}

#%% Testing
    
for i in range(10): print(fallSharn()+'\n')





