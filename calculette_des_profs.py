def affiche_terminal(reg):
    print(reg)


def saisit_terminal():
    return input('> ')


def est_chiffre(entree):
    """Renvoie True si chaine est un chiffre, False sinon.
    exemple :
    >>> est_chiffre('*')
    False
    >>> est_chiffre('3')
    True
    """
    return len(entree) == 1 and '0' <= entree <= '9'
    # ou :
    # return entree in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']


def est_operateur(entree):
    """Renvoie True si chaine est un opérateur (+, -, * ou d), False sinon.
    exemple :
    >>> est_operateur('*')
    True
    >>> est_operateur('3')
    False
    """
    return (entree == '+'
            or entree == '-'
            or entree == '*'
            or entree == 'd')
    # ou :
    # return entree in ['+', '-', '*', 'd']


def complete_entier(entier, chiffre):
    """Ajoute c comme nouveau chiffre des unités à n, en décalant les autres
    chiffres vers la gauche.
    exemple :
    >>> complete_entier(13, 4)
    134
    """
    return entier * 10 + chiffre


def calcule(a, op, b):
    """Renvoie le résultat de l'opération op appliquée aux opérandes a et b.
    Attention, la division effectuée est la division entière.
    exemple :
    >>> calcule(3, '+', 4)
    7
    >>> calcule(13, 'd', 4)
    3
    """
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    elif op == 'd':
        return a // b
    else:
        return 'ERROR'
    # ou :
    # op = '//' if op == 'd' else op
    # return eval(str(a) + op + str(b))


def calculette(saisie=saisit_terminal, affichage=affiche_terminal):
    # initialisation de l'état de la calculatrice
    X = Y = 0
    OP = '+'
    entree = ''
    # est-on sur le point de saisir un nouveau nombre ?
    attente_nombre = True

    # boucle principale de traitement de l'entrée
    while entree != 'q':
        # print('X = {:<8} Y = {:<8} op = {}'.format(X, Y, OP))
        affichage(X)
        entree = saisie()
        if est_chiffre(entree):
            if attente_nombre:
                Y = X
                X = 0
                attente_nombre = False
            X = complete_entier(X, int(entree))
        elif est_operateur(entree):
            if not attente_nombre:
                X = calcule(Y, OP, X)
                attente_nombre = True
            OP = entree
        elif entree == '=':
            if not attente_nombre:
                X = calcule(Y, OP, X)
                attente_nombre = True
                OP = '+'
                Y = 0
        elif entree != 'q':
            print('saisie incorrecte')

if __name__ == '__main__':
    message_aide = """
    ------------------------------------------------
    Fonctionnement de la calculette.
    Sur chaque ligne, les saisies possibles sont :
    - chiffre (0 à 9) : construit un nombre entier
    - opération (+, -, *, d) : opération suivante
    - signe égal (=) : fin du calcul
    - lettre q : quitte le programme
    ------------------------------------------------
    """

    print(message_aide)
    calculette()
