"""
BTS SIO 1 - Python
Cours 02 : manipulation et formatage des chaînes de caractères

Objectifs :
- concaténer du texte ;
- insérer des valeurs avec format() et les f-strings ;
- comprendre la mini-langue de formatage ;
- formater chaînes, entiers et flottants ;
- comprendre les bases décimale, binaire, octale et hexadécimale ;
- utiliser les arrondis round(), ceil() et floor().

Chaque exemple affiché comporte son résultat attendu en commentaire.
"""

import math


# ============================================================
# 1. CONCATÉNATION DE CHAÎNES DE CARACTÈRES
# ============================================================

un_nombre = 25
un_texte = "Test de texte"

# L'opérateur + concatène deux chaînes.
# Comme un_nombre est un int, il faut d'abord le convertir avec str().
un_resultat = un_texte + str(un_nombre)
print(un_resultat)                   # Résultat attendu : Test de texte25

# On peut ajouter soi-même un espace dans la chaîne :
un_resultat_espace = un_texte + " " + str(un_nombre)
print(un_resultat_espace)            # Résultat attendu : Test de texte 25


# ============================================================
# 2. INSÉRER DES VARIABLES DANS UNE CHAÎNE
# ============================================================

mon_genre = "Garçon"
mon_age = 14

# Méthode historique avec str.format() :
ma_chaine_formatee = "Je suis un {0} et j'ai {1} ans !".format(mon_genre, mon_age)
print(ma_chaine_formatee)            # Résultat attendu : Je suis un Garçon et j'ai 14 ans !

# Méthode moderne recommandée : la f-string.
# On ajoute f devant la chaîne puis on place les variables entre { }.
ma_chaine_formatee2 = f"Je suis un {mon_genre} et j'ai {mon_age} ans !"
print(ma_chaine_formatee2)           # Résultat attendu : Je suis un Garçon et j'ai 14 ans !


# ============================================================
# 3. MINI-LANGUE DE FORMATAGE : VUE D'ENSEMBLE
# ============================================================

"""
Syntaxe générale simplifiée :

{valeur:[remplissage][alignement][signe][#][0][largeur][,][.precision][type]}

Les éléments entre crochets sont optionnels.

- remplissage : caractère utilisé pour remplir l'espace disponible.
  Il se place juste avant un symbole d'alignement.
  Exemple : *^10 signifie « centrer et remplir avec * ».

- alignement :
  <  : alignement à gauche
  >  : alignement à droite
  ^  : centrage

- signe : utilisé avec les nombres.
  +       : affiche toujours le signe (+ ou -).
  -       : n'affiche que le signe des nombres négatifs (comportement usuel).
  espace  : affiche un espace devant les positifs et - devant les négatifs.
            L'espace occupe la place qu'occuperait le signe - et facilite
            l'alignement de nombres positifs et négatifs en colonne.

- # : ajoute le préfixe permettant d'identifier la base numérique :
  0b pour le binaire, 0o pour l'octal, 0x pour l'hexadécimal.
  IMPORTANT : # ne choisit pas la base. Ce sont b, o, x ou X qui choisissent
  l'affichage. # ajoute seulement le préfixe qui rend la base plus visible.

- 0 : placé avant la largeur, comme 05d, complète un nombre par des zéros
  à gauche. Exemple : 42 formaté en 05d devient 00042.
  Pour utiliser 0 comme caractère de remplissage avec un autre alignement,
  on écrit explicitement 0<, 0^ ou 0>.

- largeur : largeur MINIMALE du champ. Si le contenu est plus long, Python
  ne le coupe pas automatiquement : le champ s'agrandit.

- , : ajoute un séparateur de milliers selon la convention anglo-saxonne.
  Exemple : 1234567 devient 1,234,567.

- .precision :
  avec f : nombre de chiffres après la virgule ;
  avec s : nombre maximal de caractères affichés.

- type : indique comment afficher la valeur.
  f : flottant en notation fixe
  e : notation scientifique
  g : notation compacte
  d : entier décimal
  s : chaîne de caractères
  b : entier en binaire
  o : entier en octal
  x : entier en hexadécimal (a-f en minuscules)
  X : entier en hexadécimal (A-F en majuscules)
  % : pourcentage
"""


# ============================================================
# 4. PRÉCISION DES FLOTTANTS
# ============================================================

