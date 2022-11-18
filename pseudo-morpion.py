#Importer la fonction random

#declarer grille en tant que list
#ajouter a grille la list (1,2,3)
#ajouter a grille la list (4,5,6)
#ajouter a grille la list (7,8,9)

#declarer visual en tant que list
#ajouter a visual ("","","")
#ajouter a visual ("","","")
#ajouter a visual ("","","")

#initiealiser winplayer1 a false
#initiealiser winplayer2 a false

#definir la fonction case pour parametre choix
    #si choix verifie 1
        #x egal 2
        #y egal 0
        #retourne x,y
    #sinon choix verifie 2
        #x egal 2
        #y egal 1
        #retourne x,y
    #sinon choix verifie 3
        #x egal 2
        #y egal 2
        #retourne x,y
    #sinon choix verifie 4
        #x egal 1
        #y egal 0
        #retourne x,y
    #sinon choix verifie 5
        #x egal 1
        #y egal 1
        #retourne x,y
    #sinon choix verifie 6
        #x egal 1
        #y egal 2
        #retourne x,y
    #sinon choix verifie 7
        #x egal 0
        #y egal 0
        #retourne x,y
    #sinon choix verifie 8
        #x egal 0
        #y egal 1
        #retourne x,y
    #sinon choix verifie 9
        #x egal 0
        #y egal 2
        #retourne x,y

#definir winCondition qui a pour parametre visual ,xchoix ,ychoix
    #si ychoix verifie 0
        #si la fonction visual qui a pour parametre xchoix et ychoix + 1 verifie la fonction visual pour parametre xchoix et ychoix ET la fonction visual qui a pour parametre xchoix et ychoix + 2 verifie la fonction visual pour parametre xchoix et ychoix 
            #retourner la fonction visual avec les parametre xchoix et y choix
    #sinon si ychoix verifie 1
        #si la fonction visual qui a pour parametre xchoix et ychoix + 1 verifie la fonction visual pour parametre xchoix et ychoix ET la fonction visual qui a pour parametre xchoix et ychoix + 2 verifie la fonction visual pour parametre xchoix et ychoix 
            #retourner la fonction visual avec les parametre xchoix et y choix
    #sinon si ychoix verifie 2
        #si la fonction visual qui a pour parametre xchoix et ychoix + 1 verifie la fonction visual pour parametre xchoix et ychoix ET la fonction visual qui a pour parametre xchoix et ychoix + 2 verifie la fonction visual pour parametre xchoix et ychoix 
            #retourner la fonction visual avec les parametre xchoix et y choix
    #si ychoix verifie 0
        #si la fonction visual qui a pour parametre xchoix + 1 et ychoix verifie la fonction visual pour parametre xchoix et ychoix ET la fonction visual qui a pour parametre xchoix + 2 et ychoix verifie la fonction visual pour parametre xchoix et ychoix 
            #retourner la fonction visual avec les parametre xchoix et y choix
    #sinon si ychoix verifie 1
        #si la fonction visual qui a pour parametre xchoix + 1 et ychoix verifie la fonction visual pour parametre xchoix et ychoix ET la fonction visual qui a pour parametre xchoix + 2 et ychoix verifie la fonction visual pour parametre xchoix et ychoix 
            #retourner la fonction visual avec les parametre xchoix et y choix
    #sinon si ychoix verifie 2
        #si la fonction visual qui a pour parametre xchoix + 1 et ychoix verifie la fonction visual pour parametre xchoix et ychoix ET la fonction visual qui a pour parametre xchoix + 2 et ychoix verifie la fonction visual pour parametre xchoix et ychoix 
            #retourner la fonction visual avec les parametre xchoix et y choix 
    #si xchoix verifie 1 et ychoix verifie 1
        #si visual pour parametre 0 et 0 verifie visual parametre xchoix et ychoix et visual pour parametre 2,2 verifie visual pour parametre 1,1
            #retourner visual parametre xchoix et ychoix
        #sinon si visual pour parametre 0 et 2 verifie visual parametre xchoix et ychoix et visual pour parametre 2,0 verifie visual pour parametre 1,1
            #retourner visual parametre xchoix et ychoix

