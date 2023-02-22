#TIC TAC TOE IN PYTHON 

w =4
h =4
global a_b
a_b= [['_' for x in range(w) ] for y in range(h)]
global player
player = 'x'
global plays 
plays=0
winner=""

#Give initial values to the playing grid 
def init():
    for i in range(w):
        for j in range(h):
            print('_',end=" ")
        print('\n')
#Clearing the screen 
def Clearscreen():
    import os
    os.system('cls')
#checking the inputs if it's right or not
def validate(number):
    number=int(number)
    if (number>=1 and number<=3):
        return True 
    else:
        print ("please pick a value between 1 to 3")
        return False
#understanding who is the winner 
def gameover ():
    global plays
    plays+=1
    if (plays > 5):
       if (a_b[1][1]==a_b[1][2] and a_b[1][2]==a_b[1][3] and a_b[1][2]!='_' ):
             print ("player",winner,"win." )
             return True 
       elif (a_b[2][1] == a_b[2][2] and a_b[2][2] == a_b[2][3] and a_b[2][2] != '_'):
             print ("player",winner,"win." )
             return True 
       elif (a_b[3][1] == a_b[3][2] and a_b[3][2] == a_b[3][3] and a_b[3][2] != '_'):
             print ("player",winner,"win." )
             return True 
       elif (a_b[1][1] == a_b[2][1] and a_b[2][1] == a_b[3][1] and a_b[2][1]):
             print ("player",winner,"win." )
             return True 
       elif (a_b[1][2] == a_b[2][2] and a_b[2][2] == a_b[3][2] and a_b[2][2] != '_'):
             print ("player",winner,"win." )
             return True
       elif (a_b[1][3] == a_b[2][3] and a_b[2][3] == a_b[3][3] and a_b[2][3] != '_'):
             print ("player",winner,"win." )
             return True
       elif (a_b[1][1] == a_b[2][2] and a_b[2][2] == a_b[3][3] and a_b[2][2] != '_'):
             print ("player",winner,"win." )
             return True
       elif (a_b[1][3] == a_b[2][2] and a_b[2][2] == a_b[3][1] and a_b[2][2] != '_'):
             print ("player",winner,"win." )
             return True
    return False
#the code for playing -------------------------------------
def showBoard ():
    global player
    while (not gameover()): #while statement to check gameover() state
         print('x') if player == 'x' else print ('o')
         Clearscreen()
         row = 0
         col = 0
         print ("it's",player,"'s turn","\n")
#printing column numbers 
         print ("\t")
         for i in range(1,4):
            print (" ",i,end=" ")
         print ("\n")
#print numbers and _s
         for i in range(1,4):
            print (i,end="  ")
            for j in range(1,4):
                print(a_b[i][j] ,end="  ")
            print("\n") 
#getting the row and column
         while (not validate(row)):
            row=int(input("In what row would you like to play? =>"))
         while(not validate(col)):
            col=int(input("In what column would you like to play? => "))
         
#putting the parameter in right place
         a_b[row][col]=player 
         print ('x') if  player =='x' else print ('o')
         player='o' if player=='x' else 'x'
#main function          
def main():
    plays=0
    print ("hello world !")
    init()
    showBoard()
main()