# .2f signifie : afficher le flottant avec exactement 2 décimales.
ma_chaine_formatee3 = "Ma moyenne est de {0:.2f} / 20".format(14.4999)
print(ma_chaine_formatee3)           # Résultat attendu : Ma moyenne est de 14.50 / 20

ma_chaine_formatee4 = f"Ma moyenne est de {14.5:.2f} / 20"
print(ma_chaine_formatee4)           # Résultat attendu : Ma moyenne est de 14.50 / 20

pi = 3.14159265
print(f"{pi:.3f}")                  # Résultat attendu : 3.142
print(f"{pi:.0f}")                  # Résultat attendu : 3

# L'affichage est arrondi à la précision demandée.


# ============================================================
# 5. LARGEUR, ALIGNEMENT ET REMPLISSAGE
# ============================================================

# Une largeur est une largeur MINIMALE.
print(f"|{25:6}|")                  # Résultat attendu : |    25|
print(f"|{4.99:15.1f}|")            # Résultat attendu : |            5.0|

# Alignement des chaînes :
mot = "Python"
print(f"|{mot:<8s}|")               # Résultat attendu : |Python  |
print(f"|{mot:^8s}|")               # Résultat attendu : | Python |
print(f"|{mot:>8s}|")               # Résultat attendu : |  Python|

# Remplissage personnalisé :
print(f"|{mot:.^10s}|")             # Résultat attendu : |..Python..|
print(f"|{42:*^8d}|")               # Résultat attendu : |***42***|

# Si la valeur dépasse la largeur minimale, elle n'est pas tronquée :
print(f"|{'SuperLongMot':4s}|")      # Résultat attendu : |SuperLongMot|


# ============================================================
# 6. TRONQUER UNE CHAÎNE
# ============================================================

mon_mot = "Pierre"
print(f"{mon_mot:.3s}")             # Résultat attendu : Pie

# Le slicing [début:fin] prend les caractères depuis l'indice « début »
# inclus jusqu'à l'indice « fin » exclu.
print(mon_mot[2:4])                  # Résultat attendu : er




# ============================================================
# 6 bis. MODIFIER LA CASSE D'UNE CHAÎNE : MAJUSCULES ET MINUSCULES
# ============================================================

texte = "PyThOn pour les BTS SIO"

# upper() met tous les caractères alphabétiques en MAJUSCULES.
print(texte.upper())                    # Résultat attendu : PYTHON POUR LES BTS SIO

# lower() met tous les caractères alphabétiques en minuscules.
print(texte.lower())                    # Résultat attendu : python pour les bts sio

# capitalize() met le premier caractère de la chaîne en majuscule
# et le reste de la chaîne en minuscules.
phrase = "bONJOUR LES ÉLÈVES"
print(phrase.capitalize())              # Résultat attendu : Bonjour les élèves

# title() met en majuscule le premier caractère de chaque mot
# et met les autres caractères de chaque mot en minuscules.
nom_complet = "dAVID dONISA"
print(nom_complet.title())              # Résultat attendu : David Donisa

# IMPORTANT : les chaînes de caractères (str) sont immuables en Python.
# Les méthodes upper(), lower(), capitalize() et title()
# ne modifient donc pas la chaîne d'origine : elles renvoient une NOUVELLE chaîne.
message = "Bonjour"
message.upper()
print(message)                          # Résultat attendu : Bonjour

# Pour conserver la transformation, il faut réaffecter le résultat à une variable.
message = message.upper()
print(message)                          # Résultat attendu : BONJOUR

# On peut aussi appliquer directement ces méthodes à une chaîne littérale.
print("python".upper())                 # Résultat attendu : PYTHON
print("PYTHON".lower())                 # Résultat attendu : python

# Cas d'usage classique : normaliser une saisie utilisateur avant une comparaison.
# Exemple : quelle que soit la casse saisie par l'utilisateur, on compare en minuscules.
reponse = "OuI"
print(reponse.lower())                  # Résultat attendu : oui

