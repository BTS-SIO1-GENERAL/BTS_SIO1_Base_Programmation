import math as mon_math  # On importe le module math avec l'alias mon_math.

# ============================================================
# BTS SIO 1 - Python
# Cours 03 : les opérateurs
# ============================================================
#
# Dans ce fichier, chaque affichage est accompagné de son résultat attendu.
# Les élèves n'ont pas encore étudié if : les expressions booléennes sont donc
# présentées ici comme des calculs produisant simplement True ou False.
# ============================================================


# ============================================================
# 1. LES OPÉRATEURS ARITHMÉTIQUES
# ============================================================

mon_resultat_a = 12 + 8  # Addition
print(mon_resultat_a)  # Résultat attendu : 20

mon_resultat_b = 12 - 8  # Soustraction
print(mon_resultat_b)  # Résultat attendu : 4

mon_resultat_c = 12 / 8  # Division classique : le résultat est un float.
print(mon_resultat_c)  # Résultat attendu : 1.5

mon_resultat_d = 12 * 8  # Multiplication
print(mon_resultat_d)  # Résultat attendu : 96

mon_resultat_cb = 12 // 8
# // réalise une DIVISION ENTIÈRE, plus précisément une division "plancher".
#
# DIFFÉRENCE ENTRE DIVISION RÉELLE ET DIVISION ENTIÈRE
#
# 1) DIVISION RÉELLE avec /
#    Python poursuit le calcul après la virgule afin d'obtenir un résultat réel
#    (en Python : un float).
#
#       12 / 8 -> 1.5
#
#    Pourquoi obtient-on 1.5 ?
#
#    Après avoir trouvé 1 comme partie entière, il reste 4 :
#
#       12 = 8 × 1 + 4
#
#    Dans une division réelle, on ne s'arrête PAS à ce reste 4.
#    On place une virgule dans le quotient puis on peut ajouter un zéro
#    au dividende : le reste 4 devient alors 40 dixièmes.
#
#       40 ÷ 8 = 5
#
#    On obtient donc :
#
#       12 ÷ 8 = 1.5
#
# 2) DIVISION ENTIÈRE avec //
#    La division entière cherche uniquement un quotient entier et un reste.
#
#       12 // 8 -> 1
#
#    Dès que tous les chiffres ENTIERS du dividende ont été utilisés,
#    on s'arrête. On n'ajoute PAS artificiellement de 0 après une virgule,
#    car cela ferait passer de la division entière à la division réelle.
#
#    Le reste 4 est donc conservé comme RESTE de la division euclidienne :
#
#       12 = 8 × 1 + 4
#
#    Ainsi :
#       quotient entier = 1
#       reste            = 4
#
# ============================================================
# RAPPEL : DIVISION POSÉE ET DIVISION EUCLIDIENNE
# ============================================================
#
# DÉTAIL DU CALCUL, comme dans une division posée :
#
# Présentation visuelle de la division posée (notation française) :
#
#        12 │ 8
#       - 8 │────
#       ─── │ 1
#         4 │
#
# Si l'on faisait une DIVISION RÉELLE, on pourrait continuer ainsi :
#
#        12,0 │ 8
#       - 8   │────
#       ───   │ 1,5
#         40  │
#       - 40  │
#       ───   │
#          0  │
#
# Mais pour la DIVISION ENTIÈRE, on s'arrête au reste 4.
#
# Lecture :
# - 12 est le dividende ;
# - 8 est le diviseur ;
# - 1 est le quotient entier ;
# - 4 est le reste.
#
# Étapes :
# 1) On cherche combien de fois 8 entre dans 12 sans dépasser 12.
#       8 × 1 = 8
#       8 × 2 = 16  → trop grand
#    On écrit donc 1 au quotient.
#
# 2) On calcule :
#       12 - 8 = 4
#
# 3) Il ne reste plus de chiffre à abaisser : 4 est donc le reste.
#
# On retrouve donc la division euclidienne :
#       12 = 8 × 1 + 4
#       dividende = diviseur × quotient + reste
#
# Donc :
#       12 // 8 = 1
#       12 % 8  = 4
#
print(mon_resultat_cb)  # Résultat attendu : 1
print(12 % 8)           # Résultat attendu : 4
print(12 / 8)           # Résultat attendu : 1.5


