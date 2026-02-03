import turtle
import random
def dessiner_carre(stylo, x, y, taille, couleur):
    stylo.penup()
    stylo.goto(x, y)
    stylo.pendown()
    stylo.fillcolor(couleur)
    stylo.begin_fill()
    for i in range(4):
        stylo.forward(taille)
        stylo.right(90) 
    stylo.end_fill()
def dessiner_triangle(stylo, x, y, taille, couleur):
    stylo.penup()
    stylo.goto(x, y)
    stylo.pendown()
    stylo.fillcolor(couleur)
    stylo.begin_fill()
    for i in range(3):
        stylo.forward(taille)
        stylo.right(120) 
    stylo.end_fill()
def dessiner_cercle(stylo, x, y, rayon, couleur):
    stylo.penup()
    stylo.goto(x, y)
    stylo.pendown()
    stylo.fillcolor(couleur)
    stylo.begin_fill()
    stylo.circle(rayon)
    stylo.end_fill()
def main():
    print("==================================")
    print("Dessin Graphique avec Turtle ")
    print("==================================")
    
    nombre = int(input("Entrez un nombre (0 a 9) : "))
    if nombre < 0 or nombre > 9:
        print("Erreur : entrez un nombre entre 0 et 9")
        return
    fenetre = turtle.Screen()
    fenetre.setup(800, 600)
    stylo = turtle.Turtle()
    stylo.speed(10)
    formes = ["carre", "triangle", "cercle"]
    couleurs = ["red", "blue", "green", "yellow", "orange", "purple", "pink", "cyan"]  
    for i in range(nombre):
    print("========================================================") 
    print("\tFIN DU PROGRAMME Dessin Graphique avec Turtle")
    print("\t*Mahamadou Soumaila Abdoulahic*")
    print("=========================================================") 
if __name__ == "__main__":
    main()
