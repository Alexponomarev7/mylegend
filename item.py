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

class item:
    itype = None
    name = None
    about = None
    strength = None
    image_id = None
    effects = None
    
    def __init__(self, itype, name, about, strength, image_id):
        self.itype = itype
        self.name = name
        self.about = about
        self.strength = strength
        self.image_id = image_id
        
    def add_effect(self, type_effect, effect):
        if self.effects is None:
            self.effects = dict()
            self.effects[type_effect] = effect
        else:
            self.effects[type_effect] = effect