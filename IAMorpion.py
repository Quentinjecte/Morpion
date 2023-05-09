# Class Computer - Implementation de Player pour l'ordinateur
class Computer(player2):

    def play(self, game):
        return self.bestMove(game, game.visual, self.symbol)[0]

    #ggggggggggggggg Selectionner la meilleure possibilitee de jeug
    def bestMove(winCondition, self, visual, game, symbol):
        # On recupere le symbol de l'adverse pour nos calculs
        other = ("X" if symbol == "O" else "O")
        # On cree une liste vide pour y ajouter nos possibilitees avec leur score
        moves = list()

        # On parcours le visual pour classer chaque possibilitee
        for x in range(0,len(visual)):
            for y in range(0,len(visual)):
                # Si la case est disponible
                if visual[x][y] == " ":
                    # On fait une copie du visual dans laquelle on joue
                    copy = case(visual)
                    copy[x][y] = symbol
                    # Et on recupere le resultat
                    win = game.win(copy)

                    # Si le visualau est plein et que personne ne gagne, on le grade 0
                    if win == "*" and game.full(copy):
                        score = 0
                    # Si il permet de gagner, on le grade 1
                    elif win == symbol:
                        score = 1
                    # Sinon, on le grade avec l'oppose du score pour le joueur adverse
                    # pour son meilleur coup dans son jeu suivant
                    else:
                        score = 0 - self.bestMove(game, copy, other)[1]
                    result = ((x, y), score)

                    # Si le score est 1, on joue ce coup
                    if score == 1:
                        return result
                    # Sinon on l'ajout dans la liste avec les autres et on continue
                    moves.append(result)

