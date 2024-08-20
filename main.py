from random import randint
import array as arr

def lancerDe():
    de = randint(1,6)
    return de

def compter(Tab,Nb):
    points = 0
    for Number1 in range(0, len(Tab)):
        if Number1 == Nb :
          points = points + Nb
    return points

if __name__ == '__main__':
    Name = input('Entre ton nom  : ')
    Grille = [Name, "X", "X", "X", "X", "X", "X"]
    print('Voici ta grille de Yams de ' + Name)
    for Number in range(1,len(Grille)):
        print(str(Grille[Number]))

    tabDes = [lancerDe(), lancerDe(), lancerDe(), lancerDe(), lancerDe()]
    print('Tu lances les dés, et tu obtiens : ')
    print (str(tabDes[0]) + ' / ', str(tabDes[1]) + ' / ', str(tabDes[2]) + ' / ', str(tabDes[3]) + ' / ', str(tabDes[4]))
    print ('Que fais tu ?')
    choix1 = input()
    if choix1 =='1':
        print(compter(tabDes,1))
    else:
        print('mauvais choix!')
