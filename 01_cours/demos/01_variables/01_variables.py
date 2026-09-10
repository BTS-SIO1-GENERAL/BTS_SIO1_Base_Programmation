"""
BTS SIO 1 - Python
Cours 01 : les bases, les variables, les types et les entrées utilisateur

Objectifs :
- afficher du texte avec print() ;
- créer et modifier des variables ;
- reconnaître les principaux types ;
- comprendre que input() renvoie toujours une chaîne de caractères (str) ;
- convertir une valeur avec int(), float() ou str().

IMPORTANT : dans ce cours, chaque exemple d'affichage est accompagné du
résultat attendu en commentaire. Pour les exemples utilisant input(), le
résultat dépend évidemment de ce que saisit l'utilisateur ; un exemple de
saisie est donc indiqué.
"""


# ============================================================
# 1. PREMIER AFFICHAGE : print()
# ============================================================

print("Hello World")                 # Résultat attendu : Hello World
print('Hello World')                 # Résultat attendu : Hello World

# En Python, les guillemets doubles "..." et les apostrophes '...'
# permettent tous les deux de créer une chaîne de caractères (str).


# ============================================================
# 2. AFFECTATION DE VARIABLES
# ============================================================

# Une variable est un nom auquel on associe une valeur.
# Le symbole = est l'opérateur d'affectation : il stocke la valeur de droite
# dans la variable placée à gauche.

mon_texte = "Bla bla"               # Type : str ; valeur : Bla bla
mon_texte2 = 'Bla bla2'              # Type : str ; valeur : Bla bla2
mon_nombre = 25                      # Type : int ; valeur : 25
mon_nombre_virgule = 3.14            # Type : float ; valeur : 3.14
ma_variable = None                   # Type : NoneType ; signifie « absence de valeur »

# Attention : None n'est ni 0, ni "", ni False.
# C'est une valeur spéciale signifiant qu'aucune valeur utile n'est présente.


# ============================================================
# 3. COMMENTAIRES
# ============================================================

# Un commentaire commence par # et n'est pas exécuté par Python.
# Exemple :
# mon_texte = "Cette ligne n'est pas exécutée"

# Dans VS Code, pour commenter/décommenter plusieurs lignes sélectionnées,
# on peut utiliser le raccourci CTRL + /.


# ============================================================
# 4. CHAÎNES SUR PLUSIEURS LIGNES
# ============================================================

# Une chaîne peut s'étendre sur plusieurs lignes grâce à trois guillemets
# doubles ou trois apostrophes.

mon_texte3 = """Bonjour
Je m'appelle
David"""

mon_texte4 = '''Bonjour
Je m'appelle
DONISA'''

print(mon_texte3)
# Résultat attendu :
# Bonjour
# Je m'appelle
# David

print(mon_texte4)
# Résultat attendu :
# Bonjour
# Je m'appelle
# DONISA


# ============================================================
# 5. AFFICHAGE DE VARIABLES
# ============================================================

print("La variable mon_texte vaut :", mon_texte)
# Résultat attendu : La variable mon_texte vaut : Bla bla

print("La variable mon_texte2 vaut :", mon_texte2)
# Résultat attendu : La variable mon_texte2 vaut : Bla bla2

print(mon_nombre)                    # Résultat attendu : 25
print(mon_nombre_virgule)            # Résultat attendu : 3.14

print(mon_texte, mon_nombre, mon_nombre_virgule)
# Résultat attendu : Bla bla 25 3.14
# Lorsque plusieurs valeurs sont données à print(), Python les sépare
# par défaut par un espace.


# ============================================================
# 6. TYPE D'UNE VALEUR : type()
# ============================================================

print(type(mon_texte))               # Résultat attendu : <class 'str'>
print(type(mon_nombre))              # Résultat attendu : <class 'int'>
print(type(mon_nombre_virgule))      # Résultat attendu : <class 'float'>
print(type(ma_variable))             # Résultat attendu : <class 'NoneType'>

# Principaux types rencontrés au début du cours :
# str   : chaîne de caractères (texte)
# int   : nombre entier
# float : nombre à virgule
# bool  : booléen, True ou False
# NoneType : type de la valeur None


# ============================================================
# 7. RÉCUPÉRATION D'UNE SAISIE UTILISATEUR : input()
# ============================================================

# input() affiche un message, attend une saisie au clavier puis renvoie
# TOUJOURS une chaîne de caractères (str), même si l'utilisateur tape 25.

input_user = input("Veuillez entrer un nombre : ")
# Exemple de saisie utilisateur : 25
# Valeur obtenue dans input_user : "25" (texte, pas encore un entier)

print(input_user)
# Si l'utilisateur a saisi 25 -> Résultat attendu : 25

print(type(input_user))
# Si l'utilisateur a saisi 25 -> Résultat attendu : <class 'str'>


# ============================================================
# 8. CONVERSION DE TYPE (« CASTING »)
# ============================================================

# int() tente de convertir une valeur en entier.
# La chaîne "25" peut être convertie en entier 25.

input_en_nombre = int(input_user)

print(input_en_nombre)
# Si l'utilisateur a saisi 25 -> Résultat attendu : 25

print(type(input_en_nombre))
# Si l'utilisateur a saisi 25 -> Résultat attendu : <class 'int'>

# Autres conversions courantes :
texte_nombre = str(42)
print(texte_nombre)                  # Résultat attendu : 42
print(type(texte_nombre))            # Résultat attendu : <class 'str'>

nombre_decimal = float("3.5")
print(nombre_decimal)                # Résultat attendu : 3.5
print(type(nombre_decimal))          # Résultat attendu : <class 'float'>

# Attention : toutes les chaînes ne sont pas convertibles en nombre.
# int("bonjour") provoquerait une ValueError à l'exécution.


# ============================================================
# 9. CONVERSION DIRECTEMENT AU MOMENT DE LA SAISIE
# ============================================================

# On peut combiner input() et int() sur une même ligne.
input_user_2 = int(input("Veuillez entrer un nombre entier : "))
# Exemple de saisie utilisateur : 42
# input() produit d'abord "42", puis int("42") produit l'entier 42.

print(input_user_2)
# Si l'utilisateur a saisi 42 -> Résultat attendu : 42

print(type(input_user_2))
# Si l'utilisateur a saisi 42 -> Résultat attendu : <class 'int'>


# ============================================================
# 10. POINT IMPORTANT POUR LE VIBE CODING / L'IA
# ============================================================

# Une IA peut très facilement générer :
# age = input("Votre âge : ")
# if age >= 18:
#     print("Majeur")
#
# Ce code paraît plausible, mais il provoque une erreur car age est un str
# et 18 est un int. Le développeur doit comprendre les types pour contrôler
# le code produit par l'IA.
#
# Version correcte (qui sera étudiée avec les conditions) :
# age = int(input("Votre âge : "))