# À RETENIR :
# upper()      -> tout en MAJUSCULES
# lower()      -> tout en minuscules
# capitalize() -> première lettre de la chaîne en majuscule, reste en minuscules
# title()      -> première lettre de chaque mot en majuscule
#
# ATTENTION À title() AVEC LES NOMS PROPRES :
#
# title() applique une règle purement mécanique : Python considère les débuts
# de mots et met leur première lettre en majuscule, puis les lettres suivantes
# en minuscules. Python ne sait pas qu'une chaîne représente un vrai nom de
# personne et il ne connaît pas les conventions particulières de ce nom.
#
# Exemple 1 : certaines particules d'un nom peuvent devoir rester en minuscules.
nom_avec_particule = "marie de la tour"
print(nom_avec_particule.title())       # Résultat attendu : Marie De La Tour
# Or, selon le nom réel et la convention souhaitée, on peut vouloir écrire :
# Marie de la Tour
# title() ne peut pas deviner que "de" et "la" doivent éventuellement rester
# en minuscules.
#
# Exemple 2 : certains noms possèdent une majuscule à l'intérieur du mot.
nom_complexe = "mcdonald"
print(nom_complexe.title())             # Résultat attendu : Mcdonald
# Or le nom peut devoir s'écrire : McDonald
# title() ne connaît pas cette règle particulière et transforme seulement le
# premier caractère du mot en majuscule.
#
# À RETENIR :
# title() est pratique pour présenter rapidement un texte sous la forme
# "Première Lettre De Chaque Mot En Majuscule", mais il ne faut pas considérer
# son résultat comme forcément correct pour des noms de personnes, de lieux ou
# des marques. Pour des données réelles, il peut être nécessaire de conserver
# l'orthographe saisie ou d'appliquer des règles spécifiques.


# ============================================================
# 7. LE SIGNE : +, - ET ESPACE
# ============================================================

n_positif = 25
n_negatif = -25

# + : affiche toujours le signe.
print(f"{n_positif:+d}")            # Résultat attendu : +25
print(f"{n_negatif:+d}")            # Résultat attendu : -25

# - : affiche le signe uniquement si le nombre est négatif.
print(f"{n_positif:-d}")            # Résultat attendu : 25
print(f"{n_negatif:-d}")            # Résultat attendu : -25

# Un ESPACE comme option de signe réserve une position devant les positifs.
# Cela permet d'aligner visuellement positifs et négatifs en colonne.
print(f"|{n_positif: d}|")          # Résultat attendu : | 25|
print(f"|{n_negatif: d}|")          # Résultat attendu : |-25|


# ============================================================
# 8. LE ZÉRO : REMPLISSAGE NUMÉRIQUE ET ALIGNEMENT
# ============================================================

n = 42

# 05d : entier décimal, largeur 5, complété par des zéros à gauche.
print(f"{n:05d}")                   # Résultat attendu : 00042

# Le 0 placé de cette manière sert au remplissage numérique à gauche.
# Pour remplir ailleurs, on utilise 0 comme caractère de remplissage
# AVANT le symbole d'alignement :
print(f"{n:0<7d}")                  # Résultat attendu : 4200000
print(f"{n:0^7d}")                  # Résultat attendu : 0042000
print(f"{n:0>7d}")                  # Résultat attendu : 0000042

# Lecture de 0^7d :
# 0 = caractère de remplissage
# ^ = centrage
# 7 = largeur minimale
# d = entier décimal


# ============================================================
# 9. SÉPARATEUR DE MILLIERS : ,
# ============================================================

print(f"{1234567:,d}")              # Résultat attendu : 1,234,567
print(f"{1234567.0:,.2f}")          # Résultat attendu : 1,234,567.00

# Remarque : la virgule est ici le séparateur de milliers de la convention
# anglo-saxonne. Ce n'est pas nécessairement la présentation française usuelle.


# ============================================================
# 10. BASES NUMÉRIQUES : DÉCIMAL, BINAIRE, OCTAL, HEXADÉCIMAL
# ============================================================

"""
Nous utilisons habituellement le système DÉCIMAL (base 10), avec 10 chiffres :
0 1 2 3 4 5 6 7 8 9

En informatique, on rencontre aussi :

1) BINAIRE - base 2
   Chiffres disponibles : 0 et 1.
   Chaque position représente une puissance de 2.
   Exemple : 101010 en binaire = 42 en décimal.
   Le binaire est fondamental car l'information informatique est représentée
   à l'aide de bits, généralement modélisés par 0 et 1.

2) OCTAL - base 8
   Chiffres disponibles : 0 à 7.
   Exemple : 52 en octal = 42 en décimal.
   On rencontre encore l'octal, notamment dans certains contextes Unix/Linux.

3) HEXADÉCIMAL - base 16
   Symboles disponibles : 0 à 9 puis A, B, C, D, E, F.
   A=10, B=11, C=12, D=13, E=14, F=15.
   Exemple : 2A en hexadécimal = 42 en décimal.
   L'hexadécimal est très utilisé en informatique : couleurs HTML/CSS,
   adresses mémoire, représentation d'octets, analyse bas niveau, etc.

IMPORTANT : 42, 101010 (base 2), 52 (base 8) et 2A (base 16)
peuvent représenter exactement la MÊME VALEUR dans des bases différentes.
"""

