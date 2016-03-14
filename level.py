""" "Legend of ponomar" - a rpg
Copyright (C) 2015 Alex Ponomarev

Это свободная программа; вы можете повторно распространять ее и/или
модифицировать ее в соответствии с Универсальной Общественной Лицензией
GNU, опубликованной Фондом Свободного ПО; либо версии 2, либо (по вашему
выбору) любой более поздней версии.

Эта программа распространяется в надежде, что она будет полезной, но БЕЗ
КАКИХ-ЛИБО ГАРАНТИЙ; даже без подразумеваемых гарантий КОММЕРЧЕСКОЙ
ЦЕННОСТИ или ПРИГОДНОСТИ ДЛЯ КОНКРЕТНОЙ ЦЕЛИ.  Для получения подробных
сведений смотрите Универсальную Общественную Лицензию GNU.

Вы должны были получить копию Универсальной Общественной Лицензии GNU
вместе с этой программой; если нет, напишите в Free Software Foundation,
Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA"""

import os
from item import item
from block import block, parser

def lvl(const):
    if const == 1:
        floar_id = 2
        wall_id = 0
        
        f_r = open('./levels/level_1.txt', 'r')
        
        lvl1 = [list(line) for line in f_r]
        for i in range(len(lvl1)):
            for j in range(len(lvl1[i])):
                lvl1[i][j] = parser(lvl1[i][j], floar_id, wall_id)
        
        f_r.close()
        
        lvl1[5][17].add_loot(items["potion_1"])
        lvl1[19][17].add_loot(items["sword_1"])
        
        lvl1[12][18].next_lvl = 2
        
        return lvl1, 5, 12
    elif const == 2:
        floar_id = 6
        wall_id = 7
        
        f_r = open('./levels/level_2.txt', 'r')
        
        lvl2 = [list(line) for line in f_r]
        for i in range(len(lvl2)):
            for j in range(len(lvl2[i])):
                lvl2[i][j] = parser(lvl2[i][j], floar_id, wall_id)
        
        f_r.close()
        
        return lvl2, 5, 12 # [], [[4, 12, 1], [11, 20, 3]], 6, 7, [[10, 4, True, 11, 4, '>']]
    elif const == 3:
        
        f_r = open('./levels/level_3.txt', 'r')
        lvl3 =  [list(line) for line in f_r]
                                                
        f_r.close() 
        
        about_helmet = "Мда... Ведро - оно и есть ведро"
        about_shield = "Достаточно прочный старый стальной щит, тяжелый правда, но скорость не снизит, а вот уставать сильнее буду"
        loot = [[5, 19, helmet(10, 100, 2, "usual helmet", about_helmet)],
                [7, 19, shield(10, 100, 3, "usual shield", about_shield)]]
        
        return lvl3, 6, 5, loot, [[6, 4, 2], [6, 20, 4]], 9, 10, []
    elif const == 4:
        
        f_r = open('./levels/level_4.txt', 'r')
        lvl4 =  [list(line) for line in f_r]
                                                
        f_r.close()        
        
        loot = []
        
        return lvl4, 10, 23, loot, [[10, 22, 2], [6, 20, 4]], 9, 10, []        


items = dict([])
for file in os.listdir(path="./items"):
    f_r = open("./items/" + file, 'r')
    
    itype = f_r.readline().split(':')[1].strip()
    name = f_r.readline().split(':')[1].strip()
    about = f_r.readline().split(':')[1].strip()
    strength = f_r.readline().split(':')[1].strip()
    image_id = f_r.readline().split(':')[1].strip()
    
    its = item(itype, name, about, strength, int(image_id))
    
    effects = f_r.read().split('\n')
    for line in effects:
        print(line.split(':'))
        type_effect, effect = line.split(':')
        
        its.add_effect(type_effect, int(effect))
        
    items[file.split('.')[0]] = its