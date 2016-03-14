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

from tkinter import *

def exit_(event):
    root.destroy()


def go_try(self, direction):
    block = self.level_map[self.y + direction[0]][self.x + direction[1]]
    
    return block.is_floar and self.state["stamina"] > 0


def setting(self, knight):
    self.bind('<e>', knight.interact)
    self.bind('<r>', knight.relax)
    self.bind('<d>', knight.right)
    self.bind('<a>', knight.left)
    self.bind('<s>', knight.down)
    self.bind('<w>', knight.up)
    self.bind('<Control-KeyPress-1>', knight.information)
    self.bind('<Control-KeyPress-2>', knight.information)
    self.bind('<Control-KeyPress-3>', knight.information)
    self.bind('<Control-KeyPress-4>', knight.information)
    self.bind('<Control-KeyPress-5>', knight.information)
    self.bind('<Control-KeyPress-6>', knight.information)
    self.bind('<Control-KeyPress-7>', knight.information)
    self.bind('<Control-KeyPress-8>', knight.information)
    self.bind('<Control-KeyPress-9>', knight.information)     
    self.bind('<KeyPress-1>', knight.using)
    self.bind('<KeyPress-2>', knight.using)
    self.bind('<KeyPress-3>', knight.using)
    self.bind('<KeyPress-4>', knight.using)
    self.bind('<KeyPress-5>', knight.using)
    self.bind('<KeyPress-6>', knight.using)
    self.bind('<KeyPress-7>', knight.using)
    self.bind('<KeyPress-8>', knight.using)
    self.bind('<KeyPress-9>', knight.using)
    self.bind('<Control-KeyPress-l>', knight.droplefthand)   
    self.bind('<Control-KeyPress-r>', knight.droprighthand)     
    self.bind('<Control-KeyPress-h>', knight.drophelmet)     
    self.bind('<Control-z>',exit_)


def make_label_for(self, txt):
    return Label(self, text=txt, anchor=NW, fg="green", bg="black", font=FONT)


IMAGES = ["src/stones/stone.gif",    #0
          "src/mobs/hero.gif",       #1
          "src/floar/floar.gif",     #2
          "src/loot/chest.gif",      #3
          "src/doors/door.gif",      #4
          "src/floar/road.gif",      #5
          "src/floar/floar1.gif",    #6
          "src/stones/skull.gif",    #7
          "src/floar/fire.gif",      #8
          "src/floar/floar2.gif",    #9
          "src/stones/stone2.gif",   #10
          "src/floar/fontan.gif",    #11
          "src/loot/helmet.gif",     #12
          "src/stones/stone_btn.gif"]#13
          

V_LOOT = ["src/loot/sword1.gif",   # 0
          "src/loot/health1.gif",  # 1
          "src/loot/helmet.gif",   # 2
          "src/loot/armor.gif"]    # 3


UP = (-1, 0)
DOWN = (1, 0)
LEFT = (0, -1)
RIGHT = (0, 1)

step_x = [0, 0, 1, -1]
step_y = [1, -1, 0, 0]

FONT = "Symbol 20 underline"
ARIAL = 'Arial 14 italic'

CHEST = "chest"
DOOR = "door"

DESK_WIDTH = 179 * 2
DESK_HEIGHT = 179 * 2