n = 42

# d = decimal (base 10)
print(f"{n:d}")                     # Résultat attendu : 42

# b = binary (binaire, base 2)
print(f"{n:b}")                     # Résultat attendu : 101010

# o = octal (base 8)
print(f"{n:o}")                     # Résultat attendu : 52

# x = hexadecimal en minuscules ; X = hexadecimal en majuscules.
print(f"{n:x}")                     # Résultat attendu : 2a
print(f"{n:X}")                     # Résultat attendu : 2A


# ============================================================
# 11. LE SYMBOLE # : AFFICHER LE PRÉFIXE DE LA BASE
# ============================================================

# Sans #, on voit la représentation mais pas son « étiquette » de base :
print(f"{n:b}")                     # Résultat attendu : 101010
print(f"{n:o}")                     # Résultat attendu : 52
print(f"{n:x}")                     # Résultat attendu : 2a

# Avec #, Python ajoute un préfixe reconnaissable :
print(f"{n:#b}")                    # Résultat attendu : 0b101010
print(f"{n:#o}")                    # Résultat attendu : 0o52
print(f"{n:#x}")                    # Résultat attendu : 0x2a
print(f"{n:#X}")                    # Résultat attendu : 0X2A

# À RETENIR :
# b, o, x ou X choisissent la base d'affichage.
# # ne change PAS la base ; il ajoute seulement son préfixe :
# 0b = binaire ; 0o = octal ; 0x/0X = hexadécimal.


# ============================================================
# 12. NOTATION SCIENTIFIQUE ET COMPACTE
# ============================================================

grand = 1234567.0
print(f"{grand:.3e}")               # Résultat attendu : 1.235e+06
print(f"{grand:.6g}")               # Résultat attendu : 1.23457e+06

# e = notation scientifique.
# g = choisit une représentation compacte selon la valeur et la précision.


# ============================================================
# 13. POURCENTAGE
# ============================================================

taux = 0.0765
print(f"{taux:.2%}")                # Résultat attendu : 7.65%

# % multiplie la valeur par 100 pour l'affichage et ajoute le symbole %.


# ============================================================
# 14. ARRONDIS : round(), ceil() ET floor()
# ============================================================

# ceil() = plafond : plus petit entier supérieur ou égal au nombre.
print(math.ceil(1.1))                # Résultat attendu : 2
print(math.ceil(-1.1))               # Résultat attendu : -1

# floor() = plancher : plus grand entier inférieur ou égal au nombre.
print(math.floor(1.9))               # Résultat attendu : 1
print(math.floor(-1.1))              # Résultat attendu : -2

# round() utilise en Python la règle dite « ties to even » pour les .5 exacts :
# lorsque deux entiers sont à égale distance, Python choisit l'entier pair.
print(round(1.5))                    # Résultat attendu : 2
print(round(2.5))                    # Résultat attendu : 2
print(round(3.5))                    # Résultat attendu : 4
print(round(4.5))                    # Résultat attendu : 4
print(round(5.5))                    # Résultat attendu : 6
print(round(-1.5))                   # Résultat attendu : -2
print(round(-2.5))                   # Résultat attendu : -2

# Cette règle évite qu'une grande quantité de valeurs terminant exactement
# par .5 soit systématiquement arrondie dans le même sens.


# ============================================================
# 15. POINT IMPORTANT POUR LE VIBE CODING / L'IA
# ============================================================

# Une IA peut générer une f-string sophistiquée qui « fonctionne » sans que
# l'étudiant comprenne :
# print(f"{42:#08x}")
#
# Un informaticien doit savoir la lire :
# #  -> préfixe de base
# 0  -> remplissage numérique par zéros
# 8  -> largeur minimale
# x  -> hexadécimal minuscule
#
print(f"{42:#08x}")                 # Résultat attendu : 0x00002a
