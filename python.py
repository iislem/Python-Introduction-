"""
:Question:
    on donne un mot et la longeur du ligne
    centrer le mot au milieu de la ligne
"""

mot = input()
long = int(input())

print("SOL 1")
# print les espaces en gauche
for i in range((long - len(mot)) // 2):
    print(' ', end='')
print(mot, end='')
# print les espaces en droite
for i in range((long - len(mot)) // 2):
    print(' ')


print("SOL 2")
print(' ' * ((long - len(mot)) // 2), mot,
      ' ' * ((long - len(mot)) // 2), sep='')


print("SOL 3")
print(mot.center(long))

"""
:Question:
    implement une ``do {} while ()`` pour forcer l'utilisateur à entrer un
    nombre entre 2 et 8
"""

# Sol 1 (not optimale & code dupliqué)
x = int(input())
while x not in range(2, 9):
    x = int(input())

# Sol 2 (code dupliqué)
x = int(input('donner un x'))
while not 2 <= x <= 8:
    x = int(input('donner un x'))

# Sol 3 (avec break)
while True:
    x = int(input("donner x"))
    if 2 <= x <= 8:
        break

class Person:

    # constructor
    def __init__(self, nom, prenom):
        # self is `this` equvalent on python
        self.nom = nom
        self.prenom = prenom

    def whoami(self):
        print("I'm", self.nom, self.prenom)

    # toString() on python
    def __str__(self):
        return "{} {}".format(self.nom, self.prenom)

p = Person("Islem", "Lahmar")

print("Created person:", p)
p.whoami()


class Employee(Person):

    def __init__(self, nom, prenom, job):
        # super() on python (call parent constructor)
        Person.__init__(self, nom, prenom)
        self.job = job

    def __str__(self):
        return "{} - {}".format(Person.__str__(self), self.job)

e = Employee("Lahmar", "Islem", "Etudiante")

print("Created employee:", e)
e.whoami()
print(e.job)

"""
For use cases
"""

print("For 1:")
for i in range(2, 5, 2):
    print(i)

print("For 2:")
for i in range(5, 2, -1):
    print(i)

print("For 3:")
l = [1, 5, 9]
for i in l:
    print(i)

print("For 4:")
s = "hello"
for i in s:
    print(i, end='')

def triangle(hauteur):
    largeur = (hauteur * 2) - 1
    for l in range(1, largeur + 1, 2):
        etoiles = '*' * l
        print(etoiles.center(largeur))
