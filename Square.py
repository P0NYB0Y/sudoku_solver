class square:
    def __init__(self, val_in = False):
        if val_in == False:
            self.pos = list(range(1,10))
        else:    
            self.pos = []   # Using empty adds another easy way to detect finished squares
        self.value = val_in

    def __repr__(self): #Used so manual fill can easily display rows
        if self.value == 0:
            return "?"
        else:
            return str(self.value)

    def set_val (self, val_in): #Used to set value while solving
        if self.value != False:
            print("oh no") # TODO: Replace with actual error
        self.pos = []
        self.value = val_in