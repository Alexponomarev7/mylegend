class mob:
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
    
    x, y = None, None    
    loot = None    
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
        self.loot = []