class square:
    def __init__(self):
        self.pos = list(range(1,10))
        self.value = 0   # Using zero instead of none so value and complete boolean can be same

    def __init__(self, val_in):
        if val_in == False:
            self.pos = list(range(1,10))
        else:    
            self.pos = []   # Using empty adds another easy way to detect finished squares
        self.value = val_in

    def __repr__(self): #Used so manual fill can easily display rows
        if self.value == 0:
            return "?"
        else:
            return str(self.value)   # TODO: Add fitering to display "?" instead of 0

    def set_val (self, val_in): #Used to set value while solving
        self.pos = []
        self.value = val_in


table = [[],[],[],[],[],[],[],[],[]]    #TODO: implement class for board

# for i in table:
#     for j in range(9):
#         i.append(square(0)) 

def fill_squares():
    for i in table:
        for j in i:
            if len(j.pos): #if there is only one item in list
                j.set_val(j.pos[0])


def manual_fill_table():    # Allows user to fill out table manually
    print ("Fill the table by row moving from left to right; use zero for squares which are not filled in.")
    for x in range(9):
        correct, input_valid = False, False
        while correct == False:
            print ("Filling row", x + 1)
            for y in range(9):  # TODO: Add input verification and maybe have user input "?" instead of zero
                usr_val_in = input("Input number: ")
                table[x].append(square(usr_val_in))
            while input_valid == False:
                print ("Is", table[x], "correct? (y/n)")
                usr_in = input()
                if usr_in.upper() == "Y" or usr_in.upper() == "N":
                    input_valid = True
                else:
                    print ("Invalid Input, Try Again.")
            if usr_in.upper() == "N":
                table[x].clear()
                print ("Fill Row Again.")
                input_valid = False
            else:
                correct = True
                

def print_table():  # Could remove ? cases with use of get value function in square class
    horiz = 0
    for i in table:
        vert = 0
        for j in i:
            vert += 1
            if (vert % 3 == 0 and vert < 9):
                if j.value == False:
                    print ("?","", end="")
                else:
                    print (j.value,"", end="")
                print ("|",end=" ")
            else:
                if j.value == False:    # If value is 0 (unknown) then display as "?"
                    print ("?","  ", end="")
                else:
                    print (j.value,"  ", end="")
        horiz += 1
        if (horiz % 3 == 0 and horiz < 9):
            print ("\n")
            for k in range(33):
                print ("-",end="")
        print("\n")

# manual_fill_table()
# print_table()