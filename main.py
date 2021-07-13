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
            return str(self.value)

    def set_val (self, val_in): #Used to set value while solving
        self.pos = []
        self.value = val_in


table = [[],[],[],[],[],[],[],[],[]]    #TODO: implement class for board

# for i in table:
#     for j in range(9):
#         i.append(square(0)) 

def fill_squares(table_in):
    for i in table_in:
        for j in i:
            if len(j.pos) == 1: #if there is only one item in list
                j.set_val(j.pos[0])
    return

def hor_comp(table_in):
    for i in table_in:
        temp_table = []
        for j in i:
            if not len(j.pos):
                temp_table.append(j.value)
        for j in i:
            j.pos = [x for x in j.pos if x not in temp_table]
    return

def vert_comp(table_in):
    for x in range(1):
        temp_table = []
        for i in table_in:
            if not len(i[x].pos):
                temp_table.append(i[x].value)
        for i in table_in:
            if len(i[x].pos) > 1:
                i[x].pos = [x for x in i[x].pos if x not in temp_table]
    return

def square_check(table_in):
    hor_index, vert_index = [0,3,6]
    for h_start in hor_index:
        square_lst = []
        for v_start in vert_index:
            for x in range(3):
                for y in range (3):
                    if (table_in[h_start + x][v_start + y].value != 0):
                        square_lst.append(table_in[h_start + x][v_start + y].value)
        for v_start in vert_index:
            for x in range(3):
                for y in range (3):
                    #add removal part here
                    return #just added to stop error message
    return


def manual_fill_table(table_in):    # Allows user to fill out table manually
    print ("Fill the table by row moving from left to right; use zero for squares which are not filled in.")
    for x in range(9):
        correct, input_valid = False, False
        while correct == False:
            print ("Filling row", x + 1)
            for y in range(9):  # TODO: Add input verification and maybe have user input "?" instead of zero
                usr_val_in = input("Input number: ")
                table_in[x].append(square(usr_val_in))
            while input_valid == False:
                print ("Is", table_in[x], "correct? (y/n)")
                usr_in = input()
                if usr_in.upper() == "Y" or usr_in.upper() == "N":
                    input_valid = True
                else:
                    print ("Invalid Input, Try Again.")
            if usr_in.upper() == "N":
                table_in[x].clear()
                print ("Fill Row Again.")
                input_valid = False
            else:
                correct = True
    return
                

def print_table(table_in):  # Could remove ? cases with use of get value function in square class
    horiz = 0
    for i in table_in:
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
    return

# manual_fill_table()
# print_table()

# test1 = square (0)
# test1.pos = [8,9]
# test2 = square (9)
# test_table = [[test1,test2]]

# hor_comp(test_table)
# print (test1.pos)

test1 = square (0)
test1.pos = [2,9]
test2 = square (2)
test3 = square (3)
test4 = square (0)
test4.pos = [2,8]
test5 = square (5)
# test6 = square (6)
# test7 = square (7)
# test8 = square (8)
# test9 = square (9)
test_table = [[test1],[test2],[test3],[test4],[test5]]

# print_table(test_table)
vert_comp(test_table)
fill_squares(test_table)
print (test1)
print (test4)
# fill_squares(test_table)
# print_table(test_table)

# lst_1 = [1,2]
# lst_2 = [2,5,6]
# lst_1 = [x for x in lst_1 if x not in lst_2]
# print (lst_1)