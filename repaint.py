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

BLUE = "blue"
RED = "red"
HEALTH_POS = (326, 276, 294)
MANA_POS = (376, 276, 349)
STAMINA_POS = (440, 276, 413)

from tkinter import *
from const import *

def clean(hero):
    for i in hero.images["loot_pan"]:
        hero.loot_pan.delete(i)
    hero.images["loot_pan"] = []
    
    for i in hero.images["desk"]:
        hero.desk.delete(i)
    hero.images["desk"] = []
    
    for i in hero.images["character"]:
        hero.character.delete(i)
    hero.images["character"]
    
    
def repaint(hero):
    clean(hero)
    
    HIGH_H = 109 + ((100 - hero.state["health"])/ 100) * (86 * 2)
    HIGH_M = 109 + ((100 - hero.state["mana"])/ 100) * (86 * 2)
    HIGH_S = 109 + ((100 - hero.state["stamina"] )/ 100) * (276 - 109)
    
    health = hero.character.create_rectangle(HEALTH_POS, HIGH_H, fill=RED)
    hero.images["character"].append(health)
    
    mana = hero.character.create_rectangle(MANA_POS, HIGH_M, fill=BLUE)
    hero.images["character"].append(mana)
    
    stamina = hero.character.create_rectangle(STAMINA_POS, HIGH_S, fill="green") 
    hero.images["character"].append(stamina)
    
    equips = ["right_hand", "helmet", "left_hand", "boots", "armory"]
    
    for equip in equips:
        if hero.state[equip] != None:
            hero.labels[equip].configure(text=hero.state[equip].name)  
        else:
            hero.labels[equip].configure(text="")              
    
    for i in range(len(hero.loot)):
        img = hero.loot[i].image_id
        pos = (37 + 34 * i, 5)
        hero.images["loot_pan"].append(hero.loot_pan.create_image(pos, anchor=NE, image=V_LOOT[img]))
        
    
    for i in range(-5, 6):
        for j in range(-5, 6):
            x = (99 * 2) + j * 32
            y = (83 * 2) + i * 32
            
            block = hero.level_map[hero.y + i][hero.x + j]
            if block is None:
                continue
            
            
            if block.wall_id != None:
                wall = hero.desk.create_image(x, y, anchor=NE, image=IMAGES[block.wall_id])
                hero.images["desk"].append(wall)
            
            if block.floar_id != None:
                floar = hero.desk.create_image(x, y, anchor=NE, image=IMAGES[block.floar_id])
                hero.images["desk"].append(floar)
            
            its = hero.desk.create_image(x, y, anchor=NE, image=IMAGES[block.image_id])
            hero.images["desk"].append(its)
            
    knight = hero.desk.create_image((99 * 2), (83 * 2), anchor=NE, image=IMAGES[1])
    hero.images["desk"].append(knight)    