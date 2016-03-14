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

from repaint import repaint
from tkinter import *
from const import *

class hero:    
    state = dict()
    state["helmet"] = None
    state["armory"] = None
    state["left_hand"] = None
    state["boots"] = None
    state["right_hand"] = None
    
    state["armor"] = 0
    state["health"] = 100
    state["mana"] = 100
    state["stamina"] = 100
    state["damage"] = 20
    
    images = dict()
    images["loot_pan"] = []
    images["character"] = []
    images["desk"] = []
    
    labels = dict()
    labels["helmet"] = None
    labels["armory"] = None
    labels["left_hand"] = None
    labels["boots"] = None
    labels["right_hand"] = None
    
    loot = []
    
    # Canvases
    desk = None
    loot_pan = None
    character = None
    # end
    
    level = 1
    level_map = None
    
    x, y = None, None
    
    stamina_point = 1
    
    
    def __init__(self, x_pos, y_pos):
        self.x = x_pos
        self.y = y_pos
    
    
    def droplefthand(self, event):
        if self.state["left_hand"] != None:
            for i in self.state["left_hand"].effects:
                self.state[i] -= self.state["left_hand"].effects[i]
                
            self.loot.append(self.state["left_hand"])
            self.state["left_hand"] = None
        
        self.update()
           
              
    def droprighthand(self, event):
        if self.state["right_hand"] != None:
            for i in self.state["right_hand"].effects:
                self.state[i] -= self.state["right_hand"].effects[i]
                
            self.loot.append(self.state["right_hand"])
            self.state["right_hand"] = None
        
        self.update()   
              
              
    def drophelmet(self, event):
        if self.state["helmet"] != None:
            for i in self.state["helmet"].effects:
                self.state[i] -= self.state["helmet"].effects[i]
                
            self.loot.append(self.state["helmet"])
            self.state["helmet"] = None
        
        self.update()   
    
    
    def up(self, event):
        IMAGES[1] = PhotoImage(file="src/mobs/hero1.gif")
        
        if go_try(self, UP):
            self.y -= 1
            self.state["stamina"] -= self.stamina_point
            
        self.update()
    
        
    def down(self, event):
        IMAGES[1] = PhotoImage(file="src/mobs/hero.gif")   
        
        if go_try(self, DOWN):
            self.y += 1
            self.state["stamina"]  -= self.stamina_point
            
        self.update()
        
        
    def left(self, event):
        if go_try(self, LEFT):
            self.x -= 1
            self.state["stamina"] -= self.stamina_point
            
        self.update()
        
        
    def right(self, event):
        if go_try(self, RIGHT):
            self.x += 1
            self.state["stamina"] -= self.stamina_point
            
        self.update()

        
    def relax(self, event):
        self.state["stamina"] = min(100, self.state["stamina"] + 5)
        self.update()
        
        
    def information(self, event):
        if len(self.loot) >= int(event.keysym):
            item = self.loot[int(event.keysym) - 1]
            
            inf = Tk()
            inf.title(item.name)
            inf.resizable(width=False, height=False)
              
            cnv = Canvas(inf)
            cnv.pack()
                        
            Label(cnv, text='Name: ' + item.name).grid(row=1, column=2)
            Label(cnv, text='Strength: ' + item.strength).grid(row=2, column=2)
            
            row_num = 3
            for i in item.effects:
                count = str(item.effects[i])
                Label(cnv, text=i + ": " + count).grid(row=row_num, column=2)
                row_num += 1
                
            t = Text(cnv, height=4, width=50, font=ARIAL, wrap=WORD, fg='blue')
            t.insert(1.0, item.about)

            scr = Scrollbar(cnv)
            scr.config(command=t.yview)                    
            t.config(state = 'disabled', yscrollcommand=scr.set)
            t.grid(row=5, column=1+1)
            scr.grid(row=5,column=1+2, sticky='ns')
            
              
    def interact(self, event):
        for i in range(4):
            block = self.level_map[self.y + step_y[i]][self.x + step_x[i]]

            if block.itype == CHEST:
                print(1)
                while len(self.loot) < 8 and len(block.loot) > 0:
                    self.loot.append(block.loot[0])
                    del(block.loot[0])
                
                self.level_map[self.y + step_y[i]][self.x + step_x[i]] = block
        
        self.update()
        
        
    def using(self, event):
        if int(event.keysym) <= len(self.loot):
            item = self.loot[int(event.keysym) - 1]
            del(self.loot[int(event.keysym) - 1])
            
            self.state[item.itype] = item
            for name_effect in item.effects:
                self.state[name_effect] += item.effects[name_effect]
                
                     
        self.update()
        
        
    def update(self):
        repaint(self)