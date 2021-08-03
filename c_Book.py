# Importing frameworks

import numpy as np
import os

# Writing the functions part

def cr_con_Book():

    x_1 = input("Enter name: ")
    x_2 = input("Enter p_Number: ")
    with open('B_1.txt', 'w')as f:
        f.write(f'This list is for {x_1}\nHis p_Number is {x_2}')
    print("Done!\n")

def s_List():
    
    with open('B_1.txt', 'r')as n:
        d = n.read()
        print(d)
        print("\n")

def a_Con():

    z_2 = input("Enter person's name: ")
    z_3 = input("Enter his number\n")
    with open('B_1.txt', 'a')as z:
        z.write(f'\n{z_2}: {z_3}')
    print("Done!\n")

def erase_line(fname, line_num):
    ''' In-place replacement of line `line_num` in file `fname` with
        a line of DEL chars of the same length, retaining the newline.
    '''
    DEL = '#'
    with open(fname, 'r+') as f:
        for i in range(line_num - 1):
            f.readline()
        start = f.tell()
        line = f.readline()
        line = DEL * (len(line) - 1) + '\n'
        f.seek(start)
        f.write(line)

def del_Con():

    v = input("Enter the username you want to remove: ")
    with open('B_1.txt', 'r+')as k:
        
        for num, line in enumerate(k, 1):
            num = int(num)
            if v in line:
                erase_line('B_1.txt', num)
    print("Done!\n")

def find_con():

    s = input("Search the username here: ")
    with open("B_1.txt", "r+")as z:
        for j, j1 in enumerate(z, 1):
            if s in j1:
                try:
                    print(f'\n{j1}\n')

                except:
                    print("User is not in your contact list!")

if __name__=="__main__":

# Making an interface for the user

    while(True):

        print("Welcome to our Con_List software!!!")

        x = input("Enter your wish\n")

# Making conditions

        if x == "create list":
                cr_con_Book()

        elif x == "see list":
                s_List()

        elif x == "add contact":
                a_Con()

        elif x == "del contact":
                del_Con()
        
        elif x == "search contact":
                find_con()
        
        else:
                break