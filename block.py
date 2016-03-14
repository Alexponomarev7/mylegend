from const import *

class block:
    symbol = None
    floar_id = None
    wall_id = None
    is_floar = None
    image_id = None
    itype = None
    
    next_lvl = None
    loot = None
    
    def __init__(self, symbol, image_id, is_floar, wall_id=None, floar_id=None, itype=None):
        self.symbol = symbol
        self.image_id = image_id
        self.is_floar = is_floar
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
        
    return result