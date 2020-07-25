#!/usr/bin/env python3
from math import inf as infinity
from random import choice
import platform
import time
from os import system

def clean():
    """
    Clears the console
    """
    os_name = platform.system().lower()
    if 'windows' in os_name:
        system('cls')
    else:
        system('clear')


def choose_domino(first_player,second_player):
    while(True):
        #print("First player :\n")
        first_player = input("Type V to choose Vertical domino, type H to choose horizontal domino: ").upper()
        if first_player == "V":
            second_player = "H"
            break
        elif(first_player == "H"):   
            second_player = "V"
            break
        else:
            pass
    return first_player,second_player


def gui(moves):
    clean()
    print('\n')
    for row in moves:
        for cell in row: 
            print(f'| {cell} |', end='')
        print('\n' )
        



def makemove(x,y,rows,columns,moves,move):
    if((x >= rows) or (y >= columns)):
        #print("Invalid Input")
        return 0
    else:
        if(move == "H"):
            if(y == columns-1):
                #print("Invalid move")
                return 0
            elif((moves[x][y] != " ") or (moves[x][y+1] != " ")):
                #print("Invalid move")
                return 0
            else:
                moves[x][y] = move
                moves[x][y+1] = move
                return 1
        else:
            if((moves[x][y]) != " "):
                #print("Invalid move")
                return 0
            else:
                moves[x][y] = move
                return 1



def undomove(x,y,state,move):
    board = state
    
    if(move == "H"):
        board[x][y] = " "
        board[x][y+1] = " "
    else:
        board[x][y] = " "

    return board

def win(player,first_player,second_player):
    if(player == first_player):
        return 1
    else:  
        return -1

'''============================================ Alpha beta algorithm code=================================================='''
'''def max_value(state,alpha,beta,player,first_player,second_player):
    if(not gamenotfinish(state,player)):
        score = (win(player,first_player,second_player))
        return [-1,-1,score]
    else:
        v =[-1,-1,-infinity]
        board = state
        for row in range(len(board)):
            for column in range(len(board[row])):
                if(makemove(row,column,len(board),len(board[row]),board,player)):
                    if(player == first_player):
                        player = second_player
                    else:
                        player = first_player
                    score = min_value(board,alpha,beta,player,first_player,second_player)
                    score[2] = max(v[2],score[2])
                    score[0] = row
                    score[1] = column
                    if(score[2] != v[2]):
                        v = score
                    if(v[2] >= beta):
                        return v
                    alpha = max(alpha,v[2]) 
        return v

def min_value(state,alpha,beta,player,first_player,second_player):
    if(not gamenotfinish(state,player)):
        score = (win(player,first_player,second_player))
        return [-1,-1,score]
    else:
        v =[-1,-1,+infinity]
        board = state
        for row in range(len(board)):
            for column in range(len(board[row])):
                if(makemove(row,column,len(board),len(board[row]),board,player)):
                    if(player == first_player):
                        player = second_player
                    else:
                        player = first_player
                    score = max_value(board,alpha,beta,player,first_player,second_player)
                    score[2] = min(v[2],score[2])
                    score[0] = row
                    score[1] = column
                    if(score[2] != v[2]):
                        v = score
                    if(v[2] <= alpha):
                        return v
                    beta = min(beta,v[2]) 
        return v


def ai_turn(state,first_player,second_player,player):
    v=max_value(state,-infinity,infinity,player,first_player,second_player)
    return v'''

'''==============================================================================================================='''

def gamenotfinish(moves,move):
    for row in moves:
        for column in range(len(row)):
            if(row[column] == " "):
                if(move == "H"):
                    if(column != len(row)-1):
                        if(row[column+1] == " "):
                            return 1
                elif(move == "V"):
                    return 1
    return 0



'''----------------------The below function is for two human players------------------------------'''

