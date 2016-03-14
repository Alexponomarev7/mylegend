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
        