#definir la fonction affichergrille
    #pour e allant de 0 a la valeur renvoyer par la fonction len(grille)
        #afficher la valeur de la jointur epour toutes valeur de grille transforme en string "print(" | ".join(str(e) for e in grille[i]))"

#definir la fonction affichervisual
     #pour e allant de 0 a la valeur renvoyer par la fonction len(visual)
        #afficher la valeur de la jointur epour toutes valeur de visual transforme en string "print(" | ".join(str(e) for e in visual[i]))"

#definir la fonction breaker
    #afficher "____________"

#definir la fonction breakertwo
    #afficher " "

#executer la fonction breaker
#afficher "Bienvenue dans le jeu du morpion !\n"
    #   "Règles du jeu :\n"
    #   "Pour gagner, il faut que vous aligner trois de vos symboles :\n"
    #   "  - Sur une même ligne\n"
    #   "  - Sur une même colonne\n"
    #   "  - Sur une même diagonale\n\n"
    #   "  - Voici la reference du visualleau"

#executer la fonction affichergrille
#executer breaker

#initaliser restart egal O
#initialiser player1 egal "prenom" : "", "symbole" : "X"
#initialiser player2 egal "prenom" : "", "symbole" : "O"

#tant que  winplayer1 verifie False et winplayer2 verifie False et restart verifie 'O'
    #executer player1 'prenom' egal a l'input "Entrez le prénom du joueur 1 : "
    #executer player2 'prenom' egal a l'input "Entrez le prénom du joueur 2 : "

#executer breaker

#afficher player1 'prenom',"tu joueras les X"
#afficher player2 'prenom',"tu joueras les O"
#afficher "Un tirage au sort va désigner le premier joueur..."
#initialiser turnPlayer egal a random.choise pour parametre player1 et player2

#executer breaker

#tant que vrai
    #afficher turnPlayer "prenom"," à ton tour !"
    #afficher "Reference du visualleau\n"
    #executer affichergrille
    #executer breakertwo
    #afficher turnPlayer "prenom"," à ton tour !"
    #executer breakertwo
    #afficher affichervisual

    #tant que vrai
        #initialier player1 egal a X
        #initialiser player2 egal a O

        #si turnPlayer verifie player1
            #executer choix egal string input "\nQuelle case souhaites-tu jouer ? "
            #x,y egal case parametre choix

            #tant que visual parametre x , y n'est pas egal a " "
                #afficher "\nCette case est deja prise"
                #executer choix egal string input "\nQuelle case souhaites-tu jouer ? "
                #x,y egal case parametre choix
                #executer visual parametre x , y egal a X
                #executer breakertwo
                #executer affichergrille
                #executer breakertwo
                #afficher affichervisual

                #si winCondition pour parametre visual ,x ,y verifie X
                    #executer winplayer1 egal vrai
                    #afficher "gg wp"
                    #casser
            
            #sinon
                #executer choix egal string input "\nQuelle case souhaites-tu jouer ? "
                #executer x, y egal case parametre choix

                    #tant que visual parametre x , y n'est pas egal a " "
                        #afficher "\nCette case est deja prise"
                        #executer choix egal string input "\nQuelle case souhaites-tu jouer ? "
                        #executer x,y egal case parametre choix
                    #executer visual parametre x , y egal a O
                    #executer breakertwo
                    #executer affichergrille
                    #executer breakertwo
                    #afficher affichervisual

                    #si winCondition pour parametre visual ,x ,y verifie O
                         #executer winplayer2 egal vrai
                        #afficher "gg wp"
                        #casser
            
                #si turnPlayer verifie player1
                    #turnPlayer egal player2
                #sinon
                    #turnPlayer egal player1
