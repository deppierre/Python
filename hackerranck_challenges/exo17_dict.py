#!/bin/python3

if __name__ == '__main__':

    nb_entry = int(input())

    annuaire = {}
    element_tofind = []
 
    for i in range(nb_entry):
        list_elements = input().split()
        annuaire[list_elements[0]] = list_elements[1]

    line = "init"
    while line != "":
        try:
            line = input()
            if line in annuaire: print(line+"="+annuaire[line])
            else: print("Not found")
        except EOFError:
            break