# RAPPEL :
# Une division euclidienne s'écrit toujours sous la forme :
#
#     dividende = diviseur × quotient + reste
#
# En Python, pour des entiers positifs :
#
#     quotient = dividende // diviseur
#     reste     = dividende % diviseur
#
# ------------------------------------------------------------
# DEUXIÈME EXEMPLE : 17 // 5
# ------------------------------------------------------------
#
# Présentation visuelle de la division posée (notation française) :
#
#        17 │ 5
#      - 15 │────
#      ──── │ 3
#         2 │
#
# Lecture :
# - 17 est le dividende ;
# - 5 est le diviseur ;
# - 3 est le quotient entier ;
# - 2 est le reste.
#
# Étapes :
# 1) On cherche combien de fois 5 entre dans 17 sans dépasser 17.
#       5 × 1 = 5
#       5 × 2 = 10
#       5 × 3 = 15
#       5 × 4 = 20  → trop grand
#    On écrit donc 3 au quotient.
#
# 2) On calcule :
#       17 - 15 = 2
#
# 3) Il ne reste plus de chiffre à abaisser : 2 est donc le reste.
#
# On retrouve la forme de la division euclidienne :
#
#       dividende = diviseur × quotient + reste
#       17         = 5        × 3        + 2
#
# Vérification du reste :
#       0 <= 2 < 5
#
# Donc :
#       17 // 5 = 3
#       17 % 5  = 2
#
mon_resultat_cb2 = 17 // 5
print(mon_resultat_cb2)  # Résultat attendu : 3
print(17 % 5)            # Résultat attendu : 2

# Comparaison avec la division réelle :
print(17 / 5)            # Résultat attendu : 3.4
#
# Pourquoi 3.4 avec / ?
# Après avoir trouvé 3, il reste 2 :
#
#     17 = 5 × 3 + 2
#
# La division réelle continue après la virgule :
# - le reste 2 devient 20 dixièmes ;
# - 20 ÷ 5 = 4.
#
# Donc :
#     17 / 5 = 3.4
#
# La division entière, elle, s'arrête dès que tous les chiffres entiers
# du dividende ont été utilisés :
#     17 // 5 = 3
#     17 % 5  = 2


# ============================================================
# DIVISION POSÉE À UN CHIFFRE
# Exemple : 632 divisé par 4
# ============================================================
#
# Ici, le DIVISEUR comporte un seul chiffre : 4.
#
# Instruction Python correspondante :
#
#     632 // 4
#
# Elle permet d'obtenir le quotient entier.
#
# Pour obtenir le reste :
#
#     632 % 4
#
# Présentation graphique de la division posée :
#
#       632 │ 4
#      - 4  │────
#      ───  │ 158
#       23  │
#      -20  │
#      ───  │
#        32 │
#      -32  │
#      ───  │
#         0 │
#
# DÉTAIL DES ÉTAPES :
#
# Étape 1 :
# - On commence par le premier chiffre du dividende : 6.
# - On cherche combien de fois 4 entre dans 6.
#
#       4 × 1 = 4
#       4 × 2 = 8  -> trop grand
#
# - On écrit donc 1 au quotient.
# - On soustrait :
#
#       6 - 4 = 2
#
# - On abaisse ensuite le chiffre suivant, 3.
# - On obtient alors 23.
#
# Étape 2 :
# - On cherche combien de fois 4 entre dans 23.
#
#       4 × 5 = 20
#       4 × 6 = 24  -> trop grand
#
# - On écrit donc 5 au quotient.
# - On soustrait :
#
#       23 - 20 = 3
#
# - On abaisse ensuite le chiffre suivant, 2.
# - On obtient alors 32.
#
# Étape 3 :
# - On cherche combien de fois 4 entre dans 32.
#
#       4 × 8 = 32
#
# - On écrit donc 8 au quotient.
# - On soustrait :
#
#       32 - 32 = 0
#
# Le quotient est donc 158 et le reste est 0.
#
# RAPPEL : principe de la division euclidienne
#
#     dividende = diviseur × quotient + reste
#
# Ici :
#
#     632 = 4 × 158 + 0
#
# Vérification du reste :
#
#     0 <= 0 < 4
#
# En Python :
quotient_un_chiffre = 632 // 4
reste_un_chiffre = 632 % 4

