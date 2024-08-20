from random import randint
import array as arr

def lancerDe():
    return randint(1,6)

def compter(Tab,Nb):
    points = 0
    for Number1 in range(0, len(Tab)):
        if Tab[Number1] == Nb :

            points = points + Nb
    return points
def calculTotal(Grille):
    total = 0
    for i in range(1, len(Grille)):
        if Grille[i] != "X":
            total = total + int(Grille[i])
    return total


if __name__ == '__main__':
    Name = "Toto" # input('Entre ton nom stp : ')
    Grille = [Name, "X", "X", "X", "X", "X", "X"]
    print('Voici la grille de Yams de ' + Name)

    for Tour in range(1,len(Grille)):
        tabDes = [lancerDe(), lancerDe(), lancerDe(), lancerDe(), lancerDe()]
        print('Tu lances les dés, et tu obtiens : ')
        print (str(tabDes[0]) + ' / ', str(tabDes[1]) + ' / ', str(tabDes[2]) + ' / ', str(tabDes[3]) + ' / ', str(tabDes[4]))
        choix1 = input('Que fais tu ?' )
        result = (compter(tabDes,int(choix1)))
        Grille[int(choix1)] = result
        print('Voici ta grille :')
        for Number in range(1,len(Grille)):
            print(str(Number) + ' : '  + str(Grille[Number]))
        print("Total : " + str(calculTotal(Grille)))
