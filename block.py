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

from const import *

class block:
    symbol = None
    floar_id = None
    wall_id = None
    is_floar = None
    image_id = None
    itype = None
    
    next_lvl = None
    next_pos = None
    
    loot = None
    
    def __init__(self, smb, img, flag, wall_id=None, floar_id=None, itype=None):
        self.symbol = smb
        self.image_id = img
        self.is_floar = flag
        self.wall_id = wall_id
        self.floar_id = floar_id
        self.itype = itype
        
    def add_loot(self, item):
        if self.loot is None:
            self.loot = [item]
        else:
            self.loot.append(item)
  
        
def parser(symbol, floar_id, wall_id):
    result = None
    
    if symbol == '.':
        result = block(symbol, floar_id, True)
    elif symbol == '#':
        result = block(symbol, wall_id, False)
    elif symbol == 'T':
        result = block(symbol, 3, False, floar_id=floar_id)
        result.itype = CHEST
    elif symbol == '_':
        result = block(symbol, 5, True)
    elif symbol == '>':
        result = block(symbol, 4, False, wall_id=wall_id)
        result.itype = DOOR
    elif symbol == 'K':
        result = block(symbol, 8, False, floar_id=floar_id)        
        
        
    return result