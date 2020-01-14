#!/bin/python3

import os
import sys

def isaRookAroundMe(x,y):
    #Check ligne
    checkColumn = checkRow = False
    checkRow = True if "o" in board[y] else False
    for i in range(n):
        if board[i][x] == "o":
            checkColumn = True
            break
    
    if checkColumn+checkRow == 0:
        return False
    else:
        return True


def addRock(x,y):
    newY = list(board[y])
    newY[x] = 'o'
    board[y] = "".join(newY)

    print("New row: "+str(board[y]))


def jumpingRooks(k, board):
    RockAdded = 0
    for y in range(n):
        for x in range(len(board[y])):
            if not isaRookAroundMe(x,y): 
                print("Cell free, position:"+str(x)+","+str(y))
                addRock(x,y)
                RockAdded += 1
    return RockAdded
              
if __name__ == '__main__':

    nk = input().split()

    #n = taille de la grille
    n = int(nk[0])

    #k = rocks a positionner
    k = int(nk[1])

    board = []

    for _ in range(n):
        board_item = input()
        board.append(board_item)

    result = jumpingRooks(k, board)

    print("Rock beat: "+str(2 * (k - result)))
    print("Final board: ")
    for row in range(n): print(str(board[row]))