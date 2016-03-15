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
from level import *
from  repaint import *
import math, threading, time
import subprocess
import pyglet
from hero import hero
from const import *

def load():
     for i in range(len(IMAGES)):
          IMAGES[i] = PhotoImage(file=IMAGES[i])
          
     for i in range(len(V_LOOT)):
          V_LOOT[i] = PhotoImage(file=V_LOOT[i])
          

if __name__ == '__main__':
     knight = hero(5, 12)
     knight.level_map = lvl(1)
          
     root = Tk()     
     root.state("zoomed")     
     w, h = root.winfo_screenwidth(), root.winfo_screenheight()
     root.geometry("{}x{}+0+0".format(w, h))     
     root["bg"] = "black"
     root.title("LEGEND OF PONOMAR 2")
     root.attributes('-fullscreen', 1)
     root.resizable(width=False, height=False)
     
     load()     
     
     f_width = (w - ((32 * 11) + 454)) / 2
     new = Frame(root, highlightthickness=0, width=f_width, height=0, bd=0, relief='ridge', bg="black")
     new.grid(row=1,column=0)     
     
     knight.desk = Canvas(root, highlightthickness=0, width=DESK_WIDTH, height=DESK_HEIGHT, bd=0, relief='ridge', bg="black")
     knight.desk.create_rectangle(6, 6, 179 * 2 - 1, 179 * 2 - 1, fill="black")
     knight.desk.grid(row=1,column=1)
     
     knight.character = Canvas(root, width=460, highlightthickness=0, height = 298, bg="black", bd=0, relief='ridge')
     knight.character.grid(row=1, column=2,sticky=NW)          
     img = PhotoImage(file="src/system/char.gif")
     knight.character.create_image(3, 3, anchor=NW, image=img)
     
     knight.loot_pan = Canvas(root, width = 416, height=42, highlightthickness=0, bg="black", bd=0, relief='ridge')
     knight.loot_pan.grid(row=1, column=2,sticky=S)
     img1 = PhotoImage(file="src/system/slot.gif")
     knight.loot_pan.create_image(3, 3, anchor=NW, image=img1)
     
     knight.labels["right_hand"] = label_for_equip(root)
     knight.labels["right_hand"].grid(row=3, column=2, sticky=NE)
     
     knight.labels["left_hand"] = label_for_equip(root)
     knight.labels["left_hand"].grid(row=2, column=2, sticky=NE)

     knight.labels["helmet"] = label_for_equip(root)
     knight.labels["helmet"].grid(row=2, column=1, sticky=NE)

     knight.labels["boots"] = label_for_equip(root)
     knight.labels["boots"].grid(row=4, column=1, sticky=NE)

     knight.labels["armory"] = label_for_equip(root)
     knight.labels["armory"].grid(row=3, column=1, sticky=NE)
     
     
     make_label_for(root, "Helmet: ").grid(row=2, column=1, sticky=NW)
     make_label_for(root, "Armory: ").grid(row=3, column=1, sticky=NW)
     make_label_for(root, "Boots: ").grid(row=4, column=1, sticky=NW)
     make_label_for(root, "Jewel: ").grid(row=5, column=1, sticky=NW)
     make_label_for(root, "Left hand: ").grid(row=2, column=2, sticky=NW)
     make_label_for(root, "Right hand: ").grid(row=3, column=2, sticky=NW)
     make_label_for(root, "Bow: ").grid(row=4, column=2, sticky=NW)
     setting(root, knight)
     
     knight.update()
     
     root.mainloop()
     