def startgame(first_player,second_player,rows,columns,moves):
    player = first_player
    while(gamenotfinish(moves,player)):
        gui(moves)
        x,y = input("Enter x and y coordinate both starting from 1: ").split()
        while(x == '0' or y=='0'):
            x,y = input("Enter x and y coordinate both starting from 1: ").split()
        x = int(x)
        y = int(y)
        while(not makemove(x-1,y-1,rows,columns,moves,player)):
            x,y = input("Enter x and y coordinate [1...]: ").split()
            x = int(x)
            y = int(y)
        gui(moves)
        if(player == first_player):
            player = second_player
        else:
            player = first_player
    
    if(player == first_player):
        print("second player wins the game")
    else:
        print("first player wins the game")

''' --------------------------------------------------------------------------------'''

'''-----------------------Computer vs Human----------------------------------'''
'''CODE IS NOT CORRECT
    TRY FIXING IT
    APLHA BETA ALGORITHMS MAY ALSO BE WRONG , NOT SURE'''

def startgame_ai(first_player,second_player,rows,columns,state):
    clean()
    gui(state)
    turn = input("Do you want to move first? y/n ")
    while(turn.lower() != "y" and turn.lower() != "n"):
        clean()
        gui(state)
        turn = "Please enter the right value :"
    if(turn.lower() == "y"):
        move = first_player
    else:
        move = second_player
    
    while(True):
        if(move == first_player):
            while(True):
                clean()
                gui(state)
                while(True):
                    coordinates = input("Enter the coordinates to make your move : ").split()
                    while(len(coordinates) != 2):
                        clean()
                        gui(state)
                        coordinates = input("Please re-enter the right coordinates : ").split()
                    while(True):
                        try:
                            x = int(coordinates[0])
                            y = int(coordinates[1])
                            break
                        except:
                            print("Please enter integer values!\n")
                    if(x >= rows or y >= columns):
                        print("Please enter the correct coordinates!\n\n");
                    else:
                        break
                if(makemove(x,y,rows,columns,state,move)):
                    move = second_player
                    clean()
                    gui(state)
                    break
                else:
                    print("Please enter valid coordinates! \n")
            if(not gamenotfinish(state,move)):
                break
        else:
            clean()
            gui(state)
            #board = state
            board = state
            coordinates,state= ai_turn(board,-infinity,+infinity,move,first_player,second_player)
           
            v = makemove(coordinates[0],coordinates[1],rows,columns,state,move)
                
            move = first_player
            
            clean()
            gui(state)
            print(coordinates,v)
            
            if(not gamenotfinish(state,move)):
                break
    
    if(move == first_player):
        print("You lost!\n")
    else:
        print("You won!\n")
'''-----------------------------------------------------------------------------------------'''

def ai_turn(board,alpha,beta,move,first_player,second_player):
    
    if(not gamenotfinish(board,move)):
        score = win(move,first_player,second_player)
        return [-1,-1,score],board

    if(move == second_player):
        value = [-1,-1,-infinity]
        for row in range(len(board)):
            for column in range(len(board[row])):
                if(makemove(row,column,len(board),len(board[row]),board,move)):
                    state = board
                    score,state = ai_turn(state,alpha,beta,first_player,first_player,second_player)
                    state = undomove(row,column,state,move)
                    score[0], score[1] = row,column
                    if(value[2] < score[2]):
                        value = score
                    alpha = max(alpha,value[2])
                    if(alpha >= beta):
                        break
        return value,state
    
    else:
        value = [-1,-1,infinity]
        for row in range(len(board)):
            for column in range(len(board[row])):
                if(makemove(row,column,len(board),len(board[row]),board,move)):
                    state = board
                    score,state = ai_turn(state,alpha,beta,second_player,first_player,second_player)
                    state = undomove(row,column,state,move)
                    score[0], score[1] = row,column
                    if(value[2] > score[2]):
                        value = score
                    beta = min(beta,value[2])
                    if(alpha >= beta):
                        break
        return value,state







def main():
    while(True):
        try:
            rows,columns = input("rows,columns: ").split()
            rows=int(rows)
            columns = int(columns)
            break
        except:
            print("Please enter the right values!\n")
    first_player = ""
    second_player = ""
    state = []
    for i in range(rows):
        state.append([" "]*columns)

    first_player,second_player=choose_domino(first_player,second_player)
    startgame_ai(first_player,second_player,rows,columns,state)


if __name__ == '__main__':
    main()
