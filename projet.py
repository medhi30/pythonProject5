# faire list animeaux
# ajouter la list
# supprime la list
# modifier la list
# le chef de projet et Romain
# list : lion, zebre, pinguin, hippopotame, girafe
#



def ajouterAnimeaux(nom, race, sexe, age, pays, list):
    list.append([nom, race, sexe, age, pays, list])
    afficherAnimeaux(list)
    return list




def menuAjoutAnimeaux(list):
    print("Quel est votre nom ?")
    nom = input()
    print("Quel est votre race ?")
    race = input()
    print("Quel est votre sexe ?")
    sexe = input()
    print("Quel est votre age")
    age = input()
    print("De quel pays venez-vous")
    pays = input()

    list = ajouterAnimeaux(nom, race, sexe, age, pays, list)

    return list




def afficherAnimeaux(list):
    print(list)






def remplacerAnimeaux(list):
    print(list)




def update(list):
    print(list)



def menusupp(list):
    print("Quel animal voulez vous supprimer ?")
    nom = input()
    for i in range(len(list)):
        if list[i][0] == nom:
            confirmation(i)



def confirmation(i):
    print(list[i])
    print ("Confirmez la suppression y/n")
    choix = input()
    if choix == "y":
        del list[i]
        return list
    elif choix == "n":
        menu()





def supprimerAnimeaux(list):
    print(list)






def menu():#menu principal
    list = []
    print("Bienvenue au zoo TSSR, vous disposez de plusieurs choix pour gÃ©rer vos animaux :")
    flag = True
    while flag:
        print(" 1 : Ajouter Animal")
        print(" 2 : Supprimer Animal")
        print(" 3 : Afficher liste")
        print(" 4 : Remplacer")
        print(" 5 : Modifier")
        print(" 6 : exit")

        choix = input()
        match choix:
            case "1":
                list = menuAjoutAnimeaux(list)
            case "2":
                list = menusupp(list)
            case "3":
                list = afficherAnimeaux(list)
            case "4":
                list = remplacerAnimeaux(list)
            case "5":
                list = update(list)
            case"6":
                flag = False
            case _:
                print("erreur de saisie")
                menu()

def main():
    menu()



if __name__ == '__main__':
    main()


