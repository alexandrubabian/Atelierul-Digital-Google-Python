def inceput():
    vector=[0]*9
    return vector

def XSAUO(x):
    if x==1:
        return 'O'
    elif x==0:
        return ' '
    return 'X'

def afisare(vector):
    print("\n")
    for i in range(3):
        print(XSAUO(vector[i*3+0])+'|'+XSAUO(vector[i*3+1])+'|'+XSAUO(vector[i*3+2]))
        if i != 2:
            print("_ _ _")

def alege(vector):
    if vector[4]==0:
        vector[4]=1
        return vector
    elif vector[0]==0:
        vector[0] = 1
        return vector
    elif vector[2]==0:
        vector[2] = 1
        return vector
    elif vector[6]==0:
        vector[6] = 1
        return vector
    elif vector[8]==0:
        vector[8] = 1
        return vector
    else:
        for i in range(1,8,2):
            if vector[i]==0:
                vector[i] = 1
                return vector

def over(vector, tip):
    #returneaza adevarat daca jocul s-a terminat
    #verificare vertical
    for i in range(3):
        if vector[i]==tip and vector[i+3]==tip and vector[i+6]==tip:
            if tip==1:
                afisare(vector)
                print("The robot won")
            else:
                print("Well done, you have won on the vertical")
            return True
    #verificare orizontal
    for i in range(0,7,3):
        if vector[i]==tip and vector[i+1]==tip and vector[i+2]==tip:
            if tip==1:
                afisare(vector)
                print("The robot won")
            else:
                print("Well done, you won on the orizontal")
            return True
    #verificare diagonala principala
    if vector[0] == tip and vector[4] == tip and vector[8] == tip:
        if tip == 1:
            afisare(vector)
            print("The robot won")
        else:
            print("Well done, you won on the main diagonal")
        return True
    #verificare diagonala secundara
    if vector[2] == tip and vector[4] == tip and vector[6] == tip:
        if tip == 1:
            afisare(vector)
            print("The robot won")
        else:
            print("Well done, you won on the secondary diagonal")
        return True
    return False

vector=inceput()
while not over(vector,1) and not over(vector,2):
    afisare(vector)
    if not 0 in vector:
        print("Draw")
        break
    x=input("Insert the position from 1 to 9 where you want to draw X:")
    x=int(x)
    while(vector[x-1]!=0):
        x=input("You have taken an occupied position, choose another one:")
        x=int(x)
    vector[x-1]=2
    afisare(vector)
    if over(vector,2):
        break
    else:
        if 0 in vector:
            vector=alege(vector)