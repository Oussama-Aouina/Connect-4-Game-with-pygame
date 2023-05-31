#indiquer s'il y'a une diagonale complete de gauche vers la droite:
def checkDiagonalGD(x):
    global l
    test=False
    i=5
    while i>2 and test == False:
        j=0
        while j<4 and test == False:
            test = True
            for k in range(4):
                if l[i-k][j+k]!=x:
                    test = False
            j+=1
        i-=1
    return test
#indiquer s'il y'a une diagonale complete de droite vers la gauche:
def checkDiagonalDG(x):
    global l
    test=False
    i=5
    while i>2 and test == False:
        j=6
        while j>=4 and test == False:
            test = True
            for k in range(4):
                if l[i-k][j-k]!=x:
                    test = False
            j-=1
        i-=1
    return test


#indiquer s'il y'a une diagonale complete:
def checkDiagonal(x):
    return checkDiagonalGD(x) or checkDiagonalDG(x)

#indiquer s'il y'a une ligne complete:
def checkLigne(x):
    global l
    i=5
    test=False
    while i>=0 and test == False:
        j=0
        while j<4 and test == False:
            test = True
            for e in l[i][j:j+4]:
                if e!=x:
                    test = False
            j+=1
        i-=1
    return test

#indiquer s'il y'a une colonne complete:
def checkColumn(x):
    global l
    i=5
    j=0
    test=False
    while j<7 and test==False:
        i=5
        while i>2 and test == False:
            test = True
            for k in range(4):
                if l[i-k][j] != x:
                    test = False
            i-=1
        j+=1
    return test




class game():
    #initialisation de nombre des pions a 42 puis il se decremente a chaque fois on a mis un


    #initialisation de la matrice vide
    def __init__(self):
        self.pions=42
        global l
        # l=[[0 for i in range(7)] for i in range(6)]
        l=[
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0]
        ]



    #affichage de la matrice d'origine
    def __str__(self):
        s=""
        for e in l:
            for j in e:
                s+=f"{j} "
            s+=f"\n"
        return s


    #indiquer s'il y'a un gagnant:
    def checkWinner(self,x):
        return checkColumn(x) or checkDiagonal(x) or checkLigne(x)

    #ajouter un pion a sa position convenable par num de colonne:
    def putPion(self,x,a):
        global l
        test = False
        i=5
        while i>=0 and test == False:
            test = True
            if l[i][a] == 0:
                l[i][a] = x
                test = True
                self.pions-=1
                #print("putted")
            else:
                i-=1
                #print("inputted")
                test = False

        return i


if __name__ == '__main__':
    g=game()
    for i in range(70):
        print(g.putPion(1,2))

    print(g)
    print(g.checkWinner(1))