print(quotient_un_chiffre)  # Résultat attendu : 158
print(reste_un_chiffre)     # Résultat attendu : 0

# Comparaison avec la division réelle :
print(632 / 4)              # Résultat attendu : 158.0
#
# Ici, la division tombe juste : le reste final vaut 0.
# Il n'est donc pas nécessaire de poursuivre après la virgule.
#
# La différence est surtout le TYPE et le sens de l'opération :
# - 632 // 4 produit le quotient entier 158 ;
# - 632 / 4 produit le quotient réel 158.0 (float).
#
# Comme le reste est nul :
#     632 = 4 × 158 + 0


# ============================================================
# DIVISION POSÉE À DEUX CHIFFRES
# Exemple : 987 divisé par 23
# ============================================================
#
# Ici, le DIVISEUR comporte deux chiffres : 23.
#
# Instruction Python correspondante :
#
#     987 // 23
#
# Elle permet d'obtenir le quotient entier.
#
# Pour obtenir le reste :
#
#     987 % 23
#
# Présentation graphique de la division posée :
#
#       987 │ 23
#      - 92 │────
#      ──── │ 42
#        67 │
#      - 46 │
#      ──── │
#        21 │
#
# DÉTAIL DES ÉTAPES :
#
# Étape 1 :
# - Le diviseur est 23.
# - Le premier chiffre du dividende est 9.
# - 23 ne peut pas entrer dans 9.
# - On prend donc les deux premiers chiffres du dividende : 98.
#
# - On cherche combien de fois 23 entre dans 98.
#
#       23 × 4 = 92
#       23 × 5 = 115  -> trop grand
#
# - On écrit donc 4 au quotient.
# - On soustrait :
#
#       98 - 92 = 6
#
# - On abaisse ensuite le chiffre suivant, 7.
# - On obtient alors 67.
#
# Étape 2 :
# - On cherche combien de fois 23 entre dans 67.
#
#       23 × 2 = 46
#       23 × 3 = 69  -> trop grand
#
# - On écrit donc 2 au quotient.
# - On soustrait :
#
#       67 - 46 = 21
#
# - Il n'y a plus de chiffre à abaisser.
# - 21 est donc le reste.
#
# Le quotient est donc 42 et le reste est 21.
#
# RAPPEL : principe de la division euclidienne
#
#     dividende = diviseur × quotient + reste
#
# Ici :
#
#     987 = 23 × 42 + 21
#
# Vérification :
#
#     23 × 42 = 966
#     966 + 21 = 987
#
# Vérification du reste :
#
#     0 <= 21 < 23
#
# En Python :
quotient_deux_chiffres = 987 // 23
reste_deux_chiffres = 987 % 23

print(quotient_deux_chiffres)  # Résultat attendu : 42
print(reste_deux_chiffres)     # Résultat attendu : 21

# Comparaison avec la division réelle :
print(987 / 23)  # Résultat attendu : 42.91304347826087
#
# Pourquoi la division entière s'arrête-t-elle à 21 ?
#
# Parce que tous les chiffres entiers de 987 ont déjà été abaissés.
# En division entière, 21 reste donc le RESTE :
#
#     987 = 23 × 42 + 21
#
# On vérifie bien :
#     0 <= 21 < 23
#
# Avec la division réelle (/), on peut au contraire continuer après la virgule.
# On écrit alors 987,0 puis on transforme le reste 21 en 210 dixièmes :
#
#     210 ÷ 23 = 9, reste 3
#
# puis :
#     30 ÷ 23 = 1, reste 7
#
# puis :
#     70 ÷ 23 = 3, reste 1
#
# etc.
#
# C'est ainsi que l'on obtient progressivement :
#
#     987 / 23 = 42.91304347826087...
#
# À retenir :
# - // s'arrête avec un quotient ENTIER et un reste ;
# - / poursuit le calcul après la virgule pour produire un quotient réel.


