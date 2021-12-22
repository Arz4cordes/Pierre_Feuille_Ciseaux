"""
Hello world !
This is my version of the famous Rock Paper Scissors.
You can play with the computer every round you want,
and when you quit the game, final score will be displayed
Have fun with this simple game,
and Python Forever !
by Arz 4C, 2021
"""

import random as rnd
import time


phrases_player_wins = ["Mais c'est du pur hasard",
                       "Comment as vous avez deviné ce que j'allais faire ?",
                       "L'IA n'est pas encore prête à dominer ce monde...",
                       "Votre choix était judicieux.",
                       "Mais ne prenez pas trop la confiance...",
                       "Pourtant j'ai tout donné sur ce coup.",
                       "Quelle partie captivante, vous êtes coriace...",
                       "Je voulais choisir comme vous, \
                        je n'aurai pas dû hésiter.",
                       "Ce n'est que partie remise. Je veux ma revanche !",
                       "Il fait beau aujoud'hui n'est-il pas ?"]
phrases_ia_wins = ["Les PC sont les meilleurs !!",
                   "Tu as choisi... bien mal...",
                   "Pauvre simple humain...",
                   "Vous ne croyez pas pouvoir me battre comme ça",
                   "Inutile de résister, ma carte mère \
                    tourne à plein régime !",
                   "Mes processeurs ont bien chauffés sur ce coup là",
                   "Vous ne passerez... pas !",
                   "Ce jeu, whaou... C'est de toute beauté.",
                   "Je suis au top, là.",
                   "Je savais ce que vous alliez faire ce choix, \
                    #ImInYourMind"]

choices = ["pierre", "feuille", "ciseau"]


def user_choice():
    """
    demande à l'utilisateur de choisir pierre, feuille ou ciseau
    puis valide le choix ou relance la question
    :return: 1, 2, ou 3 au foramt str
    """
    answer = "un numéro"
    while answer not in ["1", "2", "3"]:
        print("\nVeuillez choisir en tapant le numéro correspondant:")
        print("1) Pierre")
        print("2) Feuille")
        print("3) Ciseau")
        answer = input()
    return answer


def compare_choices(answer, ia_choice):
    """ compare les résultats des deux joueurs
    :param: answer1 et answer2 sont du type int
    et valent 1, 2 ou 3
    :return: answer est du type int
    answer vaut 1 si answer est gagnant
    answer vaut 0 en cas de match nul
    answer vaut -1 si ia_choice est gagnant
    """
    cond1 = (answer == 1) and (ia_choice == 3)
    cond2 = (answer == 2) and (ia_choice == 1)
    cond3 = (answer == 3) and (ia_choice == 2)
    expected_list = [1, 2, 3]
    cond4 = (answer in expected_list) and (ia_choice in expected_list)
    if (answer == ia_choice) or (not cond4):
        winner = 0
    elif cond1 or cond2 or cond3:
        winner = 1
    else:
        winner = -1
    return winner


def game_result(user_score, ia_score, winner):
    """
    imprime une ou plusieurs phrases en fonction du résultat du match
    ajoute un point au joueur si il a gagné la manche,
    ou ajoute un point à l'IA si il a gagné la manche
    :param: winner est un int qui vaut -1, 0 ou 1
            user_score et ia_score sont des int
    :return: les valeurs ia_score et user_score (type int) mises à jour
    """
    if winner == 0:
        print("\nMatch nul ! Le score total de chacun de change pas...")
    elif winner == 1:
        print("\nVous gagnez cette manche ! Bien joué !")
        phrase = rnd.choice(phrases_player_wins)
        print(phrase)
        print("Vous marquez un point.")
        user_score += 1
    elif winner == -1:
        phrase = rnd.choice(phrases_ia_wins)
        print("\nJe gagne." + phrase)
        print("J'augmente mon score de 1.")
        ia_score += 1
    else:
        print("\n Erreur dans la gestion des scores,")
        print("les scores de chacun restent inchangés")
    if user_score > 1:
        text = f"Le score actuel est de {user_score} points pour vous"
        text += f" et de {ia_score} pour ce PC."
        print(text)
    else:
        text = f"Le score actuel est de {user_score} point pour vous"
        text += f" et de {ia_score} pour ce PC."
        print(text)
    return user_score, ia_score


def new_game(user_score, ia_score):
    """
    lance la fonction user_choice,
    transforme le choix validé du user en type int,
    puis effectue le choix de l'IA,
    lance la fonction qui compare les résultats des 2 joueurs,
    et enfin lance la fonction de mise à jour des scores
    :return: les valeurs ia_score et user_score (type int) mises à jour
    """
    try:
        answer = int(user_choice())
        print("\nVous avez choisi: ")
        choice = choices[answer - 1]
        print(choice)
        # choix de l'IA
        ia_choice = rnd.randint(1, 3)
        print("\nJe fais mon choix,\n")
        for i in range(1, 4):
            print(f"{i}...")
            time.sleep(1)
        choice = choices[ia_choice - 1]
        print(f"{choice} \n")
        # lance la fonction compare_choice pour déterminer l'éventuel gagnant
        winner = compare_choices(answer, ia_choice)
        # lance la fonction game_result pour calculer les nouveaux scores
        user_score, ia_score = game_result(user_score, ia_score, winner)
    except ValueError:
        print("Erreur dans la récupération du choix de l'utilisateur")
        print("Les scores de chacun restent inchangés")
    return user_score, ia_score


def end_game(user_score, ia_score):
    print("Merci d'avoir joué.")
    if user_score > 1:
        text = f"Le score final est de {user_score} points pour vous"
        text += f" et de {ia_score} pour ce PC."
        print(text)
    else:
        text = f"Le score final est de {user_score} point pour vous"
        text += f"et de {ia_score} pour ce PC."
        print(text)


def main():
    """
    fonction principale
    définit la liste des choix pierre, feuille, ciseau,
    puis lance la boucle pour jouer plusieurs parties,
    affiche les scores finaux lorsque la boucle est terminée
    """
    user_score = 0
    ia_score = 0
    again = "rejouer ou non"
    print("\nBienvenue dans le jeu de Pierre-Feuille-Ciseau.")
    while not (again.lower() == "n"):
        # lancement d'une partie avec la fonction new_game
        user_score, ia_score = new_game(user_score, ia_score)
        again = "rejouer ou non"
        while again.lower() not in ["o", "n"]:
            print("\nVoulez-vous faire une partie (répondez O ou N) ?")
            again = input()
    end_game(user_score, ia_score)


if __name__ == "__main__":
    main()
