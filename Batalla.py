#programa que nos permite elegir entre 4 personajes y luchar entre ellos para ver quien gana

class Personaje:
    def __init__(self, nombre, salud, ataque):
        self.nombre = nombre
        self.salud = salud
        self.ataque = ataque

    #creamos la representación para mostrar a los personajes en pantalla
    def __repr__(self):
        return f"{self.nombre} (Salud:{self.salud}, Ataque: {self.ataque})"

    #método atacar
    def atacar(self, otro_pj):
        #le restamos la cantidad de salud al otro personaje dependiendo de la cantidad de ataque que posea el atacante
        otro_pj.salud = otro_pj.salud - self.ataque


#función que genera la batalla entre ambos personajes elegidos
def batalla(personaje1, personaje2):
    #mientras la salud de ambos personajes sea mayor a cero, se atacarán por turnos
    while personaje1.salud > 0 and personaje2.salud > 0:
        # Turno del primer personaje
        personaje1.atacar(personaje2)
        print(f"{personaje1.nombre} ataca a {personaje2.nombre}.")
        print(personaje2)
        print("")

        if personaje2.salud <= 0:
            print(f"{personaje2.nombre} ha sido derrotado. ¡{personaje1.nombre} gana!")
            break

        # Turno del segundo personaje
        personaje2.atacar(personaje1)
        print(f"{personaje2.nombre} ataca a {personaje1.nombre}.")
        print(personaje1)
        print("")

        if personaje1.salud <= 0:
            print(f"{personaje1.nombre} ha sido derrotado. ¡{personaje2.nombre} gana!")
            break


#creación de los 5 personajes
goku = Personaje("Goku", 200, 50)
vegeta = Personaje("Vegeta", 180, 60)
krillin = Personaje("Krillin", 150, 40)
freezer = Personaje("Freezer", 190, 70)
bardock =Personaje("Bardock", 175, 55)

#mostramos los personajes disponibles para elegir
print("----------Personajes disponibles----------")
print(goku)
print(vegeta)
print(krillin)
print(freezer)
print(bardock)

#hacemos que el usuario seleccione los dos personajes que lucharán entre sí
print("")
pj1 = input("Elija el primer personaje: ")
pj2 = input("Elija el segundo personaje: ")

# Verifica que los nombres de los personajes seleccionados existan
#para verificarlo creamos un diccionario en el que están todos los pj disponibles
personajes_disponibles = {"Goku": goku, "Vegeta": vegeta, "Krillin": krillin, "Freezer": freezer, "Bardock": bardock}
#si alguno de los dos nombres no está en el dict personajes_disponibles (ya sea por que el pj no existe o está mal escrito) se mostrará una mensaje al usuario
if pj1 not in personajes_disponibles or pj2 not in personajes_disponibles:
    print("Uno o ambos personajes seleccionados no existen o están mal escritos.")
#caso contrario inicia la batalla
else:
    print("\n¡Comienza la batalla!\n")
    batalla(personajes_disponibles[pj1], personajes_disponibles[pj2])