# ============================================================
# À RETENIR : DIVISION RÉELLE / DIVISION ENTIÈRE
# ============================================================
#
# DIVISION RÉELLE : /
# - produit un résultat de type float ;
# - peut poursuivre le calcul après la virgule ;
# - lorsqu'il reste une valeur, on peut ajouter des zéros après la virgule
#   pour continuer la division.
#
# Exemple :
#     12 / 8 = 1.5
#
# DIVISION ENTIÈRE : //
# - cherche seulement le quotient entier ;
# - s'arrête quand tous les chiffres entiers du dividende ont été utilisés ;
# - le nombre qui reste devient le reste de la division euclidienne ;
# - on n'ajoute donc pas de zéro pour poursuivre après la virgule.
#
# Exemple :
#     12 // 8 = 1
#     12 % 8  = 4
#
# Dans une division euclidienne :
#
#     dividende = diviseur × quotient + reste
#
# Exemple :
#
#     12 = 8 × 1 + 4
#
# C'est précisément pour cette raison que, dans la division entière de 12 par 8,
# on s'arrête au reste 4 au lieu de transformer 4 en 40 :
# transformer 4 en 40 revient à poursuivre la division APRÈS LA VIRGULE,
# donc à effectuer une division réelle et non plus une division entière.
#
# ------------------------------------------------------------
# LIEN ENTRE /, // ET %
# ------------------------------------------------------------
#
# RAPPEL DU PRINCIPE DE LA DIVISION EUCLIDIENNE :
#
#     dividende = diviseur × quotient + reste
#
# En Python :
#
#     quotient = dividende // diviseur
#     reste     = dividende % diviseur
#
# Pour des nombres positifs :
#
#       /   donne le quotient avec sa partie décimale ;
#       //  donne le quotient entier ;
#       %   donne le reste.
#
# Exemple avec 17 et 5 :
print(17 / 5)   # Résultat attendu : 3.4
print(17 // 5)  # Résultat attendu : 3
print(17 % 5)   # Résultat attendu : 2
#
# Vérification :
#       5 × 3 + 2 = 17


# ATTENTION : // ne signifie pas toujours simplement
# "supprimer les chiffres après la virgule".
# Python effectue une division plancher : il arrondit vers -∞.
#
# Exemple avec un nombre négatif :
#
#       -12 / 8 = -1.5
#
# Les deux entiers voisins sont :
#
#       -1      et      -2
#
# Or -2 est inférieur à -1.5.
# Python choisit donc -2 :
#
print(-12 // 8)          # Résultat attendu : -2
#
# C'est pour cette raison que // est appelé opérateur de division plancher.

mon_resultat_e = 12 % 8
# % est le modulo : il donne le reste de la division euclidienne.
#
# RAPPEL : principe de la division euclidienne
# Pour deux entiers positifs a et b (avec b != 0), on peut écrire :
#
#     a = b × q + r
#
# avec :
#     a = dividende
#     b = diviseur
#     q = quotient entier
#     r = reste
#
# et le reste vérifie toujours :
#
#     0 <= r < b
#
# Exemple :
#     12 = 8 × 1 + 4
#
# Donc :
#     12 // 8 = 1   -> quotient entier
#     12 % 8  = 4   -> reste
print(mon_resultat_e)  # Résultat attendu : 4

mon_resultat_f = 12 ** 8
# ** signifie "élevé à la puissance".
# 12 ** 8 = 12 × 12 × 12 × 12 × 12 × 12 × 12 × 12
print(mon_resultat_f)  # Résultat attendu : 429981696

mon_resultat_g = "Fifi" + " " + "Nono"
# Avec des chaînes de caractères, + effectue une concaténation.
print(mon_resultat_g)  # Résultat attendu : Fifi Nono


# ============================================================
# 2. QUELQUES FONCTIONS DU MODULE math
# ============================================================

print("L'arrondi au supérieur de 1.9 vaut", mon_math.ceil(1.9))
# Résultat attendu : L'arrondi au supérieur de 1.9 vaut 2

print("L'arrondi de 1.9 vaut", round(1.9))
# Résultat attendu : L'arrondi de 1.9 vaut 2

print("L'arrondi à l'inférieur de 1.9 vaut", mon_math.floor(1.9))
# Résultat attendu : L'arrondi à l'inférieur de 1.9 vaut 1


# ============================================================
# 3. CONSTANTES COURANTES DU MODULE math
# ============================================================
#
# Le module math fournit plusieurs constantes utiles :
#
# +----------------+-----------------------------------------------------------+
# | Constante      | Signification                                             |
# +----------------+-----------------------------------------------------------+
# | mon_math.pi    | π ≈ 3.141592653589793 : cercle, trigonométrie, etc.       |
# | mon_math.e     | e ≈ 2.718281828459045 : exponentielle, logarithmes, etc.  |
# | mon_math.tau   | τ = 2π ≈ 6.283185307179586 : un tour complet en radians.  |
# | mon_math.inf   | +∞ : valeur flottante spéciale représentant l'infini.     |
# | mon_math.nan   | "Not a Number" : valeur flottante spéciale indéterminée.  |
# +----------------+-----------------------------------------------------------+
#
# IMPORTANT :
# mon_math.inf et mon_math.nan ont bien le TYPE float :
print(type(mon_math.inf))  # Résultat attendu : <class 'float'>
print(type(mon_math.nan))  # Résultat attendu : <class 'float'>
#
# Cependant, ce ne sont pas des nombres réels ordinaires :
# - inf représente une quantité plus grande que tout nombre flottant fini ;
# - nan représente une valeur numérique absente, invalide ou indéterminée.
#
# Ce sont des valeurs spéciales du format des nombres flottants utilisé
# notamment par Python (IEEE 754).

print("La valeur de PI est :", mon_math.pi)
# Résultat attendu : La valeur de PI est : 3.141592653589793

print("La valeur de e est :", mon_math.e)
# Résultat attendu : La valeur de e est : 2.718281828459045

print("La valeur de tau est :", mon_math.tau)
# Résultat attendu : La valeur de tau est : 6.283185307179586


# ------------------------------------------------------------
# math.inf ET math.nan : PEUT-ON LES MANIPULER COMME DES NOMBRES ?
# ------------------------------------------------------------
#
# Oui : math.inf et math.nan sont bien des valeurs de type float.
# Python permet donc de les utiliser dans des calculs, des comparaisons,
# des variables et certaines fonctions mathématiques.
#
# MAIS ce sont des valeurs flottantes SPÉCIALES :
#
# - math.inf représente l'infini positif ;
# - -math.inf représente l'infini négatif ;
# - math.nan signifie "Not a Number" et représente un résultat numérique
#   indéterminé ou invalide.
#
print(type(mon_math.inf))  # Résultat attendu : <class 'float'>
print(type(mon_math.nan))  # Résultat attendu : <class 'float'>


# ------------------------------------------------------------
# A. MANIPULER math.inf DANS DES CALCULS
# ------------------------------------------------------------
#
# L'infini peut participer à des opérations arithmétiques.
#
print(mon_math.inf + 100)  # Résultat attendu : inf
print(mon_math.inf * 2)    # Résultat attendu : inf
print(-mon_math.inf)       # Résultat attendu : -inf

# Un nombre fini est inférieur à +inf :
print(1_000_000 < mon_math.inf)  # Résultat attendu : True

# Et supérieur à -inf :
print(1_000_000 > -mon_math.inf)  # Résultat attendu : True

# Certaines opérations n'ont toutefois pas de résultat mathématique défini.
# Par exemple : inf - inf.
# Python renvoie alors nan :
print(mon_math.inf - mon_math.inf)  # Résultat attendu : nan


# ------------------------------------------------------------
# B. EXEMPLE CONCRET D'UTILISATION DE math.inf :
#    INITIALISER UNE RECHERCHE DE MINIMUM
# ------------------------------------------------------------
#
# Imaginons que l'on cherche la distance la plus courte.
# Avant d'avoir examiné la moindre distance, on peut considérer que
# la "meilleure distance" est infiniment grande.
#
meilleure_distance = mon_math.inf
print(meilleure_distance)  # Résultat attendu : inf

# Toute distance réelle raisonnable sera alors plus petite :
distance_1 = 350
print(distance_1 < meilleure_distance)  # Résultat attendu : True

# Plus tard, lorsqu'ils auront étudié les boucles et les conditions,
# les élèves pourront utiliser ce principe pour rechercher un minimum.
#
# Idée future :
#
# meilleure_distance = math.inf
# pour chaque distance :
#     si distance < meilleure_distance :
#         meilleure_distance = distance
#
# math.inf évite ainsi de devoir inventer une valeur initiale arbitraire
# comme 999999999.


# ------------------------------------------------------------
# C. AUTRE EXEMPLE CONCRET DE math.inf :
#    REPRÉSENTER UNE ABSENCE DE LIMITE
# ------------------------------------------------------------
#
# Exemple conceptuel : une durée maximale qui n'a pas encore de limite.
duree_maximale = mon_math.inf
print(duree_maximale > 10_000)  # Résultat attendu : True

# Python fournit aussi math.isinf() pour savoir si une valeur est infinie :
print(mon_math.isinf(duree_maximale))  # Résultat attendu : True
print(mon_math.isinf(25.0))            # Résultat attendu : False


# ------------------------------------------------------------
# D. MANIPULER math.nan DANS DES CALCULS
# ------------------------------------------------------------
#
# math.nan peut lui aussi être stocké dans une variable et utilisé
# dans des opérations.
#
mesure = mon_math.nan
print(mesure)  # Résultat attendu : nan

# Une opération avec nan propage généralement nan :
print(mesure + 10)  # Résultat attendu : nan
print(mesure * 2)   # Résultat attendu : nan

# Cela signifie que si une donnée de départ est indéterminée,
# le résultat d'un calcul qui en dépend devient lui aussi indéterminé.


# ------------------------------------------------------------
# E. EXEMPLE CONCRET D'UTILISATION DE math.nan :
#    UNE MESURE DE CAPTEUR MANQUANTE OU INVALIDE
# ------------------------------------------------------------
#
# Imaginons un capteur qui doit fournir une température,
# mais qui n'a renvoyé aucune mesure exploitable.
#
temperature_capteur = mon_math.nan
print(temperature_capteur)  # Résultat attendu : nan

# Si l'on tente malgré tout de convertir cette mesure en ajoutant 2 degrés,
# le résultat reste indéterminé :
temperature_corrigee = temperature_capteur + 2
print(temperature_corrigee)  # Résultat attendu : nan


# ------------------------------------------------------------
# F. EXEMPLE CONCRET D'UTILISATION DE math.nan :
#    DONNÉE NUMÉRIQUE NON DISPONIBLE
# ------------------------------------------------------------
#
# On peut également représenter une valeur encore inconnue.
#
note_examen = mon_math.nan
print(note_examen)  # Résultat attendu : nan

# Lorsque la note devient disponible, la variable pourra être remplacée
# par un vrai nombre :
note_examen = 14.5
print(note_examen)  # Résultat attendu : 14.5


# ------------------------------------------------------------
# G. ATTENTION AUX COMPARAISONS AVEC nan
# ------------------------------------------------------------
#
# Une propriété très importante de nan :
# nan n'est égal à rien, pas même à lui-même.
#
valeur_inconnue = mon_math.nan

print(valeur_inconnue == mon_math.nan)
# Résultat attendu : False

print(valeur_inconnue == valeur_inconnue)
# Résultat attendu : False

# Il ne faut donc PAS tester une valeur NaN avec ==.
#
# La bonne méthode consiste à utiliser math.isnan() :
print(mon_math.isnan(valeur_inconnue))
# Résultat attendu : True

print(mon_math.isnan(25.0))
# Résultat attendu : False


# ------------------------------------------------------------
# H. TESTER SI UNE VALEUR EST FINIE
# ------------------------------------------------------------
#
# math.isfinite() indique si une valeur est un nombre flottant fini,
# c'est-à-dire ni infini ni NaN.
#
print(mon_math.isfinite(25.0))        # Résultat attendu : True
print(mon_math.isfinite(mon_math.inf))  # Résultat attendu : False
print(mon_math.isfinite(mon_math.nan))  # Résultat attendu : False


# ------------------------------------------------------------
# À RETENIR
# ------------------------------------------------------------
#
# math.inf :
# - type float ;
# - représente +∞ ;
# - peut être utilisé dans des calculs et des comparaisons ;
# - très utile comme valeur initiale lorsqu'on cherche un minimum ;
# - se teste avec math.isinf().
#
# math.nan :
# - type float ;
# - signifie "Not a Number" ;
# - représente une valeur numérique indéterminée ou invalide ;
# - les calculs avec nan donnent généralement nan ;
# - ne doit PAS être testé avec == ;
# - se teste avec math.isnan().
#
# math.isfinite(x) :
# - renvoie True si x est une valeur numérique finie ;
# - renvoie False pour +inf, -inf et nan.
#
# IMPORTANT :
# math.inf et math.nan peuvent donc être MANIPULÉS comme des flottants,
# mais leur comportement est particulier et il faut les traiter explicitement.


# ============================================================
# 4. OPÉRATEURS D'AFFECTATION COMPOSÉS
# ============================================================

ma_variable = 25
print(ma_variable)  # Résultat attendu : 25

ma_variable = ma_variable * 2
# Python lit d'abord la valeur actuelle de ma_variable (25),
# calcule 25 * 2, puis range le résultat 50 dans ma_variable.
print(ma_variable)  # Résultat attendu : 50

ma_variable *= 2
# *= est une écriture condensée de :
# ma_variable = ma_variable * 2
print(ma_variable)  # Résultat attendu : 100

# Autres exemples d'écritures condensées :
# x += 3  équivaut à  x = x + 3
# x -= 3  équivaut à  x = x - 3
# x *= 3  équivaut à  x = x * 3
# x /= 3  équivaut à  x = x / 3


# ============================================================
# 5. LES OPÉRATEURS DE COMPARAISON
# ============================================================
#
# Une comparaison produit une valeur booléenne :
# - True  : vrai
# - False : faux
#
# IMPORTANT : il n'est pas nécessaire d'avoir déjà étudié if pour comprendre
# ces expressions. Une comparaison est simplement une expression que Python
# évalue, exactement comme une expression arithmétique.
#
# Exemple détaillé :
#
#     mon_resultat_l_a = 21 > 5
#
# Python procède en deux étapes :
#
# 1) Il évalue l'expression située à droite du signe =
#
#        21 > 5
#
#    La question posée est : "21 est-il strictement supérieur à 5 ?"
#    La réponse est oui, donc Python produit la valeur booléenne True.
#
# 2) Le signe = affecte ensuite cette valeur à la variable :
#
#        mon_resultat_l_a = True
#
# Autrement dit :
#
#     mon_resultat_l_a = 21 > 5
#
# est une écriture condensée de l'idée :
#
#     calculer d'abord 21 > 5, puis stocker le résultat dans mon_resultat_l_a.
#
# ATTENTION :
# =  signifie "affecter une valeur à une variable".
# == signifie "comparer deux valeurs pour savoir si elles sont égales".

mon_resultat_l_a = 21 > 5  # Supériorité stricte
print(mon_resultat_l_a)  # Résultat attendu : True

mon_resultat_l_b = 21 >= 5  # Supériorité ou égalité
print(mon_resultat_l_b)  # Résultat attendu : True

mon_resultat_l_c = 2 < 50  # Infériorité stricte
print(mon_resultat_l_c)  # Résultat attendu : True

mon_resultat_l_d = 21 <= 50  # Infériorité ou égalité
print(mon_resultat_l_d)  # Résultat attendu : True

mon_resultat_l_e = 21 == 5  # Égalité : attention, on utilise == et non =
print(mon_resultat_l_e)  # Résultat attendu : False

mon_resultat_l_f = 21 != 5  # Différence : "différent de"
print(mon_resultat_l_f)  # Résultat attendu : True


# ============================================================
# 6. OPÉRATEURS LOGIQUES ET TABLES DE VÉRITÉ
# ============================================================
#
# Les opérateurs logiques permettent de combiner ou d'inverser des valeurs
# booléennes True et False.
#
# ------------------------------------------------------------
# TABLE DE VÉRITÉ DE and  ("ET")
# ------------------------------------------------------------
#
# and ne donne True que lorsque LES DEUX valeurs sont True.
#
# Convention binaire utilisée dans les tables ci-dessous :
#     False = 0
#     True  = 1
#
# Table booléenne                 Équivalent avec 0 et 1
#
# +-------+-------+---------+     +---+---+---------+
# |   A   |   B   | A and B |     | A | B | A and B |
# +-------+-------+---------+     +---+---+---------+
# | False | False | False   |     | 0 | 0 |    0    |
# | False | True  | False   |     | 0 | 1 |    0    |
# | True  | False | False   |     | 1 | 0 |    0    |
# | True  | True  | True    |     | 1 | 1 |    1    |
# +-------+-------+---------+     +---+---+---------+
#
# À retenir :
# 1 and 1 -> 1
# Tous les autres cas donnent 0.
#
# ------------------------------------------------------------
# TABLE DE VÉRITÉ DE or  ("OU inclusif")
# ------------------------------------------------------------
#
# or donne True lorsqu'AU MOINS UNE des deux valeurs est True.
#
# Table booléenne                 Équivalent avec 0 et 1
#
# +-------+-------+--------+      +---+---+--------+
# |   A   |   B   | A or B |      | A | B | A or B |
# +-------+-------+--------+      +---+---+--------+
# | False | False | False  |      | 0 | 0 |   0    |
# | False | True  | True   |      | 0 | 1 |   1    |
# | True  | False | True   |      | 1 | 0 |   1    |
# | True  | True  | True   |      | 1 | 1 |   1    |
# +-------+-------+--------+      +---+---+--------+
#
# À retenir :
# 0 or 0 -> 0
# Tous les autres cas donnent 1.
#
# ------------------------------------------------------------
# TABLE DE VÉRITÉ DE ^  ("OU EXCLUSIF", XOR) SUR DES BOOLÉENS
# ------------------------------------------------------------
#
# Avec des booléens, ^ donne True lorsque les deux valeurs sont DIFFÉRENTES.
# Il donne False lorsqu'elles sont identiques.
#
# Table booléenne                 Équivalent avec 0 et 1
#
# +-------+-------+-------+       +---+---+-------+
# |   A   |   B   | A ^ B |       | A | B | A ^ B |
# +-------+-------+-------+       +---+---+-------+
# | False | False | False |       | 0 | 0 |   0   |
# | False | True  | True  |       | 0 | 1 |   1   |
# | True  | False | True  |       | 1 | 0 |   1   |
# | True  | True  | False |       | 1 | 1 |   0   |
# +-------+-------+-------+       +---+---+-------+
#
# À retenir :
# le XOR donne 1 uniquement lorsque les deux bits sont différents.
#
# Remarque importante :
# ^ est, à l'origine, l'opérateur XOR bit à bit de Python.
# Avec True et False, il se comporte comme un OU exclusif logique.
#
# ------------------------------------------------------------
# TABLE DE VÉRITÉ DE not  ("NON")
# ------------------------------------------------------------
#
# not inverse une valeur booléenne.
#
# Table booléenne                 Équivalent avec 0 et 1
#
# +-------+-------+               +---+-------+
# |   A   | not A |               | A | not A |
# +-------+-------+               +---+-------+
# | False | True  |               | 0 |   1   |
# | True  | False |               | 1 |   0   |
# +-------+-------+               +---+-------+
#
# À retenir :
# not 0 -> 1
# not 1 -> 0
#
resultat_and = (25 > 5) and (125 != 2)
# 25 > 5    -> True
# 125 != 2  -> True
# True and True -> True
print(resultat_and)  # Résultat attendu : True

resultat_or = (25 > 50) or (125 != 2)
# 25 > 50   -> False
# 125 != 2  -> True
# False or True -> True
print(resultat_or)  # Résultat attendu : True

resultat_xor = (25 < 50) ^ (125 != 2)
# 25 < 50   -> True
# 125 != 2  -> True
# True ^ True -> False
print(resultat_xor)  # Résultat attendu : False

resultat_not = not True
# not inverse True.
print(resultat_not)  # Résultat attendu : False


# ============================================================
# 7. À RETENIR
# ============================================================
#
# +, -, *, /, //, %, **  -> calculs arithmétiques
# =                       -> affectation
# +=, -=, *=, /=          -> affectations condensées
# >, >=, <, <=, ==, !=    -> comparaisons donnant True ou False
# and, or, not             -> opérateurs logiques
# ^ sur des booléens       -> OU exclusif (XOR)
#
# Une expression telle que :
#
#     resultat = 21 > 5
#
# peut donc être comprise SANS connaître if :
# Python calcule d'abord la comparaison 21 > 5, obtient True,
# puis affecte True à la variable resultat.
